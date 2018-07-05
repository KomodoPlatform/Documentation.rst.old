*****************************************
Common Useful Komodo and Bitcoin commands
*****************************************

Get Wallet information
======================

You can use ``getwalletinfo`` command to see just your wallet's balance, unconfirmed balance, wallet version and such.

.. code-block:: shell

	# For Komodo
	$ ./komodo-cli getwalletinfo
	{
	    "walletversion" : 60000,
	    "balance" : 89.46187742,
	    "unconfirmed_balance" : 0.00000000,
	    "immature_balance" : 0.00000000,
	    "txcount" : 484,
	    "keypoololdest" : 1482746526,
	    "keypoolsize" : 101
	}

	# For Bitcoin
	$ bitcoin-cli getwalletinfo
	{
	  "walletversion": 130000,
	  "balance": 0.03281999,
	  "unconfirmed_balance": 0.00000000,
	  "immature_balance": 0.00000000,
	  "txcount": 251,
	  "keypoololdest": 1477183290,
	  "keypoolsize": 100,
	  "paytxfee": 0.00000000,
	  "hdmasterkeyid": "de5e4d25f2887886eb2eca1fba625be46d3fd8f2"
	}

Check all addresses in your wallet and their funds
==================================================

.. code-block:: shell

	$ bitcoin-cli listaddressgroupings
	[
	  [
	    [
	      "14dEGV9AdBgm6awo4uxojWAEYHTMf5QuQm", 
	      0.03281999, 
	      ""
	    ]
	  ], 
	  [
	    [
      	  "15R3C2ZKmak5pCc4duLY2jLtFD3o1jaeNd", 
	      0.00460000, 
	      "15R3C2ZKmak5pCc4duLY2jLtFD3o1jaeNd"
	    ]
	  ]
	]

**TODO**


