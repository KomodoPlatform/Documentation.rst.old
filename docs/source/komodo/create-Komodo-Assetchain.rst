***********************
Creating New Assetchain
***********************

To create and start generating/mining with new Assetchain
=========================================================

.. code-block:: shell

	./komodod -ac_name=EXAMPLECHAIN -ac_supply=1000000 -gen &

The above will start a new assetchain with name "EXAMPLECHAIN" and start generating on-demand blocks every 60 seconds. The first node which spawned a new assetchain will mine first 100 blocks. And that same first node will also hold the supply of this assetchains' token 1000000.

500 milliom max is good to use, to avoid 64 bit overflows.

Querying Assetchain
===================

You can query for assetchain blocks and balances with this komodo CLI command:

.. code-block:: shell

	./komodo-cli -ac_name=EXAMPLECHAIN getinfo

Connecting to Assetchain as a node
==================================

Now, the other nodes which need to use the same Assetchain will need to connect to the first node which spawned this new Assetchain. For that the client nodes will use this komodo daemon command:

.. code-block:: shell

	./komodod -ac_name=EXAMPLECHAIN -ac_supply=1000000 -addnode=<ipaddr of 1st node>

So, for example, the first node which spawned this new Assetchain had Public static IPv4 "123.123.123.123". The command for nodes connecting to this assetchain will look like this:

.. code-block:: shell

	./komodod -ac_name=EXAMPLECHAIN -ac_supply=1000000 -addnode=123.123.123.123

Secure this Assetchain with Delayed Proof of Work
=================================================

You can also setup your own Notary Nodes other than Official Komodo Notary Nodes.

These notary nodes will only be specific to your Assetchain, and will notarize the assetchain blocks to Komodo network. Since Komodo network is secured with DPoW by notarising it's blocks on to Bitcoin blockchain, Assetchains inherit that security via Komodo.

New ``komodod -ac`` Parameters
==============================

* New ``komodod -ac`` parameters for parallel chains. If ``-ac_reward=<satoshis>`` is non-zero, the chain will mine normally and start with ``-ac_reward`` for the block reward.

* If ``-ac_end=<endheight>`` is set, then ``-ac_reward`` will be ``0`` after ``endheight`` is reached.

* If ``-ac_halving=<halvingperiod>`` is set, then every ``<halvingperiod>`` blocks the block reward is reduced according to one of three methods. 1440 (approx a day) is the most frequent halving period.

* If ``-ac_decay`` is not set, then the normal bitcoin halving is done.

* If ``-ac_decay=<numerator>`` is set to be exactly ``100000000``, then the ``-ac_reward`` is scaled linearly toward ``0``, with ``0`` at ``endheight``.

For all other values of numerator (less than 100000000) the reward is iteratively reduced by the number of "halving" periods, ie.

.. code-block:: shell

    numhalvings = (height / -ac_halving);
    for (i=0; i<numhalvings; i++)
        reward = (reward * -ac_decay) / 100000000;

* If ``-ac_perc=<satoshis>`` is nonzero and less than equal ``100000000`` and ``-ac_pubkey=<secp_pubkey33>`` is set to a 33byte hexstr (len 66 starting with 02 or 03) then the txfee is increased by the commission rate indicated by ``-ac_perc``, with 100000000 being the max of 100%. wallets will need to be customised to make sure to pay the ``-ac_perc`` of transaction size as txfee. chains with a percentage override can only be mined by the ``-ac_pubkey address``.

Bitcoin behaviour would be ``-ac_reward=5000000000 -ac_halving=210000`` KMD behaviour would be ``-ac_reward = 300000000 -ac_end=7777777``

A more smoothly reducing reward that halves every 210000 blocks would be:

.. code-block:: shell

	-ac_reward=5000000000 -ac_halving=10000 -ac_decay=96777000 -ac_cc=1

-ac_staked=perc
===============

*(Currently available only in jl777 branch)*

We added PoW balancing to the ``-ac_staked``, so the ``-ac_staked=nn`` means target nn% of blocks to be staked and the rest PoW. 

.. code-block:: shell

	./komodod -ac_name=STEST3 -ac_staked=77 -ac_supply=100000000 -ac_reward=300000000 -addnode=136.243.58.134 &

In some cases it is desirable to have as secure a way to create blocks as possible without relying on hashrate. In order to achieve this the ``-ac_staked`` option has been created. The percentage parameter sets the target percentage of blocks that are generated via PoS.

The constraints of ``-ac_staked`` were to be a decent implementation that doesn't change the block or tx format so it can be fully compatible with the existing infrastructure of wallets, explorers, atomic swaps, etc. In order to achieve this a special tx is added to the block as the last transaction. This is the transaction that spends the utxo that staked the block.

The following are the (current) rules for staking a block:

	#. block timestamps are used as the monotonically increasing timestamp.

	#. In order to start staking you need to have ``-pubkey`` set

	#. A utxo is not eligible without ``nLockTime`` set and until 100*expected blocktimes has passed, 6000 seconds.

	#. There are 64 different subsets of addresses, based on the hash of the destination address. Each subset will take turns being subset0 at each height, ie. (height % 64) -> the subset0 for that height. All other subsets will adjust the elapsed time by subsetid seconds

	#. A new block is eligible to be staked, 1 seconds after median blocktime. By 64 seconds after the median blocktime, all subsets are eligible.

	#. Coinage calculated from the adjusted time is used to divide hash(address + pastblockhash) to create the value compared against the diff to determine if a block is won or not.

	#. This means that the first timestamp that a specific utxo is elibible to stake a block can be calculated ahead of time, using the largest eligible utxo.

The dividing of all the utxos into 64 subsets creates 64 independent competitions (within a one second window) to stake a block. In order for a 51% stakeholder to dominate staking blocks, the 51% would need to be allocated across 64 (or 33) different subsets, which then allows the remaining 49% to dominate within specific subsets. What percentage of stake is needed to dominate the block production is left to the mathematicians to calculate. In practice the usage of different subsets has the beneficial effect of reducing the number of eligible blocks arriving at close to the same time, ie. 64x less collisions. Whatever additional effects it has to make 51% domination of the chain is an added bonus.
