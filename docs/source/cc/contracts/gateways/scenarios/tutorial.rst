*****************************************************
Working with the Gateways Contract (Work in Progress)
*****************************************************

Overview of GatewaysCC
======================
 
    * Deposit BTC in a special address -> receive tokens that represents the BTC onchain.
    * Do onchain transactions with the BTC tokens. 
    * Anyone who obtains the BTC tokens can redeem them and get actual BTC in their withdraw address.

By bringing the operations onchain, we can avoid the need for complex crosschain swaps for each trade. The crosschain transfers do still have to happen on the deposit and withdraw, but that is all. 

There is just one aspect that makes it not fully decentralized, which is the reliance on a ``MofN`` multisig. However, with ``N`` trusted community members and a reasonable ``M`` value, it is not expected to be a big barrier. Since all operations are automated, the only trust needed is that ``M`` of the ``N`` multisig signers are running their nodes with the Gateways dapp active and also that ``M`` of them wont collude to steal the funds locked in the multisig.

Creating a Gateway
==================

In this guide, we will 

    * Create tokens which would represent KMD on a Blockchain created using ``komodod``
    * Convert these tokens for **GatewaysCC** usage
    * Prepare a special Oracle of the date type: ``Ihh`` , which will get information regarding Komodo's chainstate through the **Oraclefeed dAPP**
    * Bind these Tokens and the Oracle to a Gateway
    * Deposit KMD 
    * Exchange it with other tokens on chain
    * Withdraw to get KMD back.

0. Create a new Blockchain 
--------------------------

