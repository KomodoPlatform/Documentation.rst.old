*********************************************
Get your Coin/Token/Asset listed on barterDEX
*********************************************

Adding a coin to the BarterDEX is as simple as writing one line of code if your coin is a Bitcoin compatible. Below is a breakdown of the information needed from the source code and coin parameters. The first step is to gather all the information below and contact our specialists for review. 

For ETH compatibles go to: :ref:`How to Add new ERC20 Tokens in BarterDEX`

Coin Spec
=========

The Proposed coin must have support for the following API calls and must have BIP65 implemented.

.. code-block:: shell

	estimatefee
	getblock
	getblockhash
	getinfo
	getrawmempool
	getrawtransaction
	gettxout
	importaddress
	importprivkey
	listunspent
	listreceivedbyaddress
	listtransactions
	sendrawtransaction
	signrawtransaction
	validateaddress

Information Required
====================

Example
-------

	* **Coin Ticker** : LTC
	* **Coin Name**: litecoin
	* **rpcport** : 9332
	* **pubtype** : 48
	* **taddr** : 0
	* **p2shtype** : 50
	* **wiftype** : 176
	* **txfee** : 1000000
	* **active** : 1
	
Other info to take note of
--------------------------

1. Need an icon too. After getting confirmation from our specialists, submit a pull request to the repository: https://github.com/jl777/coins

2. The file https://github.com/jl777/coins/blob/master/coins contains all the info required to list the coin in BarterDEX

3. The explorer repository of the proposed coin also contains some of the info required to connect BarterDEX to the coin's own explorer infrastructure.

4. The coin devs will have to send us an amount of the proposed coin to test the swaps with.

5. Please use the info from coins-db-repo for the newest electrums, explorers and so on

6. Electrum servers are in the electrums-directory. Every coin has its own file there: https://github.com/jl777/coins/tree/master/electrums

Json Output Example:
--------------------

.. code-block:: shell

	{\"coin\":\"LTC\", \"name\": \"litecoin\", \"active\":1, \"rpcport\":9332,\"pubtype\":48, \"p2shtype\":50, \"wiftype\":176, \"txfee\":100000}

Note:
-----

	For **taddr** , 1 means yes and 0 means no and it refers to the coin having transparent and zaddresses. Mostly this is for zcash forks.


Search for the information on Github
====================================

All of the information and parameters required are normally contained within but not limited to these files (depends on your coin):

	* init.cpp: https://github.com/litecoin-project/litecoin/blob/master/src/init.cpp

	* base58.h: https://github.com/litecoin-project/litecoin/blob/master/src/base58.h

	* chainparamsbase.h: https://github.com/litecoin-project/litecoin/blob/master/src/chainparamsbase.h

Additional Information
======================

	* Lead developer's Github account:
	* Bitcointalk Account:
	* Information about the team and purpose of the coin:
	* Social Media Accounts

Once the information is gathered, please contact us via email: coinintegration@komodoplatform.com or #tradebots channel in our Discord (Invite Link: https://komodoplatform.com/discord) and request a coin addition. Provide us with all the relevant information and our specialists will get in touch.

How to Add new ERC20 Tokens in BarterDEX
========================================

Adding ERC20 tokens in BarterDEX is very easy. We just need some information about the token.

Requirements:
-------------

	* ``approve`` and ``transferFrom`` methods are a must for the swaps to work
	* Contract address
	* Ticker Symbol
	* Name of the token
	* CoinMarketCap name (for the autoprice with CMC to work)
	* Token Logo
	* Some tokens for testing
	* rpcport is same for all tokens in BarterDEX

The following is an example using OmiseGo (OMG)

.. code-block:: json

	{
	  "coin": "OMG",
	  "name": "omisego",
	  "fname": "OmiseGo",
	  "etomic": "0xd26114cd6EE289AccF82350c8d8487fedB8A0C07",
	  "rpcport": 80
	}

Once the information is gathered, please contact us via email coinintegration@komodoplatform.com or at #etomic channel in our Discord (Invite Link: https://komodoplatform.com/discord ) in order to add the information to the BarterDEX and to perform the required test atomic swaps to make sure it performs properly. 

You can send some tokens to test to the following BarterDEX test engineers. 

Cipi: ``0xdf38dd108bab50da564092ad0cd739c4634d963c``


