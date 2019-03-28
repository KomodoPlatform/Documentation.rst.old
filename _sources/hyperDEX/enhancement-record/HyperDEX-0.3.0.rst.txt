***************************
HyperDEX-0.3.0-Enhancements
***************************

1. Make the swap list rows clickable. You now click anywhere in the row instead of the "View" button. `Commit Details <https://github.com/atomiclabs/hyperdex/commit/5768b3ef897649b6d1853e5634b17f3b5ed5993a>`__

.. image:: images/HyperDEX-0.3.0/image1.png
   :align: center
   :scale: 75 %

2. Add filters to the trade history. `Commit Details <https://github.com/atomiclabs/hyperdex/commit/6074f21d37d001495e588d8387a1b1b0055d51bb>`__

a. Within the Trade History of Trades view you may now filter by date (yyyy-mm-dd), order pair, and order type (buy or sell)
    
.. image:: images/HyperDEX-0.3.0/image2.png
   :align: center
   :scale: 75 %

3. Add a copy button to the modal that shows your seed phrase. `Commit Details <https://github.com/atomiclabs/hyperdex/commit/be63d250e049fb6d75e2d35e9bc3dc8bcb44048c>`__

a. A copy function has now been added when retrieving your seed, to do so first go to the Settings view

.. image:: images/HyperDEX-0.3.0/image3.png
   :align: center
   :scale: 75 %

b. Once selected a prompt will appear for passphrase entry, enter your passphrase then select Submit

.. image:: images/HyperDEX-0.3.0/image4.png
   :align: center
   :scale: 75 %

c. Now your passphrase will be shown with the ability to copy it

.. image:: images/HyperDEX-0.3.0/image5.png
   :align: center
   :scale: 75 %

4. In the Dashboard view, show 6 fractional digits for currencies worth less than 1. `Commit Details <https://github.com/atomiclabs/hyperdex/commit/1cab80f13e538e4f4c201d2195b7822032cd04fb>`__

.. image:: images/HyperDEX-0.3.0/image6.png
   :align: center
   :scale: 75 %

5. Add Pungo Token (PGT) currency. `Commit Details <https://github.com/atomiclabs/hyperdex/commit/b84139d81b6da4c418b098bd7ef89a3ab42d9e06>`__

a. Pungo Token (PGT) may now be added in the Settings view

.. image:: images/HyperDEX-0.3.0/image7.png
   :align: center
   :scale: 75 %

b. Once added in the Settings view PGT will be available in the Dashboard view

.. image:: images/HyperDEX-0.3.0/image8.png
   :align: center
   :scale: 75 %

6. Move enabled currencies from the app settings to the portfolio data. It is automatically migrated. This means portfolios can have different enabled currencies. `Commit Details <https://github.com/atomiclabs/hyperdex/commit/37996edd80f8aa1671758d0d66edf3dc81448078>`__

Fixes
=====

    * Fix a small zero being accidentally shown after the wallet currency price. `Commit Details <https://github.com/atomiclabs/hyperdex/commit/9d9769e47abd945ebe977d3fa578cfe0ad3ca99e>`__
    * Fix the price history fetching error handling. `Commit Details <https://github.com/atomiclabs/hyperdex/commit/fb23e3284a4ba7c6a671502fa2e2850c179e3b74>`__
    * Fix the dashboard price history graph. `Commit Details <https://github.com/atomiclabs/hyperdex/commit/b0d9d7d61db593589d1e4ea668be1f683d7e0c42>`__

Dev Only
========

    * Update to `BarterDEX Marketmaker v1.0.1026 <https://github.com/artemii235/SuperNET/releases/tag/v1.0.1026>`__. `Commit Details <https://github.com/atomiclabs/hyperdex/commit/d04da2e16d4801ad65595a44ace512a81ce1c34f>`__
    * Remove DNR, ARG, MAC, and CALL currencies. See `#577 (comment) <https://github.com/atomiclabs/hyperdex/pull/577#issuecomment-445567840>`__. `Commit Details <https://github.com/atomiclabs/hyperdex/commit/69b388d25c40d77de437cf0fa467a6e1b0ee3d98>`__
    * Update LTC and BCH Electrum servers. `Commit Details <https://github.com/atomiclabs/hyperdex/commit/69b388d25c40d77de437cf0fa467a6e1b0ee3d98>`__
