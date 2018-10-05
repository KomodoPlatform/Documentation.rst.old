***********
Rewards RPC
***********

Rewards contract allows us to create a master-node like rewards program. Which gives a user the ability to earn rewards by locking coins.

APR and minimum deposit are configurable per rewards plan (there can be many active at any given time), even the required holding period.

.. note::

    If you create a plan with ``mindeposit: 10000``, make sure you have added 10000 + tx fees using the ``rewardsaddfunding`` call after creating the plan. The Rewards contract is set to require deposit amount of funding in rewards plan as assurance it will have the funds needed to pay.

Available RPC Calls
===================

* :doc:`rewardsaddfunding name fundingtxid amount <>`
* :doc:`rewardsaddress [pubkey] <>`
* :doc:`rewardscreatefunding name amount APR mindays maxdays mindeposit <>`
* :doc:`rewardsinfo fundingtxid <>`
* :doc:`rewardslist <>`
* :doc:`rewardslock name fundingtxid amount <>`
* :doc:`rewardsunlock name fundingtxid [txid] <>`
