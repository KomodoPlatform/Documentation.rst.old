*****************
JUMBLR Whitepaper
*****************

*jl777 11 June, 2017 | v1.0*

Komodo based fully decentralized anonymizer utilizing native DEX
================================================================

The problems with bitcoin not being anonymous are well known, as are the risks of using a centralized mixing service where you give up control of your coins for the duration. Other decentralized coin mixing methods, like coin shuffle, require coordinating with other parties for each mix and the possibility of a mix being disrupted, or even worse, privacy leaked.

JUMBLR solves all these issues with a two-layer approach. At the core is the Komodo JUMBLR process that is built into ``iguana``. It works with Komodo (KMD) and converts ordinary KMD into anonymized KMD. Of course, care must be taken after it is anonymized to not lose it, but the ability to create the anonymized KMD in a fully decentralized way with no direct group of other parties is a vast improvement.

Building on top of the JUMBLR core is the native DEX using cross chain atomic swaps to convert BTC (or any other bitcoin protocol coin) into KMD, doing the JUMBLR and then using DEX again into an anonymized BTC address. In a sense, JUMBLR is a client of the ``iguana`` DEX service. Since the native DEX has been described already, it will only be referred to here as a mechanism that is able to convert BTC <-> KMD, thus reducing the anonymization problem to converting transparent KMD into anonymized KMD.

At first, it might seem that simply using the innate zcash protected Z-transactions will be sufficient. However, there are some pitfalls to just naively using the Z-transactions and to benefit from most of the protection a few attacks need to be prevented.

	#. Timing attack
	#. Knapsack attack

**Timing attack** is especially an issue when there are not many ongoing JUMBLR processes. At the degenerate case of only a single JUMBLR process going on, there is actually no anonymization provided at all! After all, if you know who started the JUMBLR process (we do due to transparent address) and if there is only one active participant, it doesn’t take any difficult analysis to determine whose coins come out of the JUMBLR process.

**Knapsack attack** is somewhat similar to the timing attack, but as applied to amounts. If there is only one address that JUMBLR’ed 777 KMD and 777 KMD appears at the output of the JUMBLR process, then again it is not hard to correlate.

So, while the zcash zk-SNARK proofs shield the value, it is still advantageous to limit the denominations that are allowed for the JUMBLR. To achieve this, three orders of magnitude are allowed, 100 KMD, 1000 KMD and 10000 KMD lots. So all user’s JUMBLR funds end up in one of the three denominations. Still, it allows some correlations, but in the presence of a large number of JUMBLR processes, it degrades to noise level correlations, i.e. random guessing.

If the user can keep KMD in shielded form for a long time, then the anon set grows ever larger. However it is envisioned that a lot of users will simply want to convert the BTC as quickly as possible, so we will concentrate on the JUMBLR operation for such cases keeping in mind that significantly greater privacy is achieved by delaying the conversion out of the shielded (protected) mode KMD.

JUMBLR Interface In order to minimize the complexity of using JUMBLR a very simple interface has been designed. There are two JUMBLR API calls:

.. code-block:: shell

	STRING_ARG(jumblr,setpassphrase,passphrase)
	ZERO_ARGS(jumblr,status)

Conceptually, ``iguana`` is creating an automated payment processor for a single special address, the one that is mapped from the passphrase. Relying on SHA256 to not be reversible, we can generate an arbitrary number of special addresses that are all linked to the main passphrase by just prefixing (or suffixing) special strings. The advantage of making it based on passphrase is that the identical ``iguana`` GUI can be used to access the JUMBLR’ed funds as for normal funds.

A further simplification is for the JUMBLR passphrase to be derived from the user’s main passphrase by prefixing “jumblr “ to the main passphrase. This removes even the step of specifying a JUMBLR passphrase as it can be done automatically without any ill effect. Unless the user specifically sends funds to the deposit address, JUMBLR stays dormant.

As soon as JUMBLR detects a deposit has arrived, it can start the ``t -> z, z -> z, z -> t`` process, however, we need to avoid the Timing attack. So what is done is a very deliberate slowdown to the entire process. Every twentieth minute, the JUMBLR process activates and checks to see if any tasks are pending. Each hour thus has 3 different JUMBLR phases, ``t -> z, z -> z and z -> t``. If it is determined that there is an appropriate transaction to be sent during the special minute, it is processed approx half the time. The reason for this is to make the completion time random as it relates to a number of funds being JUMBLR’ed and also to avoid having any predictable activity on a node.

The initial step of ``t -> z`` determines the lot size by trying the largest 100x size first, then the 10x then the normal. Once it finds a valid lot size it can do, it does a single lot and stops for the phase. The other two phases process whatever total amount it has received and sends it onto the next step.

Three phases: ``t -> z, z -> z, z -> t``
========================================

``t -> z`` is going from the transparent deposit address to a ``Z-address``. Once in an address, the funds are shielded but the fact that it came from a transparent address leaks a bit of information. To fully shield it, a ``z -> z`` transaction is done and finally to retrieve it to the destination address a final ``z -> t`` transaction completes the cycle.

From the relatively simple behavior above, both the timing attack and knapsack attack are defeated, thus fully leveraging the zcash zk-SNARK technology. The more participants in the JUMBLR, the more privacy there is and the cost for having an ongoing JUMBLR is comparable to the APR being earned. In other words for little if any net cost, KMD users can anonymize their funds and provide more privacy for everyone else.

BTC layer
=========

In order to provide the practically needed BTC <-> anonymized BTC service, the JUMBLR process monitors the BTC deposit address and when funds arrive, it issues a DEX request to convert to KMD and routes the KMD to the JUMBLR KMD deposit address. Once there the JUMBLR process will automatically process it until it arrives at the destination KMD address. At which point a reverse DEX of KMD to BTC is done from the JUMBLR destination address, thus not leaking any information about the source of the funds.

Due to market fluctuations, it is possible for there to be on the order of 5% price slippage by requiring two open market DEX transactions. While it would be possible to prearrange the swap back, there is no known way to do that without leaking information about the party doing the second half of the swap, so the most private are to rely on the open market DEX LP nodes.
