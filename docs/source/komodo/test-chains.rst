*****************
Test Asset Chains
*****************

The purpose of this is to give a better understanding of asset chain parameters via example. All chains must have at least ac_name and ac_supply set. The ac_pubkey parameters can be used with any of these chains. Without setting ac_perc, the only effect it has is having the genesis block mined to the corresponding address

1
*

ac_reward
=========

``./komodod -ac_name=1REW -ac_supply=999999 -ac_reward=100000000``

999999 coin premine 

1 coin block reward that does not end.

ac_halving
==========

``./komodod -ac_name=1HALV -ac_supply=999999 -ac_halving=2000``

999999 coin premine 

default block reward of .0001; on demand blocks after block 128

-ac_halving has no effect unless -ac_reward is set

ac_decay
========
``./komodod -ac_name=1DECAY -ac_supply=999999 -ac_decay=50000000 -addnode=$IP``
999999 coin premine
default block reward of .0001; on demand blocks after block 128
-ac_decay has no effect unless -ac_reward is set

ac_end
======

``./komodod -ac_name=1END -ac_supply=999999 -ac_end=25000 -addnode=$IP``

999999 coin premine

default block reward of .0001; on demand blocks after block 128

block reward end at block 25000


ac_perc_ac_pubkey
=================

``./komodod -ac_name=1PERC -ac_supply=999999 -ac_perc=5000000 -ac_pubkey=027dc7b5cfb5efca96674b45e9fda18df069d040b9fd9ff32c35df56005e330392``

if ac_perc is set, ac_reward must be set also.


this chain does not work at all because ac_reward is not set.


ac_staked
=========

``./komodod -ac_name=STAKETEST -ac_supply=999999 -ac_reward=100000000 -ac_staked=90``

999999 coin premine

1 coin block reward

Chain adjusts difficulty so 90% of blocks are proof of stake, 10% proof of work

It’s important to start staking immediately for high percentages of POS. If too many POW blocks are mined consecutively at the start of the chain, the POW difficulty may increase enough to stop the chain entirely, meaning you can’t send a transaction to staking nodes. 

2
*

ac_reward ac_halving
====================

``./komodod -ac_name=2REWHALV -ac_supply=999999 -ac_reward=500000000 -ac_halving=2000 -addnode=$IP``

999999 coin premine

5 coin block reward 

Block reward halves every 2000 blocks

ac_reward -ac_decay
===================

``./komodod -ac_name=2REWDECAY -ac_supply=999999 -ac_reward=500000000 -ac_decay=75000000 -addnode=$IP``

999999 coin premine

5 coin block reward

-ac_decay has no effect without -ac_halving.

ac_reward ac_end
================
``./komodod -ac_name=2REWEND -ac_supply=999999 -ac_reward=500000000 -ac_end=200``

999999 coin premine

5 coin block reward

block reward ends at block 200

ac_reward ac_perc_ac_pubkey
===========================

``./komodod -ac_name=2REWPERC -ac_supply=999999 -ac_perc=5000000 -ac_reward=500000000 -ac_pubkey=027dc7b5cfb5efca96674b45e9fda18df069d040b9fd9ff32c35df56005e330392``

999999 coin premine

5 coin block reward

Pubkey address receives .25 coin for every mined block(an additional 5% of block reward) 

Pubkey address receives an additional 5% for every transaction made on the chain. For example, if a transaction sends 100 coins, an additional 5 coins 
are created and sent to the pubkey address. 

ac_perc chains are currently incompatible with z-nomp. The coinbase transaction vout type must be pubkey as opposed to pubkeyhash. 

ac_reward ac_staked
===================

``./komodod -ac_name=STAKE2 -ac_supply=100000 -ac_reward=100000000 -ac_staked=2``

1000000 coin premine

10 coin block reward

2% POS blocks, 98% POW blocks

ac_halving -ac_decay
====================

``./komodod -ac_name=2HALVDECAY -ac_supply=999999 -ac_halving=2000 -ac_decay=50000000 -addnode=$IP``

999999 coin premine

default block reward of .0001; on demand blocks after block 128

ac_halving has no effect if ac_reward is not set

-ac_decay has no effect if ac_reward is not set

ac_halving ac_end
=================

``./komodod -ac_name=2HALVEND -ac_supply=999999 -ac_halving=2000 -ac_end=10000 -addnode=$IP``

999999 coin premine

default block reward of .0001; blocks are on-demand after block 128

block reward ends at block 10000

