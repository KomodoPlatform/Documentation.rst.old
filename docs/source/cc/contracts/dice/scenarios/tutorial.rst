*******************************************************
Guide to Start the KMDICE Chain and Play Dice Using CLI
*******************************************************

Requirements:
=============

    * Latest Komodo binaries
    * Funds

Get Komodo binaries:
--------------------

    * :doc:`Compile Locally </komodo/install-Komodo-manually>`
    * `Download pre-compiled binaries <https://github.com/KomodoPlatform/komodo/releases>`_

Funds:
------

There are 3 ways you can get KMDICE coins now.

    * Mine ``KMDICE``
    * Atomic Swap using `BarterDEX <https://github.com/KomodoPlatform/BarterDEX/releases>`_
    * OTC trades in `Komodo Discord <https://komodoplatform.com/discord>`_

Getting started
===============
 
Get ``pubkey`` value
--------------------

We need to get ``pubkey`` value for the smartaddress you are going to use the KMDICE wallet with. ``pubkey`` is needed for using the contracts. If you already know the ``pubkey`` of the address you are going to use, please skip to the :ref:`next section <start-kmdice-with-pubkey>`.

Step 1
++++++

Start the chain with the following command and wait for the daemon to sync.

.. code-block:: shell

    ./komodod -ac_name=KMDICE -ac_supply=10500000 -ac_reward=2500000000 -ac_halving=210000 -ac_cc=2 -addressindex=1 -spentindex=1 -addnode=144.76.217.232 &

Step 2
++++++

Get a new address

.. code-block:: shell

    ./komodo-cli -ac_name=KMDICE getnewaddress

Step 3
++++++

Use ``validateaddress`` command with the address you got to get the pubkey displayed

.. code-block:: shell

    ./komodo-cli -ac_name=KMDICE validateaddress RPCeZmqW4Aam52DFLmMraWtu5CuXPxqk92

This will display the following info from where you get the pubkey.

.. code-block:: json

    {
        "isvalid": true,
        "address": "RPCeZmqW4Aam52DFLmMraWtu5CuXPxqk92",
        "scriptPubKey": "76a91498b5caa42ffe9868844c51ba6e085e5e7e92fc2588ac",
        "segid": 13,
        "ismine": true,
        "iswatchonly": false,
        "isscript": false,
        "pubkey": "02f183a71e93dfa7672ce7212187e45eabcf4077fed575348504b20295751ab1a2",
        "iscompressed": true,
        "account": ""
    }

Step 4
++++++

Stop the ``KMDICE`` chain with the following command. (Make sure to use this command every time you want to stop the chain. Otherwise, you risk corrupting the local database and have to rescan the blockchain again.)

.. code-block:: shell

    ./komodo-cli -ac_name=KMDICE stop

.. _start-kmdice-with-pubkey:

Start KMDICE with ``pubkey`` to Play Dice Game
----------------------------------------------

Use the following command to start ``KMDICE`` with ``pubkey`` for address you are going to use. If you don't have a pubkey, please follow the earlier steps.

.. code-block:: shell

    ./komodod -ac_name=KMDICE -pubkey=02f183a71e93dfa7672ce7212187e45eabcf4077fed575348504b20295751ab1a2 -ac_supply=10500000 -ac_reward=2500000000 -ac_halving=210000 -ac_cc=2 -addressindex=1 -spentindex=1 -addnode=144.76.217.232 &

How to bet?
===========

Find the Diceplan you want to use
---------------------------------

.. code-block:: shell

    ./komodo-cli -ac_name=KMDICE dicelist

This will return you the following:

.. code-block:: shell

    [
      "5be49570c56d036abb08b6d084da93a8a86f58fc48db4a1086be95540d752d6f"
    ]

Get info for the Diceplan
-------------------------

.. code-block:: shell

    ./komodo-cli -ac_name=KMDICE diceinfo 5be49570c56d036abb08b6d084da93a8a86f58fc48db4a1086be95540d752d6f

This will return the following:

.. code-block:: json

    {
        "result": "success",
        "fundingtxid": "5be49570c56d036abb08b6d084da93a8a86f58fc48db4a1086be95540d752d6f",
        "name": "KMDICE",
        "sbits": 76155294338379,
        "minbet": "0.00100000",
        "maxbet": "1000.00000000",
        "maxodds": 1500,
        "timeoutblocks": 600,
        "funding": "10469598.73974446"
    }

Now, you have all info needed to place a bet. Make sure that you have KMDICE funds too.

Place a Bet
-----------

This is a 2 step process using CLI. First you need to use the ``dicebet`` command with the required info. That will create a raw transaction HEX value which we need to brodcast to the network using ``sendrawtransaction`` API. This is the example command: ``dicebet name fundingtxid amount odds``

.. code-block:: shell

    ./komodo-cli -ac_name=KMDICE dicebet KMDICE 5be49570c56d036abb08b6d084da93a8a86f58fc48db4a1086be95540d752d6f 10 1

Output:

