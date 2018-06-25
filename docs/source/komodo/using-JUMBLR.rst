************
Using JUMBLR
************

Introduction and Explanation
============================

For instructions jump to :ref:`Instructions for using JUMBLR`

``komodod`` now has ``jumblr_deposit`` and ``jumblr_secret`` RPC calls.

Jumblr works like described in the whitepaper where all the nodes with jumblr active synchronize their ``tx`` activity during the same block to maximize the mixing effect. However, unlike all other mixers/tumblers, you never give up control of your coins to anybody else. JUMBLR uses a one to many allocations of funds, ie. one deposit address and many secret addresses. You can always run multiple ``komodod`` daemons to get multiple active deposit addresses.

JUMBLR implements ``t -> z, z -> z`` and ``z -> t`` transactions to maximize privacy of the destination ``t`` (transparent) address. So while it is transparent, its first activity is, funds coming from an untraceable ``z`` address.

Which of the three stages is done is randomly selected at each turn. Also when there is more than one possible transaction at the selected stage, a random one is selected. This randomization prevents analyzing incoming ``z -> t`` transactions by its size to correlate it to the originating address.

``jumblr_deposit`` designates the deposit address as the jumblr deposit address for that session. You can select an address that already has funds in it and it will immediately start jumblr process. If there are no funds, it will wait until you send funds to it.

There are three sizes of a jumblr transaction: 10.1 KMD, 101 KMD, 7777 KMD. There is also a fixed interval of blocks where all JUMBLR nodes are active. Currently, it is set to be 10, but this is subject to change. Only during every 1010 blocks are the largest 7777 KMD transactions processed, so this concentrates all the large transactions every NN blocks.

``jumblr_secret`` notifies JUMBLR where to send the final ``z -> t`` transactions. In order to allow larger accounts to obtain privacy, up to 777 secret addresses are supported. Whenever a ``z -> t`` stage is activated, a random secret address from the list of the then active secret addresses is selected.

**Practical Advice:** *Obtaining privacy used to be very difficult. JUMBLR makes it as simple as issuing two command line calls. Higher level layers can be added to help manage the addresses, ie. linking them at the passphrase level. Such matters are left to each implementation.*

*Once obtained, it is very easy to lose all the privacy. With a single errant transaction that combines some previously used address and the* ``secretaddress``, well, the ``secretaddress`` *is no longer so private.*

**The advice is to setup a totally separate node!**

This might seem a bit drastic, but if you want to maintain privacy, it is best to make it look like all the transactions are coming from a different node. The easiest way for most people to do this is to actually have a different node.

It can be a dedicated laptop (recommended) or a VPS (for smaller amounts) with a totally fresh komodod wallet. Generate an address on this wallet and use that as the ``jumblr_secret`` address on your main node. As the JUMBLR operates funds will teleport into your secret node's address. If you are careful and never use the same IP address for both your nodes, you will be able to maintain very good privacy.

Of course, don't send emails that link the two accounts together! Don't use secret address funds for home delivery purchases! Etc. There are many ways to lose the privacy, just think about what linkages can be done at the IP and blockchain level and that should be a useful preparation.

What if you have 100,000 KMD and you don't want others to know you are such a whale?

Instead of generating 1 secret address, generate 100 and make a script file with:

.. code-block:: shell

	./komodo-cli jumblr_secret
	./komodo-cli jumblr_secret
	... 
	./komodo-cli jumblr_secret

And make sure to delete all traces of this when the JUMBLR is finished. You will end up with 100 addresses that have an average of 1000 KMD each. So as long as you are careful and don't do a 10,000 KMD transaction (that will link 10 of your secret addresses together), you can appear as 100 different people each with 1000 KMD.

Instructions for using JUMBLR
=============================

1. Install Komodo following the :doc:`installation guide <install-Komodo-manually>`

2. Start the Komodo daemon

.. code-block:: shell

	cd komodo/src

	./komodod &

3. Designate an address with funds. (``jumblr_deposit``)

(The funds that are already within or deposited in the future of the specified address will go through Jumblr. 10 coins is the minimum plus the Jumblr fee which is 1/777 of the transaction. Therefore you should deposit atleast 10.024 KMD)


.. code-block:: shell

	./komodo-cli jumblr_deposit "KMD Address with Funds"

#Example:

.. code-block:: shell

	./komodo-cli jumblr_deposit RT4mSUjG35QeuGcedsfpHtP5MhDeEGTAqb


4. Designate an address to deposit Jumblr'ed funds. (``jumblr_secret``)

(Now that the Jumblr process has started, you should wait at least 20 minutes before this step. We want to designate an address non-related to your wallet where you will receive the Jumblr'ed funds.)

.. code-block:: shell

	./komodo-cli jumblr_secret "Address where unlinked funds will go"

#Example:

.. code-block:: shell

	./komodo-cli jumblr_secret RS46GZ5iTkt2exdauQG3JJ8fdnZNJUvAc1

5. Wait for funds to arrive.....and you have successfully tumbled coins with zcash privacy!

.. warning::

	Jumblr is created to be resistant against time-based analysis. That means it is not meant to be fast. Make sure you initiate the Jumblr process only if you have plenty of time for the process to finish.



