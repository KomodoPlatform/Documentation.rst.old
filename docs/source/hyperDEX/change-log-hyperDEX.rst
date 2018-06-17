*********************
Change Log (HyperDEX)
*********************

.. note::

	Keep in mind that HyperDEX is currently in alpha release. There is a risk of loss of funds. Only trade in real currency if you can take that risk. We recommend trading in the test currencies ``BEER`` and ``PIZZA`` instead. You can get ``BEER`` for free `here <https://www.atomicexplorer.com/#/faucet>`_.

0.1.0-alpha.6
=============

Note:
-----
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

