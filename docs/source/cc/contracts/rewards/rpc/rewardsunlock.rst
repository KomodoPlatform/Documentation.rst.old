*************
rewardsunlock
*************

Unlock Rewards 
==============

This will unlock your funds from specific Rewards Plan after the minimum lock time is met. Otherwise, you will get the following error:

::

    {
      "result": "error",
      "error": "reward 0 is <= the transaction fee"
    }

And the following prints in the console:

::

    APR 5.00000000 minseconds.86400 maxseconds.864000 mindeposit 10.00000000
    duration 74628 < minseconds 86400
    reward 0 is <= the transaction fee
    amount 200.00000000 -> reward 0.00000000

Usage: 
------

``rewardsunlock name fundingtxid [txid]``

Step 1: Create raw transaction
==============================

Example Command:
----------------

.. code-block:: shell

    ./komodo-cli -ac_name=CCNG rewardsunlock FREE e020151cd81647b20aa45a0e6850216ae52d3e895443bbe1ae97dea3ae6767bd 494c4e8ab19ab73db9fde0454762e50ff3621d9708170083ea9d925918ec0263

Output:
-------



Step 2: Broadcast raw transaction
=================================

Example Command:
----------------

Output:
-------



Step 3: Decode raw transaction (optional to check if the values are sane)
=========================================================================

Example Command:
----------------

Output:
-------


