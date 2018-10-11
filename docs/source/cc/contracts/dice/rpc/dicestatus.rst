**********
dicestatus
**********

Dice Status
===========

Dice Status prints the status of a ``dicebet``. It will show whether the bet won or lost.

Usage:
------

``dicestatus name fundingtxid bettxid``

Example Command:
----------------

.. code-block:: shell

    ./komodo-cli -ac_name=AT1 dicestatus DICE3 4132ca8e8d46df9f8a8cbe83c99794497e06bbd190bd71f4abcdedf84e90952e d54335073e549cd75a050fd4d6ba5939307cda7096ba0f3da779fb7d07e46343

Output:
-------

.. code-block:: json

    {
      "result": "success",
      "status": "loss"
    }
