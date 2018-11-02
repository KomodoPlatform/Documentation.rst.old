***********
oraclesdata
***********

Publish data to Oracle
======================

Usage:
------

``oraclesdata oracletxid hexstr``

.. note::

    Have to set string length in the beginning bytes of the hexstring (``hexstr``)

Step 1: Subscribe to a Oracle Plan and get the hex value
========================================================

Example Command:
----------------

.. code-block:: shell

    ./komodo-cli -ac_name=CCNG oraclesdata 0df7c4d844f08dba08abd4bb174558739f17cfe268feb005fb6333b3761d9203 00000000ffffffff

Output:
-------

.. code-block:: json

    {
        "result": "success",
        "hex": "010000000359db76b9b8e9cfaa4514dcc198c375f910b9fb7367d1c9d556cd5eb43b5f4d2d02000000484730440220645b49d6d85454b1015d82a53ec51685fc3b8bf1d092696c3c253b88cab3033a02207023511219897a374ad94951dd2af70b14d99eccbb404eaf783120f3170bd5e301ffffffff75a5881417ab6700c089a6083d71abadc8cd74018bded0cfba423e027d513c8f010000007b4c79a276a072a26ba067a5658021035933ab0bd2e2ceb712e7cab393a8c9096ba4be2e3a76f5aaeab72bce4aa61857814047697a246e4442888a3b6ffc4a8c5ae940eec7d19f72053a07b6d8a2968a260626c8001c9138e9fd0e3cfabb811ae71bd8c1c555ca8c8410cb9121ce25860507a100af038001eca10001ffffffff59db76b9b8e9cfaa4514dcc198c375f910b9fb7367d1c9d556cd5eb43b5f4d2d000000007b4c79a276a072a26ba067a565802103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b581404fa0de32bbb96b2e2f61fe823cdba4c3b9fef786ea8c65196f97653a942656812e675e91643ff0ec33853fd2481d40fc48fa51e18c9cbffb49e714c15b47babda100af038001eca10001ffffffff05c09ee60500000000302ea22c802092392e766d63f73dd7c68ff9eaf9f009f13b17c4167472e8aebb00d96be66aa68103120c008203000401cc1027000000000000302ea22c80200648c12e7e058c98f0a5cc288ac271ad08bd493e1fb7de83edeea69789338fc58103120c008203000401cc40420f0000000000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5acd7bb49a204000000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5ac0000000000000000706a4c6dec4403921d76b33363fb05b0fe68e2cf179f73584517bbd4ab08ba8df044d8c4f70d75a5881417ab6700c089a6083d71abadc8cd74018bded0cfba423e027d513c8f2103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b50800000000ffffffff00000000"
    }

Step 2: Send raw transaction / Broadcast the hex value
======================================================

Example Command:
----------------

.. code-block:: shell

    ./komodo-cli -ac_name=CCNG sendrawtransaction 010000000359db76b9b8e9cfaa4514dcc198c375f910b9fb7367d1c9d556cd5eb43b5f4d2d02000000484730440220645b49d6d85454b1015d82a53ec51685fc3b8bf1d092696c3c253b88cab3033a02207023511219897a374ad94951dd2af70b14d99eccbb404eaf783120f3170bd5e301ffffffff75a5881417ab6700c089a6083d71abadc8cd74018bded0cfba423e027d513c8f010000007b4c79a276a072a26ba067a5658021035933ab0bd2e2ceb712e7cab393a8c9096ba4be2e3a76f5aaeab72bce4aa61857814047697a246e4442888a3b6ffc4a8c5ae940eec7d19f72053a07b6d8a2968a260626c8001c9138e9fd0e3cfabb811ae71bd8c1c555ca8c8410cb9121ce25860507a100af038001eca10001ffffffff59db76b9b8e9cfaa4514dcc198c375f910b9fb7367d1c9d556cd5eb43b5f4d2d000000007b4c79a276a072a26ba067a565802103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b581404fa0de32bbb96b2e2f61fe823cdba4c3b9fef786ea8c65196f97653a942656812e675e91643ff0ec33853fd2481d40fc48fa51e18c9cbffb49e714c15b47babda100af038001eca10001ffffffff05c09ee60500000000302ea22c802092392e766d63f73dd7c68ff9eaf9f009f13b17c4167472e8aebb00d96be66aa68103120c008203000401cc1027000000000000302ea22c80200648c12e7e058c98f0a5cc288ac271ad08bd493e1fb7de83edeea69789338fc58103120c008203000401cc40420f0000000000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5acd7bb49a204000000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5ac0000000000000000706a4c6dec4403921d76b33363fb05b0fe68e2cf179f73584517bbd4ab08ba8df044d8c4f70d75a5881417ab6700c089a6083d71abadc8cd74018bded0cfba423e027d513c8f2103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b50800000000ffffffff00000000
    # This will output a unique txid which will be refered as oraclesdatatxid or ID of the oracle data transaction.

Output:
-------

::

    9530bdf82744ac57a5ffe0855595f5510c339341cdc3c8728ee547d3f3153433

Step 3: Decode raw transaction (optional to check if the values are sane)
=========================================================================

Example Command:
----------------

