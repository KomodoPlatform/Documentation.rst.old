********************
How to update Komodo
********************

Sometimes it is needed to update Komodo. This is how I did it.

Reboot your node (to start clean).

Go into the Komodo folder

.. code-block:: shell

	cd komodo

Do a git pull

.. code-block:: shell

	git pull

**ATTENTION: When it is not a new beta version you do make in the** ``~/komodo/src`` **dir**

.. code-block:: shell

	cd src
	make

**ATTENTION: If it is a new beta version you forget above and do what is down under**

.. code-block:: shell

	git checkout dPoW

Follow the following steps:

.. code-block:: shell

	./zcutil/fetch-params.sh
	./zcutil/build.sh -j8

After that, go to your .komodo folder

.. code-block:: shell

	cd ~/.komodo

Remove the following files

.. code-block:: shell

	rm -rf blocks chainstate debug.log komodostate db.log

Go back to you home folder

.. code-block:: shell

	cd ~

Run your start script

.. code-block:: shell

	./start

Let it resync (check with the getinfo command). When it is done resync, start Iguana

.. code-block:: shell

	cd ~/KomodoPlatform/iguana
	./m_notary

It has been done

Problems?
=========

I receive the following error when i do ``./zcutil/build.sh -j8``

.. code-block:: shell

	EXCEPTION: St13runtime_error
	could not load param file at /home/j/.zcash-params/sprout-verifying.key
	Komodo in AppInit()

You have to do ``./zcutil/fetch-params.sh`` first and after that ``./zcutil/build.sh -j8``
