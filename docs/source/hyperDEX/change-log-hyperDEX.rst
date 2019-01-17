*********************
Change Log (HyperDEX)
*********************

.. note::

	Keep in mind that HyperDEX is currently in beta release. Although the risk of loss of funds is minimal, it could take some troubleshooting/contact with our supportstaff to resolve issues. Only trade in real currency if you can take that risk. We recommend trading in the test currencies ``BEER`` and ``PIZZA`` instead. You can get ``BEER`` for free `here <https://www.atomicexplorer.com/#/faucet>`__.

Remember to report issues through the ``Feedback`` button in the app.

.. contents:: Links
   :depth: 3

0.4.0
=====

    * Drop support for macOS 10.9 `4600c1a <https://github.com/atomiclabs/hyperdex/commit/4600c1acb7c8c3fed2a9afc5639aeb1201b56c80>`__
    * Remove ``QMC`` currency (Its Electrum servers are down) `6c706d9 <https://github.com/atomiclabs/hyperdex/commit/6c706d99e437ea370d3af7026b31db5a4deda80e>`__
    * Remove ``BCBC`` currency (Its Electrum servers are down) `ca25377 <https://github.com/atomiclabs/hyperdex/commit/ca25377006d6975322dceeec850b8fb005aaf872>`__
    * Update Electrum servers and some currency data (#588) `ca25377 <https://github.com/atomiclabs/hyperdex/commit/ca25377006d6975322dceeec850b8fb005aaf872>`__
    * Update to BarterDEX Marketmaker v1.0.1096 `b3c6f0b <https://github.com/atomiclabs/hyperdex/commit/b3c6f0b450663f6d92c267bef918142d218eecb4>`__
    * Add "Debug" menu item to show the file of the current portfolio (`#579 <https://github.com/atomiclabs/hyperdex/pull/579>`_) `e1aae1f <https://github.com/atomiclabs/hyperdex/commit/e1aae1f875eb5d283f0e3f8625f6ed0d3faa419b>`__

0.3.0
=====

    * Add Pungo Token (``PGT``) currency. `b84139d <https://github.com/atomiclabs/hyperdex/commit/b84139d81b6da4c418b098bd7ef89a3ab42d9e06>`__
    * Remove ``DNR``, ``ARG``, ``MAC``, and ``CALL`` currencies. See `#577 (comment) <https://github.com/atomiclabs/hyperdex/pull/577#issuecomment-445567840>`__. `69b388d <https://github.com/atomiclabs/hyperdex/commit/69b388d25c40d77de437cf0fa467a6e1b0ee3d98>`__
    * Update LTC and BCH Electrum servers. `69b388d <https://github.com/atomiclabs/hyperdex/commit/69b388d25c40d77de437cf0fa467a6e1b0ee3d98>`__
    * Fix the dashboard price history graph. `b0d9d7d <https://github.com/atomiclabs/hyperdex/commit/b0d9d7d61db593589d1e4ea668be1f683d7e0c42>`__
    * Move enabled currencies from the app settings to the portfolio data. It is automatically migrated. This means portfolios can have different enabled currencies. `37996ed <https://github.com/atomiclabs/hyperdex/commit/37996edd80f8aa1671758d0d66edf3dc81448078>`__
    * Update to `BarterDEX Marketmaker v1.0.1026 <https://github.com/artemii235/SuperNET/releases/tag/v1.0.1026>`__. `d04da2e <https://github.com/atomiclabs/hyperdex/commit/d04da2e16d4801ad65595a44ace512a81ce1c34f>`__

0.2.1
=====

    * Make the swap list rows clickable. You now click anywhere in the row instead of the "View" button. `5768b3e <https://github.com/atomiclabs/hyperdex/commit/5768b3ef897649b6d1853e5634b17f3b5ed5993a>`__
    * Add filters to the trade history. `6074f21 <https://github.com/atomiclabs/hyperdex/commit/6074f21d37d001495e588d8387a1b1b0055d51bb>`__
    * Add a copy button to the modal that shows your seed phrase. `be63d25 <>https://github.com/atomiclabs/hyperdex/commit/be63d250e049fb6d75e2d35e9bc3dc8bcb44048c`__
    * Fix a small zero being accidentally shown after the wallet currency price. `9d9769e <https://github.com/atomiclabs/hyperdex/commit/9d9769e47abd945ebe977d3fa578cfe0ad3ca99e>`__
    * Fix the price history fetching error handling. `fb23e32 <https://github.com/atomiclabs/hyperdex/commit/fb23e3284a4ba7c6a671502fa2e2850c179e3b74>`__
    * In the Dashboard view, show 6 fractional digits for currencies worth less than 1. `1cab80f <https://github.com/atomiclabs/hyperdex/commit/1cab80f13e538e4f4c201d2195b7822032cd04fb>`__
    * Update to `BarterDEX Marketmaker v1.0.861 <https://github.com/artemii235/SuperNET/releases/tag/v1.0.861>`__. `700fed4 <https://github.com/atomiclabs/hyperdex/commit/700fed480170f72721a70adc6bdb2b79596f428b>`__

0.2.0
=====

    * Update Electrum servers for ``VIA``, ``VTC``, ``BTG``. `bd63e9e <https://github.com/atomiclabs/hyperdex/commit/bd63e9e2ff08320eac6e4668d079399bec9c5536>`__
    * Update Electrum servers for ``CRW`` and ``CHAIN``. `12b61a4 <https://github.com/atomiclabs/hyperdex/commit/12b61a4e97068b4af69c0e5d3541fb04bd15fa66>`__
    * Add QMCoin (``QMC``) currency. `1d4ed32 <https://github.com/atomiclabs/hyperdex/commit/1d4ed3234b482e769124725c7e979eef5cd72d24>`__
    * Add Etheera (``ETA``) currency. `793fb4a <https://github.com/atomiclabs/hyperdex/commit/793fb4acf371197d3764d9f0673d5ee2fde44e03>`__
    * Hide the empty Swap view. (It will come back sometime in the future) `c6c795e <https://github.com/atomiclabs/hyperdex/commit/c6c795e8ab5e3ca063ffda6fd9bcc5f6e9ccc0e2>`__
    * Improve errors. `9cdd7ff <https://github.com/atomiclabs/hyperdex/commit/9cdd7ffa1f3cf7037a3db7955730062cc39110d8>`__

0.1.4
=====

    * Fix ``Document update conflict`` error. (`#531 <https://github.com/atomiclabs/hyperdex/pull/531>`__) `a4a5914 <https://github.com/atomiclabs/hyperdex/commit/a4a59144a540d8af224bff8eaf7c9a2208b5d305>`_
    * Silence ``new Buffer()`` deprecation warnings on macOS and Window (`but not on Linux <https://github.com/atomiclabs/hyperdex/issues/535#issuecomment-425848117>`__). `5036501 <https://github.com/atomiclabs/hyperdex/commit/50365013fe0e94b5f8c58e447a062cca499857a0>`_
    * Fix Gemini dollar (GUSD) fiat price. (`#538 <https://github.com/atomiclabs/hyperdex/pull/538>`__) `406c639 <https://github.com/atomiclabs/hyperdex/commit/406c639c759702f5c7a2dbd0fcec4f67e01eb97a>`_
    * Persist the window size and position. (`#534 <https://github.com/atomiclabs/hyperdex/pull/534>`__) `420a443 <https://github.com/atomiclabs/hyperdex/commit/420a443369623ee9eb6e4d4d77609b0faf7430ba>`_
    * Rename ``EQL`` to ``EQLI`` in the list of default currencies. `5750560 <https://github.com/atomiclabs/hyperdex/commit/575056075278db372a724cde549743e0ba000bb2>`_
    * Warn about withdrawing the whole balance. (`#533 <https://github.com/atomiclabs/hyperdex/pull/533>`__) `20b2834 <https://github.com/atomiclabs/hyperdex/commit/20b283403d8e122ff7ab1b9010658ab83d17ea4b>`_

0.1.3
=====

    * Fix missing EQLI icon. `ecb82c8 <https://github.com/atomiclabs/hyperdex/commit/ecb82c82debf937fa6f219060988dee59d5be4c8>`_

0.1.2
=====

    * Update to BarterDEX Marketmaker v1.0.707 to fix slow login time. `16ed5d9 <https://github.com/atomiclabs/hyperdex/commit/16ed5d9fd361527107a466af9f52adc8f1042f34>`_

0.1.1
=====

    * Fixes login issue on Windows. `0af57df <https://github.com/atomiclabs/hyperdex/commit/0af57df815bc727646d463fadd9ed9a630d9d215>`_

0.1.0
=====

	* Update wording Alpha => Beta `a48d294 <https://github.com/atomiclabs/hyperdex/commit/a48d294ab54dc5c58a3e31b934067042aab6a336>`_
	* Update Alpha => Beta references in translation files `fd4c844 <https://github.com/atomiclabs/hyperdex/commit/fd4c844e59e8986c281afc4437a7fe3788dd1b13>`_
	* Add Gemini dollar (GUSD) `8c4eace <https://github.com/atomiclabs/hyperdex/commit/8c4eace45fd2fb26f70b7dbbfeb8442acafc55c7>`_
	* Add Old Capital (OCALL) `35f95d9 <https://github.com/atomiclabs/hyperdex/commit/35f95d9650257640f163c840ae64a1cc581ed104>`_
	* Add Capital GAS (CALLG) `34f7611 <https://github.com/atomiclabs/hyperdex/commit/34f76112d214dc517c7c2b74f6cb3f6f16bbc7af>`_
	* Add more currencies and update some Electrum servers `4b9d397 <https://github.com/atomiclabs/hyperdex/commit/4b9d39737a514c0aa11b4d951feb1f9d8d6e96b8>`_
	* Add PGP badge to readme linking to Keybase proofs `a563f84 <https://github.com/atomiclabs/hyperdex/commit/a563f84d41c6eb4cb0ff097a461499a3bf05c1f4>`_
	* Fix dashboard currency percentage price change `85b3280 <https://github.com/atomiclabs/hyperdex/commit/85b3280254126538d8014e6583e6f8838b95ba2b>`_
	* Update BTC donation address. `59cf1fd <https://github.com/atomiclabs/hyperdex/commit/59cf1fd9b120708e631234e50019ad613a8423a2>`_

0.1.0-alpha.13
==============

.. note::

	If you have used any previous beta version, you need to delete your trade history as this version has an incompatible format. Right after opening this version, go to the "Debug" menu and choose "Delete Trade History".

Changes
-------

	* GTC orders. `0040d04 <https://github.com/atomiclabs/hyperdex/commit/0040d040fb988100cd0052dc97a41d2b6574524b>`_
	* All orders are now Good 'Till Cancelled (GTC) orders. If you place an order it will stay pending and keep re-broadcasting the order every 10 minutes until it either matches or the user cancels it. `Read more <https://github.com/atomiclabs/hyperdex/pull/481>`_ .
	* Only show open orders on the exchange view. `a95f256 <https://github.com/atomiclabs/hyperdex/commit/a95f25675a34ea9ada82b531e2fabfe76fba6ec7>`_
	* Because of GTC, we now only show open orders in the Exchange view. Go to the Trades view to view completed/failed orders.
	* Add donate button. `e2660ef <https://github.com/atomiclabs/hyperdex/commit/e2660ef3dd3d910e756f4dd6db8e1307da2cfc0c>`_
	* Add ability to sort orders in the Trades view. `d505b8e <https://github.com/atomiclabs/hyperdex/commit/d505b8e93da4248cc40504dfbff5ef5520d7a9b5>`_
	* Improve login performance. `8aec0fa <https://github.com/atomiclabs/hyperdex/commit/8aec0faf4466ed28db0346d074fe18dd48483311>`_
	* Disable Debug Mode by default in production. You can re-enable it in the ``Help`` menu. `e00eff5 <https://github.com/atomiclabs/hyperdex/commit/e00eff53cc68a5fe25281f08be51eb835dbf7697>`_
	* Update to `BarterDEX Marketmaker v1.0.543 <https://github.com/artemii235/SuperNET/releases/tag/v1.0.543>`_. `34d88e4 <https://github.com/atomiclabs/hyperdex/commit/34d88e4da1ec1ca96ddcb5695f2f5669b00080c0>`_

0.1.0-alpha.12
==============

.. note::
	
	If you're upgrading from ``alpha.10``, you need to delete your trade history as this version has an incompatible format. Right after opening this version, go to the "Debug" menu and choose "Delete Trade History".

Changes
-------

	* Switch from CoinMarketCap API to CoinGecko. No more CoinMarketCap-related errors. `dbecfaf <https://github.com/atomiclabs/hyperdex/commit/dbecfaf3ae1efdd621df1536009659a78d77df0e>`_
	* Improve handling of Marketmaker crashing or being unavailable during login. `f12fe3c <https://github.com/atomiclabs/hyperdex/commit/f12fe3c39207b738731d003d9678628180543dd7>`_
	* Add initial macOS Touch Bar support. `d494ad4 <https://github.com/atomiclabs/hyperdex/commit/d494ad43f6a9fbcf95b476fad77c97db1fdd93d1>`_
	* New Crowdin translations. `3a56e46 <https://github.com/atomiclabs/hyperdex/commit/3a56e466f3152a62c74d9127ea452e511be6899f>`_
	* Fix icon for Trades view. `36725ec <https://github.com/atomiclabs/hyperdex/commit/36725ecb8cc676fbf6e81d5ed504efd10c216c3f>`_
	* Fix window height on Linux. `631e3b2 <https://github.com/atomiclabs/hyperdex/commit/631e3b287cc1ef3acdbe61f2405aff4a298706c2>`_
	* Make the hit-target for the modal close button larger. `ece080d <https://github.com/atomiclabs/hyperdex/commit/ece080d2061e43e4a2b37d58830de8b70212796a>`_

0.1.0-alpha.11
==============

.. note::

	If you have used any previous beta version, you need to delete your trade history as this version has an incompatible format. Right after opening this version, go to the "Debug" menu and choose "Delete Trade History".

Changes
-------

	* Support for `ERC20 tokens <https://en.wikipedia.org/wiki/ERC-20>`_. `cbfce65 <https://github.com/atomiclabs/hyperdex/commit/cbfce65f47e6dbc664e61986353171fbe3aa883f>`_
	* Add Unicoin (MYTH) to default currencies. `7779532 <https://github.com/atomiclabs/hyperdex/commit/77795327dd1fed260f63a046cbe128a8a7588303>`_
	* Add ability to export trade history to CSV. For example, for use in Excel. (`#450 <https://github.com/atomiclabs/hyperdex/pull/450>) `5bb5c3b <https://github.com/atomiclabs/hyperdex/commit/5bb5c3b912ff1a285690cd60abbf010ed0ee3cff>`_
	* In the swap details modal, link transactions to block explorer web pages. (`#453 <https://github.com/atomiclabs/hyperdex/pull/453>`_) `7bd9644 <https://github.com/atomiclabs/hyperdex/commit/7bd964460f005b1a3cc04f01cc9f2fbfdceaf998>`_
	* Limit the amount of swaps shown in the "Recent Swaps" box in the Exchange view. (`#445 <https://github.com/atomiclabs/hyperdex/pull/445>`_) `3e97ea9 <https://github.com/atomiclabs/hyperdex/commit/3e97ea9194105816d0549eacc8af0ded52dc74b9>`_
	* Render numbers with decimal instead of exponential notation in number input fields. (`#434 <https://github.com/atomiclabs/hyperdex/pull/434>`_) `8c612c5 <https://github.com/atomiclabs/hyperdex/commit/8c612c52b307aa972ef3a27b3afb1ed0bdec0d97>`_
	* Swap details modal tweaks. `6654b8d <https://github.com/atomiclabs/hyperdex/commit/6654b8d70f9031ea00bfc1115124ec9346f34929>`_ `5e7512d <https://github.com/atomiclabs/hyperdex/commit/5e7512d7da4dad04478702cf106e846e8139bc2b>`_
	* Add "Help" menu item to report security issues. `cfdbb9a <https://github.com/atomiclabs/hyperdex/commit/cfdbb9af64a90b753849e4f9885fe7d4cfd2bf13>`_
	* Fix duplicate labels in the portfolio charts. (`#443 <https://github.com/atomiclabs/hyperdex/pull/443>`_) `2c9df69 <https://github.com/atomiclabs/hyperdex/commit/2c9df69aa66928a7217b3429de5c60df413f1d02>`_
	* Use official HyperDEX PGP key when signing checksums. `6f57087 <https://github.com/atomiclabs/hyperdex/commit/6f5708775a72570475fde2ed4082c2919d0aba09>`_
	* Update to `BarterDEX Marketmaker v1.0.342 <https://github.com/artemii235/SuperNET/releases/tag/v1.0.342>`_. `e3538f8 <https://github.com/atomiclabs/hyperdex/commit/e3538f87c68ecd18040def3c511fc7cc8b191da8>`_
	* Translation updates. (#`448 <https://github.com/atomiclabs/hyperdex/pull/448>`_) `e20fa6d <https://github.com/atomiclabs/hyperdex/commit/e20fa6d33bb3c914622e18004e2619f95b35c63b>`_

0.1.0-alpha.10
==============

	* **Automatically fixes stuck swaps.** `1d4a0bc <https://github.com/atomiclabs/hyperdex/commit/1d4a0bc7a193f72a82d52077fd3f5f6f545e930c>`_
	* **Add ability to view the portfolio seed phrase.** `5634172 <https://github.com/atomiclabs/hyperdex/commit/5634172785a5b22ad7f6308a316701dd10ffda2d>`_
	* **Add ability to rename and delete the portfolio.** `5634172 <https://github.com/atomiclabs/hyperdex/commit/5634172785a5b22ad7f6308a316701dd10ffda2d>`_
	* Add GLX Token (GLXT) currency. `9ddb1f3 <https://github.com/atomiclabs/hyperdex/commit/9ddb1f3345d02dd1a0933ed7f58aaaf865770592>`_
	* Add Chainmakers (CHAIN) currency. `8fc85bc <https://github.com/atomiclabs/hyperdex/commit/8fc85bc6f53a62394b54ead4b0032fdc4cf11a38>`_
	* Add PACcoin ($PAC) currency. `31d55a7 <https://github.com/atomiclabs/hyperdex/commit/31d55a73254bacbcd8e90024ed698d15a26a5673>`_
	* Add Rapture (RAP) currency. `478bb91 <https://github.com/atomiclabs/hyperdex/commit/478bb9184facd71ba576bf34e31ff11e87f892ec>`_
	* Update some Electrum servers. `ca94790 <https://github.com/atomiclabs/hyperdex/commit/ca9479058d0b94a3c34228c9c148a71e928b3643>`_
	* Fix order selection calculation. `87fa824 <https://github.com/atomiclabs/hyperdex/commit/87fa8242cb863286675abed10c44478631397651>`_
	* Fix Portfolio menu being visible even when logging out. `406c7d1 <https://github.com/atomiclabs/hyperdex/commit/406c7d1276b629390b4054c295d1faa64c6ced99>`_
	* Fix the dropdown of the currency selector being cut off and make settings scrollable. `90cbbb6 <https://github.com/atomiclabs/hyperdex/commit/90cbbb6477b302b19575f02cf45ecef5ad7a1544>`_
	* Reset inputs in the Exchange view when currency changes. `98f53c2 <https://github.com/atomiclabs/hyperdex/commit/98f53c289cda974cf2b51a85756a11ea9c2521e7>`_
	* Update to `BarterDEX Marketmaker v1.0.315. <https://github.com/artemii235/SuperNET/releases/tag/v1.0.315>`_ `b37b40e <https://github.com/atomiclabs/hyperdex/commit/b37b40e1368587df98820e8cccd4539f8fe365ed>`_

0.1.0-alpha.9
=============

Light theme
-----------

You can now choose a new light theme in the settings. On macOS, it follows the system dark mode by default.

.. image:: /_static/images/hyperdex-light-mode.png
   :align: center
   :scale: 50 %


Localization
------------

HyperDEX is now available in 22 languages!!!

It uses your system language by default. Please let us know if the auto-detection is not working.

We're also looking for feedback on the translations. Report any mistakes or improvements to us on the Discord channel. Also, let us know if you want to help add additional languages or want to help maintain an existing language. You can find the translations `here <https://crowdin.com/project/hyperdex>`_.

Languages:

 * Arabic
 * Bengali
 * Chinese Simplified
 * Chinese Traditional
 * French
 * German
 * Hindi
 * Indonesian
 * Italian
 * Japanese
 * Korean
 * Norwegian
 * Persian
 * Polish
 * Russian
 * Spanish
 * Swahili
 * Swedish
 * Thai
 * Turkish
 * Urdu (Pakistan)
 * Vietnamese

Other changes
-------------

 * HyperDEX releases now come with PGP-signed checksums. (Look for the SHASUMS256.txt.asc file) `a2f2ec6 <https://github.com/hyperdexapp/hyperdex/commit/a2f2ec6f02323c40031298f94a824f09ac4ac1a5>`_
 * Add ChainZilla (ZILLA) currency. `2d9df30 <https://github.com/hyperdexapp/hyperdex/commit/2d9df30ce001aa63acc16006f5d3206f4548db5d>`_
 * Add dashboard intro. `829f158 <https://github.com/hyperdexapp/hyperdex/commit/829f1586424e842b84e87c4a6183f37a04b01d5a>`_


0.1.0-alpha.8
=============

	* Update to BarterDEX `Marketmaker v1.0.270 <https://github.com/artemii235/SuperNET/releases/tag/v1.0.270>`_ which contains a bug fix to improve order match rate. `74624bb <https://github.com/hyperdexapp/hyperdex/commit/74624bbdc8a01c55b366f7698542a33b57d1b5df>`_
	* Improve Content Security Policy `5d27515 <https://github.com/hyperdexapp/hyperdex/commit/5d2751566ac8f305d9df5c5c214cf09bbe7e942a>`_
	* Add translation files `00b4f84 <https://github.com/hyperdexapp/hyperdex/commit/00b4f84a8a6426d147c9244a66a458122f41fbd1>`_
	* Add icons for currencies BCBC, MNZ, DNR, EQL `3e3ff11 <https://github.com/hyperdexapp/hyperdex/commit/3e3ff118c567a4b3e1b8b6547eb484d14d8696f2>`_

0.1.0-alpha.7
=============

	* We have decided to remove the "Cancel" button from the Trades view. It was not working as expected and it doesn't look like it going to be possible to fix it until Marketmaker v2 (which will not be done soon). `60d9fee <https://github.com/hyperdexapp/hyperdex/commit/60d9feecda1449222ac914f92e247b6e2cf54957>`_
	* Enable the EQL currency by default. `280f7dd <https://github.com/hyperdexapp/hyperdex/commit/280f7ddad60b7059cc63bd4d4a54b801bf10d2e3>`_
	* Update to `BarterDEX Marketmaker v1.0.261 <https://github.com/artemii235/SuperNET/releases>`_. `27ca8b2 <https://github.com/hyperdexapp/hyperdex/commit/27ca8b2cdf08a942d8cbba9a71dadec653291e6b>`_
	* Correctly handle inverse values for sell orders. `167b892 <https://github.com/hyperdexapp/hyperdex/commit/167b89284c6623ae261219710e07973d54cef53e>`_
	* Fix stuck pending swaps. `0ed0acd <https://github.com/hyperdexapp/hyperdex/commit/0ed0acdf2638b0b628099a8753a4d4049d3b6833>`_
	* Fix not being able to type space in the seed phrase input. `856c971 <https://github.com/hyperdexapp/hyperdex/commit/856c9715b99596dbabfbebb373b9886f185cf25b>`_
	* Fix USD calculation in the withdraw modal. `a4fec46 <https://github.com/hyperdexapp/hyperdex/commit/a4fec46296178d58b47183fa1f1f557c054418b6>`_
	* Fix issue when clicking the "Max" button in the withdraw modal. `37a35f5 <https://github.com/hyperdexapp/hyperdex/commit/37a35f53d3b87be547017337d965f06ca0d767d0>`_
	* Split Settings into Portfolio and App Settings. `9f3f1a7 <https://github.com/hyperdexapp/hyperdex/commit/9f3f1a72cfc81bd0d69d9eaa1def072eee9a2bfc>`_
	* Add some stats to the Trades view. `7d996b4 <https://github.com/hyperdexapp/hyperdex/commit/7d996b46533bc965409f53150b9b037731bc040c>`_
	* Fix problem with having currencies with a number in the name enabled. `e6b435b <https://github.com/hyperdexapp/hyperdex/commit/e6b435b6ccd27be24b3da566e899a0e014afd2da>`_

0.1.0-alpha.6
=============

Note:

Don't download this version if you have currencies enabled where the symbol contains a number, see `issue: #356 <https://github.com/lukechilds/hyperdex/issues/356>`_

	* Support for the `Equaliser (EQL) <https://equaliser.org/>`_ currency. `commit: 1c3930b <https://github.com/lukechilds/hyperdex/commit/1c3930b5584c9f528b20d17d9632c36b94777c64>`_
	* Displays order failures using a system notification. `commit: 621d934 <https://github.com/lukechilds/hyperdex/commit/621d93443249b6aa99083e637dd67d2749454594>`_
	* Shows the worth of a swap in USD in the order column in the Exchange view. `commit: 7960014 <https://github.com/lukechilds/hyperdex/commit/79600143389a5af84cb203a59e46f97e7de74186>`_
	* Fixed a crash caused by number some inputs having the incorrect data type. `commit: 991c988 <https://github.com/luk;echilds/hyperdex/commit/991c9881e564dfe773b087f3eea537da79af71b0>`_
	* Now gracefully handles Electrum errors. `commit: a179fb8 <https://github.com/lukechilds/hyperdex/commit/a179fb83c9a3009a060f506540655514528976ce>`_
	* Added a debug menu item to delete swap history. `commit: 0d40526 <https://github.com/lukechilds/hyperdex/commit/0d4052638d76d766c29479385cfa612c93d4dd74>`_
	* Updated to BarterDEX Marketmaker v1.0.238. `commit: fb934da <https://github.com/lukechilds/hyperdex/commit/fb934da8c92ad48ba5d90ac459e5d3e0b612a4f8>`_

0.1.0-alpha.5
=============

	* Fixed clicking orders in the order book.
	* Fixed another issue with number inputs.

0.1.0-alpha.3
=============

	* Fixed pasting a multiline seed phrase in the "Restore Portfolio" view.
	* Fixed all the problems with number inputs.
	* Added icons for all the Komodo asset chains. You can now trade ``PIZZA`` and ``BEER`` in style!
	* The Buy/Sell buttons are now disabled while the order is placed to prevent accidental double-buy and to reduce chances of marketmaker problems.
	* HyperDEX will present a confirmation dialog if you try to quit while you have in-progress swaps.
	* Various user-interface improvements.
	* All changes: `Github compare <https://github.com/lukechilds/hyperdex/compare/v0.1.0-alpha.2...v0.1.0-alpha.3>`__

0.1.0-alpha.2
=============

	* Various user-interface improvements. Larger text in some places. Less scrollbars.
	* Added the Denarius (DNR) currency.
	* Fixed the Electrum port for ``BTCH`` and ``CRYPTO``.
	* Fixed a problem with typing zero after a decimal point in input fields `Issue #240 on Github repo <https://github.com/lukechilds/hyperdex/issues/240>`_
	* The SnowGem currency ticker was incorrect and was changed from ``SNG`` to ``XSG``. You need to enable it again if you had it enabled previously.
	* The ``HODL`` and ``HODLC`` currencies are temporarily removed while we sort out some confusion. `Issue #289 on Github repo <https://github.com/lukechilds/hyperdex/issues/289>`_
	* Now shows the "View" button also in the "Open Orders" view.
	* Added a ``Copy Swap Debug Data`` button to the swap modal dialog, so you can more easily share debug data with us.
	* ``PIZZA`` and ``BEER`` no longer shows a price since they're just test currencies.
	* All changes: `Github compare <https://github.com/lukechilds/hyperdex/compare/v0.1.0-alpha.1...v0.1.0-alpha.2>`__

