***********
rewardslock
***********

Lock Rewards
============

This will lock your funds for rewards to the specified Rewards Plan.

Usage:
------

``rewardslock name fundingtxid amount``

Step 1: Create raw transaction
==============================

Example Command:
----------------

.. code-block:: shell

    ./komodo-cli -ac_name=CCNG rewardslock FREE e020151cd81647b20aa45a0e6850216ae52d3e895443bbe1ae97dea3ae6767bd 200

Output:
-------

.. code-block:: json

    {
        "result": "success",
        "hex": "010000000180a53d85b02f6f61c5ddf94052c2d46a0161888c029114a9bf8dceeb4ea98c000100000049483045022100cf5581a6729eb0f37d03f0975dd6cfaca79ea08d380dae7df25b2335931bff5d02204feaf188f7f28d90c056a7b2bfa1f8d38fdf242c333470cf1e0cd3534ef1609701ffffffff0400c817a804000000302ea22c802065686d47a4049c2c845a71895a915eb84c04445896eec5dc0be40df0b31372da8103120c008203000401cc1027000000000000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5acb048d709fa080000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5ac00000000000000002c6a2ae54c4652454500000000bd6767aea3de97aee1bb4354893e2de56a2150680e5aa40ab24716d81c1520e000000000"
    }

Step 2: Broadcast raw transaction
=================================

Example Command:
----------------

.. code-block:: shell

    ./komodo-cli -ac_name=ATEST sendrawtransaction 010000000180a53d85b02f6f61c5ddf94052c2d46a0161888c029114a9bf8dceeb4ea98c000100000049483045022100cf5581a6729eb0f37d03f0975dd6cfaca79ea08d380dae7df25b2335931bff5d02204feaf188f7f28d90c056a7b2bfa1f8d38fdf242c333470cf1e0cd3534ef1609701ffffffff0400c817a804000000302ea22c802065686d47a4049c2c845a71895a915eb84c04445896eec5dc0be40df0b31372da8103120c008203000401cc1027000000000000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5acb048d709fa080000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5ac00000000000000002c6a2ae54c4652454500000000bd6767aea3de97aee1bb4354893e2de56a2150680e5aa40ab24716d81c1520e000000000

Output:
-------

``494c4e8ab19ab73db9fde0454762e50ff3621d9708170083ea9d925918ec0263``

Step 3: Decode raw transaction (optional to check if the values are sane)
=========================================================================

Example Command:
----------------

.. code-block:: shell

    ./komodo-cli -ac_name=ATEST decoderawtransaction 010000000180a53d85b02f6f61c5ddf94052c2d46a0161888c029114a9bf8dceeb4ea98c000100000049483045022100cf5581a6729eb0f37d03f0975dd6cfaca79ea08d380dae7df25b2335931bff5d02204feaf188f7f28d90c056a7b2bfa1f8d38fdf242c333470cf1e0cd3534ef1609701ffffffff0400c817a804000000302ea22c802065686d47a4049c2c845a71895a915eb84c04445896eec5dc0be40df0b31372da8103120c008203000401cc1027000000000000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5acb048d709fa080000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5ac00000000000000002c6a2ae54c4652454500000000bd6767aea3de97aee1bb4354893e2de56a2150680e5aa40ab24716d81c1520e000000000

Output:
-------

.. code-block:: json

    {
        "txid": "494c4e8ab19ab73db9fde0454762e50ff3621d9708170083ea9d925918ec0263",
        "size": 322,
        "version": 1,
        "locktime": 0,
        "vin": [
            {
                "txid": "008ca94eebce8dbfa91491028c8861016ad4c25240f9ddc5616f2fb0853da580",
                "vout": 1,
                "scriptSig": {
                    "asm": "3045022100cf5581a6729eb0f37d03f0975dd6cfaca79ea08d380dae7df25b2335931bff5d02204feaf188f7f28d90c056a7b2bfa1f8d38fdf242c333470cf1e0cd3534ef1609701",
                    "hex": "483045022100cf5581a6729eb0f37d03f0975dd6cfaca79ea08d380dae7df25b2335931bff5d02204feaf188f7f28d90c056a7b2bfa1f8d38fdf242c333470cf1e0cd3534ef1609701"
                },
                "sequence": 4294967295
            }
        ],
        "vout": [
            {
                "value": 200.00000000,
                "valueSat": 20000000000,
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
                "value": 98699.99950000,
                "valueSat": 9869999950000,
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
                    "asm": "OP_RETURN e54c4652454500000000bd6767aea3de97aee1bb4354893e2de56a2150680e5aa40ab24716d81c1520e0",
                    "hex": "6a2ae54c4652454500000000bd6767aea3de97aee1bb4354893e2de56a2150680e5aa40ab24716d81c1520e0",
                    "type": "nulldata"
                }
            }
        ],
        "vjoinsplit": []
    }