-ac_halving has no effect without ac_reward being set.

ac_halving ac_perc_ac_pubkey
============================

``./komodod -ac_name=2HALVPUB -ac_supply=999999 -ac_halving=2000 -ac_perc=5000000 -ac_pubkey=027dc7b5cfb5efca96674b45e9fda18df069d040b9fd9ff32c35df56005e330392``

if ac_perc is set, ac_reward must be set also.

This chain does not work at all because ac_reward is not set.

ac_halving has no effect if ac_reward is not set.

ac_halving ac_staked
====================

``./komodod -ac_name=2HALVSTAKE -ac_supply=999999 -ac_halving=2000 -ac_staked=10 -addnode=$IP``

default block reward of .0001

-ac_halving has no effect without ac_reward being set.

ac_decay ac_end
===============

``./komodod -ac_name=2ENDDECAY -ac_supply=999999 -ac_end=10000 -ac_decay=5000000 -addnode=$IP``

999999 coin premine

default block reward of .0001; blocks are on-demand after block 128

-ac_decay has no effect without -ac_reward set

ac_decay ac_perc_ac_pubkey
==========================

ac_perc does not work without setting ac_reward

ac_decay has no effect without setting ac_reward

If ac_perc is set, ac_reward must be set also.

This chain does not work at all because ac_reward is not set.

ac_decay ac_staked
==================

``./komodod -ac_name=2DECAYSTAKE -ac_supply=999999 -ac_decay=5000000 -ac_staked=50 -addnode=$IP``

default block reward of .0001

ac_decay has no effect without ac_reward set

50% of blocks are POS, 50% POW

ac_end ac_perc_ac_pubkey
========================

``./komodod -ac_name=2ENDPUB -ac_supply=999999 -ac_end=10000 -ac_perc=5000000 -ac_pubkey=027dc7b5cfb5efca96674b45e9fda18df069d040b9fd9ff32c35df56005e330392``

If ac_perc is set, ac_reward must be set also.

This chain does not work at all because ac_reward is not set.

ac_end ac_staked
================

``./komodod -ac_name=2ENDSTAKE -ac_supply=999999 -ac_end=10000 -ac_staked=5``

999999 coin premine

default block reward of .0001

block reward ends at block 10000

5% POS blocks, 95% POW blocks

ac_perc_ac_pubkey ac_staked
===========================

if ac_perc is set, ac_reward must be set also.

this chain does not work at all because ac_reward is not set.


3
*

ac_reward ac_halving ac_decay
=============================

``./komodod -ac_name=3REWHALVDEC -ac_supply=999999 -ac_reward=1000000000 -ac_halving=2000 -ac_decay=75000000``

999999 coin premine

10 coin block reward

Block reward decreases by 25% every 2000 blocks

ac_reward ac_halving ac_end
===========================

``./komodod -ac_name=3REWHALVEND -ac_supply=999999 -ac_reward=500000000 -ac_halving=2000 -ac_end=10000``

999999 coin premine

5 coin block reward

Block reward decreases by 50% every 2000 blocks

Block reward ends at block 10000

ac_reward ac_halving ac_perc_ac_pubkey
======================================

``./komodod -ac_name=3REWHALVPUB -ac_supply=999999 -ac_reward=500000000 -ac_halving=1440 -ac_pubkey=027dc7b5cfb5efca96674b45e9fda18df069d040b9fd9ff32c35df56005e330392 -ac_perc=50000000``

999999 coin premine

5 coin block reward

Block reward decreases by 50% every 1440 blocks.

The pubkey address receives an additional 50% of the block reward for each mined block. For example, before the first halving, the pubkey address will receive 2.5 coins(50% of 5 coin block reward) for every mined block. After the first halving, the pubkey address will receive an additional 1.25 coins.

The pubkey address receives an additional 50% for every transaction made on the chain. For example, if a transaction sends 100 coins, an additional 50 coins are created and sent to the pubkey address. 

ac_perc chains are currently incompatible with z-nomp. The coinbase transaction vout type must be pubkey as opposed to pubkeyhash. 


ac_reward ac_halving ac_staked
==============================

``./komodod -ac_name=3REWHALVSTAKE -ac_supply=999999 -ac_reward=100000000 -ac_havling=2000 -ac_staked=10``

999999 coin premine

1 coin block reward

block reward decreases by 50% every 2000 blocks

10% of blocks are POS, 90% POW

ac_reward -ac_decay ac_end
==========================

