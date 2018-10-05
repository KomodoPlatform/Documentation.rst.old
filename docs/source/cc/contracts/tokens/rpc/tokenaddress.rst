************
tokenaddress
************

Check token address for a specific pubkey
=========================================

Usage:
------

``tokenaddress [pubkey]``

Example command:
----------------

.. code-block:: shell

	./komodo-cli -ac_name=ATEST tokenaddress 028702e30d8465d6aa85f35d2f58c06a6ee17f23f376b56044dadf7b793f2c12b9

Output:
-------

.. code-block:: json

    {
        "result": "success",
        "AssetsCCaddress": "RGKRjeTBw4LYFotSDLT6RWzMHbhXri6BG6",
        "Assetsmarker": "RFYE2yL3KknWdHK6uNhvWacYsCUtwzjY3u",
        "CCaddress": "RG6mr23tQ9nUhmi5GEnYqjfkqZt9x2MRXz",
        "myCCaddress": "RG6mr23tQ9nUhmi5GEnYqjfkqZt9x2MRXz",
        "myaddress": "RDjG4sM1y4udiJSszF6BLotqUnZX79Rom9"
    }