As the very first step you have to either :doc:`create a new Blockchain </komodo/create-Komodo-Assetchain>` (if you don't have any yet) or start an existing one (Ask for the startup paramaters of a test chain in the ``#cryptoconditions`` channel of the `Komodo Discord <https://komodoplatform.com/discord>`__).

The testchain in this guide is named ``ORCL1`` so its startup parameters will have ``-ac_name=ORCL1`` in it. 

.. note::

    * At the moment of writing this guide, GatewaysCC version is available in ``komodod`` built from the repo: https://github.com/jl777/komodo with branch: ``FSM``
    * The name of the testchain is arbitrary and assume that it has been properly created and running for the rest of the guide.
    * The Komodo main chain needs to be :doc:`synced </komodo/install-Komodo-manually>` for following this guide any further.

.. warning::

    Before you proceed any further, please open an empty text file and remember to save all output transaction ids, hex from each step with notes so as to not get lost.
 

1. Create a token for on-chain representation of an external Cryptocurrency
---------------------------------------------------------------------------

    * As GatewaysCC expects tokens which represent an external Cryptocurrency, we start with creating such tokens.
    * There is the :doc:`TokensCC </cc/contracts/tokens/introduction>` which can be accessed via its RPC.
    * Let's create a token which will represent KMD. 

.. note::
    
    * At this stage, you have to set the maximum possible supply that will be issued.
    * The total supply of the token created by this call is equal to ``Number of Native tokens used \* 10^8`` (Ex. For ``1`` ``ORCL1`` used, the token supply will be ``100000000``, for ``10 ORCL1`` used, 1000000000 tokens are created and so on)

Creating the tokens:

.. code-block:: shell

    ./komodo-cli -ac_name=ORCL1 tokencreate KMD 1000 KMD_equivalent_token_for_gatewaysCC

Where:
 
    * KMD - Name of the on-chain token
    * 1000 - total supply
    * KMD_equivalent_token_for_gatewaysCC - description     

You'll get a ``<hex>`` as a response to the above command. Broadcast it by:

.. code-block:: shell

    ./komodo-cli -ac_name=ORCL1 sendrawtransaction <hex>

After broadcasting the transaction, you'll receive the transaction id which will be called **<tokenid>** from now.

As soon as the transaction is succesfully mined, (i.e., doesn't presist in mempool, which is possible to check using:

.. code-block:: shell

    ./komodo-cli -ac_name=ORCL1 getrawmempool
 
you'll able to use your newly created Tokens.)

For example check it's information using:

.. code-block:: shell

    ./komodo-cli -ac_name=ORCL1 tokeninfo <tokenid>

Or check the token balance for a specific pubkey (after creation your pubkey should have all the supply):

.. code-block:: shell

    ./komodo-cli -ac_name=ORCL1 tokenbalance <tokenid> <pubkey>

2. Convert the tokens to use with GatewaysCC
--------------------------------------------

Before using these Tokens as representative of real KMD that will be locked and redeemed, they need to be converted. The reason for this is to change the rules that constrain the CC vouts. Initially the TokensCC constrains the vouts as it was the one that created them. Now when we do ``tokenconvert`` the vouts are now constrained by the GatewaysCC.

If the tokens vout isn't changed to gateways vout, then only the TokensCC enforcement is done and it would just allow a simple transfer from the "locked" funds as the locking enforcement is done by the GatewaysCC.   

The GatewaysCC automatically converts the vout to a Tokens vout when ``gatewaysclaim`` is called. This trick of converting tokens to a different CC is the way to add additional constraints to another CC vout.

To do all that is described above, first find the **<GatewaysPubkey>** by:

.. code-block:: shell

    ./komodo-cli -ac_name=ORCL1 gatewaysaddress

Then convert 100% of tokens supply (which you've created in step 1) to GatewayCC by the special ``tokenconvert`` call with the evalcode of ``GatewaysCC`` (241) as the first parameter.

Please note that you have to set the supply in the number of tokens for this command whereas for the token creation command the supply was in the units of the Native currency of the chain (i.e., multiply total token supply by ``10^(-8)``).  You can verify this supply by calling ``tokeninfo`` for your **<tokenid>**

.. code-block:: shell

    ./komodo-cli -ac_name=ORCL1 tokeninfo <tokenid>

The ``tokenconvert`` call:

.. code-block:: shell

    ./komodo-cli -ac_name=ORCL1 tokenconvert 241 <tokenid> <GatewaysPubkey>  <totalsupply>

The above command will output a **<hex>** which should be broadcast to the network using ``sendrawtransaction``:

.. code-block:: shell

    ./komodo-cli -ac_name=ORCL1 sendrawtransaction <hex>

3. Create an Oracle for storing "blockheader data" on the Blockchain
--------------------------------------------------------------------

To add external data to the Blockchain, we use the OracleCC. For a description of the OraclesCC, see: :doc:`/cc/book-jl/chapter11`

We have to create an Oracle with the identical name, ie. KMD and the format must start with ``Ihh`` (height, blockhash, merkleroot):

.. code-block:: shell

    ./komodo-cli -ac_name=ORCL1 oraclescreate KMD blockheaders Ihh

    # Broadcast the <hex> that is output after the above command

    ./komodo-cli -ac_name=ORCL1 sendrawtransaction <hex>

Where:

    * KMD - oracle name (identical to external coin)
    * blockcheaders - oracle custom description
    * Ihh - oracle data type (height, blockhash, merkleroot)

The above commands out puts a trasactio id, that will be refered to as **<oracleid>** from here on.

After that you have to register as a datapublisher for the above created Oracle by:

.. code-block:: shell

    ./komodo-cli -ac_name=ORCL1 oraclesregister <oracleid> <datafeeinsatoshis>

    # Broadcast the <hex> that is output after the above command 
    
    ./komodo-cli -ac_name=ORCL1 sendrawtransaction <hex>

Where:

    * <datafeeinsatoshis> is the fee per datapoint denominated in satoshis. (Note that the datafee must be atleast as big as ``txfee`` of the chain)

Then you have to subscribe to it for getting the UTXOs for data publishing. The number of data publishing transactions you can perform in a block is equal to the number of active subscriptions there are. 

Get the **data-publisher's pubkey** from the ``oracesinfo`` call:

.. code-block:: shell

    ./komodo-cli -ac_name=ORCL1 oraclesinfo <oracleid> 

Sample output for the above call:

.. code-block:: json

    {
        "result": "success",
        "txid": "46e2dc958477160eb37de3a1ec1bb18899d77f5b47bd52b8a6f7a9ce14729157",
        "name": "KMD",
        "description": "blockheaders",
        "format": "Ihh",
        "marker": "RNFz9HAuzXhAjx6twEJzcHXconzChfiNM6",
        "registered": [
            {
                "publisher": "03810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5",
                "baton": "RWg43P8s8RtJatAGNa2kV8N2abhQqH93w9",
                "batontxid": "99dd11f4eac1369f3fe8c6428f49e63da26e1b493f69b5bde29edbfbd06eb785",
                "lifetime": "0.00000000",
                "funds": "0.00000000",
                "datafee": "0.01000000"
            }
        ]
    }

The entry ``"publisher"`` in the entry ``"registered"`` of the above json is the **data-publisher's pubkey** (which is hereby known as <publisherpubkey>). 
  
Subscribe with a custom fee in coins  (Please note that there is some missmatch in ``oraclesregister`` and ``oraclessubscribe`` fees calculations which might be changed in the next GatewaysCC fixes):

.. code-block:: shell

    ./komodo-cli -ac_name=ORCL1 oraclessubscribe <oralcleid> <publisherpubkey> <datafeeincoins>

    # Broadcast the <hex> that is output after the above command 

    ./komodo-cli -ac_name=ORCL1 sendrawtransaction <hex>

.. note::

    It might be a good idea to broadcast more than one ``oraclessubscribe`` in case if you need to broadcast more than one oraclesdata in each block (in our example if you want to oraclize more than one KMD height per block)

Now you can check the information about the Oracle by:

.. code-block:: shell

    ./komodo-cli -ac_name=ORCL1 oraclesinfo <oracleid>

Please keep in mind the flow of the Oracle data fees : 

    * Publisher sets datafee in the ``oraclesregister`` call
    * Then anyone can subscribe to this publisher on this Oracle with a custom fee.
    * This custom-fee is made available to this particular publisher and each time the publisher uses ``oraclesdata`` to publish the data, an amount equal to the **datafee** set during ``oracleregister`` is paid to them. ( In other words, if a publisher calls ``oraclesregister`` with datafee ``1 KMD``, and someone subscribed with a customfee ``1000 KMD`` it will be enough to put 1000 data samples to this Oracle. After that the publisher balance will be ``0`` and will need topup/more subscribers to broadcast more data.

4. Bind the Tokens and Oracle as a Gateway
------------------------------------------

If you followed the previous steps you should already have:

    a) Converted token which will represent external coin
    b) Prepared an Oracle with the data-type ``Ihh`` for publishing the merkleroot data by the oraclefeed dAPP (will be covered on step 5)

It's time to connect things together to get the Exchange Gateway, which will realize locking/redeeming between the **"External coin"** and the **"onchain-tokens which represent external coin"**
 
We are using simpliest case with both ``M`` and ``N`` values as ``1`` in this guide. For more complicated case with a multisig gateway, see here: :doc`PLACE HOLDER TEXT`

.. note::

    Use the data for token and oracle from previous preparation steps, use KMD as coinname and as pubkey use yours.

.. code-block:: shell

    ./komodo-cli -ac_name=ORCL1 gatewaysbind <tokenid> <oracleid> <coinname> <tokensupply> 1 1 <trustedpubkey>

    # Broadcast the <hex> that is output after the above command

    ./komodo-cli -ac_name=ORCL1 sendrawtransaction <hex>

As a result you'll get a transaction id, which will be refered to as **<bindtxid>** . This is the id of the Gateway that has just been created for which you have the **<trustedpubkey>**.

In case of a succesfull creation, you'll able to get info on your Gateway by:

.. code-block:: shell

    ./komodo-cli -ac_name=ORCL1 gatewaysinfo <bindtxid>

Now verify if the **<tokenid>** and **<oracleid>** match with the ones created in previous steps.

5. Compile the Oraclefeed dAPP and run it to store the merkelroot data of an External coin onto the chain (to Oracle)
---------------------------------------------------------------------------------------------------------------------

Oraclefeed dAPP will handles the the transfer of merkleroot data to the Oracle that has been created in step 3.

First we need to compile it:

.. code-block:: shell

    cd  ~/komodo/src/
    gcc cc/dapps/oraclefeed.c -lm -o oraclefeed

Run it as:

.. code-block:: shell

    ./oraclefeed $ACNAME $ORACLETXID $MYPUBKEY $FORMAT $BINDTXID &

Where:

    * $ACNAME - Name of assetchain we're using. In our example it's ORCL1
    * $ORACLETXID - ID of the Oracle (data-type: ``Ihh``) which we've created in step 2
    * $MYPUBKEY - Your pubkey
    * $FORMAT - ``Ihh``
    * $BINDTXID - id of your gateway bind from step 4 (**<bindtxid>**)

If oraclefeed is started and working as expected, you'll see something like:
::

    (succesfull oraclization of KMD heights):
    KMD ht.1023334 <- 669d0f009eaf85900be0d54fa1b5f455d49edfc1d9dcfe71c43b8be19b7927dda3ecd20c0175bc7b8eb98d857baeeef6a18fc7d6b58bd34b4eb00beaa18c5842bbe5566a
    broadcast ORCL1 txid.(9484283d8d4bf28b4053e21e7b7e8210eb59c41668e9c7280c4e6c4fbf61579a)
    KMD ht.1023335 <- 679d0f00173d5dc169a64bba92e5765fde848cc620a700295ecce8837cb2a13b05000000ed71033532278f72c8f64990e27f0cb185310df163b3278faf267e87d12bf84b
    broadcast ORCL1 txid.(837c132ab47f1ac1eee2e03828a9818369b919c1de128b99958ac95ffdc96551)
    KMD ht.1023336 <- 689d0f0006a53215d5a07d9ee1c9206dcdccacd1c364968b555c56cdf78f9f0c40f87d08b30fdf63299d25bd9a09a3b3fb8a26800a0a4f6e93ca6cd8cb41b98b756dd937
    broadcast ORCL1 txid.(f33d5ffaec7d13f14605556cee86262299db8fad0337d1baefadc59ec24b6055)

6. Using the Gateway
--------------------

6.1) GatewaysDeposit
++++++++++++++++++++

To make a deposit to the Gateway (i.e., lock external coins in exchange for on-chain tokens), send the funds to the "deposit" address on KMD chain, along with a small amount to the address corresponding to the pubkey you want to get the assetized KMD to appear in the ``ORCL1`` chain:

.. code-block:: shell

    ./komodo-cli z_sendmany "addressFromWhichYouAreSendingFunds" '[{"address":"addressOfPubkeyYouWantTokenizedKmdAppearIn","amount":0.0001},{"address":"gatewaysDepositAddress","amount":0.1}]'

The transaction id produced by the above command will be called **cointxid**

This transaction should have two vouts ( i.e., two addresses declared as recepients) and change.
To get **gatewaysDepositAddress** , use (**<bindtxid>** you got in step 4):

.. code-block:: shell

    ./komodo-cli -ac_name=ORCL1 gatewaysinfo <bindtxid>

As a result you'll get a transaction ID for which you have to collect some more data to use in futher calls.

Now you should have enough data to proceed with gatewaysdeposit call which will broadcast data about KMD deposit to blockchain for gateway node validation:

.. code-block:: shell

    ./komodo-cli gatewaysdeposit bindtxid height coin cointxid claimvout deposithex proof destpub amount

    # Broadcast the <hex> that is output after the above command

    ./komodo-cli -ac_name=ORCL1 sendrawtransaction <hex>

The transaction id obtained for the above command will be called the **deposittxid**

Where:

    * bindtxid - bindtxid from step 4
    * height - height of <txid of z_sendmany> block
    * coin - KMD for this example
    * cointxid - <txid of z_sendmany>
    * claimvout - vout of claim (on the first run should be 0)
    * deposithex - get it from <txid of z_sendmany>
    * proof - get it by  ./komodo-cli gettxoutproof '["<txid of z_sendmany>"]'
    * destpub - public key which is eligible to get these tokens (to which the  <addressOfPubkeyYouWantTokenizedKmdAppearIn>  from z_sendmany belongs)
    * amount - amount of deposit (in this case 0.1)

Please note that for the deposit to process succesfully the needed height must be succesfully oraclized already by the oraclefeed dapp which you've compiled and run in step 5

6.2) GatewaysClaim
++++++++++++++++++

