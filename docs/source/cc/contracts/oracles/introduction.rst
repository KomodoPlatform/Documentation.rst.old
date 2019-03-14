*******
Oracles
*******

Visit https://developers.komodoplatform.com/basic-docs/cryptoconditions/cc-oracles.html for the latest Documentation.

For an introduction to CC in general, see: :ref:`Using the Contracts on a Komodo based Blockchain`

To enable and test contracts:

    * The Blockchain must have the parameter ``-ac_cc`` as described in :ref:`Using the Contracts on a Komodo based Blockchain`
    * The Blockchain must be started using the parameter ``-pubkey`` with a pubkey whose privatekey is owned by only you and imported into the wallet of this particular chain.

Introduction
============

Oracles contract is useful for making offchain data available on-chain. 

The contract can be used as follows:

    * Anyone can create an Oracle using ``oraclescreate`` which takes a name, description, expected format of the data as arguments.
    * Anyone can register as a publisher of data for an Oracle using ``oraclesregister`` which takes the transaction-id of an Oracle already created and datafee (fee required for each upload of data ) as arguments.
    * ``oracleslist`` , ``oraclesinfo`` , ``oraclessamples`` can be used in that specific order to find the available Oracles, their publishers and data samples from any specific publisher.  
    * Anyone can subscribe to a particular publisher for an Oracle through ``oraclessubscribe``
    * A publisher can publish data using ``oraclesdata`` and collect the ``datafee`` 

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

Example:
--------

.. code-block:: shell

    ./komodo-cli -ac_name=ORCL oraclescreate "Oracle1" "testing oracle" "L"
    # "L" is when the data to be submitted is a 8 byte unsigned little endian number

