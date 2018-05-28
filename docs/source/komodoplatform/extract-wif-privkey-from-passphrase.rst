*******************************************
Extracting WIF/privkey from Komodo Platform
*******************************************

To be able to get the privkey of the Smart Address created by the Komodo Platform Passphrase you will need to add the ``wif:1`` handle to the **MarketMaker** command. The **MarketMaker** execution command is in ``./client``.

.. code-block:: shell

	cd ~/KomodoPlatform/iguana/dexscripts
	nano ./client

You will see the ``./client`` script like this:

.. code-block:: shell

	./marketmaker "{\"gui\":\"nogui\",\"client\":1, \"userhome\":\"/${HOME#"/"}\", \"passphrase\":\"$passphrase\", \"coins\":$coins}" &

**Now you need to add the** ``wif:1`` **handle like this:**

.. code-block:: shell

	./marketmaker "{\"gui\":\"nogui\",\"client\":1,\"wif\":1, \"userhome\":\"/${HOME#"/"}\", \"passphrase\":\"$passphrase\", \"coins\":$coins}" &

Once this edit is done, now start **MarketMaker**:

.. code-block:: shell

	cd ~/KomodoPlatform/iguana/dexscripts
	./client

**Execute** ``./setpassphrase`` **API command**

With that command you will see all active coins listed with their respective WIF privkeys.
