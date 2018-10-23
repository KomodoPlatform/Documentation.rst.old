*******************
A Note to Exchanges
*******************

There is a small chance that an outbound transaction will give an error due to mismatched values in wallet calculations. There is a parameter called ``-exchange`` that you can run the Komodo daemon (``komodod``) with, that solves this problem. 

.. note:: 

    Please make sure to recreate the wallet.dat with the privatekeys from the previous wallet imported and resync the chain when starting the Komodo daemon (``komodod``) with the ``-exchange`` parameter. Otherwise you will get wallet conflicts as the previous transaction history will have slightly different values before the ``exchange`` mode is enabled.

Example:
--------

If you normally start the daemon using the command:

.. code-block:: shell

    ./src/komodod -addnode=78.47.196.146 -daemon

adding the - parameter ``-exchange`` will make it:

.. code-block:: shell

    ./src/komodod -addnode=78.47.196.146 -exchange -daemon

This post on Bitcointalk gives the context related to addition of the parameter to Komodo: https://bitcointalk.org/index.php?topic=1605144.msg17732151#msg17732151

.. warning::

    * Enabling the ``exchange`` mode makes the wallet pretend that there is no Reward to be claimed when it creates a transaction. This has the effect of shifting the Reward accrued from the exchange to the miners/notaries.

    * An exchange is free to not run in this mode by adding error handling while creating a transaction. 
