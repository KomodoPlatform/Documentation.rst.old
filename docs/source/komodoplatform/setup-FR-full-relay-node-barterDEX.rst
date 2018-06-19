**********************************************
Setting up a Full Relay(FR) Node for BarterDEX
**********************************************

What is Full Relay (FR) node?
=============================

Full Relay node (FR) creates the p2p network & only relays packets for BarterDEX and allows ordermatch to happen. They don't trade. FR nodes never touch any funds of any sort and are just a bulletin board. 0 balance needed to run an FR node. Bob and Alice connect to the FR network. Bob places orders and Alice fills the orders. It is ideal to have at least 3 FR nodes in each netid.

How to setup an FR node?
========================

It is just ``marketmaker`` launched with ``client:0`` parameter. Very easy to setup, just follow along without skipping any step.

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

Clone the SuperNET repo from github & Install:
----------------------------------------------

Clone the repo, checkout ``dev`` branch for latest and install.

.. code-block:: shell

	cd ~
	git clone https://github.com/jl777/SuperNET
	cd ~/SuperNET/iguana/exchanges
	git checkout dev
	./install

Edit the ``client`` script
--------------------------

The client script inside the directory ``~/SuperNET/iguana/dexscripts`` should look as follows to be running as a FR node.

.. code-block:: shell

	#!/bin/bash
	source passphrase
	source coins
	./stop
	git pull;
	cp ../exchanges/updateprices .;./updateprices
	cd ..; 
	./m_mm;
	pkill -15 marketmaker; 
	stdbuf -oL $1 ./marketmaker "{\"gui\":\"nogui\",\"client\":0, \"userhome\":\"/${HOME#"/"}\", \"passphrase\":\"$passphrase\", \"coins\":$coins}" &

barterDEX is now installed in your system.

Starting FR node
----------------

Every time you want to run Full Relay (FR) open a new terminal window and type the following:

.. code-block:: shell

	cd ~/SuperNET/iguana/dexscripts
	./client &

How to setup FR nodes for different netid?
==========================================

You need to edit the value of ``netid`` in the ``client`` script along with ``client:0`` param.

``client``
----------

.. code-block:: shell

	#!/bin/bash
	source passphrase
	source coins
	./stop
	git pull;
	cp ../exchanges/updateprices .;./updateprices
	cd ..; 
	./m_mm;
	pkill -15 marketmaker; 
	stdbuf -oL $1 ./marketmaker "{\"gui\":\"nogui\",\"client\":0,\"netid\":1024, \"userhome\":\"/${HOME#"/"}\", \"passphrase\":\"$passphrase\", \"coins\":$coins}" &

Stopping a FR node
------------------

Just use the following command in any terminal session to stop marketmaker. This will stop the running FR node.

.. code-block:: shell

	pkill -15 marketmaker
