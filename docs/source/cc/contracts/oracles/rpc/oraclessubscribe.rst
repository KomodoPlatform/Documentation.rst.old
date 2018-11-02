****************
oraclessubscribe
****************

Subscribe to a Oracle plan
==========================

Usage:
------

``oraclessubscribe oracletxid publisher datafee``

Step 1: Subscribe to a Oracle Plan and get the hex value
========================================================

Example Command:
----------------

.. code-block:: shell

    ./komodo-cli -ac_name=CCNG oraclessubscribe 0df7c4d844f08dba08abd4bb174558739f17cfe268feb005fb6333b3761d9203 03810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5 1
    # This will output an unique txid which will be refered as oraclesubscribtiontxid or ID of the oracle subscription transaction.

Output:
-------

.. code-block:: json

    {
        "result": "success",
        "hex": "010000000175a5881417ab6700c089a6083d71abadc8cd74018bded0cfba423e027d513c8f0200000048473044022006449e2f324ba8c262ca73eea4642f77ccf906fee5bab4fdc85bcc8c350ce81b022047d76840076f6e02aebe77ffb59b052974badb8747c7b435fd77351fcfbee95e01ffffffff0400e1f50500000000302ea22c802092392e766d63f73dd7c68ff9eaf9f009f13b17c4167472e8aebb00d96be66aa68103120c008203000401cc102700000000000023210203921d76b33363fb05b0fe68e2cf179f73584517bbd4ab08ba8df044d8c4f70dace7e249a204000000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5ac00000000000000004f6a4c4cec5303921d76b33363fb05b0fe68e2cf179f73584517bbd4ab08ba8df044d8c4f70d2103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b500e1f5050000000000000000"
    }

.. note::

    Without anyone subscribing to a Oracle Plan by a publisher, the publisher can't send data to the blockchain.

Step 2: Send raw transaction / Broadcast the hex value
======================================================

Example Command:
----------------

.. code-block:: shell

    ./komodo-cli -ac_name=CCNG sendrawtransaction 010000000175a5881417ab6700c089a6083d71abadc8cd74018bded0cfba423e027d513c8f0200000048473044022006449e2f324ba8c262ca73eea4642f77ccf906fee5bab4fdc85bcc8c350ce81b022047d76840076f6e02aebe77ffb59b052974badb8747c7b435fd77351fcfbee95e01ffffffff0400e1f50500000000302ea22c802092392e766d63f73dd7c68ff9eaf9f009f13b17c4167472e8aebb00d96be66aa68103120c008203000401cc102700000000000023210203921d76b33363fb05b0fe68e2cf179f73584517bbd4ab08ba8df044d8c4f70dace7e249a204000000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5ac00000000000000004f6a4c4cec5303921d76b33363fb05b0fe68e2cf179f73584517bbd4ab08ba8df044d8c4f70d2103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b500e1f5050000000000000000

Output:
-------

::

    2d4d5f3bb45ecd56d5c9d16773fbb910f975c398c1dc1445aacfe9b8b976db59

Step 3: Decode raw transaction (optional to check if the values are sane)
=========================================================================

Example Command:
----------------

.. code-block:: shell

    ./komodo-cli -ac_name=CCNG decoderawtransaction 010000000175a5881417ab6700c089a6083d71abadc8cd74018bded0cfba423e027d513c8f0200000048473044022006449e2f324ba8c262ca73eea4642f77ccf906fee5bab4fdc85bcc8c350ce81b022047d76840076f6e02aebe77ffb59b052974badb8747c7b435fd77351fcfbee95e01ffffffff0400e1f50500000000302ea22c802092392e766d63f73dd7c68ff9eaf9f009f13b17c4167472e8aebb00d96be66aa68103120c008203000401cc102700000000000023210203921d76b33363fb05b0fe68e2cf179f73584517bbd4ab08ba8df044d8c4f70dace7e249a204000000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5ac00000000000000004f6a4c4cec5303921d76b33363fb05b0fe68e2cf179f73584517bbd4ab08ba8df044d8c4f70d2103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b500e1f5050000000000000000

Output:
-------

.. code-block:: json

    {
        "txid": "2d4d5f3bb45ecd56d5c9d16773fbb910f975c398c1dc1445aacfe9b8b976db59",
        "size": 356,
        "version": 1,
        "locktime": 0,
        "vin": [
            {
                "txid": "8f3c517d023e42bacfd0de8b0174cdc8adab713d08a689c00067ab171488a575",
                "vout": 2,
                "scriptSig": {
                    "asm": "3044022006449e2f324ba8c262ca73eea4642f77ccf906fee5bab4fdc85bcc8c350ce81b022047d76840076f6e02aebe77ffb59b052974badb8747c7b435fd77351fcfbee95e01",
                    "hex": "473044022006449e2f324ba8c262ca73eea4642f77ccf906fee5bab4fdc85bcc8c350ce81b022047d76840076f6e02aebe77ffb59b052974badb8747c7b435fd77351fcfbee95e01"
                },
                "sequence": 4294967295
            }
        ],
        "vout": [
            {
                "value": 1.00000000,
                "valueSat": 100000000,
                "n": 0,
                "scriptPubKey": {
                    "asm": "a22c802092392e766d63f73dd7c68ff9eaf9f009f13b17c4167472e8aebb00d96be66aa68103120c008203000401 OP_CHECKCRYPTOCONDITION",
                    "hex": "2ea22c802092392e766d63f73dd7c68ff9eaf9f009f13b17c4167472e8aebb00d96be66aa68103120c008203000401cc",
                    "reqSigs": 1,
                    "type": "cryptocondition",
                    "addresses": [
                        "RTk2Tgp1iAcxxSeuXYDREmtfydMvNkCmq8"
                    ]
                }
            },
            {
                "value": 0.00010000,
                "valueSat": 10000,
                "n": 1,
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
                "value": 199.02620391,
                "valueSat": 19902620391,
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
                    "asm": "OP_RETURN ec5303921d76b33363fb05b0fe68e2cf179f73584517bbd4ab08ba8df044d8c4f70d2103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b500e1f50500000000",
                    "hex": "6a4c4cec5303921d76b33363fb05b0fe68e2cf179f73584517bbd4ab08ba8df044d8c4f70d2103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b500e1f50500000000",
                    "type": "nulldata"
                }
            }
        ],
        "vjoinsplit": []
    }

