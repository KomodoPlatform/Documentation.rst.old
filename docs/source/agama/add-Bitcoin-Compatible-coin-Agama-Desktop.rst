**********************************************
Add a Bitcoin Compatible coin to Agama Desktop
**********************************************

To learn about adding Komodo Assetchains to Agama look :doc:`here <add-Komodo-Assetchains-Agama-Desktop>` . This guide will help you to add Bitcoin compatible coins into Agama desktop wallet. You have to edit the backend part and the UI part to add. Follow the guide carefully.

Backend
=======

* Add coin specific params to networks file `/routes/electrumjs/electrumjs.networks.js@v0.25 <https://github.com/KomodoPlatform/Agama/blob/v0.25/routes/electrumjs/electrumjs.networks.js>`_
* Depending on a coin type you might need to add a coin to ``isPoS`` or ``isZcash`` helpers here `/routes/shepherd/electrum/network.js@v0.25 <https://github.com/KomodoPlatform/Agama/blob/v0.25/routes/shepherd/electrum/network.js>`_
* Add an electrum server `/routes/electrumjs/electrumServers.js@v0.25 <https://github.com/KomodoPlatform/Agama/blob/v0.25/routes/electrumjs/electrumServers.js>`_
* Submit a `PR <https://github.com/KomodoPlatform/Agama>`_

UI:
===

* Add a coin to UI coin helper file KomodoPlatform/EasyDEX-GUI:`react/src/util/coinHelper.js@v0.25#L9 <https://github.com/KomodoPlatform/EasyDEX-GUI/blob/v0.25/react/src/util/coinHelper.js#L9>`_
* Add an asset chain to Add Coin component render `KomodoPlatform/EasyDEX-GUI:react/src/components/addcoin/addcoinOptionsCrypto.js@v0.25#L19 <https://github.com/KomodoPlatform/EasyDEX-GUI/blob/v0.25/react/src/components/addcoin/addcoinOptionsCrypto.js#L19>`_
* Drop a 100 x 100 px (better 200 x 200 px) logo into `KomodoPlatform/EasyDEX-GUI:react/src/assets/images/cryptologo@v0.25 <https://github.com/KomodoPlatform/EasyDEX-GUI/tree/v0.25/react/src/assets/images/cryptologo>`_
* Add an explorer `KomodoPlatform/EasyDEX-GUI:react/src/util/explorerList.js@v0.25#L4 <https://github.com/KomodoPlatform/EasyDEX-GUI/tree/v0.25/react/src/assets/images/cryptologo>`_
* Submit a `PR <https://github.com/KomodoPlatform/Agama>`_

Please make sure an asset chain is working in Agama before making a commit. Pull requests containing partial information or not working assets/servers will remain unmerged until all requirements are fulfilled.
