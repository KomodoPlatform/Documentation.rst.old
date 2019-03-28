*********************
Agama-v0.2.41-Updates
*********************

Enhancements
============

1. Custom electrum servers config

a. The ability to configure a custom electrum server list has been added to ``Settings -> App Config``

.. image:: images/Agama-v0.2.41/image1.png
   :align: center
   :scale: 75 %

2. Extended argv - **Dev only**

3. KV electrum list

a. The ability to sync the electrum servers list from KV has been added to ``Settings -> App Config``

.. image:: images/Agama-v0.2.41/image2.png
   :align: center
   :scale: 75 %

4. Load coins list from file on app initialization
 
a. To enable loading your favorite coins from a file select the Load coins list from file option in ``Settings -> App Config``

.. image:: images/Agama-v0.2.41/image3.png
   :align: center
   :scale: 75 %

5. KV electrum servers list

a. The KV electrum server list may now be downloaded by selecting the Download KV Electrum servers list button in ``Settings->App Config``

.. image:: images/Agama-v0.2.41/image4.png
   :align: center
   :scale: 75 %

6. Spv watch-only hides KMD claim button

a. If ``KMD`` is logged in as watch only, then the claim rewards button will now be hidden.

.. image:: images/Agama-v0.2.41/image5.png
   :align: center
   :scale: 75 %

7. Updated support page

a. Support tickets link has been updated to https://support.komodoplatform.com

.. image:: images/Agama-v0.2.41/image6.png
   :align: center
   :scale: 75 %

8. Spv balance subtract unconfirmed balance, displays info icon

a. The info icon has been added to the ``Send -> Confirming`` screen

.. image:: images/Agama-v0.2.41/image7.png
   :align: center
   :scale: 75 %

9. Updated asset explorers to point to \*.kmdexplorer.io - **Dev only**

10. ZILLA coin added.

a. Chainzilla coin is now available in the Activate Coin screen

.. image:: images/Agama-v0.2.41/image8.png
   :align: center
   :scale: 75 %

b. Chainzilla wallet creation

.. image:: images/Agama-v0.2.41/image9.png
   :align: center
   :scale: 75 %

11. Tx history csv export

a. Exporting the tx history in csv format is now available in the bottom portion of Transactions screen

.. image:: images/Agama-v0.2.41/image10.png
   :align: center
   :scale: 75 %

12. Spv ``Send`` - no valid utxo - message handling

a. A new utxo validation message will now display with more detail

.. image:: images/Agama-v0.2.41/image11.png
   :align: center
   :scale: 75 %

13. Spv send confirm with pin

a .To require a pin for send transactions go to ``Settings -> App Config -> Require pin to confirm transaction`` tab

.. image:: images/Agama-v0.2.41/image12.png
   :align: center
   :scale: 75 %

b. Once enabled save changes then restart the wallet. Now when making a send transaction your pin is required before confirming

.. image:: images/Agama-v0.2.41/image13.png
   :align: center
   :scale: 75 %

Fixes
=====

* KV null history display fix
* KV history refresh fix
* KV history refresh button fix
* Native send result table css overflow fix
* Fixed settings save bug that got socket timeout param broken
* Fixes the recent SPV connectivity issues




