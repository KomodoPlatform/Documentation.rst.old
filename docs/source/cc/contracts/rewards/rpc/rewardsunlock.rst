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

.. code-block:: json

    {
        "result": "success",
        "hex": "01000000026302ec1859929dea83001708971d62f30fe5624745e0fdb93db79ab18a4e4c49000000007b4c79a276a072a26ba067a565802103da60379d924c2c30ac290d2a86c2ead128cb7bd571f69211cb
95356e2dcc5eb98140dd5c7a6e8436748501608056b934a6b6cd54122f9451a1ca76f3d41568cb0e7a08e4d4f9045083425f42a4171e42b2d32f5e331f87d5b45298e006b909c706d2a100af038001e5a10001ffffffff
45fc2d61dd7bf709409c3e5b9021ebd6191901a2a43fa7ed2704c03aa0d3a682000000007b4c79a276a072a26ba067a565802103da60379d924c2c30ac290d2a86c2ead128cb7bd571f69211cb95356e2dcc5eb9814011
825693143f97dc51d34b47638f314146c20c92b5020673fb7411ab37018c2003870255e17d87d46b7af7d042335579de566ce492fd8c3c4e883253870ba329a100af038001e5a10001ffffffff0349f04c481700000030
2ea22c802065686d47a4049c2c845a71895a915eb84c04445896eec5dc0be40df0b31372da8103120c008203000401cca79841a804000000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523
318047b5ac00000000000000002c6a2ae5554652454500000000bd6767aea3de97aee1bb4354893e2de56a2150680e5aa40ab24716d81c1520e000000000"
    }

Step 2: Broadcast raw transaction
=================================

Example Command:
----------------

.. code-block:: shell

    ./komodo-cli -ac_name=CCNG sendrawtransaction 01000000026302ec1859929dea83001708971d62f30fe5624745e0fdb93db79ab18a4e4c49000000007b4c79a276
a072a26ba067a565802103da60379d924c2c30ac290d2a86c2ead128cb7bd571f69211cb95356e2dcc5eb98140dd5c7a6e8436748501608056b934a6b6cd54122f9451a1ca76f3d41568cb0e7a08e4d4f9045083425f42
a4171e42b2d32f5e331f87d5b45298e006b909c706d2a100af038001e5a10001ffffffff45fc2d61dd7bf709409c3e5b9021ebd6191901a2a43fa7ed2704c03aa0d3a682000000007b4c79a276a072a26ba067a5658021
03da60379d924c2c30ac290d2a86c2ead128cb7bd571f69211cb95356e2dcc5eb9814011825693143f97dc51d34b47638f314146c20c92b5020673fb7411ab37018c2003870255e17d87d46b7af7d042335579de566ce4
92fd8c3c4e883253870ba329a100af038001e5a10001ffffffff0349f04c4817000000302ea22c802065686d47a4049c2c845a71895a915eb84c04445896eec5dc0be40df0b31372da8103120c008203000401cca79841
a804000000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5ac00000000000000002c6a2ae5554652454500000000bd6767aea3de97aee1bb4354893e2de56a2150680e5aa40ab2
4716d81c1520e000000000

Output:
-------

``7a69605f5ecfeb0613c8573cbc4ae2471698a65b60c983ec21fb41f09975c000``

Step 3: Decode raw transaction (optional to check if the values are sane)
=========================================================================

Example Command:
----------------

.. code-block:: shell

    ./komodo-cli -ac_name=CCNG decoderawtransaction 01000000026302ec1859929dea83001708971d62f30fe5624745e0fdb93db79ab18a4e4c49000000007b4c79a2
76a072a26ba067a565802103da60379d924c2c30ac290d2a86c2ead128cb7bd571f69211cb95356e2dcc5eb98140dd5c7a6e8436748501608056b934a6b6cd54122f9451a1ca76f3d41568cb0e7a08e4d4f9045083425f
42a4171e42b2d32f5e331f87d5b45298e006b909c706d2a100af038001e5a10001ffffffff45fc2d61dd7bf709409c3e5b9021ebd6191901a2a43fa7ed2704c03aa0d3a682000000007b4c79a276a072a26ba067a56580
2103da60379d924c2c30ac290d2a86c2ead128cb7bd571f69211cb95356e2dcc5eb9814011825693143f97dc51d34b47638f314146c20c92b5020673fb7411ab37018c2003870255e17d87d46b7af7d042335579de566c
e492fd8c3c4e883253870ba329a100af038001e5a10001ffffffff0349f04c4817000000302ea22c802065686d47a4049c2c845a71895a915eb84c04445896eec5dc0be40df0b31372da8103120c008203000401cca798
41a804000000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5ac00000000000000002c6a2ae5554652454500000000bd6767aea3de97aee1bb4354893e2de56a2150680e5aa40a
b24716d81c1520e000000000

Output:
-------

.. code-block:: json

    {
        "txid": "7a69605f5ecfeb0613c8573cbc4ae2471698a65b60c983ec21fb41f09975c000",
        "size": 492,
        "version": 1,
        "locktime": 0,
        "vin": [
            {
                "txid": "494c4e8ab19ab73db9fde0454762e50ff3621d9708170083ea9d925918ec0263",
                "vout": 0,
                "scriptSig": {
                    "asm": "a276a072a26ba067a565802103da60379d924c2c30ac290d2a86c2ead128cb7bd571f69211cb95356e2dcc5eb98140dd5c7a6e8436748501608056b934a6b6cd54122f9451a1ca76f3d41568cb0e7a
08e4d4f9045083425f42a4171e42b2d32f5e331f87d5b45298e006b909c706d2a100af038001e5a10001",
        "hex": "4c79a276a072a26ba067a565802103da60379d924c2c30ac290d2a86c2ead128cb7bd571f69211cb95356e2dcc5eb98140dd5c7a6e8436748501608056b934a6b6cd54122f9451a1ca76f3d41568cb
0e7a08e4d4f9045083425f42a4171e42b2d32f5e331f87d5b45298e006b909c706d2a100af038001e5a10001"
                },
                "sequence": 4294967295
            },
            {
                "txid": "82a6d3a03ac00427eda73fa4a2011919d6eb21905b3e9c4009f77bdd612dfc45",
                "vout": 0,
                "scriptSig": {
                    "asm": "a276a072a26ba067a565802103da60379d924c2c30ac290d2a86c2ead128cb7bd571f69211cb95356e2dcc5eb9814011825693143f97dc51d34b47638f314146c20c92b5020673fb7411ab37018c20
03870255e17d87d46b7af7d042335579de566ce492fd8c3c4e883253870ba329a100af038001e5a10001",
        "hex": "4c79a276a072a26ba067a565802103da60379d924c2c30ac290d2a86c2ead128cb7bd571f69211cb95356e2dcc5eb9814011825693143f97dc51d34b47638f314146c20c92b5020673fb7411ab3701
8c2003870255e17d87d46b7af7d042335579de566ce492fd8c3c4e883253870ba329a100af038001e5a10001"
                },
                "sequence": 4294967295
            }
        ],
        "vout": [
            {
                "value": 999.97249609,
                "valueSat": 99997249609,
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
                "value": 200.02740391,
                "valueSat": 20002740391,
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
                    "asm": "OP_RETURN e5554652454500000000bd6767aea3de97aee1bb4354893e2de56a2150680e5aa40ab24716d81c1520e0",
                    "hex": "6a2ae5554652454500000000bd6767aea3de97aee1bb4354893e2de56a2150680e5aa40ab24716d81c1520e0",
                    "type": "nulldata"
                }
            }
        ],
        "vjoinsplit": []
    }
