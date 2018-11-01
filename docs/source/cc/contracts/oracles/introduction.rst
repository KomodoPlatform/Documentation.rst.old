*******
Oracles
*******

For an introduction to CC in general, see: :ref:`Using the Contracts on a Komodo based Blockchain`

To enable and test contracts:

    * The Blockchain must have the parameter ``-ac_cc`` as described in :ref:`Using the Contracts on a Komodo based Blockchain`
    * The Blockchain must be started using the parameter ``-pubkey`` with a pubkey whose privatekey is owned by only you and imported into the wallet of this particular chain.

Introduction
============

Oracles contract is useful for making offchain data available on-chain. 

The contract can be used as follows:

    * Anyone can create an Oracle using ``oraclescreate`` which takes a name, description, expected format of the data as arguments.
    * Anyone can register to provide data to an Oracle already created using ``oraclesregister`` which takes the transaction-id of an Oracle already created and datafee (fee required for each upload of data ) as arguments.
    * ``oracleslist`` , ``oraclesinfo`` , ``oraclessamples`` can be used in that specific order to find the available Oracles, their publishers and data samples from any specific publisher.  
    * Anyone can subscribe to a particular publisher for an Oracle through ``oraclessubscribe``
    * A publisher can publish data using ``oraclesdata`` and collect the ``datafee`` 

A tutorial describing the usage of Oracles contract is :doc:`here <scenarios/tutorial>`

.. _oracles-rpc:

Available RPC Calls
===================

    * :doc:`oraclesaddress [pubkey] <oraclesaddress>`
    * :doc:`oraclescreate name description format <oraclescreate>`
    * :doc:`oraclesinfo oracletxid <oraclesinfo>`
    * :doc:`oracleslist <oracleslist>`
    * :doc:`oraclesregister oracletxid datafee <oraclesregister>`
    * :doc:`oraclessubscribe oracletxid publisher datafee <oraclessubscribe>`
    * :doc:`oraclesdata oracletxid hexstr <oraclesdata>`
    * :doc:`oraclessamples oracletxid batonutxo num <oraclessamples>`

