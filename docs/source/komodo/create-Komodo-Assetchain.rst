***************************************************
Creating a new Blockchain using Komodo's technology
***************************************************

Requirements
============

* 2 Computers with the ability to open ports. (simpler if they have static public IP addresses)
* At least 4GB RAM each
* At least 2 CPU cores each
* 64-bit Operating System (Ubuntu 16.04 recommended)
* ``komodod`` built on each, see :ref:`Installing Komodo Manually` (No need to download the Komodo blockchain)

Creating a new blockchain
=========================

Note: Do not include the ``<>`` characters in commands. If you are using windows, replace ``./komodod`` and ``./komodo-cli`` with ``komodod.exe`` and ``komodo-cli.exe`` for each step. Replace ``cd ~/komodo/src`` with the folder where ``komodod.exe`` is located.

.. code-block:: shell

	cd ~/komodo/src
	./komodod -ac_name=EXAMPLECHAIN -ac_supply=1000000 -addnode=<IP address of the second node> &

This is the simplest possible set of parameters. This will create a coin with the ticker symbol ``EXAMPLECHAIN`` with ``1000000`` premined coins. Blocks will be on-demand after block 128(the chain is only mined when a transaction is in the mempool) and the block reward will be ``.0001``. 

.. note::

	The parameter -ac_supply should be set to a whole number without any decimals places and it should be less than 2000000000 to avoid 64 bit overflows.

Please refer to :doc:`this doc </komodo/assetchain-params>` for a full list of parameters to customize your blockchain.

After issuing this command, you will see the p2p port in the terminal window. 

.. code-block:: shell

	>>>>>>>>>> EXAMPLECHAIN: p2p.8096 rpc.8097 magic.c89a5b16 3365559062 1000000 coins

This p2p port must not be blocked by a firewall. If the computers do not have public IP addresses, you will need to port-forward the p2p port on both computers and append the forwarded port to the IP. For example:

.. code-block:: shell

	./komodod -ac_name=EXAMPLECHAIN -ac_supply=1000000 -addnode=<IP of the second node>:8096


Connecting with the second node
===============================

On the second node, you now need to issue the same command, but with the first node's IP address along with setting ``-gen -genproclimit=$(nproc)``.

.. code-block:: shell

	cd ~/komodo/src
	./komodod -ac_name=EXAMPLECHAIN -ac_supply=1000000 -addnode=<IP address of the first node> -gen -genproclimit=$(nproc)

When this second node connects to the first node, the second node will begin to mine blocks. The premine will be mined in the genesis block to the wallet of the node that set ``-gen -genproclimit=$(nproc)``.

You can check the contents of the wallet by executing the following command in another terminal:

.. code-block:: shell

	./komodo-cli -ac_name=EXAMPLECHAIN getwalletinfo

More info can be found in the debug.log of the chain found at ``~/.komodo/EXAMPLECHAIN/debug.log`` or ``%appdata%\komodo\EXAMPLECHAIN\debug.log`` on windows.

Querying the Assetchain
=======================

You can query for assetchain blocks and balances with this komodo CLI command:

.. code-block:: shell

	./komodo-cli -ac_name=EXAMPLECHAIN getinfo

Use the ``help`` command for a list of commands:

.. code-block:: shell

	./komodo-cli -ac_name=EXAMPLECHAIN help

Secure this Assetchain with Delayed Proof of Work (dPoW)
========================================================

Your new chain can be secured via dPoW by the Komodo Notary Nodes giving it Bitcoin level security. If you are interested in having a new chain notarized, please contact @siu or @PTYX on the Komodo discord.

@PTYX has launched `ChainZilla <https://www.chainzilla.io/>`_ and @siu:matrix.org has launched `Chainmakers <https://www.chainmakers.co/>`_ to provide assetchain creation, electrum server setup, explorers, dICO services etc.

Please send any critique/feedback to Alright or gcharang on matrix or discord.

`Discord Invite <https://komodoplatform.com/discord>`_
