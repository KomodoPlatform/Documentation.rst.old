*******************
A Note to Exchanges
*******************

There is a small chance that an outbound transaction will give an error due to mismatched values in wallet calculations. There is a parameter called ``-exchange`` that you can run the Komodo daemon (``komodod``) with, that solves this problem. 

.. warning:: 

    Please make sure to have the entire transaction history under the same ``-exchange`` mode. Otherwise you will get wallet conflicts.

Example:
--------

If you normally start the daemon using the command:

.. code-block:: shell

    ./src/komodod -addnode=78.47.196.146 -daemon

adding the - parameter ``-exchange`` will make it:

.. code-block:: shell

    ./src/komodod -addnode=78.47.196.146 -exchange -daemon

This post on Bitcointalk gives the context related to addition of the parameter to Komodo: https://bitcointalk.org/index.php?topic=1605144.msg17732151#msg17732151
