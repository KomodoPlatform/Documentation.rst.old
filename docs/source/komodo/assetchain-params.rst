*********************************************************************
Parameters to customize Blockchains created using Komodo's technology
*********************************************************************

For instructions on how to create an assetchain see :doc:`create-Komodo-Assetchain`

For examples see :doc:`example-asset-chains`

-ac_name
========

This is the ticker symbol for the coin you wish to create. It is recommended to use only numbers and uppercase letters.

-ac_supply
==========

This is the amount of premined coins you would like the chain to have. The node that sets ``-gen`` during the creation process will mine these coins in the genesis block. If this is not set, ``-ac_reward`` must be set, and the default value of 10 coins will be used. If ``-ac_founders`` is set, the  premined coins will be mined to the founders reward address. This parameter should be set to a whole number without any decimals places. This should be to set to less than ``2000000000`` to avoid 64 bit overflows. 

Note: An additional fraction of a coin will be added to this based on the chain's parameters. This is used by nodes to verify the genesis block. For example, the DEX chain's ``-ac_supply`` parameter is set to ``999999``, but in reality the genesis block was ``999999.13521376``.

-ac_reward
==========
This is the block reward for each mined block in satoshis. If this is not set, the block reward will be ``10000`` satoshis, and blocks will be on-demand after block 127 (a new block will not be mined unless there is a transaction in the mempool.)

-ac_end
=======
This is the block height in which block rewards will end. Every block after this height will have 0 block reward.

-ac_halving
===========

This is the number of blocks between each block reward halving. This parameter will have no effect if ``-ac_reward`` is not set. The lowest possible value is ``1440`` (~1 day). If this parameter is set, but ``-ac_decay`` is not, the reward will decrease by 50% each halving. 

-ac_decay
=========

This is the percentage by which the block reward will decrease on each block reward halving. For example, if this is set to ``75000000``, the block reward will drop 25% from the previous block reward each halving. This parameter will have no effect if ``-ac_reward`` is not set.  
This is the formula that ``-ac_decay`` follows:

.. code-block:: shell

	numhalvings = (height / -ac_halving);
	for (i=0; i<numhalvings; i++)
	reward = (reward * -ac_decay) / 100000000;

-ac_eras
========

This parameter allows the block reward to be manipulated based on the current "era" the chain is in. There is a limit of 3 eras. Currently, ``-ac_eras`` is able to interact with ``-ac_reward``, ``-ac_decay`` and ``-ac_halving``. No other parameters are compatible. The value for each era should follow the previous value separated by a comma. If a value is not set for a specific era, the previous era's value will be used. For example, if a chain has ``-ac_reward=100000000,200000000 -ac_halving=100 -ac_eras=2``, the ``ac_halving`` value for both eras will be ``100``.

A ``-ac_decay`` value of ``100000000`` and a ``-ac_halving`` value of ``1`` can be used for linear growth from the previous era's ``-ac_reward`` value to the next era's ``-ac_reward`` value.

A ``-ac_end`` value of ``0`` indicates that the era will last indefinitely. A ``0`` value should only be used for the last era.  

For example, this can be used for a "slow start":
::

    ./komodod -ac_name=EXAMPLE -ac_reward=0,10000000000 -ac_end=1000,0 -ac_decay=100000000,100000000 -ac_halving=1 -ac_eras=2

This chain's block reward will grow linearly from 0 to 100 over 1000 blocks then stay at 100 block reward indefinitely. 


``komodo-cli -ac_name=EXAMPLE getblocksubsidy <blockheight>`` should be used to verify your chain will work as you expect it to.  

-ac_perc
========

This parameter has two different functionailites depending on the configuation of the chain params. 

If this parameter is used without ``-ac_founders`` the chain will follow an inflation tax model. The ``-ac_perc`` parameter is the percentage added to the block reward and transactions that will be sent to the ``-ac_pubkey`` address. ``-ac_pubkey`` must be set for this functionality. For example, if ``-ac_reward=100000000`` and ``-ac_perc=10000000``, for each block mined, the miner receives 1 coin along with the ``-ac_pubkey`` address receiving 0.1 coin. For every transaction sent, the pubkey address will receive 10% of the overall transaction value. This 10% is not taken from the user, rather it is created at this point. Each transaction inflates the overall supply. The maximum amount of coins created per block by this mechanism is capped at ``(1000000 * <percentage>)``.

