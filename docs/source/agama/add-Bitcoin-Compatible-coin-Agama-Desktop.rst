**********************************************
Add a Bitcoin Compatible coin to Agama Desktop
**********************************************

To learn about adding Komodo Assetchains to Agama look :doc:`here <add-Komodo-Assetchains-Agama-Desktop>` . This guide will help you to add Bitcoin compatible coins into Agama desktop wallet. You have to edit the backend part and the UI part to add. Follow the guide carefully.

Backend
=======

* Add network params `pbca26/agama-wallet-lib:src/bitcoinjs-networks.js@dev <https://github.com/pbca26/agama-wallet-lib/blob/dev/src/bitcoinjs-networks.js>`_. Make use of isPoS or isZcash flags if applicable in your case.
* Add an electrum server `pbca26/agama-wallet-lib:src/electrum-servers.js@dev#L1 <https://github.com/pbca26/agama-wallet-lib/blob/dev/src/electrum-servers.js#L1>`_
* Add a safe fixed fee (per transaction) `pbca26/agama-wallet-lib:src/fees.js@dev#L1 <https://github.com/pbca26/agama-wallet-lib/blob/dev/src/fees.js#L1>`_.
* Add an explorer `pbca26/agama-wallet-lib:src/coin-helpers.js@dev#L62 <https://github.com/pbca26/agama-wallet-lib/blob/dev/src/coin-helpers.js#L62>`_.
* Submit a PR to the ``dev`` branch of the repo: https://github.com/pbca26/agama-wallet-lib.

UI:
===

* Drop a 100 x 100 px (better 200 x 200 px) logo into `KomodoPlatform/EasyDEX-GUI:react/src/assets/images/cryptologo@dev<https://github.com/KomodoPlatform/EasyDEX-GUI/tree/dev/react/src/assets/images/cryptologo>`_ .
* Add your coin name to EN translation file `KomodoPlatform/EasyDEX-GUI:react/src/translate/en.js@dev <https://github.com/KomodoPlatform/EasyDEX-GUI/blob/dev/react/src/translate/en.js>`_, look for "CRYPTO".
* Submit a PR to ``dev`` branch of the repo https://github.com/KomodoPlatform/EasyDEX-GUI .

Please make sure an asset chain is working in Agama before making a commit. Pull requests containing partial information or not working assets/servers will remain unmerged until all requirements are fulfilled.