``./komodod -ac_name=3REWDECEND -ac_supply=999999 -ac_reward=500000000 -ac_decay=75000000 -ac_end=5000``

999999 coin premine

5 coin block reward

Block reward ends at block 5000.

-ac_decay has no effect without -ac_halving set

ac_reward -ac_decay ac_perc_ac_pubkey
=====================================

``./komodod -ac_name=3REWDECPUB -ac_supply=999999 -ac_reward=500000000  -ac_decay=75000000 -ac_perc=10000000 -ac_pubkey=027dc7b5cfb5efca96674b45e9fda18df069d040b9fd9ff32c35df56005e330392``

999999 coin premine

5 coin block reward

Pubkey address receives .5 coin for every mined block(an additional 10% of block reward) 

Pubkey address receives an additional 10% for every transaction made on the chain. For example, if a transaction sends 100 coins, an additional 10 coins are created and sent to the pubkey address. 

ac_perc chains are currently incompatible with z-nomp. The coinbase transaction vout type must be pubkey as opposed to pubkeyhash. 

ac_reward -ac_decay ac_staked
=============================

``./komodod -ac_name=3REWDECSTAKE -ac_supply=999999 -ac_reward=1000000000 -ac_decay=25000000 -ac_staked=50``

999999 coin premine

10 coin block reward

50% POS blocks, 50% POW blocks

-ac_decay has no effect if -ac_halving is not set

ac_reward ac_end ac_perc_ac_pubkey
==================================

``./komodod -ac_name=3ENDPUBREW -ac_supply=999999 -ac_reward=5000000000 -ac_end=10000 -ac_perc=5000000 -ac_pubkey=027dc7b5cfb5efca96674b45e9fda18df069d040b9fd9ff32c35df56005e330392``

999999 coin premine

50 coin block reward

Block reward ends at block 10000.

Pubkey address receives 2.5 coins for every mined block(an additional 5% of block reward) 

Pubkey address receives an additional 5% for every transaction made on the chain. For example, if a transaction sends 100 coins, an additional 5 coins are created and sent to the pubkey address. 

ac_perc chains are currently incompatible with z-nomp. The coinbase transaction vout type must be pubkey as opposed to pubkeyhash. 

ac_reward ac_end ac_staked
==========================

``./komodod -ac_name=3REWENDSTAKE -ac_supply=500000 -ac_reward=10000000000 -ac_end=15000 -ac_staked=60``

500000 coin premine

100 coin block reward

block reward ends at block 15000

60% POS, 40% POW

ac_reward ac_perc_ac_pubkey ac_staked
=====================================

``./komodod -ac_name=3REWPERCSTAKE -ac_supply=1000000 -ac_reward=1000000000 -ac_perc=10000000 -ac_pubkey=027dc7b5cfb5efca96674b45e9fda18df069d040b9fd9ff32c35df56005e330392 -ac_staked=50``

1000000 coin premine

10 coin block reward

50% POS, 50% POW

Pubkey address receives 1 coin for every mined block(an additional 10% of block reward) 

Pubkey address receives an additional 10% for every transaction made on the chain. For example, if a transaction sends 100 coins, an additional 5 coins are created and sent to the pubkey address. This includes the additional verification transaction in POS blocks, meaning the pubkey address receives more coins for every POS block.

ac_perc chains are currently incompatible with z-nomp. The coinbase transaction vout type must be pubkey as opposed to pubkeyhash. 

ac_halving -ac_decay ac_end
===========================

``./komodod -ac_name=3HALVDECEND -ac_supply=999999 -ac_end=100000 -ac_halving=5000 -ac_end=100000``

999999 coin premine

Default block reward of .0001; Blocks are on-demand after block 128.

Block reward ends at block 100000.

ac_halving has no effect if ac_reward is not set.

ac_halving -ac_decay ac_perc_ac_pubkey
======================================

If ac_perc is set, ac_reward must be set also.
This chain does not work at all because ac_reward is not set.
ac_halving has no effect if ac_reward is not set.

ac_halving -ac_decay ac_staked
==============================

ac_halving has no effect if ac_reward is not set

ac_halving ac_end ac_perc_ac_pubkey
===================================

If ac_perc is set, ac_reward must be set also.

This chain does not work at all because ac_reward is not set.

ac_halving has no effect if ac_reward is not set.

ac_halving ac_end ac_staked
===========================

ac_halving has no effect if ac_reward is not set

ac_halving ac_perc_ac_pubkey ac_staked
======================================