Note: Vout 1 of each coinbase transaction must be the correct amount sent to the corresponding pubkey. The ``vout`` type for all coinbase vouts must be ``pubkey`` as opposed to ``pubkeyhash``. This only affects a miner trying to use a stratum. Blackjok3r's coinbase overide method can be used. Please see `this repo <https://github.com/blackjok3rtt/knomp#disable-coinbase-mode>`__ for details. 

Please see ``-ac_founders`` for founder's reward functionality. 

-ac_founders
============

This parameter can be used to enforce a "founder's reward". If this parameter is used, ``-ac_perc`` must be set. ``-ac_pubkey`` OR ``-ac_script`` must also be set. The ``-ac_perc`` value will determine the percentage of block rewards paid to the founder's reward address. The ``-ac_founders`` value itself will determine how often this founder's reward is to be paid. For example, this configuration, ``-ac_reward=100000000 -ac_perc=10000000 -ac_founders=100``, will result in block rewards being 1 coin except for every 100th block where it will be 1 coin and 10 additional coins paid to the founder's reward address.

``-ac_pubkey`` can be used to send the founder's reward to a normal address. ``-ac_script`` can be used to send the founder's reward to a multisig address. 

-ac_pubkey
==========

This parameter should not be set unless the chain uses ``-ac_founders``, ``-ac_perc`` or ``-ac_import=PUBKEY``. This should be set to a 66 character string(compressed pubkey).  You can get the pubkey of an address by using the ``validateaddress`` command in ``komodo-cli``. The address must be imported to the wallet before using ``validateaddress``. If this parameter is used, block 1(premine) will be mined to this address.

Note: This must be set to a compresssed pubkey as opposed to an uncompressed pubkey. To simplify, the pubkey must start with ``02`` or ``03``.

-ac_script
==========

This parameter enables the ``-ac_founders`` founder's reward to be sent to a multisig address or any p2sh address. If this parameter is used, block 1(premine) will be mined to this address. This parameter should only be used in combination with ``-ac_founders``. If ``-ac_script`` is set, ``-ac_pubkey`` must not be. 

This should be set to the ``"hex"`` value of ``"scriptPubKey"``. To get this value, first create a multisig address with ``createmultisig`` command in ``komodo-cli``.

Example:
::

	komodo-cli -ac_name=EXAMPLE createmultisig 2 "[\"RMnZJpfLbFHUxMS3HM5gkvtFKeduhr96Ec\",\"RW2Yx4Tk9WGfUvhbJTXGFiRhr7PKcVtrm5\",\"RQ1uqBj9yk94BcxEZodbeNqb3jWv8pLeA4\"]"
	{
	  "address": "bGHcUFb7KsVbSFiwcBxRufkFiSuhqTnAaV",
	  "redeemScript": 	"522102040ce30d52ff1faae7a673c2994ed0a2c4115a40fa220ce055d9b85e8f9311ef2102a2ba4606206c032914dd48390c15f5bf996d91bf9dbd07614d972f39d93a511321026014ef4194f6c7406a475a605d6a393ae2d7a2b12a6964587299bae84172fff053ae"
	}

On a test chain, send this address some coins then look at the resulting transaction with ``getrawtransaction <txid> 1``:

::

	komodo-cli -ac_name=EXAMPLE sendtoaddress bGHcUFb7KsVbSFiwcBxRufkFiSuhqTnAaV 10
	ef0d05f14ea2a5bfa1c99142c2e3d78c851223d7476ed2e57b61b6e07f741f0f

	komodo-cli -ac_name=EXAMPLE getrawtransaction ef0d05f14ea2a5bfa1c99142c2e3d78c851223d7476ed2e57b61b6e07f741f0f 1

Look at the output to the address:

