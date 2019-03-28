************************************
HyperDEX-0.1.0-alpha.14-Enhancements
************************************

1. Add Gemini dollar (GUSD) `Commit Details <https://github.com/atomiclabs/hyperdex/commit/8c4eace45fd2fb26f70b7dbbfeb8442acafc55c7>`__ 

a. Gemini dollar coin may now be added in the enabled currencies section of the Settings view

.. image:: images/HyperDEX-0.1.0-alpha.14/image1.png
   :align: center
   :scale: 75 %

b. Once added in the Settings view the Gemini dollar coin will now be added to the portfolio in the Dashboard view

.. image:: images/HyperDEX-0.1.0-alpha.14/image2.png
   :align: center
   :scale: 75 %

c. Gemini dollar may also be traded in the Exchange view

.. image:: images/HyperDEX-0.1.0-alpha.14/image3.png
   :align: center
   :scale: 75 %

2. Add Old Capital (OCALL) `Commit Details <https://github.com/atomiclabs/hyperdex/commit/35f95d9650257640f163c840ae64a1cc581ed104>`__ 

a. Old Capital coin may now be added in the enabled currencies section of the Settings view

.. image:: images/HyperDEX-0.1.0-alpha.14/image4.png
   :align: center
   :scale: 75 %

b. Once added in the Settings view the Old Capital coin will now be added to the portfolio in the Dashboard view

.. image:: images/HyperDEX-0.1.0-alpha.14/image5.png
   :align: center
   :scale: 75 %

c. Old Capital may also be traded in the Exchange view

.. image:: images/HyperDEX-0.1.0-alpha.14/image6.png
   :align: center
   :scale: 75 %

3. Add Capital GAS (CALLG) `Commit Details <https://github.com/atomiclabs/hyperdex/commit/34f76112d214dc517c7c2b74f6cb3f6f16bbc7af>`__ 

a. Old Capital coin may now be added in the enabled currencies section of the Settings view

.. image:: images/HyperDEX-0.1.0-alpha.14/image7.png
   :align: center
   :scale: 75 %

b. Once added in the Settings view the Old Capital coin will now be added to the portfolio in the Dashboard view

.. image:: images/HyperDEX-0.1.0-alpha.14/image8.png
   :align: center
   :scale: 75 %

c. Old Capital may also be traded in the Exchange view

.. image:: images/HyperDEX-0.1.0-alpha.14/image9.png
   :align: center
   :scale: 75 %

4. Rename EQL to EQLI in the list of default currencies. `Commit Details <https://github.com/atomiclabs/hyperdex/commit/575056075278db372a724cde549743e0ba000bb2>`__ 

a. The Equaliser coin ticker has been updated in the Settings view list of currencies

.. image:: images/HyperDEX-0.1.0-alpha.14/image10.png
   :align: center
   :scale: 75 %

5. Warn about withdrawing the whole balance. (`Github #533 <https://github.com/atomiclabs/hyperdex/pull/533>`__) `Commit Details <https://github.com/atomiclabs/hyperdex/commit/20b283403d8e122ff7ab1b9010658ab83d17ea4b>`__ 

a. A brief message is now displayed on the withdrawal form with the following text: “Note: HyperDEX doesn't yet calculate the TX fee, so you can't withdraw the whole balance. Try withdrawing slightly”

.. image:: images/HyperDEX-0.1.0-alpha.14/image11.png
   :align: center
   :scale: 75 %

6. Update BTC donation address. `Commit Details <https://github.com/atomiclabs/hyperdex/commit/59cf1fd9b120708e631234e50019ad613a8423a2>`__

a. The BTC donation address has been updated to the following:1HyperDEXfMx459ZFh6Ram5uymS8AiRAQf

b. KMD is also now acceptable as a donation, the address is the following: RHyper8TJyHK6uZ3AXzUwC2uVRdt7cfxEC

.. image:: images/HyperDEX-0.1.0-alpha.14/image12.png
   :align: center
   :scale: 75 %

Fixes
=====

    * Fix Document update conflict error. (`Github #531 <https://github.com/atomiclabs/hyperdex/pull/531>`__) `Commit Details <https://github.com/atomiclabs/hyperdex/commit/a4a59144a540d8af224bff8eaf7c9a2208b5d305>`__
    * Fix Gemini dollar (GUSD) fiat price. (`Github #538 <https://github.com/atomiclabs/hyperdex/pull/538>`__) `Commit Details <https://github.com/atomiclabs/hyperdex/commit/406c639c759702f5c7a2dbd0fcec4f67e01eb97a>`__
    * Fix missing EQLI icon. `Commit Details <https://github.com/atomiclabs/hyperdex/commit/ecb82c82debf937fa6f219060988dee59d5be4c8>`__
    * Fixes login issue on Windows. `Commit Details <https://github.com/atomiclabs/hyperdex/commit/0af57df815bc727646d463fadd9ed9a630d9d215>`__
    * Fix dashboard currency percentage price change `Commit Details <https://github.com/atomiclabs/hyperdex/commit/85b3280254126538d8014e6583e6f8838b95ba2b>`__ 

Dev Only
========

    * Add more currencies and update some Electrum servers `Commit Details <https://github.com/atomiclabs/hyperdex/commit/4b9d39737a514c0aa11b4d951feb1f9d8d6e96b8>`__
    * Add PGP badge to readme linking to Keybase proofs `Commit Details <https://github.com/atomiclabs/hyperdex/commit/a563f84d41c6eb4cb0ff097a461499a3bf05c1f4>`__
    * Silence new Buffer() deprecation warnings on macOS and Window (`but not on Linux <https://github.com/atomiclabs/hyperdex/issues/535#issuecomment-425848117>`__). `Commit Details <https://github.com/atomiclabs/hyperdex/commit/50365013fe0e94b5f8c58e447a062cca499857a0>`__
    * Persist the window size and position. (`Github #534 <https://github.com/atomiclabs/hyperdex/pull/534>`__) `Commit Details <https://github.com/atomiclabs/hyperdex/commit/420a443369623ee9eb6e4d4d77609b0faf7430ba>`__
    * Update to BarterDEX Marketmaker v1.0.707 to fix slow login time. `Commit Details <https://github.com/atomiclabs/hyperdex/commit/16ed5d9fd361527107a466af9f52adc8f1042f34>`__
    * Update wording Alpha => Beta `Commit Details <https://github.com/atomiclabs/hyperdex/commit/a48d294ab54dc5c58a3e31b934067042aab6a336>`__
    * Update Alpha => Beta references in translation files `Commit Details <https://github.com/atomiclabs/hyperdex/commit/fd4c844e59e8986c281afc4437a7fe3788dd1b13>`__

