***********
oraclesinfo
***********

Oracles Info
============

Displays information about a specific Oracle using ``oracletxid``. Use ``oracleslist`` to get a list of ``oracletxid``s that you can use here.

Usage:
------

``oraclesinfo oracletxid``

Terminology:
------------

::
    
    oracletxid = transaction id of the creation of the Oracle    

Example Command:
----------------

.. code-block:: shell

    ./komodo-cli -ac_name=CCNG oraclesinfo 0df7c4d844f08dba08abd4bb174558739f17cfe268feb005fb6333b3761d9203                                   

Output:
-------

.. code-block:: json

    {
        "result": "success",
        "txid": "0df7c4d844f08dba08abd4bb174558739f17cfe268feb005fb6333b3761d9203",
        "name": "NYWTHR",
        "description": "Weather in NYC",
        "format": "L",
        "marker": "RGEug5JPPkERBpqsGSgw6GQPYTB9v9i4Fj",
        "registered": [
            {
                "publisher": "03810d28146f60a42090991b044fe630d1664f3f8f46286c61e7420523318047b5",
                "baton": "RWg43P8s8RtJatAGNa2kV8N2abhQqH93w9",
                "batontxid": "8f3c517d023e42bacfd0de8b0174cdc8adab713d08a689c00067ab171488a575",
                "lifetime": "0.00000000",
                "funds": "0.00000000",
                "datafee": "0.01000000"
            }
        ]
    }

