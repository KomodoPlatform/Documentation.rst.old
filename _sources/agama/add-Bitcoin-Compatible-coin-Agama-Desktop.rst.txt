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
* Submit a PR

UI:
===

* Drop a 100 x 100 px (better 200 x 200 px) logo into `KomodoPlatform/EasyDEX-GUI:react/src/assets/images/cryptologo/btc@dev <https://github.com/KomodoPlatform/EasyDEX-GUI/tree/dev/react/src/assets/images/cryptologo/btc>`_ .
* Add your coin name to EN translation file `KomodoPlatform/EasyDEX-GUI:react/src/translate/coins.js@dev <https://github.com/KomodoPlatform/EasyDEX-GUI/blob/dev/react/src/translate/coins.js>`_, look for ``CRYPTO``.
* Add your coin to coins helper file `KomodoPlatform/EasyDEX-GUI:react/src/util/coinHelper.js@dev#L300 <https://github.com/KomodoPlatform/EasyDEX-GUI/blob/dev/react/src/util/coinHelper.js#L300>`_.
* Submit a PR to ``dev`` branch of each repo .

How to get network parameters
=============================

* pubKeyHash: `KomodoPlatform/komodo:src/chainparams.cpp@fbb3b3e#L169 <https://github.com/KomodoPlatform/komodo/blob/fbb3b3e9a0c432173a8d733ebbcbd7b0324d58df/src/chainparams.cpp#L169>`_
* scriptHash: `KomodoPlatform/komodo:src/chainparams.cpp@fbb3b3e#L170 <https://github.com/KomodoPlatform/komodo/blob/fbb3b3e9a0c432173a8d733ebbcbd7b0324d58df/src/chainparams.cpp#L170>`_
* wif: `KomodoPlatform/komodo:src/chainparams.cpp@fbb3b3e#L171 <https://github.com/KomodoPlatform/komodo/blob/fbb3b3e9a0c432173a8d733ebbcbd7b0324d58df/src/chainparams.cpp#L171>`_
* bip32 public: `KomodoPlatform/komodo:src/chainparams.cpp@fbb3b3e#L172 <https://github.com/KomodoPlatform/komodo/blob/fbb3b3e9a0c432173a8d733ebbcbd7b0324d58df/src/chainparams.cpp#L172>`_
* bip32 private: `KomodoPlatform/komodo:src/chainparams.cpp@fbb3b3e#L173 <https://github.com/KomodoPlatform/komodo/blob/fbb3b3e9a0c432173a8d733ebbcbd7b0324d58df/src/chainparams.cpp#L173>`_

.. note::

    * You need to convert pubKeyHash (PUBKEY_ADDRESS), scriptHash (SCRIPT_ADDRESS) and wif (SECRET_KEY) decimal values to hexadecimal representation. You can use this website to do the conversion: https://www.binaryhexconverter.com/decimal-to-hex-converter . 
    * PUBKEY_ADDRESS conversion example (KMD): ``60 dec -> 0x3c hex``
    * In case if ``SECRET_KEY`` consists of two decimal numbers (e.g. ``63 + 128``) sum them up and use the result (``192``) on the converter website listed above.

If you can't find ``chainparams.cpp`` in your code base, try checking one of the files listed :ref:`here <search-info-on-github>`

Please make sure the BTC compatible coin is working in Agama before making a PR. Pull requests containing partial information or not working assets/servers will remain unmerged until all requirements are fulfilled.