::

    {
      "value": 10.00000000,
      "valueSat": 1000000000,
      "n": 1,
      "scriptPubKey": {
        "asm": "OP_HASH160 2706324daaac92c93420e985f55d88ea20e22ae1 OP_EQUAL",
        "hex": "a9142706324daaac92c93420e985f55d88ea20e22ae187",
        "reqSigs": 1,
        "type": "scripthash",
        "addresses": [
          "bGHcUFb7KsVbSFiwcBxRufkFiSuhqTnAaV"
        ]
      }
    }

This "hex" value is what ``-ac_script`` must be set to. For example, ``-ac_script=a9142706324daaac92c93420e985f55d88ea20e22ae187``.

-ac_cc
======

This is the network cluster on which the chain can interact with other chains via cross chain `crypto conditions <https://developers.komodoplatform.com/basic-docs/start-here/cc-overview.html>`__. This functionality is still in testing. If this is set to 1, the chain will have crypto conditions enabled, but it will not be able to interact with other chains. If this is set to any number >1 and <100, the chain can validate transactions on chains on the same network cluster via the `MoMoM protocol <https://komodoplatform.com/komodo-platforms-new-scalability-tech/>`__. For example, all ``-ac_cc=2`` chains can interact with each other but may not interact with ``-ac_cc=3`` chains. This cross-chain validation relies on both chains being notarized by the same notary node network. If this is set to >100, the chain will be fungible via the burn protocol with other chains on the same network cluster.

-ac_staked
==========

This is the percentage of blocks the chain will aim to have as POS. For example, a ``-ac_staked=90`` chain will have 90% POS blocks/10% POW blocks. This isn't exact, but the POW difficulty will automatically adjust based on the overall percentage of POW mined blocks.

Each staked block will have an additional transaction added to the coinbase in which the coins that staked the block are sent back to the same address. This is used to verify which coins staked the block, and this allows for compatibility with existing Komodo infrastructure such as Agama, BarterDEX and explorers. If ``-ac_staked`` is used in conjunction with ``-ac_perc``, the ``-ac_pubkey`` address will receive slightly more coins for each staked block compared to a mined block because of this extra transaction.

The following are the (current) rules for staking a block:

	#. Block timestamps are used as the monotonically increasing timestamp. It is important to have a synced system clock.

	#. In order to stake, you must use ``-gen -genproclimit=0`` while launching the daemon or ``komodo-cli -ac_name=<CHAINNAME> setgenerate true 0`` after launching the daemon.

	#. A utxo is not eligible without ``nLockTime`` set and until 6000 seconds has passed from this lock time. ``(100 * expected blocktimes) to be exact``

	#. There are 64 different segments(``segids``) of addresses, based on the hash of the destination address. ``((nHeight + addrhash.uints[0]) & 0x3f)`` The segid of an address can be found with the ``validateaddress`` command. Each segid will take turns being segid0 at each height. ``(height % 64) = the segid0 for that height.`` All other segid will adjust the elapsed time by ``segid`` seconds.

	#. A new block is eligible to be staked 2 seconds after median blocktime. For example, segid0 for a given height will be eligible to submit a block 2 seconds after median blocktime, whereas segid1 will be eligible to submit a block 4 seconds after median blocktime. For the next block, segid0 from the previous block will now be segid63 and will be eligible to submit a block 128 seconds after median blocktime. This means by 128 seconds after the median blocktime, all segids are eligible.

	#. Coinage calculated from the adjusted time is used to divide hash(address + pastblockhash) to create the value compared against the difficulty to determine if a block is won or not. This means a UTXO is more likely to win a block within a segid based on age of the UTXO and amount of coins.

To create a chain using this parameter, start the first node with ``-gen -genproclimit=0``. Start the second node with ``-gen -genproclimit=$(nproc)``. Send coins from the second node to the first node, and it will begin staking. The first 100 blocks will allow POW regardless of the ``-ac_staked`` value. On a chain using a high percentage for POS, it's vital to have coins staking by block 100. It is also vital to stake coins in all 64 segids. For the time being, you can use the `genaddresses.py` script in `this repo <https://github.com/alrighttt/dockersegid>`_ to generate an address for each segid. This functionality will soon be integrated directly into the daemon. You can use the ``getbalance64`` command to get the balance you currently have in each segid you are staking in. 

