********************************************************************
Installing and Using Komodo Platform (barterDEX) (in linux or MacOS)
********************************************************************

**This guide is intended for developers and advanced users (Linux & MacOS) only using command line interface (CLI). GUI users, get** `BarterDEX GUI`_ **. For Windows installations please refer to this** :doc:`guide </barterDEX/install-barterDEX-CLI-windows>` **and use this** `link for the binaries.`_

Komodo Platform (barterDEX) is capable of working with Electrum servers. This means it is not necessary to download blockchain data in your computer. As a matter of fact, you don't need even download and run native coin wallet or daemon. Check the list of current Electrum servers here: :doc:`Electrum Servers List </barterDEX/electrum-servers-list>`.

If you however choose to use a native coin daemon, please make sure it is fully synced. For Komodo and other assetchains use the `latest Agama installer`_ or use the `KomodoOcean-QT`_.

For a list of currently supported native coins and instructions for the coin specific configuration file, see `Supported Native Coins <index-coin-configs-install-instructions>`_

You may want to back up your system or clone it after everything is synced and running correctly BEFORE you start installing coin daemons.

.. _BarterDEX GUI : https://github.com/KomodoPlatform/BarterDEX/releases
.. _link for the binaries. : https://github.com/KomodoPlatform/BarterDEX/tree/dev/assets/bin/win64
.. _latest Agama installer : https://komodoplatform.com/komodo-wallets
.. _KomodoOcean-QT : https://github.com/DeckerSU/komodo-qt/releases

Installing Komodo Platform (barterDEX)
======================================

Install the following dependency packages:
------------------------------------------

Linux:
^^^^^^

.. code-block:: shell

	sudo apt-get update
	sudo apt-get install cmake git libcurl4-openssl-dev build-essential libsodium-dev

Install ``nanomsg``
-------------------

Linux:
^^^^^^

.. code-block:: shell

	cd ~
	git clone https://github.com/nanomsg/nanomsg
	cd nanomsg
	cmake . -DNN_TESTS=OFF -DNN_ENABLE_DOC=OFF
	make -j2
	sudo make install
	sudo ldconfig

MacOS
^^^^^

You'll need to install ``homebrew`` (Google how to do it)

.. code-block:: shell

	brew install nanomsg

Clone the SuperNET repo from github & Install:
----------------------------------------------

Clone the repo, checkout dev branch for latest and install.

.. code-block:: shell

	cd ~
	git clone https://github.com/jl777/SuperNET
	cd ~/SuperNET/iguana/exchanges
	git checkout dev
	./install

Copy the ``passphrase`` file & using seed passphrase
----------------------------------------------------

From the same dir in terminal type the following commands to copy the ``passphrase`` file to ``~/SuperNET/iguana/dexscripts`` dir and add a strong 24 words seed passphrase in between ``""``. Save your passphrase properly without changing any word or space. Same seed **passphrase** will always show you the same **smartaddress**.

.. code-block:: shell

	cp passphrase ../dexscripts/passphrase
	cd ../dexscripts
	nano passphrase

Enter your passphrase:

.. code-block:: shell

	export passphrase="<put a very strong passphrase here>"

Press ``CTRL+X`` then ``Y`` then ``ENTER`` to save the file and exit from Nano editor.

Getting the userpass value
--------------------------

All these scripts are expecting a ``userpass`` file, which contains the definition of the ``$userpass`` variable (found inside scripts) to authenticate API access. This is to prevent malicious webpages from issuing port 7783 calls to steal your money. At first you may not know the value of ``userpass``. To find out, just run the ``client`` script first (as instructed below) and then run ``./setpassphrase``. You will notice your ``userpass`` value at the top of output and you can copy that value and put it into ``~/SuperNET/iguana/dexscripts/userpass`` file. If you don't, all subsequent API calls will get authorisation error.

Open a new terminal and type the following (for macOS please use the ``client_osx`` script):

.. code-block:: shell

	cd ~/SuperNET/iguana/dexscripts
	./client &
	./setpassphrase
	pkill -15 marketmaker
	
Edit the userpass file
----------------------

Now copy the ``userpass`` example file to ``~/SuperNET/iguana/dexscripts`` dir and edit the file to save the ``userpass`` you got from the ``./setpassphrase`` script output.

.. code-block:: shell

	cd ~/SuperNET/iguana/exchanges
	cp userpass ../dexscripts/userpass
	cd ../dexscripts
	nano userpass

Once done press ``CTRL+X`` then ``Y`` then ``ENTER`` to save the file and exit from Nano editor.

barterDEX is now installed in your system.

Running barterDEX
-----------------

Every time you want to run **barterDEX** open a new terminal window and type the following:

.. code-block:: shell

	cd ~/SuperNET/iguana/dexscripts
	./client &
	./setpassphrase

And, don't close it. Open a new terminal window to issue all other scripts/API calls from next. Get all available api list by typing ``./help`` inside ``~/SuperNET/iguana/dexscripts`` dir. You can see all scripts available for you to modify, test and use.

Activating coins
----------------

You can run barterDEX and activate coins for trading without downloading any blockchain data, using the Electrum mode. Edit the ``electrum`` script with the list of servers you want to use. To activate your list of electrum servers from the script, in terminal use ``./electrum``.

Native mode is faster and you need to use native wallet running with fully synced blockchain data and your barterDEX seed passphrase imported into the wallet. Edit the ``enable`` script with coin names and run ``./enable`` in terminal window to activate native coins for trading in barterDEX.

Stopping ``kill marketmaker`` / Close the app
---------------------------------------------

If you want to close barterDEX, issue ``pkill -15 marketmaker`` every time. This ensures all BarterDEX process is killed safely.

**Check the doc**: :doc:`BarterDEX API:Summary by Category </barterDEX/barterDEX-API>` **for more info on different API calls that barterDEX supports. e.g.: buy, sell, orderbook, balance etc. Just edit them for your liking and run them in 2nd terminal.**


