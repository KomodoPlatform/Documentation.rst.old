**************
oraclessamples
**************

Getting sample data by a Publisher to a particular Oracle Plan
==============================================================

Usage:
------

``oraclessamples oracletxid batonutxo num``

Terminology:

::

    batonutxo = baton transactioid (can be found from the oraclesinfo call)
    num = number of sample data points required

Example Command:
----------------

.. code-block:: shell

    ./komodo-cli -ac_name=CCNG oraclessamples 0df7c4d844f08dba08abd4bb174558739f17cfe268feb005fb6333b3761d9203 abb4fc6d7fbff88c09b35fc40d96e3a04a891fbf3a2f21e8b8536acbd95d75d7 2

Output:
-------

.. code-block:: json

    {
        "result": "success",
        "samples": [
            [
                "4982091690320855040"
            ],
            [
                "18446744069414584320"
            ]
        ]
    }    

