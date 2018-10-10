***********
Rewards RPC
***********

Rewards contract allows us to create a master-node like rewards program. Which gives a user the ability to earn rewards by locking coins.

APR, minimum deposit, required holding period are all configurable in each ``rewards`` plan (there can be many active at any given time).

The flow of a Rewards plan is as follows:

    * Anyone can create a new plan using the ``rewardscreatefunding`` RPC
    * Anyone can add funding to the plan using the ``rewardsaddfunding`` RPC
    * Anyone can query the list of all active plans using the ``rewardslist`` RPC
    * Then get the details of a particular plan by using the ``rewardsinfo`` RPC
    * After finding a plan that suits, any user can lock funds using the ``rewardslock`` RPC
    * After the minimum lock time is met, the user can use the ``rewardsunlock`` RPC to unlock the funds

.. note::

    If you create a plan with ``mindeposit: 10000``, make sure you have added 10000 + tx fees using the ``rewardsaddfunding`` call after creating the plan. The Rewards contract is set to require deposit amount of funding in rewards plan as assurance it will have the funds needed to pay.



Available RPC Calls
===================

* :doc:`rewardsaddfunding name fundingtxid amount <rpc/rewardsaddfunding>`
* :doc:`rewardsaddress [pubkey] <rpc/rewardsaddress>`
* :doc:`rewardscreatefunding name amount APR mindays maxdays mindeposit <rpc/rewardscreatefunding>`
* :doc:`rewardsinfo fundingtxid <rpc/rewardsinfo>`
* :doc:`rewardslist <rpc/rewardslist>`
* :doc:`rewardslock name fundingtxid amount <rpc/rewardslock>`
* :doc:`rewardsunlock name fundingtxid [txid] <rpc/rewardsunlock>`