if ac_perc is set, ac_reward must be set also.
this chain does not work at all because ac_reward is not set.

ac_decay ac_end ac_perc_ac_pubkey
=================================

if ac_perc is set, ac_reward must be set also.
this chain does not work at all because ac_reward is not set.
-ac_decay has no effect without -ac_halving set

ac_decay ac_end ac_staked
=========================

ac_decay has no effect without -ac_halving set

ac_decay ac_perc_ac_pubkey ac_staked
====================================

if ac_perc is set, ac_reward must be set also.
this chain does not work at all because ac_reward is not set.
-ac_decay has no effect without -ac_halving set

ac_end ac_perc_ac_pubkey ac_staked
==================================

if ac_perc is set, ac_reward must be set also.
this chain does not work at all because ac_reward is not set.

4
*

ac_reward ac_halving -ac_decay ac_end
=====================================

``./komodod -ac_name=4REWHALVDECEND -ac_supply=1000000 -ac_reward=10000000000 -ac_halving=10000 -ac_decay=25000000 -ac_end=100000``

1000000 coin premine

100 coin block reward

Block reward decreases by 75% every 10000 blocks.

Block reward ends at block 100000.

ac_reward ac_halving -ac_decay ac_perc_ac_pubkey
================================================

``./komodod -ac_name=4REWHALVDECPUB -ac_supply=999999 -ac_reward=1000000000 -ac_halving=5000 -ac_decay=60000000 -ac_perc=5000000 -ac_pubkey=027dc7b5cfb5efca96674b45e9fda18df069d040b9fd9ff32c35df56005e330392``

999999 coin premine

10 coin block reward

Block reward decreases 40% every 5000 blocks

The pubkey address receives an additional 5% of the block reward for each mined block. For example, before the first halving, the pubkey address will receive 0.5 coins(5% of 10 coin block reward) for every mined block. After the first halving, the pubkey address will receive an additional 0.3 coins.(5% of 6 coin block reward)

Pubkey address receives an additional 5% for every transaction made on the chain. For example, if a transaction sends 100 coins, an additional 5 coins 
are created and sent to the pubkey address. 

ac_perc chains are currently incompatible with z-nomp. The coinbase transaction vout type must be pubkey as opposed to pubkeyhash. 

ac_reward ac_halving -ac_decay ac_staked
========================================

``./komodod -ac_name=4REWHALVDECSTAKE -ac_supply=99999 -ac_reward=1000000000000 -ac_halving=2000 -ac_decay=60000000 -ac_staked=50``

99999 coin premine

10000 coin block reward

Block reward decreases by 40% every 2000 blocks.

50% POS blocks, 50% POW blocks

ac_reward ac_halving ac_end ac_perc_ac_pubkey
=============================================

``./komodod -ac_name=4REWPUBENDHALV -ac_supply=999999 -ac_halving=2000 -ac_reward=1000000000 -ac_end=60005 -ac_pubkey=027dc7b5cfb5efca96674b45e9fda18df069d040b9fd9ff32c35df56005e330392 -ac_perc=10000000``

999999 coin premine

10 coin block reward

Block reward decreases by 50% every 2000 blocks.

Block reward ends at block 60005

The pubkey address receives an additional 10% of the block reward for each mined block. For example, before the first halving, the pubkey address will receive 1 coin(10% of 10 coin block reward) for every mined block. After the first halving, the pubkey address will receive an additional 0.5 coins.
Pubkey address receives an additional 10% for every transaction made on the chain. For example, if a transaction sends 100 coins, an additional 10 coins are created and sent to the pubkey address. 

ac_perc chains are currently incompatible with z-nomp. The coinbase transaction vout type must be pubkey as opposed to pubkeyhash. 

ac_reward ac_halving ac_end ac_staked
=====================================

``./komodod -ac_name=4REWHALVENDSTAKE -ac_supply=99999 -ac_reward=10000000 -ac_halving=5000 -ac_end=50000 -ac_staked=40``

99999 coin premine

0.1 coin block reward

Block reward decreases by 50% every 5000 blocks.

Block reward ends at block 50000.

40% POS blocks, 60% POW blocks

ac_reward ac_halving ac_perc_ac_pubkey ac_staked
================================================

``./komodod -ac_name=4PUBREWHALVSTAKE -ac_supply=999999 -ac_reward=1000000000 -ac_halving=2000 -ac_perc=5000000 -ac_staked=50 -ac_pubkey=027dc7b5cfb5efca96674b45e9fda18df069d040b9fd9ff32c35df56005e330392``

