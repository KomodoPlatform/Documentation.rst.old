***********
rewardsinfo
***********

Information about specific reward contract
==========================================

Usage:
------

``rewardsinfo``

Terminology
-----------

::

    name = Name of the Rewards plan
    sbits = The first 8 chars of the name as a 64 bit int
    APR = Annual percentage of Rewards
    minseconds = Minimum time the funds will be locked in seconds
    maxseconds = Maximum time the funds will be locked in seconds
    mindeposit = Minimum deposit amount
    funding = The amount of funds the rewards plan contains

Example Command:
----------------

.. code-block:: shell

    ./komodo-cli -ac_name=CCNG rewardsinfo e020151cd81647b20aa45a0e6850216ae52d3e895443bbe1ae97dea3ae6767bd

Output:
-------

.. code-block:: json

    {
        "result": "success",
        "fundingtxid": "e020151cd81647b20aa45a0e6850216ae52d3e895443bbe1ae97dea3ae6767bd",
        "name": "FREE",
        "sbits": 1162170950,
        "APR": "5.00000000",
        "minseconds": 86400,
        "maxseconds": 864000,
        "mindeposit": "10.00000000",
        "funding": "1100.00000000",
        "locked": "200.00000000"
    }