.. code-block:: json

    {
        "result": "success",
        "hex": "010000000378c9b0720ac4ffda232bd8ebc1ebf10d78efe23daf59ad887439baf72a3ffd03000000007b4c79a276a072a26ba067a5658021039d966927cfdadab3ee6c56da63c21f17ea753dde4b3dfd41487103e24b27e94e8140fe35ae062eb8239b1eec5407c71e27531f281dc369b55c3d3c235a87f6c10b3d4e7a029a6420e4fa076bd1d3da013287a17973fb6684bc487335ce176e7488d3a100af038001e6a10001ffffffff0b2261be0d143f42b833bcdf6e95582d4071f7d7d1d03eb1de0893eb7dc563ef0200000049483045022100f934f292e5ef9b3c605b83381abec1d99c7119d35a3833e40e65d788191ea51402207e925062602bb603f7109e3f36009563952741e666210195686de27b61515cc801ffffffff0b2261be0d143f42b833bcdf6e95582d4071f7d7d1d03eb1de0893eb7dc563ef0300000048473044022020aa8c2d6dc9727ce32f34ae704eb374b7cf87f43250a2d10072fad266f6602e02201fce01ae5c550438f2a512ab13f4c40d411d7726f32046e989b9747af33fd4e101ffffffff0500ca9a3b00000000302ea22c80200095ece5eee67e1f313e7ba2d156c7617106cd52b75c93ed3fb110ff3fba6e998103120c008203000401cc0027b92900000000302ea22c80200095ece5eee67e1f313e7ba2d156c7617106cd52b75c93ed3fb110ff3fba6e998103120c008203000401cc1727000000000000232103fe754763c176e1339a3f62ee6b9484720e17ee4646b65a119e9f6370c7004abcacc91265bf17090000232103fe754763c176e1339a3f62ee6b9484720e17ee4646b65a119e9f6370c7004abcac00000000000000006d6a4c6ae6424b4d444469636500f74cae60f1901161cbe475ff00f1024bb3d64be778b714bfbeb75afa20fffceb6b2540dd22241ca6e72fe32c1cd1d2a9528140cad290f1599041e06589040067000000000000000000000000000000000000000000000000000000000000000000000000"
    }

Now we need to brodcast this transaction using the following command:

.. code-block:: shell

    ./komodo-cli -ac_name=KMDICE sendrawtransaction 010000000378c9b0720ac4ffda232bd8ebc1ebf10d78efe23daf59ad887439baf72a3ffd03000000007b4c79a276a072a26ba067a5658021039d966927cfdadab3ee6c56da63c21f17ea753dde4b3dfd41487103e24b27e94e8140fe35ae062eb8239b1eec5407c71e27531f281dc369b55c3d3c235a87f6c10b3d4e7a029a6420e4fa076bd1d3da013287a17973fb6684bc487335ce176e7488d3a100af038001e6a10001ffffffff0b2261be0d143f42b833bcdf6e95582d4071f7d7d1d03eb1de0893eb7dc563ef0200000049483045022100f934f292e5ef9b3c605b83381abec1d99c7119d35a3833e40e65d788191ea51402207e925062602bb603f7109e3f36009563952741e666210195686de27b61515cc801ffffffff0b2261be0d143f42b833bcdf6e95582d4071f7d7d1d03eb1de0893eb7dc563ef0300000048473044022020aa8c2d6dc9727ce32f34ae704eb374b7cf87f43250a2d10072fad266f6602e02201fce01ae5c550438f2a512ab13f4c40d411d7726f32046e989b9747af33fd4e101ffffffff0500ca9a3b00000000302ea22c80200095ece5eee67e1f313e7ba2d156c7617106cd52b75c93ed3fb110ff3fba6e998103120c008203000401cc0027b92900000000302ea22c80200095ece5eee67e1f313e7ba2d156c7617106cd52b75c93ed3fb110ff3fba6e998103120c008203000401cc1727000000000000232103fe754763c176e1339a3f62ee6b9484720e17ee4646b65a119e9f6370c7004abcacc91265bf17090000232103fe754763c176e1339a3f62ee6b9484720e17ee4646b65a119e9f6370c7004abcac00000000000000006d6a4c6ae6424b4d444469636500f74cae60f1901161cbe475ff00f1024bb3d64be778b714bfbeb75afa20fffceb6b2540dd22241ca6e72fe32c1cd1d2a9528140cad290f1599041e06589040067000000000000000000000000000000000000000000000000000000000000000000000000

This will output the ``bettxid``

.. code-block:: shell

    694c309c86a928fde1919a86381f61670479c3ede85ea0574d08636cc406e798

Check your balance for the changes to reflect after the tx confirms.

Check Bet Status
----------------

You can check your bet status (win or loss) using the following command: ``dicestatus name fundingtxid bettxid``

.. code-block:: shell

    ./komodo-cli -ac_name=KMDICE dicestatus KMDICE 5be49570c56d036abb08b6d084da93a8a86f58fc48db4a1086be95540d752d6f 694c309c86a928fde1919a86381f61670479c3ede85ea0574d08636cc406e798

