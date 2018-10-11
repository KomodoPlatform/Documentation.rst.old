*****************
rewardsaddfunding
*****************

Add your funds to a Rewards Plan
================================

Usage:
------

``rewardsaddfunding name fundingtxid amount``

Step 1: Create a raw transaction and get the HEX value
======================================================

Example Command:
----------------

.. code-block:: shell

    ./komodo-cli -ac_name=CCNG rewardsaddfunding FREE e020151cd81647b20aa45a0e6850216ae52d3e895443bbe1ae97dea3ae6767bd 100

Output:
-------

.. code-block:: json

    {
        "result": "success",
        "hex": "0100000001bd6767aea3de97aee1bb4354893e2de56a2150680e5aa40ab24716d81c1520e00200000048473044022050ab254c7498e411ab5360551148405c4afff28d68729e2bd00ba2508ab105d402204067ab95020d606c35d3604d4385dcb97c899a06aa8bf8ce30471fb7868ac7a401ffffffff0300e40b5402000000302ea22c802065686d47a4049c2c845a71895a915eb84c04445896eec5dc0be40df0b31372da8103120c008203000401ccd05eefb1fe080000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5ac00000000000000002c6a2ae5414652454500000000bd6767aea3de97aee1bb4354893e2de56a2150680e5aa40ab24716d81c1520e000000000"
    }

Step 2: Broadcast raw transaction
=================================

Example Command:
----------------

.. code-block:: shell

    ./komodo-cli -ac_name=CCNG sendrawtransaction 0100000001bd6767aea3de97aee1bb4354893e2de56a2150680e5aa40ab24716d81c1520e00200000048473044022050ab254c7498e411ab5360551148405c4afff28d68729e2bd00ba2508ab105d402204067ab95020d606c35d3604d4385dcb97c899a06aa8bf8ce30471fb7868ac7a401ffffffff0300e40b5402000000302ea22c802065686d47a4049c2c845a71895a915eb84c04445896eec5dc0be40df0b31372da8103120c008203000401ccd05eefb1fe080000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5ac00000000000000002c6a2ae5414652454500000000bd6767aea3de97aee1bb4354893e2de56a2150680e5aa40ab24716d81c1520e000000000

Output:
-------

``008ca94eebce8dbfa91491028c8861016ad4c25240f9ddc5616f2fb0853da580``

Step 3: Decode raw transaction (optional to check if the values are sane)
=========================================================================

Example Command:
----------------

.. code-block:: shell

    ./komodo-cli -ac_name=ATEST decoderawtransaction 0100000001bd6767aea3de97aee1bb4354893e2de56a2150680e5aa40ab24716d81c1520e00200000048473044022050ab254c7498e411ab5360551148405c4afff28d68729e2bd00ba2508ab105d402204067ab95020d606c35d3604d4385dcb97c899a06aa8bf8ce30471fb7868ac7a401ffffffff0300e40b5402000000302ea22c802065686d47a4049c2c845a71895a915eb84c04445896eec5dc0be40df0b31372da8103120c008203000401ccd05eefb1fe080000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5ac00000000000000002c6a2ae5414652454500000000bd6767aea3de97aee1bb4354893e2de56a2150680e5aa40ab24716d81c1520e000000000

Output:
-------

.. code-block:: json

    {
        "txid": "008ca94eebce8dbfa91491028c8861016ad4c25240f9ddc5616f2fb0853da580",
        "size": 277,
        "version": 1,
        "locktime": 0,
        "vin": [
            {
                "txid": "e020151cd81647b20aa45a0e6850216ae52d3e895443bbe1ae97dea3ae6767bd",
                "vout": 2,
                "scriptSig": {
                    "asm": "3044022050ab254c7498e411ab5360551148405c4afff28d68729e2bd00ba2508ab105d402204067ab95020d606c35d3604d4385dcb97c899a06aa8bf8ce30471fb7868ac7a401",
                    "hex": "473044022050ab254c7498e411ab5360551148405c4afff28d68729e2bd00ba2508ab105d402204067ab95020d606c35d3604d4385dcb97c899a06aa8bf8ce30471fb7868ac7a401"
                },
                "sequence": 4294967295
            }
        ],
        "vout": [
            {
                "value": 100.00000000,
                "valueSat": 10000000000,
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
                "value": 98899.99970000,
                "valueSat": 9889999970000,
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
                "value": 0.00000000,
                "valueSat": 0,
                "n": 2,
                "scriptPubKey": {
                    "asm": "OP_RETURN e5414652454500000000bd6767aea3de97aee1bb4354893e2de56a2150680e5aa40ab24716d81c1520e0",
                    "hex": "6a2ae5414652454500000000bd6767aea3de97aee1bb4354893e2de56a2150680e5aa40ab24716d81c1520e0",
                    "type": "nulldata"
                }
            }
        ],
        "vjoinsplit": []
    }