Next step is to spend the marker and deposit asset and perform claim which will actually credit asset tokens to depositer:

This call can be performed only from a node which owns the privkey corresponding to the pubkey which was used in the gatewaysdeposit call (pubkey should be in two places: ``-pubkey=`` parameter with which you started the daemon, and also it should be in the wallet --> you should have gotten it by ``-ac_name=ORCL1 validateaddress <addressfromgetaccountaddress>``

.. code-block:: shell

    ./komodo-cli -ac_name=ORCL1 gatewaysclaim bindtxid coin deposittxid destpub amount

    # Broadcast the <hex> that is output after the above command

    ./komodo-cli -ac_name=ORCL1 sendrawtransaction <hex>

Where:

    * bindtxid - bindtxid from step 4 (id of Gateway bind)
    * coin - coin ticker (e.g. KMD)
    * deposittxid - transaction ID of gatewaysdeposit from step 6.1
    * destpub - pubkey on which tokens should appear
    * amount - amount of deposit in coin - i.e., amount which has been sent to gatewaysdepositaddress in step 6.1

After this transaction has been mined, tokens should be credited to pubkey to which the address **addressOfPubkeyYouWantTokenizedKmdAppearIn** belongs to and these tokens are usable now as regular TokenCC tokens (i.e., it is possible to tokentransfer, tokenbid/ask etc.)

6.3) GatewaysWithdraw
+++++++++++++++++++++

