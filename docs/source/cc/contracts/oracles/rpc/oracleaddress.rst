**************
oraclesaddress
**************

Oracle Contract Address
=======================

To display the oracle address for a specific pubkey.

Usage:
------

``oraclesaddress , oraclesaddress [pubkey]``

Example Command:
----------------

.. code-block:: shell

    ./komodo-cli -ac_name=CCNG oraclesaddress 03810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5

Output:
-------

.. code-block:: json

    {
        "result": "success",
        "OraclesCCaddress": "REt2C4ZMnX8YYX1DRpffNA4hECZTFm39e3",
        "Oraclesmarker": "RHkFKzn1csxA3fWzAsxsLWohoCgBbirXb5",
        "GatewaysPubkey": "03ea9c062b9652d8eff34879b504eda0717895d27597aaeb60347d65eed96ccb40",
        "OraclesCCassets": "RLh5sgvh3scCyM4aq1fhYhwgfbmb5SpCkT",
        "CCaddress": "RTk2Tgp1iAcxxSeuXYDREmtfydMvNkCmq8",
        "myCCaddress": "RTk2Tgp1iAcxxSeuXYDREmtfydMvNkCmq8",
        "myaddress": "RVXhz5UCJfSRoTfa4zvBFBrpDBbqMM21He"
    }

