********
Gateways
********

**Work in progress**

Introduction
============

For an introduction to CC in general, see: :ref:`Using the Contracts on a Komodo based Blockchain`

To enable and test contracts:

    * The Blockchain must have the parameter ``-ac_cc`` as described in :ref:`Using the Contracts on a Komodo based Blockchain`
    * The Blockchain must be started using the parameter ``-pubkey`` with a pubkey whose privatekey is owned by only you and imported into the wallet of this particular chain.

The basic idea is to tokenize other crypto coins (like BTC or KMD) and then use the tokensCC to transact/swap against the tokenized crypto. By enforcing a 1:1 peg between a specific token and BTC (or KMD) and an automated deposit/withdraw mechanism, it is possible to transact in the tokenized BTC without delay or expensive BTC txfees on the Bitcoin Blockchain. Then anybody that ends up having any of the BTC tokens would be able to withdraw actual BTC by redeeming the token.

A tutorial describing the usage of Gateways contract is :doc:`here <scenarios/tutorial>`

.. _gateways-rpc:

Available RPC Calls
===================

    * :doc:` <>`
    * :doc:` <>`
    * :doc:` <>`
    * :doc:` <>`
    * :doc:` <>`
    * :doc:` <>`