999999 coin premine

10 coin block reward

Block reward decreases by 50% every 2000 blocks.

50% POS blocks, 50% POW blocks

The pubkey address receives an additional 5% of the block reward for each mined block. For example, before the first halving, the pubkey address will receive 0.5 coin(5% of 10 coin block reward) for every mined block. After the first halving, the pubkey address will receive an additional 0.25 coins.

Pubkey address receives an additional 5% for every transaction made on the chain. For example, if a transaction sends 100 coins, an additional 5 coins are created and sent to the pubkey address. 

ac_perc chains are currently incompatible with z-nomp. The coinbase transaction vout type must be pubkey as opposed to pubkeyhash. 

ac_reward -ac_decay ac_end ac_perc_ac_pubkey
============================================

-ac_decay has no effect without -ac_halving set.

ac_reward -ac_decay ac_end ac_staked
====================================

-ac_decay has no effect without -ac_halving set

ac_reward -ac_decay ac_perc_ac_pubkey ac_staked
===============================================

-ac_decay has no effect without -ac_halving set

ac_reward ac_end ac_perc_ac_pubkey ac_staked
============================================

``./komodod -ac_name=4REWENDPERCSTAKE -ac_supply=999999 -ac_reward=5000000000 -ac_end=10000 -ac_staked=33 -ac_perc=1000000 -ac_pubkey=027dc7b5cfb5efca96674b45e9fda18df069d040b9fd9ff32c35df56005e330392``

999999 coin premine

50 coin block reward

Block rewards ends at block 10000.

33% POS, 67% POW

Pubkey address receives 0.5 coin for every mined block(an additional 1% of block reward) 

Pubkey address receives an additional 1% for every transaction made on the chain. For example, if a transaction sends 100 coins, 1 additional coin is created and sent to the pubkey address. This includes the additional verification transaction in POS blocks, meaning the pubkey address receives more coins for every POS block.

ac_perc chains are currently incompatible with z-nomp. The coinbase transaction vout type must be pubkey as opposed to pubkeyhash. 

ac_halving -ac_decay ac_end ac_perc_ac_pubkey
=============================================

ac_halving has no effect if ac_reward is not set
if ac_perc is set, ac_reward must be set also.
this chain does not work at all because ac_reward is not set.

ac_halving -ac_decay ac_end ac_staked
=====================================

ac_halving has no effect if ac_reward is not set

ac_halving -ac_decay ac_perc_ac_pubkey ac_staked
================================================

ac_halving has no effect if ac_reward is not set

if ac_perc is set, ac_reward must be set also.

this chain does not work at all because ac_reward is not set.

ac_halving ac_end ac_perc_ac_pubkey ac_staked
=============================================

ac_halving has no effect if ac_reward is not set

If ac_perc is set, ac_reward must be set also.

This chain does not work at all because ac_reward is not set.

ac_decay ac_end ac_perc_ac_pubkey ac_staked
===========================================

If ac_perc is set, ac_reward must be set also.

This chain does not work at all because ac_reward is not set.

-ac_decay has no effect without -ac_halving set


5
*

ac_reward ac_halving -ac_decay ac_end ac_perc_ac_pubkey
=======================================================

``./komodod -ac_name=5REWHALVDECENDPERC -ac_supply=999999 -ac_reward=10000000000 -ac_halving=10000 -ac_decay=75000000 -ac_end=100000 -ac_perc=2000000 -ac_pubkey=027dc7b5cfb5efca96674b45e9fda18df069d040b9fd9ff32c35df56005e330392``

999999 coin premine

100 coin block reward

Block reward reduces by 25% every 10000 blocks.

Block reward ends at block 100000.

The pubkey address receives an additional 2% of the block reward for each mined block. For example, before the first halving, the pubkey address will receive 2 coins(2% of 100 coin block reward) for every mined block. After the first halving, the pubkey address will receive an additional 1.5 coins.(2% of 75 coin block reward)

Pubkey address receives an additional 2% for every transaction made on the chain. For example, if a transaction sends 100 coins, an additional 2 coins are created and sent to the pubkey address. 

ac_perc chains are currently incompatible with z-nomp. The coinbase transaction vout type must be pubkey as opposed to pubkeyhash. 

ac_reward ac_halving -ac_decay ac_end ac_staked
===============================================

``./komodod -ac_name=5REWHALVDECENDSTAKE -ac_supply=50000 -ac_reward=500000000 -ac_halving=5000 -ac_decay=75000000 -ac_end=100000 -ac_staked=80``

