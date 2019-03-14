******
Faucet
******

Visit https://developers.komodoplatform.com/basic-docs/cryptoconditions/cc-faucet.html for the latest Documentation.

Introduction
============

This is a Faucet contract. Enables anyone to setup and operate an onchain-faucet. For each faucet, there is an address to which anyone can send their funds and the address will be serving anyone who requests it as long as their address satisfies some constraints.

To claim faucet funds, the used pubkey and address must be fresh without any funds or tx associated to that address. One address can claim faucet funds only once.

``faucetget`` runs a custom PoW to deter leechers.

Faucet sends 0.1 coins and requires about 30 seconds of CPU time.


