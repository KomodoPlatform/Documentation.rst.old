******************************************
Be a marketmaker or LP using barterDEX CLI
******************************************

It is very easy to be a marketmaker or Liquidity Provider (LP) in barterDEX. Anyone can be LP using any supported coin and can provide liquidity for any pair in the market.

Benefits of being an LP node:
=============================

* LP node / seller doesn't have to pay 0.15% DEX fee
* Can do margin trading

Requirements:
=============

#. barterDEX CLI installed - guide
#. Native coin wallet(s) or Electrum server list (see below)

APIs needed
===========

You will only need :ref:`client`, :ref:`setpassphrase`, :ref:`enable` or :ref:`electrum` & :ref:`autoprice` to be a marketmaker or LP in barterDEX. All the API usage is explained in the below steps.

Steps:
------

**client**

Use ``./client &`` to start barterDEX. Do NOT use ``./run`` unless you have reliable fast connection from a datacenter or VPS. Don't change the file contents unless you know what you are doing.

**setpassphrase**

This API will set your passphrase and let you use the userpass value in every script. This is the second API/script you need to run.

**enable or electrum**

If you are planning to use native mode, coin daemons need to be installed, blockchain fully synced if using native. Native is recommended for faster performance and reliability. Alternatively, you can use electrum which does not require blockchain to be downloaded.

**[Note:** ``electrum`` **is not recommended to setup an LP node. It will create connectivity issues and you may run into trouble while trying to match and process swaps.]**

Edit the ``enable`` script with the coin names you want to activate for trading. Or, edit the ``electrum`` script to add the electrum servers for the coins that you want to trade in from the :doc:`list of electrum servers <electrum-servers-list>` to activate the coins in electrum mode.

**autoprice**

This is the most important API for LP or marketmaker. You need to edit this file to your liking. This contains the price, coin name for any pair your are making. Check :doc:`here <barterDEX-API>` for more info on the api.

Once you issue the ``./autoprice`` script, you just need to wait for alice/buyer to buy from your order. All the trade info will be shown in your console as they are happening.