.. code-block:: shell

    ./komodo-cli -ac_name=CCNG decoderawtransaction 010000000359db76b9b8e9cfaa4514dcc198c375f910b9fb7367d1c9d556cd5eb43b5f4d2d02000000484730440220645b49d6d85454b1015d82a53ec51685fc3b8bf1d092696c3c253b88cab3033a02207023511219897a374ad94951dd2af70b14d99eccbb404eaf783120f3170bd5e301ffffffff75a5881417ab6700c089a6083d71abadc8cd74018bded0cfba423e027d513c8f010000007b4c79a276a072a26ba067a5658021035933ab0bd2e2ceb712e7cab393a8c9096ba4be2e3a76f5aaeab72bce4aa61857814047697a246e4442888a3b6ffc4a8c5ae940eec7d19f72053a07b6d8a2968a260626c8001c9138e9fd0e3cfabb811ae71bd8c1c555ca8c8410cb9121ce25860507a100af038001eca10001ffffffff59db76b9b8e9cfaa4514dcc198c375f910b9fb7367d1c9d556cd5eb43b5f4d2d000000007b4c79a276a072a26ba067a565802103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b581404fa0de32bbb96b2e2f61fe823cdba4c3b9fef786ea8c65196f97653a942656812e675e91643ff0ec33853fd2481d40fc48fa51e18c9cbffb49e714c15b47babda100af038001eca10001ffffffff05c09ee60500000000302ea22c802092392e766d63f73dd7c68ff9eaf9f009f13b17c4167472e8aebb00d96be66aa68103120c008203000401cc1027000000000000302ea22c80200648c12e7e058c98f0a5cc288ac271ad08bd493e1fb7de83edeea69789338fc58103120c008203000401cc40420f0000000000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5acd7bb49a204000000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5ac0000000000000000706a4c6dec4403921d76b33363fb05b0fe68e2cf179f73584517bbd4ab08ba8df044d8c4f70d75a5881417ab6700c089a6083d71abadc8cd74018bded0cfba423e027d513c8f2103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b50800000000ffffffff00000000
    
Output:
-------

.. code-block:: json

    {
        "txid": "9530bdf82744ac57a5ffe0855595f5510c339341cdc3c8728ee547d3f3153433",
        "size": 774,
        "version": 1,
        "locktime": 0,
        "vin": [
            {
                "txid": "2d4d5f3bb45ecd56d5c9d16773fbb910f975c398c1dc1445aacfe9b8b976db59",
                "vout": 2,
                "scriptSig": {
                    "asm": "30440220645b49d6d85454b1015d82a53ec51685fc3b8bf1d092696c3c253b88cab3033a02207023511219897a374ad94951dd2af70b14d99eccbb404eaf783120f3170bd5e301",
                    "hex": "4730440220645b49d6d85454b1015d82a53ec51685fc3b8bf1d092696c3c253b88cab3033a02207023511219897a374ad94951dd2af70b14d99eccbb404eaf783120f3170bd5e301"
                },
                "sequence": 4294967295
            },
            {
                "txid": "8f3c517d023e42bacfd0de8b0174cdc8adab713d08a689c00067ab171488a575",
                "vout": 1,
                "scriptSig": {
                    "asm": "a276a072a26ba067a5658021035933ab0bd2e2ceb712e7cab393a8c9096ba4be2e3a76f5aaeab72bce4aa61857814047697a246e4442888a3b6ffc4a8c5ae940eec7d19f72053a07b6d8a2968a2606
26c8001c9138e9fd0e3cfabb811ae71bd8c1c555ca8c8410cb9121ce25860507a100af038001eca10001",
        "hex": "4c79a276a072a26ba067a5658021035933ab0bd2e2ceb712e7cab393a8c9096ba4be2e3a76f5aaeab72bce4aa61857814047697a246e4442888a3b6ffc4a8c5ae940eec7d19f72053a07b6d8a2968a
260626c8001c9138e9fd0e3cfabb811ae71bd8c1c555ca8c8410cb9121ce25860507a100af038001eca10001"
                },
                "sequence": 4294967295
            },
            {
                "txid": "2d4d5f3bb45ecd56d5c9d16773fbb910f975c398c1dc1445aacfe9b8b976db59",
                "vout": 0,
                "scriptSig": {
                    "asm": "a276a072a26ba067a565802103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b581404fa0de32bbb96b2e2f61fe823cdba4c3b9fef786ea8c65196f97653a94265681
2e675e91643ff0ec33853fd2481d40fc48fa51e18c9cbffb49e714c15b47babda100af038001eca10001",
        "hex": "4c79a276a072a26ba067a565802103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b581404fa0de32bbb96b2e2f61fe823cdba4c3b9fef786ea8c65196f97653a9426
56812e675e91643ff0ec33853fd2481d40fc48fa51e18c9cbffb49e714c15b47babda100af038001eca10001"
                },
                "sequence": 4294967295
            }
        ],
        "vout": [
            {
                "value": 0.99000000,
                "valueSat": 99000000,
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
                "value": 0.01000000,
                "valueSat": 1000000,
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
                "value": 199.02610391,
                "valueSat": 19902610391,
                "n": 3,
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
                "n": 4,
                "scriptPubKey": {
                    "asm": "OP_RETURN ec4403921d76b33363fb05b0fe68e2cf179f73584517bbd4ab08ba8df044d8c4f70d75a5881417ab6700c089a6083d71abadc8cd74018bded0cfba423e027d513c8f2103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b50800000000ffffffff",
                    "hex": "6a4c6dec4403921d76b33363fb05b0fe68e2cf179f73584517bbd4ab08ba8df044d8c4f70d75a5881417ab6700c089a6083d71abadc8cd74018bded0cfba423e027d513c8f2103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b50800000000ffffffff",
                    "type": "nulldata"
                }
            }
        ],
        "vjoinsplit": []
    }

