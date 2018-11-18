**********************************************************************************************************************
Complete Checklist for New Coins to Setup Explorers, Electrum Servers, Agama Wallet, Activate dPoW & BarterDEX Trading
**********************************************************************************************************************

This doc will guide you through creating an independent assetchain/coin using Komodo and setup explorer, electrum servers, integrate into Agama GUI wallet, dPoW and enable trading on BarterDEX.

Step 1: Create an Assetchain/Coin, Setup Insight based Explorer, Electrum Servers and Agama GUI Wallet
======================================================================================================

    1) :doc:`Create a new assetchain or coin <create-Komodo-Assetchain>`. Different Parameters to customize your coin are :doc:`here <assetchain-params>`
    2) Install explorer: `DeckerSU/komodo-explorers-install <https://github.com/DeckerSU/komodo-explorers-install>`_
    3) :doc:`Setup Electrum SPV server </barterDEX/setup-electrumX-server>`
    4) :doc:`Integrate into Agama GUI wallet <agama/add-Komodo-Assetchains-Agama-Desktop>` 

We have used Zaddex (ZEX) coin as example for some part of this doc. Please change to your coin name where ever applicable.

.. code-block:: shell

    Coin name: Zaddex
    Ticker: ZEX
    Start Command: ``./komodod -pubkey=$pubkey -ac_name=ZEX -ac_cc=2 -ac_founders=1 -ac_halving=525600 -ac_reward=13000000000 -ac_pubkey=039d4a50cc70d1184e462a22edb3b66385da97cc8059196f8305c184a3e21440af -addnode=5.9.102.210 &``
    RPCport: 26477

Step 2: PR List for Activating dPoW
===================================

In order to activate dPoW you need to submit Pull Requests into 2 GitHub repos.

    1) Komodo repo (``dev`` branch) - `jl777/komodo <https://github.com/jl777/komodo>`__
    2) SuperNET repo (``dev`` branch) - `jl777/SuperNET <https://github.com/jl777/SuperNET>`__

Step 2.1 Changes required for Komodo repo
-----------------------------------------

2 new files need to be created and 2 existing files need updating. These new files are executable scripts named as the **coin ticker with small letters**. They would go inside ``~/komodo/src/ac/`` and ``~/komodo/src/fiat/`` dir and required for quering the chain easily. i.e.: ``~/komodo/src/ac/zex getinfo`` .

Contents of these 2 new files would be as following:

.. code-block:: shell

    #!/bin/bash
    ./komodo-cli -ac_name=ZEX $1 $2 $3 $4 $5 $6

So, you will have `~/komodo/src/ac/zex <https://github.com/jl777/komodo/blob/dev/src/ac/zex>`_ and `~/komodo/src/fiat/zex <https://github.com/jl777/komodo/blob/dev/src/fiat/zex>`_ . **Make sure both of the files have proper executable permission** .

Next, is to add coin parameters at the bottom of `assetchains.json <https://github.com/jl777/komodo/blob/dev/src/assetchains.json#L202>`_ and `assetchains.old <https://github.com/jl777/komodo/blob/dev/src/assetchains.old#L47>`_ files inside ``~/komodo/src/`` directory. Please check the links to the files to understand how they were done. The ``.json`` file is basically converting the ZEX chain's startup command from shell fromat to JSON format.

Check `this commit <https://github.com/jl777/komodo/commit/7f5ed6ec453b78042bd791062203452a7043aa93>`__ to fully understand what was done to add ZEX to the Komodo repo.

Step 2.2 Changes required for SuperNET repo
-------------------------------------------

To the SuperNET repo, we need to add 1 new file called `zex_7776 <https://github.com/jl777/SuperNET/blob/dev/iguana/coins/zex_7776>`_ inside ``~/SuperNET/iguana/coins/`` (please change zex with your coin ticker). **Make sure this file has executable permission** . This file gets created automatically in the directory where you start the chain from. Generally inside ``~/komodo/src/`` dir.

And, we need to edit 4 existing files, `dpowassets <https://github.com/jl777/SuperNET/blob/dev/iguana/dpowassets#L50>`_, `iguana_notary.c <https://github.com/jl777/SuperNET/blob/dev/iguana/iguana_notary.c#L543>`_, `m_notary_run <https://github.com/jl777/SuperNET/blob/dev/iguana/m_notary_run#L106>`_ & `m_splitfund <https://github.com/jl777/SuperNET/blob/dev/iguana/m_splitfund#L51>`_) inside ``~/SuperNET/iguana/`` dir. These links points to the line where you should be checking.

Check `this commit <https://github.com/jl777/SuperNET/commit/c715f0aa4c99d20de6b99b5d173d543d2a94010f>`_ to fully understand what was done to add ZEX in SuperNET repo.

Once you have all the changes done locally, you can submit a PR to Komodo and SuperNET repo ``dev`` branch. After the PR gets merged , it will be announced and Komodo Notary Node operators will update their node and start notarizing the coin.

Step 3: PR List for enabling BarterDEX trading
==============================================

In order for the coin to be enabled in BarterDEX trading platform you need to submit a PR to `jl777/coins <https://github.com/jl777/coins>`_ repo. :doc:`Here </barterDEX/add-coin-barterDEX>` is an useful guide for the process  .

Requirements:

    1. Logo (icon) - `jl777/coins:icons/zex.png@master <https://github.com/jl777/coins/blob/master/icons/zex.png>`_ 
    2. Explorer - `jl777/coins:explorers/ZEX@master <https://github.com/jl777/coins/blob/master/explorers/ZEX>`_
    3. Coin info - `jl777/coins:coins@master#L2789 <https://github.com/jl777/coins/blob/master/coins#L2789>`_
    4. Electrum servers (BEER as example)- `jl777/coins:electrums/BEER@master <https://github.com/jl777/coins/blob/master/electrums/BEER>`_

.. note::

    If you can't do it all by yourself, there are 3rd party services (Chainmakers & Chainzilla) available who can do everything for you. Please reach them out using `Komodo Discord <https://komodoplatform.com/discord>`__ or use the `Komodo Platform Website. <http://komodoplatform.com/blockchain-starter-kit/#service-provider>`__
