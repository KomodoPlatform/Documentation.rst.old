******
Tokens
******

Visit https://developers.komodoplatform.com/basic-docs/cryptoconditions/cc-tokens.html for the latest Documentation.

Introduction to Tokens contract enabled by Komodo's Custom Consensus Framework
==============================================================================

We have core assets support for on-chain creation of coins/tokens i.e., colored coins. Any Komodo based Blockchain can now be used as a tokenizing platform. The tokens inherit the utxos. They are utxos, just special ones (colored coins actually).

These are assets, like NXT assets, or you can refer to them as tokens. They can be generated from any chain with CC enabled. There are rpc calls like: tokencreate, tokentransfer, tokenaddress which return a dedicated address where all the tokens for a pubkey end up. Also there are exchange rpc calls like: tokenbid, tokenask, tokenswap, tokenfillbid, tokenfillask and tokenfillswap. Using an explorer (addressindex) then the assets balance for an address can be tallied.

It requires locking X amount of native coins to create the supply for a token. So, if you want a unique token, make it 1 satoshi. Using 1 coin gives you 100 million tokens. Here each satoshi is 1 token, so from 1.00000000 coins it makes 100 million tokens, but without any fractions. Or you can interpret it with different decimal precision. 

.. note:: 

	If you consider 10 tokens as a single unit, then this unit can be named anything and it will be divisible to a single decimal place. All of this can be handled on the application side as it is just a change in the way of interpreting the numbers.   

How would those tokens move?
----------------------------

The tokentransfer rpc works like sendmany. The source ``txid/vout`` needs to be specified  as it is critical to match outputs with inputs. If you send to burn address, it is burnt.

