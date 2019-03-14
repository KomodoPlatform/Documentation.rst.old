*******
Rewards
*******

Visit https://developers.komodoplatform.com/basic-docs/cryptoconditions/cc-rewards.html for the latest Documentation.

Rewards contract allows us to create a master-node like rewards program. Which gives a user the ability to earn rewards by locking coins.

APR, minimum deposit, required holding period are all configurable in each ``rewards`` plan (there can be many active at any given time).

The flow of a Rewards plan is as follows:

    * Anyone can create a new plan using ``rewardscreatefunding`` 
    * Anyone can add funding to the plan using ``rewardsaddfunding`` 
    * Anyone can query the list of all active plans using ``rewardslist`` 
    * Then get the details of a particular plan by using ``rewardsinfo`` 
    * After finding a plan that suits, any user can lock funds using ``rewardslock`` 
    * After the minimum lock time is met, the user can use ``rewardsunlock`` to unlock the funds and get the additional rewards too.

.. note::

    If you create a plan with ``mindeposit: 10000``, make sure you have added 10000 + tx fees using the ``rewardsaddfunding`` call after creating the plan. The Rewards contract won't allow locking of funds greater than the amount already locked in a single transaction as it needs to assure that it will have the required funds to pay.