-ac_public
==========

If ``-ac_public`` is set to 1, zkSNARKs will be disabled. All z address functionalilty is disabled. Therefore, all transactions on the blockchain are public. 

-ac_private
===========

If ``-ac_private`` is set to 1, all transactions other than coinbase transactions(block rewards) must use zkSNARKs. All transparent address functionality other than sending mined coins from transparent addresses is disabled. 

-ac_sapling
===========

This parameter can be used to delay sapling activation. By default, sapling will activate at block 61 on a newly created assetchain. If for some reason the assetchain should not have sapling activation, set this to a block height in the future. For example, ``-ac_sapling=5000000`` will delay sapling activation to block ``5000000``. This can also be used to activate sapling prior to block 61. Activating sapling prior to block 61 should not be done on a chain intended for production use.

-ac_timelockgte, -ac_timeunlockfrom, -ac_timeunlockto
=====================================================

These parameters can be used to enforce "coinbase locking".  

``-ac_timelockgte`` should be a value in satoshis. Any block reward greater than or equal to this amount will be locked between ``-ac_timeunlockfrom`` and ``-ac_timeunlockto``. Both ``-ac_timeunlockfrom`` and ``-ac_timeunlockto`` should be set to block heights.

For example:
::

	komodod -ac_name=EXAMPLE -ac_supply=0 -ac_reward=10000000000 -ac_halving=10000 -ac_timelockgte=10000000000 -ac_timeunlockfrom=10000 -ac_timeunlockto=100000

The first 10000 block rewards on this chain will be locked until a random block between 10000 and 100000.

*********************
Parameters in testing
*********************

-ac_txpow
=========

Setting ``-ac_txpow=1`` will enforce a transaction rate limiter. It's an effective way to prevent spam transactions on an assetchain. It forces all transactions other than coinbase transactions to have a txid starting and ending with 00. This parameter is currently a proof of concept. Many of the traditional rpc commands such as ``sendtoaddress`` or ``sendmany`` are not currently supported with this parameter. ``createrawtransaction`` and ``signrawtransaction`` must be used. 

-ac_algo
========

By default, all assetchains will use equihash as their mining algorithm. This parameter allows for verushash to be used if ``-ac_algo=verushash`` is set. This is verushash1.0. The updated version of verushash is not currently supported. This serves as a proof of concept for adding support for additional mining algorithms.

Testing is being done to make ``-ac_algo`` compatible with ``-ac_staked``. Currently, this combination is not recommended.

-ac_veruspos
============

This parameter can be used as an alternative to ``-ac_staked``. The chain will use Verus's proof of stake implementation instead. The only valid value for this parameter is ``-ac_veruspos=50``. It does not have the same segid mechanism as ``-ac_staked``. It is not recommended to use this parameter for a production chain unless thorough testing is done first.


-ac_ccenable
============

This parameter can be used to limit which crypto conditions will be enabled. If this parameter is used, ``-ac_cc`` must be set. If ``-ac_cc`` is set, but ``-ac_ccenable`` is not, all crypto conditions will be enabled. This must be set to the corresponding eval codes in decimal separated by commas for the desired crypto conditions. These eval codes can be found `here <https://github.com/jl777/komodo/blob/master/src/cc/eval.h>`__. Please note that this disables spending crypto condition UTXOs for every eval code not specified. However, this does not limit creating these UTXOs. 

This is labeled as in testing because currently it does not disable the rpc commands of the disabled crypto conditions. This means using these rpc commands will result in unspendable UTXOs. 

For example, this chain will limit crypto conditions to faucet and rewards:

::

	komodod -ac_name=EXAMPLE -ac_supply=0 -ac_reward=100000000 -ac_cc=2 -ac_ccenable=228,229



Please send any critiques or feedback to Alright or gcharang on matrix or discord.

`Discord Invite <https://komodoplatform.com/discord>`_

