*************
oraclescreate
*************

Creates a new Oracle
====================

Usage:
------

``oraclescreate name description format``

The various formats of data that can be registered for an Oracle and their symbols are as follows:

::

      's' -> <256 char string
      'S' -> <65536 char string
      'd' -> <256 binary data
      'D' -> <65536 binary data
      'c' -> 1 byte signed little endian number, 'C' if unsigned
      't' -> 2 byte signed little endian number, 'T' if unsigned
      'i' -> 4 byte signed little endian number, 'I' if unsigned
      'l' -> 8 byte signed little endian number, 'L' if unsigned
      'h' -> 32 byte hash"


Step 1: Create a customized Oracle contract and get the hex value
=================================================================

Example Command:
----------------

.. code-block:: shell

    ./komodo-cli -ac_name=CCNG oraclescreate "NYWTHR" "Weather in NYC" "L"                                                              

Output:
-------

.. code-block:: json

    {
        "result": "success",
        "hex": "010000000185b76ed0fbdb9ee2bdb5693f491b6ea23de6498f42c6e83f9f36c1eaf411dd990200000049483045022100aa198a2ae959ee191e1359df48867480bf5a1a5bd4fa76b4398481c89ff3095102205034824dcd56b312183acd65c27a002a13dae84f5d22c767f1efaae09ef63a5c01ffffffff0310270000000000002321038c1d42db6a45a57eccb8981b078fb7857b9b496293fe299d2b8d120ac5b5691aac378740a804000000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5ac00000000000000001c6a1aec43064e5957544852014c0e5765617468657220696e204e594300000000"
    }

Step 2: Send raw transaction / Broadcast the hex value
======================================================

Example Command:
----------------

.. code-block:: shell

    ./komodo-cli -ac_name=CCNG sendrawtransaction 010000000185b76ed0fbdb9ee2bdb5693f491b6ea23de6498f42c6e83f9f36c1eaf411dd990200000049483045022100aa198a2ae959ee191e1359df48867480bf5a1a5bd4fa76b4398481c89ff3095102205034824dcd56b312183acd65c27a002a13dae84f5d22c767f1efaae09ef63a5c01ffffffff0310270000000000002321038c1d42db6a45a57eccb8981b078fb7857b9b496293fe299d2b8d120ac5b5691aac378740a804000000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5ac00000000000000001c6a1aec43064e5957544852014c0e5765617468657220696e204e594300000000
    # This will output an unique txid which will be refered as oracletxid or ID of the oracle.

Output:
-------

::

    0df7c4d844f08dba08abd4bb174558739f17cfe268feb005fb6333b3761d9203

.. note::

    Use ``./komodo-cli -ac_name=CCNG getrawmempool`` to find out if the tx is confirmed.

Step 3: Decode raw transaction (optional to check if the values are sane)
=========================================================================

Example Command:
----------------

.. code-block:: shell

    ./komodo-cli -ac_name=CCNG decoderawtransaction 010000000185b76ed0fbdb9ee2bdb5693f491b6ea23de6498f42c6e83f9f36c1eaf411dd990200000049483045022100aa198a2ae959ee191e1359df48867480bf5a1a5bd4fa76b4398481c89ff3095102205034824dcd56b312183acd65c27a002a13dae84f5d22c767f1efaae09ef63a5c01ffffffff0310270000000000002321038c1d42db6a45a57eccb8981b078fb7857b9b496293fe299d2b8d120ac5b5691aac378740a804000000232103810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5ac00000000000000001c6a1aec43064e5957544852014c0e5765617468657220696e204e594300000000

Output:
-------

.. code-block:: json

    {
        "txid": "0df7c4d844f08dba08abd4bb174558739f17cfe268feb005fb6333b3761d9203",
        "size": 249,
        "version": 1,
        "locktime": 0,
        "vin": [
            {
                "txid": "99dd11f4eac1369f3fe8c6428f49e63da26e1b493f69b5bde29edbfbd06eb785",
                "vout": 2,
                "scriptSig": {
                    "asm": "3045022100aa198a2ae959ee191e1359df48867480bf5a1a5bd4fa76b4398481c89ff3095102205034824dcd56b312183acd65c27a002a13dae84f5d22c767f1efaae09ef63a5c01",
                    "hex": "483045022100aa198a2ae959ee191e1359df48867480bf5a1a5bd4fa76b4398481c89ff3095102205034824dcd56b312183acd65c27a002a13dae84f5d22c767f1efaae09ef63a5c01"
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
                    "asm": "038c1d42db6a45a57eccb8981b078fb7857b9b496293fe299d2b8d120ac5b5691a OP_CHECKSIG",
                    "hex": "21038c1d42db6a45a57eccb8981b078fb7857b9b496293fe299d2b8d120ac5b5691aac",
                    "reqSigs": 1,
                    "type": "pubkey",
                    "addresses": [
                        "RHkFKzn1csxA3fWzAsxsLWohoCgBbirXb5"
                    ]
                }
            },
            {
                "value": 200.02670391,
                "valueSat": 20002670391,
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
                    "asm": "OP_RETURN ec43064e5957544852014c0e5765617468657220696e204e5943",
                    "hex": "6a1aec43064e5957544852014c0e5765617468657220696e204e5943",
                    "type": "nulldata"
                }
            }
        ],
        "vjoinsplit": []
    }

