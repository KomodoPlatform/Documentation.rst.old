*******************
A Note to Exchanges
*******************

There is a parameter called ``-exchange`` that you can run the Komodo daemon (``komodod``) with, that ignores the rewards when a transaction is sent. One benefit is it allows exchanges to manage their account balances against their accounting software without any modification during account reconciliation. 

.. note::

    Enabling the ``-exchange`` mode makes the wallet pretend that there is no Reward to be claimed when it creates a transaction. This has the effect of shifting the Reward accrued from the exchange to the miners/notaries.

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

    Please make sure to recreate the wallet.dat with the privatekeys from the previous wallet imported and resync the chain when starting the Komodo daemon (``komodod``) with the ``-exchange`` parameter. Otherwise you will get wallet conflicts as the previous transaction history will have slightly different values before the ``exchange`` mode is enabled.

If you were already running the normal mode, to enable the `-exchange` parameter,

    a) Backup all privkeys (launch ``komodod`` with ``-exportdir=<path>`` and run ``./komodo-cli dumpwallet <filename>``) 
    b) Start a totally new sync including a new ``wallet.dat``, launch with the same ``exportdir`` and the parameter `-exchange`
    c) Stop it before it gets too far and import all the privkeys backed up during step a) using ``./komodo-cli importwallet <filename>`` 
    d) Resume sync till it gets to chaintip

For example:

.. code-block:: shell

    ./komodod -exportdir=/tmp &
    ./komodo-cli dumpwallet example
    ./komodo-cli stop
    mv ~/.komodo ~/.komodo.old && mkdir ~/.komodo && cp ~/.komodo.old/komodo.conf ~/.komodo.old/peers.dat ~/.komodo
    ./komodod -exchange -exportdir=/tmp &
    ./komodo-cli importwallet /tmp/example

