***************************************
How to update Komodo (for Notary Nodes)
***************************************

Reboot your node (to start clean).

If you already have installed Komodo from it's source code on your machine, and need to update to the latest version, follow the below steps.

Please follow each step carefully and don't skip to the next one until the previous step is successfully completed. If you have the ``komodo daemon`` running, you can leave it running while updating if you have enough resources in your machine. If you prefer to stop it before updating, please use ``~/komodo/src/komodo-cli stop`` to stop the daemon and proceed with the following steps to update.


1. Navigate to your komodo directory 

.. code-block:: shell

	cd ~/komodo

2. Make sure you don't have any changes made to the source and reset it. This will ensure clean source and shouldn't create issues while pulling the latest source in the next step.

.. code-block:: shell

	git reset --hard

3. Clean the source directory

.. code-block:: shell

	make clean

4. Update the source. (If you have any changes made to the source code, this command may not pull the latest source. Please make sure you have followed the previous steps)

.. code-block:: shell

	git pull

5. Compile the latest binary

.. code-block:: shell

	./zcutil/build.sh -j$(nproc)

Start your sevices as usual. If you didn't stop the deamon before compiling, please stop it using ``~/komodo/src/komodo-cli stop`` and start again.

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

Your Komodo installation is now uptodate.

Problems?
=========

I receive the following error when i do ``./zcutil/build.sh -j8``

.. code-block:: shell

	EXCEPTION: St13runtime_error
	could not load param file at /home/j/.zcash-params/sprout-verifying.key
	Komodo in AppInit()

You have to do ``./zcutil/fetch-params.sh`` first and after that ``./zcutil/build.sh -j8``