.. note::

    This step can be done by anyone who are in posession of the tokens that can be redeemed for the External coin. They could have gotten these tokens through trading for other on-chain tokens or simply by transfer from the original depositer in return for some service rendered in the Physical World 

First you have to convert these tokens which have became "usual" ones "Gateway tokens" again by doing tokencovert back before doing a withdraw:

.. code-block:: shell

    ./komodo-cli -ac_name=ORCL tokenconvert 241 tokenid pubkey totalsupply
    
Where:

    * ``pubkey`` - pubkey on which tokens will be availiable after conversion  (pubkey should be in two places - -pubkey= param with which you started daemon, and also it should belongs to wallet - you have to get it by ``-ac_name=ORCL1 validateaddress <addressfromgetaccountaddress>``)

.. note::

    Please keep in mind that oraclefeed dapp must be running for gatewayswithdraw to work.

   After the ``tokenconvert`` transaction is mined, you can call the ``gatewayswithdraw`` RPC from the node that owns the ``pubkey`` used in ``tokenconvert``.

.. code-block:: shell

    ./komodo-cli -ac_name=ORCL1 gatewayswithdraw bindtxid coin withdrawpub amount

Where:
 
    * bindtxid - bindtxid from step 4 (id of gateway bind)
    * coin - coin ticker (e.g. KMD)
    * withdrawpub - pubkey where you want withdrawed coins to appear on external chain (so in this example, KMD pubkey)
    * amount - amount to withdraw 

Examples:

.. code-block:: shell

    ./komodo-cli -ac_name=ORCL1 tokenconvert 241 3852b3e1b24bc927758f49ded16114437ab52e5fb9afa201c47bb85e28372ea8 030cb918b90dc084cdb08fcda4297d0db9c86422987df0cafa47ffef57eb6ef647 100

    ./komodo-cli -ac_name=ORCL1 gatewayswithdraw 1023f2c31f8d5e06854cd8c3ef103679b8d2af2c4ba14ea16646dd2a10332c55 KMD 030cb918b90dc084cdb08fcda4297d0db9c86422987df0cafa47ffef57eb6ef647 0.000001
 
 That's it, if you've followed these steps you might be more familiar with gatewaysCC now and tokenized some KMD.
