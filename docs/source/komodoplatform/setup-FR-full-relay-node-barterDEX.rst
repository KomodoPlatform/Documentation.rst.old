**********************************************
Setting up a Full Relay(FR) Node for BarterDEX
**********************************************

**WORK IN PROGRESS. DO NOT USE YET**

What is Full Relay (FR) node?
=============================

Full Relay node (FR) creates the p2p network & only relays packets for BarterDEX and allows ordermatching to happen. They don't trade. FR nodes never touch any funds of any sort and are just a bulletin board. 0 balance is needed to run an FR node. Bob and Alice connect to the FR network. Bob places orders and Alice fills the orders. It is ideal to have at least 3 FR nodes in each netid.

How to setup an FR node?
========================

It is just ``marketmaker`` launched with ``client:0`` parameter.

Install the following dependency packages:
------------------------------------------

.. code-block:: shell

	sudo apt-get update
	sudo apt-get install cmake git libcurl4-openssl-dev build-essential

Install ``nanomsg``
-------------------

.. code-block:: shell

	cd ~
	git clone https://github.com/nanomsg/nanomsg
	cd nanomsg
	cmake . -DNN_TESTS=OFF -DNN_ENABLE_DOC=OFF
	make -j2
	sudo make install
	sudo ldconfig

Clone the `SuperNET repo <https://github.com/jl777/SuperNET>` from github & Install:
------------------------------------------------------------------------------------

Clone the repo, checkout ``dev`` branch for latest and install.

.. code-block:: shell

	cd ~
	git clone https://github.com/jl777/SuperNET
	cd ~/SuperNET/iguana/exchanges
	git checkout dev
	./install

Copy the ``passphrase`` file & using seed passphrase
------------------------------------------------

From the same dir in terminal type the following commands to copy the ``passphrase`` file to ``~/SuperNET/iguana/dexscripts`` dir and add a strong 24 words seed passphrase in between ``""``. Save your passphrase properly without changing any word or space. Same seed ``passphrase`` will always show you the same ``smartaddress``.

.. code-block:: shell

	cp passphrase ../dexscripts/passphrase
	cd ../dexscripts
	nano passphrase

Enter your passphrase:

``export passphrase="<put a very strong passphrase here>"``

Press ``CTRL+X`` then ``Y`` then ``ENTER`` to save the file and exit from Nano editor.

Getting the ``userpass`` value
------------------------------

All these scripts are expecting a ``userpass`` file, which contains the definition of the ``$userpass`` variable (found inside scripts) to authenticate API access. This is to block malicious webpages that try to issue port 7783 calls to steal your money. At first you may not know the value of ``userpass``. To find out, just run the ``client`` script first (as instructed below) and then run ``./setpassphrase``. You will notice your ``userpass`` value at the top of output and you can copy that value and put it into ``~/SuperNET/iguana/dexscripts/userpass`` file. If you don't, all subsequent API calls will get authorisation error.

Open a new terminal and type the following:

.. code-block:: shell

	cd ~/SuperNET/iguana/dexscripts
	./client &
	./setpassphrase
	pkill -15 marketmaker

Edit the ``userpass`` file
--------------------------

Now copy the ``userpass`` example file to ``~/SuperNET/iguana/dexscripts`` dir and edit the file to save the userpass you got from the ``./setpassphrase`` script output.

.. code-block:: shell

	cd ~/SuperNET/iguana/exchanges
	cp userpass ../dexscripts/userpass
	cd ../dexscripts
	nano userpass

Once done press ``CTRL+X`` then ``Y`` then ``ENTER`` to save the file and exit from Nano editor.

barterDEX is now installed in your system.

Running barterDEX
-----------------

Every time you want to run **barterDEX**, open a new terminal window and type the following:

.. code-block:: shell

	cd ~/SuperNET/iguana/dexscripts
	./client &
	./setpassphrase

