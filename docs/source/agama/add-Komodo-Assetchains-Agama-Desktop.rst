***************************************
Add Komodo Assetchains in Agama Desktop
***************************************

The Agama desktop code comprises of two parts. Backend and UI. This assetchain adding guide will cover both. All the files needs changing are linked. If you want to add Bitcoin compatible coins follow :doc:`this guide <add-Bitcoin-Compatible-coin-Agama-Desktop>`.

Backend
=======

* Add a default asset chain port `/routes/ports.js@dev <https://github.com/KomodoPlatform/Agama/blob/dev/routes/ports.js>`_
* Add an electrum server for your asset (optional) `/routes/electrumjs/electrumServers.js@dev <https://github.com/KomodoPlatform/Agama/blob/dev/routes/electrumjs/electrumServers.js>`_
* Add an asset chain to the list of kmd assets `/routes/shepherd/electrum/network.js@dev#L6 <https://github.com/KomodoPlatform/Agama/blob/dev/routes/shepherd/electrum/network.js#L6>`_
* Submit a `PR <https://github.com/KomodoPlatform/Agama>`_

UI:
===

* Add asset chain entries to this file `KomodoPlatform/EasyDEX-GUI:react/src/components/addcoin/payload.js@dev#L45 <https://github.com/KomodoPlatform/EasyDEX-GUI/blob/dev/react/src/components/addcoin/payload.js#L45>`_
* Add an asset chain to UI coin helper file `KomodoPlatform/EasyDEX-GUI:react/src/util/coinHelper.js@dev#L9 <https://github.com/KomodoPlatform/EasyDEX-GUI/blob/dev/react/src/util/coinHelper.js#L9>`_
* Add an asset chain to Add Coin component render `KomodoPlatform/EasyDEX-GUI:react/src/components/addcoin/addcoinOptionsAC.js@dev#L28 <https://github.com/KomodoPlatform/EasyDEX-GUI/blob/dev/react/src/components/addcoin/addcoinOptionsAC.js#L28>`_
* Drop a 100 x 100 px (better 200 x 200 px) logo into `KomodoPlatform/EasyDEX-GUI:react/src/assets/images/cryptologo@dev <https://github.com/KomodoPlatform/EasyDEX-GUI/tree/dev/react/src/assets/images/cryptologo>`_
* Add an asset chain explorer `KomodoPlatform/EasyDEX-GUI:react/src/util/explorerList.js@dev#L4 <https://github.com/KomodoPlatform/EasyDEX-GUI/blob/dev/react/src/util/explorerList.js#L4>`_ 
* Add asset chain name to EN translation file `KomodoPlatform/EasyDEX-GUI:react/src/translate/en.js@dev#L828 <https://github.com/KomodoPlatform/EasyDEX-GUI/blob/dev/react/src/translate/en.js#L828>`_
* Submit a `PR <https://github.com/KomodoPlatform/Agama>`_

Please make sure an asset chain is working in Agama before making a commit. Pull requests containing partial information or not working assets/servers will remain unmerged until all requirements are fulfilled.
