***************
oraclesregister
***************

Register to publish data to an Oracle that already exists
=========================================================

Usage:
------

``oraclesregister oracletxid datafee``

Terminology:
------------

::

    oracletxid = transaction id of the creation of the Oracle
    datafee = Fee required for publishing each datapoint for the above Oracle

Step 1: Set your parameters to create a raw transaction and get the hex value
=============================================================================

Example Command:
----------------

.. code-block:: shell

./komodo-cli -ac_name=CCNG oraclesregister 0df7c4d844f08dba08abd4bb174558739f17cfe268feb005fb6333b3761d9203 1000000

Output:
-------

.. code-block:: json

    {
        "result": "success",
        "hex": "010000000103921d76b33363fb05b0fe68e2cf179f73584517bbd4ab08ba8df044d8c4f70d010000004847304402207241f313ef2fb65d9eb1f870068ceba436f14996ce79d16ff85f2937c75357ee022025f0b888e742546469ad0b7fae9b85cf7c89cddf307170bbcf794e5e90ae28b101ffffffff04102700000000000023210203921d76b33363fb05b0fe68e2cf179f73584517bbd4ab08ba8df044d8c4f70dac1027000000000000302ea22c80200648c12e7e058c98f0a5cc288ac271ad08bd493e1fb7de83edeea69789338fc58103120c008203000401cc071240a804000000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5ac00000000000000004f6a4c4cec5203921d76b33363fb05b0fe68e2cf179f73584517bbd4ab08ba8df044d8c4f70d2103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b540420f000000000000000000"
    }

Step 2: Send/broadcast the raw transaction hex
==============================================

Example Command:
----------------

.. code-block:: shell

    ./komodo-cli -ac_name=CCNG sendrawtransaction 010000000103921d76b33363fb05b0fe68e2cf179f73584517bbd4ab08ba8df044d8c4f70d010000004847304402207241f313ef2fb65d9eb1f870068ceba436f14996ce79d16ff85f2937c75357ee022025f0b888e742546469ad0b7fae9b85cf7c89cddf307170bbcf794e5e90ae28b101ffffffff04102700000000000023210203921d76b33363fb05b0fe68e2cf179f73584517bbd4ab08ba8df044d8c4f70dac1027000000000000302ea22c80200648c12e7e058c98f0a5cc288ac271ad08bd493e1fb7de83edeea69789338fc58103120c008203000401cc071240a804000000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5ac00000000000000004f6a4c4cec5203921d76b33363fb05b0fe68e2cf179f73584517bbd4ab08ba8df044d8c4f70d2103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b540420f000000000000000000

Output:
-------

.. code-block:: shell

    8f3c517d023e42bacfd0de8b0174cdc8adab713d08a689c00067ab171488a575
    # This output is a unique txid which will be used as oracleregistrationtxid or ID of the oracle registration transaction. (wait for the tx to confirm)


.. note::

    * Use ``./komodo-cli -ac_name=CCNG getrawmempool`` to find out if the tx is confirmed.
    * Doing ``oraclesinfo`` should output registration information for this oraclesplan (After the transaction confirms).
    * dataee set in satoshis. Should be ``>=`` txfee

Step 3: Decode raw transaction (optional to check if the values are sane)
=========================================================================

Example Command:
----------------

.. code-block:: shell

    ./komodo-cli -ac_name=CCNG decoderawtransaction 010000000103921d76b33363fb05b0fe68e2cf179f73584517bbd4ab08ba8df044d8c4f70d010000004847304402207241f313ef2fb65d9eb1f870068ceba436f14996ce79d16ff85f2937c75357ee022025f0b888e742546469ad0b7fae9b85cf7c89cddf307170bbcf794e5e90ae28b101ffffffff04102700000000000023210203921d76b33363fb05b0fe68e2cf179f73584517bbd4ab08ba8df044d8c4f70dac1027000000000000302ea22c80200648c12e7e058c98f0a5cc288ac271ad08bd493e1fb7de83edeea69789338fc58103120c008203000401cc071240a804000000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5ac00000000000000004f6a4c4cec5203921d76b33363fb05b0fe68e2cf179f73584517bbd4ab08ba8df044d8c4f70d2103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b540420f000000000000000000

Output:
-------

.. code-block:: json

    {
        "txid": "8f3c517d023e42bacfd0de8b0174cdc8adab713d08a689c00067ab171488a575",
        "size": 356,
        "version": 1,
        "locktime": 0,
        "vin": [
            {
                "txid": "0df7c4d844f08dba08abd4bb174558739f17cfe268feb005fb6333b3761d9203",
                "vout": 1,
                "scriptSig": {
                    "asm": "304402207241f313ef2fb65d9eb1f870068ceba436f14996ce79d16ff85f2937c75357ee022025f0b888e742546469ad0b7fae9b85cf7c89cddf307170bbcf794e5e90ae28b101",
                    "hex": "47304402207241f313ef2fb65d9eb1f870068ceba436f14996ce79d16ff85f2937c75357ee022025f0b888e742546469ad0b7fae9b85cf7c89cddf307170bbcf794e5e90ae28b101"
                },
                "sequence": 4294967295
            }
        ],
        "vout": [
            {
                "value": 0.00010000,
                "valueSat": 10000,
                "n": 0,
                "scriptPubKey": {
                    "asm": "0203921d76b33363fb05b0fe68e2cf179f73584517bbd4ab08ba8df044d8c4f70d OP_CHECKSIG",
                    "hex": "210203921d76b33363fb05b0fe68e2cf179f73584517bbd4ab08ba8df044d8c4f70dac",
                    "reqSigs": 1,
                    "type": "pubkey",
                    "addresses": [
                        "RGEug5JPPkERBpqsGSgw6GQPYTB9v9i4Fj"
                    ]
                }
            },
            {
                "value": 0.00010000,
                "valueSat": 10000,
                "n": 1,
                "scriptPubKey": {
                    "asm": "a22c80200648c12e7e058c98f0a5cc288ac271ad08bd493e1fb7de83edeea69789338fc58103120c008203000401 OP_CHECKCRYPTOCONDITION",
                    "hex": "2ea22c80200648c12e7e058c98f0a5cc288ac271ad08bd493e1fb7de83edeea69789338fc58103120c008203000401cc",
                    "reqSigs": 1,
                    "type": "cryptocondition",
                    "addresses": [
                        "RWg43P8s8RtJatAGNa2kV8N2abhQqH93w9"
                    ]
                }
            },
            {
                "value": 200.02640391,
                "valueSat": 20002640391,
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
                    "asm": "OP_RETURN ec5203921d76b33363fb05b0fe68e2cf179f73584517bbd4ab08ba8df044d8c4f70d2103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b540420f00000$0000",
                    "hex": "6a4c4cec5203921d76b33363fb05b0fe68e2cf179f73584517bbd4ab08ba8df044d8c4f70d2103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b540420f000000000$",
                    "type": "nulldata"
                }
            }
        ],
        "vjoinsplit": []
    }

