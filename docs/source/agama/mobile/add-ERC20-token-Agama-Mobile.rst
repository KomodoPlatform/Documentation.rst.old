********************************
Add ERC20 Tokens to Agama Mobile
********************************

The Agama mobile code comprises of two parts. Agama wallet library and MeteorJS app. This assetchain adding guide will cover both. All the files needs changing are linked. If you want to add Bitcoin compatible coins follow :doc:`this guide <add-Bitcoin-Compatible-coin-Agama-Mobile>`.

Agama wallet library
====================

* Add a contract ID `pbca26/agama-wallet-lib:src/eth-erc20-contract-id.js@dev <>`_
* Add token decimals (optional, only if it's different from default 18 value) pbca26/agama-wallet-lib:src/eth-erc20-decimals.js@dev <>`_
* Submit a PR, use dev branch!

MeteorJS app
============

* Drop a 60 x 60 px logo into `/public/images/cryptologo/eth@dev <>`_ 
* Add ERC20 ticker to coins file `/imports/ui/actions/coins.js@dev#L80 <>`_
* Add asset chain name to translation file `/imports/ui/translate/en.js@dev#L475 <>`_.
* Submit a PR, use dev branch!



Please make sure the ERC20 Token is working in Agama before making a commit. Pull requests containing partial information or not working assets/servers will remain unmerged until all requirements are fulfilled.
