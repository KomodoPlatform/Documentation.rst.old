*********************************************************
Komodo’s Method Of Security: Delayed Proof Of Work (DPOW)
*********************************************************

A Foundational Discussion of Blockchain Security
================================================

Komodo’s form of providing security is called Delayed Proof of Work technology
(dPoW). It builds on the most advanced form of blockchain security in existence,
Proof of Work technology (PoW). The latter form of security is the method that the
Bitcoin network utilizes. To understand the value of Komodo’s dPoW security, we
must first explain how PoW works and why it is the most secure method of maintaining a decentralized blockchain. We must also examine PoW’s shortcomings, so
that we may understand the need for Komodo’s dPoW method and the advantages
it provides to the blockchain community.

To understand how PoW technology functions, we begin by explaining the roots
that make the Bitcoin protocol a viable means of securely transferring value.

What Is A Consensus Mechanism?
------------------------------

The "Double Spend" Problem
^^^^^^^^^^^^^^^^^^^^^^^^^^

The creation of blockchain technology stems from the early mathematical studies
of encryption using computer technology.

One such example is related to the information-encoding device, "Enigma," invented by the Germans at the end of World War I. Alan Turing, a British Intelligence
agent, famously beat the Enigma device by inventing the world’s first "digital computer." This provided enough computing power to break `Enigma’s <https://en.wikipedia.org/wiki/Enigma_machine>`_ encryption and
discover the German secret communications.

This early affair with encryption set off a race throughout the world to develop
myriad forms of securely transferring information from one party to another via
computer technology. While each new form of computer encryption provided more
advantages, there remained one problem that prevented encryption from being useful
as a means of transferring not just information, but also financial value.

This challenge is known as the "Double Spend" problem. The issue lies in the ability
of computers to endlessly duplicate information. In the case of financial value, there
are three important things to record: who owns a specific value; the time at which the person owns this value; the wallet address in which the value resides. When
transferring financial value from one person to another, it is essential that if Person A
sends money to Person B, Person A should not be able to duplicate the same money
and send it again to Person C.

The `Bitcoin protocol <https://en.wikipedia.org/wiki/Bitcoin_network>`_, invented by an anonymous person (or persons) claiming the
name of Satoshi Nakamoto, solved the Double Spend problem. The underlying math
and computer code is both highly complex and innovative. For the purposes of this
paper we need only focus on the one aspect of the Bitcoin protocol that solves the
Double Spend problem: the consensus mechanism.

The Consensus Mechanism Provides Security Against a "Double Spend"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The consensus mechanism invented by Nakamoto is perhaps one of the most powerful innovations of the twenty-first century. His invention allows individual devices to
work together, using high levels of encryption, to securely and accurately track ownership of digital value (be it financial resources, digital eal estate, etc.). It performs
this in a manner that does not allow anyone on the same network (i.e. the Internet)
to spend the same value twice.

Let us suppose a user, Alice, indicates in her digital wallet that she wants to send
cryptocurrency money to a friend. Alice’s computer now gathers several pieces of
information, including any necessary permissions and passwords, the amount that
Alice wants to spend, and the receiving address of her friend’s wallet. All this information is gathered into a packet of data, called a "transaction," and Alice’s device
sends the transaction to the Internet.

There are several types of devices that will interact with Alice’s transaction on
the Internet. These devices will share the transaction information with other devices
supporting the cryptocurrency network. For this discussion, we need only focus on
one type of device: a cryptocurrency miner.

Note: The following descriptions are simplified explanations of a truly complex byzantine
process. There are many other strategies cryptocurrency miners devise to out-mine their com-
petition, and those strategies can vary widely.
