***************************************
Add Komodo Assetchains in Agama Desktop
***************************************

The Agama desktop code comprises of two parts. Backend and UI. This assetchain adding guide will cover both. All the files needs changing are linked. If you want to add Bitcoin compatible coins follow :doc:`this guide <add-Bitcoin-Compatible-coin-Agama-Desktop>`.

Backend
=======

* Add a default asset chain port `/routes/ports.js@dev <https://github.com/KomodoPlatform/Agama/blob/dev/routes/ports.js>`_
* Add an electrum server for your asset (optional) `pbca26/agama-wallet-lib:src/electrum-servers.js@dev#L1 <https://github.com/pbca26/agama-wallet-lib/blob/dev/src/electrum-servers.js#L1>`_
* Add an asset chain to the list of kmd assets `pbca26/agama-wallet-lib:src/coin-helpers.js@dev#L1 <https://github.com/pbca26/agama-wallet-lib/blob/dev/src/coin-helpers.js#L1>`_
*  Add asset chain params to this file `/routes/chainParams.js@dev <https://github.com/KomodoPlatform/Agama/blob/dev/routes/chainParams.js>`_
* Submit a `PR <https://github.com/KomodoPlatform/Agama>`_

UI:
===

* Drop a 100 x 100 px (better 200 x 200 px) logo into `KomodoPlatform/EasyDEX-GUI:react/src/assets/images/cryptologo@dev <https://github.com/KomodoPlatform/EasyDEX-GUI/tree/dev/react/src/assets/images/cryptologo>`_
* Add an asset chain explorer `pbca26/agama-wallet-lib:src/coin-helpers.js@dev#L51 <https://github.com/pbca26/agama-wallet-lib/blob/dev/src/coin-helpers.js#L51>`_
* Add asset chain name to EN translation file [https://github.com/KomodoPlatform/EasyDEX-GUI/blob/dev/react/src/translate/en.js] (`KomodoPlatform/EasyDEX-GUI:react/src/translate/en.js@dev <https://github.com/KomodoPlatform/EasyDEX-GUI/blob/dev/react/src/translate/en.js>`_), look for ``ASSETCHAINS``. 
* Submit a `PR <https://github.com/KomodoPlatform/Agama>`_ to ``dev`` branch on each repo.

Please make sure an asset chain is working in Agama before making a commit. Pull requests containing partial information or not working assets/servers will remain unmerged until all requirements are fulfilled.