50000 coin premine

5 coin block reward

Block reward decreases by 25% every 5000 blocks.

Block reward ends at block 100000.

80% POS, 20% POW


ac_reward ac_halving -ac_decay ac_perc_ac_pubkey ac_staked
==========================================================

``./komodod -ac_name=5REWHALVDECPERCSTAKE -ac_supply=1 -ac_reward=50000000000 -ac_halving=2000 -ac_decay=25000000 -ac_perc=1000000 -ac_pubkey=027dc7b5cfb5efca96674b45e9fda18df069d040b9fd9ff32c35df56005e330392 -ac_staked=50``

1 coin coin premine

500 coin block reward

Block reward decreases by 75% every 2000 blocks.

50% POS blocks, 50% POW blocks

The pubkey address receives an additional 1% of the block reward for each mined block. For example, before the first halving, the pubkey address will receive 5 coins(1% of 500 coin block reward) for every mined block. After the first halving, the pubkey address will receive an additional 1.25 coins.(1% of 125 block reward)

Pubkey address receives an additional 1% for every transaction made on the chain. For example, if a transaction sends 100 coins, an additional 5 coins are created and sent to the pubkey address. This includes the additional verification transaction in POS blocks, meaning the pubkey address receives more coins for every POS block.

ac_perc chains are currently incompatible with z-nomp. The coinbase transaction vout type must be pubkey as opposed to pubkeyhash. 


ac_reward ac_halving ac_end ac_perc_ac_pubkey ac_staked
=======================================================

``./komodod -ac_name=5REWHALVENDPERCSTAKE -ac_supply=100 -ac_reward=100000000 -ac_halving=20000 -ac_end=100000 -ac_perc=1000000 -ac_pubkey=027dc7b5cfb5efca96674b45e9fda18df069d040b9fd9ff32c35df56005e330392 -ac_staked=90``

100 coin premine

1 coin block reward

Block reward decreases by 50% every 20000 blocks.

Block reward ends at block 100000.

90% POS, 10% POW

The pubkey address receives an additional 1% of the block reward for each mined block. For example, before the first halving, the pubkey address will receive 0.01 coin(1% of 1 coin block reward) for every mined block. After the first halving, the pubkey address will receive an additional 0.005 coin.(1% of 0.5 block reward)

Pubkey address receives an additional 1% for every transaction made on the chain. For example, if a transaction sends 100 coins, 1 additional coin is created and sent to the pubkey address. This includes the additional verification transaction in POS blocks, meaning the pubkey address receives more coins for every POS block.

ac_perc chains are currently incompatible with z-nomp. The coinbase transaction vout type must be pubkey as opposed to pubkeyhash.

ac_reward -ac_decay ac_end ac_perc_ac_pubkey ac_staked
======================================================

-ac_decay has no effect without -ac_halving set

ac_halving -ac_decay ac_end ac_perc_ac_pubkey ac_staked
=======================================================

ac_halving has no effect if ac_reward is not set

If ac_perc is set, ac_reward must be set also.

This chain does not work at all because ac_reward is not set.

6
*

ac_reward ac_halving -ac_decay ac_end ac_perc_ac_pubkey ac_staked
=================================================================

``./komodod -ac_name=6REWHALVDECENDPERCSTAKE -ac_supply=100000000 -ac_reward=100000000000 -ac_halving=100000 -ac_decay=75000000 -ac_end=1000000 -ac_perc=500000 -ac_pubkey=027dc7b5cfb5efca96674b45e9fda18df069d040b9fd9ff32c35df56005e330392 -ac_staked=1``

100000000 coin premine

1000 coin block reward

Block reward decreases by 25% every 100000 blocks

Block reward ends at block 1000000
fac_end
1% POS, 99% POW

The pubkey address receives an additional 0.5% of the block reward for each mined block. For example, before the first halving, the pubkey address will receive 5 coins(0.5% of 1000 coin block reward) for every mined block. After the first halving, the pubkey address will receive an additional 3.75 coins.(0.5% of 750 block reward)
Pubkey address receives an additional 0.5% for every transaction made on the chain. For example, if a transaction sends 100 coins, an additional 0.5 coin are created and sent to the pubkey address. This includes the additional verification transaction in POS blocks, meaning the pubkey address receives more coins for every POS block.
ac_perc chains are currently incompatible with z-nomp. The coinbase transaction vout type must be pubkey as opposed to pubkeyhash.
