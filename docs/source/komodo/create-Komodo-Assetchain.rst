***********************
Creating New Assetchain
***********************

Requirements
============
* 2 computers with the ability to open ports
* At least 4gb RAM each
* At least 2 CPU cores each
* Komodod built on each, see :ref:`Installing Komodo Manually`



Creating a new blockchain
=========================

Note: Do not include the ``<>`` characters in commands. If you are using windows, replace ``./komodod`` and ``./komodo-cli`` with ``komodod.exe`` and ``komodo-cli.exe`` for each step.

.. code-block:: shell

	./komodod -ac_name=EXAMPLECHAIN -ac_supply=1000000 -addnode=<IP of other node> &

This is the simplest possible set of parameters. This will create a coin with the ticker symbol ``EXAMPLECHAIN`` with ``1000000`` premined coins. Blocks will be on-demand after block 128(the chain is only mined when a transaction is in the mempool) and the block reward will be ``.0001``.  Please refer to :ref:`Asset Chain Parameters` for a full list of parameters.

After issuing this command, you will see the p2p port in the terminal window. 

.. code-block:: shell

	>>>>>>>>>> EXAMPLECHAIN: p2p.8096 rpc.8097 magic.c89a5b16 3365559062 1000000 coins

This p2p port must not be blocked by a firewall. If the computers do not have a public IP address, you will need to port forward the p2p port and append the forwarded port to the IP. For example:

.. code-block:: shell

	./komodod -ac_name=EXAMPLECHAIN -ac_supply=1000000 -addnode=<IP of other node>:8096


Connecting with other node
==========================

On the second node, you now need to issue the same command with the first node's IP address along with setting ``-gen``.

.. code-block:: shell

	./komodod -ac_name=EXAMPLECHAIN -ac_supply=1000000 -addnode=<ipaddr of 1st node> -gen


When this second nodes connects to the first node, the second node will begin to mine blocks. The premine will be mined in the genesis block to the wallet of the node that set ``-gen``.

More info can be found in the debug.log of the chain found at ``~/.komodo/EXAMPLECHAIN/debug.log`` or ``%appdata%\komodo\EXAMPLECHAIN\debug.log`` on windows.

Querying Assetchain
===================

You can query for assetchain blocks and balances with this komodo CLI command:

.. code-block:: shell

	./komodo-cli -ac_name=EXAMPLECHAIN getinfo

Use the ``help`` command for a list of commands:

.. code-block:: shell

	./komodo-cli -ac_name=EXAMPLECHAIN help

Secure this Assetchain with Delayed Proof of Work
=================================================

Your new chain can be secured via dPOW by the Komodo notary nodes giving it Bitcoin level security. The current rate for this is 300 KMD and 800 of the coin per year. If you are interested in having a new chain notarized, please contact @siu on the Komodo slack or discord. 

.. [credit] 
          Document written by Alright based on previous guides by siu and PTYX. Please send any critiques to Alright on matrix, slack or discord.
