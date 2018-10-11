********************
rewardscreatefunding
********************

Create new Rewards Funding
==========================

Usage:
------

``rewardscreatefunding name amount APR mindays maxdays mindeposit``

.. note::

    If you create a plan with mindeposit: 10000, make sure you have added 10000 + tx fees using the rewardsaddfunding call after creating the plan. The Rewards contract is set to require deposit amount of funding in rewards plan as assurance it will have the funds needed to pay.

Step 1: Create raw transaction HEX using your own parameter
===========================================================

For the example command we used

::

    name = FREE # Name of your Rewards plan
    amount = 1000 # Amount to start the Rewards plan
    APR = 5% # Annual percentage of rewards
    mindays = 1 # Minimum number of days the funds will be locked
    maxdays = 10 # Maximum number of days the funds will be locked
    mindeposit = 10 # Minimum deposit amount

Example Command:
----------------

.. code-block:: shell

    ./komodo-cli -ac_name=CCNG rewardscreatefunding FREE 1000 5 1 10 10

Output:
-------

.. code-block:: json

    {
        "result": "success",
        "hex": "010000000104f2435046f3ad452e76e53ec01429ae4f49d3322e8cc96da96b9e35d6ada70e0000000049483045022100ebd06f60dea0e1fbfc82fdb1f17ca265c63bae51cd2db558946871513f64453902207d4d39b2418a5206bd7ef4efb9130f93f304577e0c84cc79be4e8abe0c8b22fe01ffffffff0400e8764817000000302ea22c802065686d47a4049c2c845a71895a915eb84c04445896eec5dc0be40df0b31372da8103120c008203000401cc1027000000000000232103da60379d924c2c30ac290d2a86c2ead128cb7bd571f69211cb95356e2dcc5eb9ace069fb0501090000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5ac00000000000000002c6a2ae54646524545000000000065cd1d000000008051010000000000002f0d000000000000ca9a3b0000000000000000"
    }    

Step 2: Broadcast/send the raw hex/transaction
==============================================

This will output the txid which is the ``fundingtxid`` or the Rewards plan id.

Example Command:
----------------

.. code-block:: shell

    ./komodo-cli -ac_name=ATEST sendrawtransaction 010000000104f2435046f3ad452e76e53ec01429ae4f49d3322e8cc96da96b9e35d6ada70e0000000049483045022100ebd06f60dea0e1fbfc82fdb1f17ca265c63bae51cd2db558946871513f64453902207d4d39b2418a5206bd7ef4efb9130f93f304577e0c84cc79be4e8abe0c8b22fe01ffffffff0400e8764817000000302ea22c802065686d47a4049c2c845a71895a915eb84c04445896eec5dc0be40df0b31372da8103120c008203000401cc1027000000000000232103da60379d924c2c30ac290d2a86c2ead128cb7bd571f69211cb95356e2dcc5eb9ace069fb0501090000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5ac00000000000000002c6a2ae54646524545000000000065cd1d000000008051010000000000002f0d000000000000ca9a3b0000000000000000

Output:
-------

``e020151cd81647b20aa45a0e6850216ae52d3e895443bbe1ae97dea3ae6767bd``

Step 3: Decode the raw transaction (optional to check if the values are sane)
=============================================================================

Example Command:
----------------

.. code-block:: shell

    ./komodo-cli -ac_name=ATEST decoderawtransaction 010000000104f2435046f3ad452e76e53ec01429ae4f49d3322e8cc96da96b9e35d6ada70e0000000049483045022100ebd06f60dea0e1fbfc82fdb1f17ca265c63bae51cd2db558946871513f64453902207d4d39b2418a5206bd7ef4efb9130f93f304577e0c84cc79be4e8abe0c8b22fe01ffffffff0400e8764817000000302ea22c802065686d47a4049c2c845a71895a915eb84c04445896eec5dc0be40df0b31372da8103120c008203000401cc1027000000000000232103da60379d924c2c30ac290d2a86c2ead128cb7bd571f69211cb95356e2dcc5eb9ace069fb0501090000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5ac00000000000000002c6a2ae54646524545000000000065cd1d000000008051010000000000002f0d000000000000ca9a3b0000000000000000

Output:
-------

.. code-block:: json

    {
        "txid": "e020151cd81647b20aa45a0e6850216ae52d3e895443bbe1ae97dea3ae6767bd",
        "size": 322,
        "version": 1,
        "locktime": 0,
        "vin": [
            {
                "txid": "0ea7add6359e6ba96dc98c2e32d3494fae2914c03ee5762e45adf3465043f204",
                "vout": 0,
                "scriptSig": {
                    "asm": "3045022100ebd06f60dea0e1fbfc82fdb1f17ca265c63bae51cd2db558946871513f64453902207d4d39b2418a5206bd7ef4efb9130f93f304577e0c84cc79be4e8abe0c8b22fe01",
                    "hex": "483045022100ebd06f60dea0e1fbfc82fdb1f17ca265c63bae51cd2db558946871513f64453902207d4d39b2418a5206bd7ef4efb9130f93f304577e0c84cc79be4e8abe0c8b22fe01"
                },
                "sequence": 4294967295
            }
        ],
        "vout": [
            {
                "value": 1000.00000000,
                "valueSat": 100000000000,
                "n": 0,
                "scriptPubKey": {
                    "asm": "a22c802065686d47a4049c2c845a71895a915eb84c04445896eec5dc0be40df0b31372da8103120c008203000401 OP_CHECKCRYPTOCONDITION",
                    "hex": "2ea22c802065686d47a4049c2c845a71895a915eb84c04445896eec5dc0be40df0b31372da8103120c008203000401cc",
                    "reqSigs": 1,
                    "type": "cryptocondition",
                    "addresses": [
                        "RTsRBYL1HSvMoE3qtBJkyiswdVaWkm8YTK"
                    ]
                }
            },
            {
                "value": 0.00010000,
                "valueSat": 10000,
                "n": 1,
                "scriptPubKey": {
                    "asm": "03da60379d924c2c30ac290d2a86c2ead128cb7bd571f69211cb95356e2dcc5eb9 OP_CHECKSIG",
                    "hex": "2103da60379d924c2c30ac290d2a86c2ead128cb7bd571f69211cb95356e2dcc5eb9ac",
                    "reqSigs": 1,
                    "type": "pubkey",
                    "addresses": [
                        "RMgye9jeczNjQx9Uzq8no8pTLiCSwuHwkz"
                    ]
                }
            },
            {
                "value": 98999.99980000,
                "valueSat": 9899999980000,
                "n": 2,
                "scriptPubKey": {
                    "asm": "03810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5 OP_CHECKSIG",
                    "hex": "2103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5ac",
                    "reqSigs": 1,
                    "type": "pubkey",
                    "addresses": [
                        "RVXhz5UCJfSRoTfa4zvBFBrpDBbqMM21He"
                    ]
                }
            },
            {
                "value": 0.00000000,
                "valueSat": 0,
                "n": 3,
                "scriptPubKey": {
                    "asm": "OP_RETURN e54646524545000000000065cd1d000000008051010000000000002f0d000000000000ca9a3b00000000",
                    "hex": "6a2ae54646524545000000000065cd1d000000008051010000000000002f0d000000000000ca9a3b00000000",
                    "type": "nulldata"
                }
            }
        ],
        "vjoinsplit": []
    }

