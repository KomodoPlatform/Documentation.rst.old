***************************************
Add Komodo Assetchains in Agama Desktop
***************************************

The Agama desktop code comprises of two parts. Backend and UI. This assetchain addition guide will cover both. All the files that need to be changed are linked. If you want to add Bitcoin compatible coins follow :doc:`this guide <add-Bitcoin-Compatible-coin-Agama-Desktop>`.

Backend
=======

* Add a default asset chain port `KomodoPlatform/Agama:routes/ports.js@dev <https://github.com/KomodoPlatform/Agama/blob/dev/routes/ports.js>`_
* Add an electrum server for your asset (optional) `pbca26/agama-wallet-lib:src/electrum-servers.js@dev#L1 <https://github.com/pbca26/agama-wallet-lib/blob/dev/src/electrum-servers.js#L1>`_
* Add a fixed fee for your asset (required if you submit electrum servers list) `pbca26/agama-wallet-lib:src/fees.js@dev#L1 <https://github.com/pbca26/agama-wallet-lib/blob/dev/src/fees.js#L1>`_
* Add an asset chain to the list of kmd assets `pbca26/agama-wallet-lib:src/coin-helpers.js@dev#L1 <https://github.com/pbca26/agama-wallet-lib/blob/dev/src/coin-helpers.js#L1>`_
*  Add asset chain params to this file `KomodoPlatform/Agama:routes/chainParams.js@dev <https://github.com/KomodoPlatform/Agama/blob/dev/routes/chainParams.js>`_
* Submit a PR

Asset chains with block rewards (optional)
==========================================

* Add ``genproclimit: true`` property to allow mining with multiple CPU threads. Default value is 0 (e.g. ``-gen -genproclimit=0``) in case ``genproclimit`` option is not explicitly specified. `KomodoPlatform/Agama:routes/chainParams.js@dev <https://github.com/KomodoPlatform/Agama/blob/dev/routes/chainParams.js>`_

UI:
===

* Drop a 100 x 100 px (better 200 x 200 px) logo into `KomodoPlatform/EasyDEX-GUI:react/src/assets/images/cryptologo@dev <https://github.com/KomodoPlatform/EasyDEX-GUI/tree/dev/react/src/assets/images/cryptologo>`_
* Add an asset chain explorer `pbca26/agama-wallet-lib:src/coin-helpers.js@dev#L51 <https://github.com/pbca26/agama-wallet-lib/blob/dev/src/coin-helpers.js#L51>`_
* Add asset chain name to coins translation file `KomodoPlatform/EasyDEX-GUI:react/src/translate/coins.js@dev <https://github.com/KomodoPlatform/EasyDEX-GUI/blob/dev/react/src/translate/coins.js>`_, look for ``ASSETCHAINS``. 
* Submit a PR to ``dev`` branch on each repo.

Please make sure an assetchain is working in Agama before making a PR. Pull requests containing partial information or not working assets/servers will remain unmerged until all requirements are fulfilled.
