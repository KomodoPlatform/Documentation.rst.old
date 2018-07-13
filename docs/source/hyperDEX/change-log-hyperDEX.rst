*********************
Change Log (HyperDEX)
*********************

.. note::

	Keep in mind that HyperDEX is currently in alpha release. Although the risk of loss of funds is minimal, it could take some troubleshooting/contact with our supportstaff to resolve issues. Only trade in real currency if you can take that risk. We recommend trading in the test currencies ``BEER`` and ``PIZZA`` instead. You can get ``BEER`` for free `here <https://www.atomicexplorer.com/#/faucet>`_.

Remember to report issues through the ``Feedback`` button in the app.

.. toctree::
   :maxdepth: 3
   :caption: Quick Links

   change-log-hyperDEX.rst

0.1.0-alpha.9
=============

Light theme
-----------

You can choose a new light theme in the settings. On macOS, it follows the system dark mode by default.

.. image:: /_static/images/hyperdex-light-mode.png
   :align: center
   :scale: 50 %


Localization
------------

HyperDEX is now available in 22 languages!

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

Other changes:
--------------

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
	* All changes: `Github compare <https://github.com/lukechilds/hyperdex/compare/v0.1.0-alpha.2...v0.1.0-alpha.3>`_

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
	* All changes: `Github compare <https://github.com/lukechilds/hyperdex/compare/v0.1.0-alpha.1...v0.1.0-alpha.2>`_

