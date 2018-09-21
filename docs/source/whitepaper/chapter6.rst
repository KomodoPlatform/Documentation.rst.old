********************
Abstract (BarterDEX)
********************

Komodo’s decentralized exchange, BarterDEX, allows people to trade cryptocurrency coins without a counterparty risk. The protocol is open-source and trading is
available for any coin that any developers choose to connect to BarterDEX. The parent
project, Komodo, freely provides BarterDEX technology through open-source philosophy. Our service fully realizes decentralized order matching, trade clearing, and
settlement. The order-matching aspect uses a low-level pubkey-to-pubkey messaging
protocol, and the final settlement is executed through an atomic cross-chain protocol.
Like any exchange, our decentralized alternative requires liquidity, and we provide
methods and incentives therein.

Introduction
============

The current, most practical method for cryptocurrency exchange requires the use of
centralized exchange services. Such centralized solutions require vouchers to perform
the exchange. Among many dangers present in this system, end-users are under
the constant risk of their assets being stolen either by an inside theft or an outside
hack. Furthermore, the operators of centralized exchanges an exhibit bias in how
they facilitate trading among their users. They can also create fake levels of volume
on their exchange. To eliminate such dangers and limitations requires the creation of
a decentralized-exchange alternative.

Among all the centralized exchanges, trading tends to coalesce around a few of the
most popular. There is a reason for this behavior. Trading via vouchers is fast; a central
exchange can swap internal vouchers instantaneously, whereas trading actual cryptocurrencies through human-to-human coordination requires communication from
both parties. It requires waiting for blockchain miners to calculate transaction confirmations.

The speed advantage of a centralized exchange, therefore, creates a compounding
effect on the centralization of traders. The faster processing time of vouchers attracts
more people: the increased presence of traders creates higher liquidity: with more
liquidity, the exchange can feature better prices: the higher quality of prices in turn
attracts a larger community, and the cycle repeats. This is a classic Network Effect,
and it is the reason that a few centralized exchanges dominate with high-volume trading, while smaller exchanges—both centralized and decentralized—suffer from a
lack of liquidity.

The Beginnings and Travails of Decentralized Exchanges
------------------------------------------------------

In 2014 a project called The MultiGateway created one of the first decentralized resources for trading cryptocurrencies. The MultiGateway relied on a separate, though
related, blockchain project called the NXT Asset Exchange. The latter facilitated the
decentralized exchange of blockchain coins by using proxy tokens (as opposed to
vouchers), and these proxy tokens represented external cryptocurrencies (such as Bitcoin).

The underlying technology of this solution is still in use by many blockchain platforms, but the proxy- token protocol is too limited to compete with centralized exchanges. Because trading by the means of proxy tokens requires trading on an actual
blockchain, the trading process loses the speed of a centralized exchange. Also, a
proxy-token decentralized exchange must still have a storage center to hold the external cryptocurrencies represented by the proxy tokens. At best, this storage center is
only distributed, and therefore end-users are under the same counterparty risk that
exists in centralized exchanges. Furthermore, the process of trading on proxy-token
platforms requires using a set ofgateways (i.e. "The MultiGateway") to convert external native coins (such as Bitcoin) to and from the affiliated proxy tokens. Together,
these many problems make the proxy-token method of decentralized trading an impractical solution.

Therefore, a decentralized exchange alternative that seeks to successfully remove
the threats and limitations of centralized exchanges must feature the same speed,
liquidity, and convenience of a centralized exchange. As of today, no decentralized
exchange has successfully replaced any of their centralized counterparts.

BarterDEX: A Complete Solution
------------------------------

We now present a fully functional, new decentralized technology that makes a
competitive decentralized exchange possible. We call our technology BarterDEX, and
it allows people to freely and safely exchange cryptocurrency coins from one person
to another.

The BarterDEX decentralized exchange creates a competitive method for bartering
cryptocurrencies, combining three key components: order matching, trade clearing,
and liquidity provision. These components are combined into a single integrated
system that allows users to make a request to trade their coins, find a suitable trading
partner, and complete the trade using an atomic cross-chain protocol. Additionally,
BarterDEX provides a layer of privacy during the order-matching process, enabling
two nodes to perform a peer-to-peer atomic swap without any direct IP contact.

The "order matching" component is the process of pairing an end-user’s offer to
buy with another end- user’s offer to sell. This component is not the actual trade
itself, but is only a digitally created promise between end-users stating that they will
perform their parts of the trade.

The order-matching process is achieved by algorithms that define how the orders
are paired, and in which order they are fulfilled.

After a successful order-matching execution, the next component is the "clearing"
aspect of the trade, wherein end-users must fulfill their promises. This is the process
wherein the assets are swapped between the trading parties. BarterDEX facilitates
this process and assures the safety of the users therein.

Recall that in previous decentralized exchanges there lies a problem when an
exchange has low liquidity. BarterDEX solves this problem by creating Liquidity
Provider Nodes (LP nodes). LP’s are trading parties that act as market-makers, buying and selling assets. They provide liquidity to the exchange, and make their profit
from the spread between bid and ask orders. LP’s bring price stability to the market,
and facilitate end-users in making fast and efficient trades.

Recent Improvements in BarterDEX
--------------------------------

BarterDEX is the result of years of development and iterated versions, with each
iteration adding the next layer of required functionality to achieve our eventual goal
of large-scale adoption.

BarterDEX holds support for `SPV Electrum-based <https://en.bitcoin.it/wiki/Electrum>`_ coins (removing the need to
download a coin’s blockchain), all Bitcoin-protocol based coins running native-coin
daemons, Ethereum, and Ethereum- based ERC20 tokens. The BarterDEX API is built
to handle the nature of the SPV requirements, providing additional functionality to
developers.

BarterDEX also enables a feature known as Liquidity Multiplication, a protocol that
allows the same funds to be used in multiple requests on BarterDEX "orderbooks."
The first request to fill completes the trade, and all outstanding requests are immediately cancelled. This feature is available to the user when providing liquidity to the
exchange (called a "Bob-side" trade); it is not necessary to establish a full LP node to
engage in Liquidity Multiplication.

Liquidity Multiplication therefore allows an initial amount of funding to create an
exponentially higher amount of liquidity on the exchange. This also provides a special
advantage for traders that like to wait for below-market dumps. While this feature
is something that any other exchange could implement, few do. On BarterDEX, all
orderbook entries are 100% backed by real funds, as opposed to a centralized exchange’s vouchers, which are not as reliable and therefore would present yet another
danger for their end-users.

Barterdex Technology
====================

Before we get into details regarding the nature of atomic swaps, there are several
aspects of BarterDEX that are critical to understand.

Order Matching
--------------

The first is the decentralized orderbook. The orderbook is the collection of bids
and offers that end- users place on the network. To create our orderbook, BarterDEX
creates a custom peer-to-peer network that employs two separate types of nodes: a
full-relay node and a non-relay node.

Order Matching with Full-Relay and Non-Relay Nodes
--------------------------------------------------

The difference between a full-relay node and a non-relay node is that the former is
typically a high- volume trader who provides liquidity to the network in exchange
for being a trading hub on the network. This puts him in the position of being able to
complete trades more quickly than his trading competitors. The latter type of node
(non-relay) is the more common user, who engages with BarterDEX when trading
one cryptocurrency for another, given the user’s daily motivations.

There are no requirements or payments necessary to become either type of node,
and so anyone desiring to become a high-volume full-relay node will find no restrictions. To be successful as a full-relay node, however, one must be able to carry out
transactions on the network with a competitive Internet connection and high-capacity
bandwidth.

There are several incentives encouraging users to become full-relay nodes, as these
types of nodes are necessary to build the backbone of the BarterDEX network. One
incentive to run a full-relay node is that by being at the center of a wide network of
non-relay nodes, the full-relay node has better connectivity and thus a higher chance
of being the first to complete a trade.

A non-relay node has all the same available trading options—including the option
to be liquidity providers, and thus use liquidity multiplication. Non-relay nodes are
only limited, naturally, in terms of the total number of connections they maintain to
other users. We expect that most nodes joining the network will be non-relay nodes.

In theory, roughly 100 full-relay nodes should be able to support thousands (if
not tens of thousands) of non-relay nodes, thus providing a large and high-volume
network. We are in the process of achievingreal-world implementation. As of the
writing of this white paper, the public Komodo community has performed almost
100,000 atomic-swap trades on BarterDEX.

When limitations do arise in the scaling process, we have various contingencies
in place, one of which is the creation of clusters. It is possible to create clusters of
BarterDEX nodes that are separate from other clusters on the network. To achieve this, when one cluster approaches a level of user load that is overcapacity, users can
opt to seed a new cluster by creating an independent set of seed nodes. This feature
amplifies the scalability of the BarterDEX network, as it allows clusters of users to
form in accordance with user desires. We assume that at large scales there will be
sufficient inventory in the orderbooks for clusters to provide ample asset liquidity,
especially if the act of partitioning into a new cluster is based on trading a coin that
is overcrowded.

Furthermore, as we continue to develop this new technology, we may also create a
protocol that will allow these separate clusters to share their order boards via bridge
nodes, which in theory can act to cross-pollinate desired orders from one cluster to
another.

To optimize the network load, we minimize the hierarchical transmission of the
orderbooks and the fetching of data. There are also several different methods of obtaining data by which we can maximize the number of nodes that can fully connect
to the BarterDEX network.

Jumblr Technology Adds Privacy
------------------------------

While BarterDEX does not require non-relaying nodes to publicly share their IP
addresses, it is important to note that BarterDEX itself is not private. Instead, we use
Jumblr, an accompanying Komodo technology, to provide privacy options.

Users should assume that if privacy is important for their given trading activity,
they need to employ Komodo’s additional privacy technology, Jumblr. On the surface, non-relaying nodes perform addressing via a <curve25519> pubkey, and the IP
address of one non-relaying node is normally not directly shared with their accompanying non-relaying trading partner. However, full-relay nodes are capable of monitoring IP addresses at the lower levels of the network, and therefore a malicious actor
would be able to link IP addresses of non-relay nodes to pubkeys, thus uncovering
the most crucial aspects of their privacy.

Iguana Core Provides the Foundation for Our "Smart Address" Feature
-------------------------------------------------------------------

BarterDEX itself is a fork of one our earliest codebase experiments, Iguana Core,
which we briefly encounter in each part of this paper. All BarterDEX transactions
that use the atomic-swap protocol are created and signed in a format that is managed
by the Iguana Core codebase. This enables a powerful combination of features.

The following page is a high-level discussion of one method that Iguana Core supports the fluidity of the Komodo ecosystem. Newcomers to the cryptocurrency industry and those who are not familiar with developer language may find this section too
challenging to understand. We welcome the reader to simply read the two warnings
below, and then to skip to the next section.

.. warning::

	* Some of the features that Iguana Core enables are highly advanced, and therefore users interacting with BarterDEX and other Iguana-compatible GUI software applications should always perform proper research and exercise caution.
	* The important thing for users to understand is that they should be careful not to spend the same funding in two different standalone apps. In other words, if they are trading with funds in a BarterDEX GUI, they should not also try to spend those funds in their Agama Wallet (or another Iguana- compatible wallet). Instead, they should wait for both apps to be in sync before moving forward.

One specific feature is a specialty wallet that can manage and trade among a multiplicity of different blockchain coins. To explain the significance of this multi-coin
wallet feature, let us observe how a standalone GUI app formerly interacted with
cryptocurrencies.

Previously, for a GUI software application to manage cryptocurrencies, the soft-
ware application usually required the creation of a wallet.dat file, which is locally
stored on the user’s computer. This wallet.dat file held the privkeys—passwords that
unlock funds on a blockchain—and other encryption-enabled protocols necessary for
the user to manage funds. There are many limitations in the wallet.dat method. For
instance, typically only one software application should access the wallet.dat file at a
time, to prevent data conflict and corruption.

The Iguana Core codebase enables the user to interact with their funds on the
blockchain(s) without requiring a wallet.dat file. Because the Iguana Core codebase
works with raw transaction data, the codebase allows a user to first create and then
manage a public blockchain "smart address" that can be accessed from anywhere, by
any compatible standalone GUI, simply with a passphrase that unlocks their privkey.

To maintain control over their funds without requiring a wallet.dat file, users need
only create a smart address and then retain a copy of the accompanying passphrase
(typically a collection of 12 to 24 common dictionary words arranged in a specific
order) that is provided at the moment of creation. By entering this passphrase into
an Iguana Core compatible standalone GUI app, Iguana Core then activates their
<privkey>, which then enables users to manage their funds.

Furthermore, the smart address created by Iguana Core can manage and maintain
multiple types of coins and other blockchain assets. When a user activates any com-
patible coin using the Iguana-Core passphrase, Iguana Core can store these coins in
a separate address that is compatible with the appropriate blockchain and link this
sub-address to the other addresses unlocked by the Iguana-Core passphrase.

Therefore, in the underlying Iguana code, each of the unique coins gets an address
that is compatible with its own blockchain, but the Iguana-Core passphrase enables
the user to access these coins all at once. Therefore, a BarterDEX GUI app can use
this passphrase to enable users to actively trade between a multiplicity of coins.

One key function of the Iguana codebase that makes this possible is the <withdraw>
command in the Iguana Core API. It is this command that allows individual GUI apps, such as a standalone BarterDEX GUI app, to work with the underlying funds
in the user’s addresses.
Notice several of the freedoms this provides to the user. All the funds are only
spendable by the user with the passphrase. Because there is no need for a wallet.dat
file to be stored locally, there is less danger (though users should exercise caution) of
data corruption between different standalone software applications that are accessing
these funds.
Therefore, an end-user can have a standalone BarterDEX GUI app running on their
local machine, which they use to trade, and can also have a separate standalone GUI
wallet app that is managing their long- term cryptocurrency holdings.

This also allows standalone GUI applications that are Iguana-Core compatible
to support each other. For instance, while a BarterDEX GUI can function without
any native-coin daemon process running in the background simply by relying on
Iguana Core and public Electrum SPV servers (which remove the need to download
blockchain data), the BarterDEX GUI can also work with a native wallet’s coin daemon background process to coordinate blockchain synchronization.

For instance, a Komodo user may run the Komodo Agama wallet, which runs a
native Komodo coin daemon (and has a local wallet.dat file), alongside a BarterDEX
GUI app. Iguana Core can then enable the BarterDEX GUI to rely on the native coin
daemon running in the background of the Komodo Agama wallet, which speeds up
the trading process for an end-user, as they do not have to wait for the public Electrum
servers to update. The native Komodo coin daemon is the software we encountered
in `Part II <section-2.html>`_, Komodod.

The UTXO: an Elusive, Yet Fundamental Concept
=============================================

BarterDEX relies heavily on a rarely understood technology called the "UTXO,"
short for Unspent Transaction, which was invented in the original Bitcoin protocol.
This technology is fundamental to the operations of any blockchain project that utilizes the original Bitcoin protocol. However, even the most active of cryptocurrency
users rarely know what UTXOs are or why they exist.

Because UTXOs play an important part in BarterDEX, and to provide a pleasant
user experience, it is essential we adequately explain the UTXO concept. In the future, as the technology surrounding BarterDEX iterates, and as the cryptocurrency
community continues to learn, we hope that the concept of UTXOs will be less taxing
on a user’s learning curve.

To begin our explanation of UTXOs, let us first examine the language of a common
user when describing how much cryptocurrency money they have and how they
perceive those funds. We will therefore need to understand the concept of "satoshis,"
the way a blockchain handles the collection and distribution of funds, and how we
utilize these core technologies when trading on BarterDEX.

Comparing the UTXO to Fiat Money
--------------------------------

Let us assume a cryptocurrency user, whom we name Charlie, has $10,000 in his
physical wallet. Naturally, when Charlie thinks about the amount of physical (or
"fiat") money he has, he says to himself, "I have $10,000."

However, there is no such thing as a $10,000-dollar bill. Instead, Charlie actually
has a collection of smaller bills stacked together. For instance, he could have a stack
of $100-dollar bills, the total of which equals $10,000 dollars.

If Charlie goes to purchase an item that costs $1, and he only has $100-dollar bills
in his wallet, to make his purchase he will take out a single $100-dollar bill and give
it to the cashier. The cashier then breaks that $100-dollar bill down into a series of
smaller bills. The cost for the item, $1, remains with the cashier, and the cashier then
provides change—perhaps in the form of one $50-dollar bill, two $20- dollar bills, one
$5-dollar bill, and four $1-dollar bills.

Charlie now thinks to himself, "I have $9,999." Specifically, however, he has ninety-
nine $100-dollar bills, a $50-dollar bill, two $20-dollar bills, one $5-dollar bill, and
four $1-dollar bills.

We emphasize that not only does he not have ten thousand $1-dollar bills, he also
does not have one million pennies ($0.01). Furthermore, because pennies are the small-
est divisible unit of value in Charlie’s wallet, we could point out that each bill is a
collection of its respective units of pennies. For instance, a $1-dollar bill in Charlie’s
wallet we could describe as, "a bill that represents a collection of one hundred pennies
and their value."

Understanding Cryptocurrencies and Their UTXOs
----------------------------------------------

A Satoshi is The Smallest Divisible Unit of a Cryptocurrency
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Continuing with our explanation of UTXOs, we next need to understand the concept of "satoshis." The name "satoshi" is derived in honor of Satoshi Nakamoto, author
of the original Bitcoin white paper. By convention in the cryptocurrency community,
one satoshi is equal to one unit of a coin at the smallest divisible level. For instance,
1 satoshi of Bitcoin is equal to 0.00000001 BTC.

Let us suppose now that Charlie has 9.99000999 BTC (Bitcoin) in his digital wallet.
Assuming Charlie correctly understands the concept of satoshis, Charlie could say to
himself, "I have nine hundred and ninety-nine million, nine hundred and ninety-nine
satoshis of bitcoin."

This is how Charlie might mentally perceive the collection of money that exists in
his digital wallet, like he perceives the $9,999 in his fiat wallet.

A UTXO is a Packet of Satoshis, just as a Fiat Dollar Bill is a Packet of Pennies
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Recall now that with fiat money, Charlie did not think about how his original
$10,000 was comprised of smaller individual $100-dollar bills. Similarly, Charlie also
does not think about how his 9.99000999 BTC could be comprised of smaller collections of satoshis.

Furthermore, just as Charlie did not carry around fiat money as a collection of pennies, he also is not carrying around a raft of satoshis. Were he to try to carry a million
pennies in his physical wallet, the weight of the wallet would be unmanageable. Similarly, if the Bitcoin protocol were to attempt to manage nine hundred and ninety-nine
million, nine-hundred and ninety-nine satoshis, the "data weight" would be so heavy,
the Bitcoin protocol would be enormous and unmanageable.

To optimize "data weight," the Bitcoin protocol therefore bundles up the satoshis
into something that is like the example of dollar bills earlier, but with one important
difference. In fact, here is where the Bitcoin protocol exercises a superiority over
fiat money by deviating from the limitations fiat money must obey when bundling
smaller values into larger values.

In fiat money, one hundred pennies are bundled into a one-dollar bill, which can
then be bundled into a larger bill, and so on. All the sizes of fiat money are preset and
predetermined by the issuer of the fiat money when they print their bills and coins.

The Bitcoin protocol, however, does not need to pre-plan the sizes of "bills" (i.e. the
collections of satoshis) in the owner’s wallet. Bitcoin is freer in this sense; it can shift
and change the sizes of its "bills" at will because there is no need to accommodate for
the printing of physical coins and paper.

Instead, the Bitcoin protocol allows for the developer of digital wallets to write
code that can optimize how bitcoin satoshis are packaged into "bills," and thus the
community of developers can work together to keep the data weight of the blockchain
manageable. The better the digital-wallet developer, the more efficient the size of the
"bills" (a.k.a. the packets of satoshis).

The Bitcoin protocol does have one limitation, however: It must keep track of how
these satoshis are being collected into larger "bills" in everyone’s digital wallets. After
all, the very idea of Bitcoin stands in the idea that everything happens under the
public eye, where it can be verified. Because the Bitcoin blockchain must keep track
of the sizes of these packets of satoshis, the only time the packets can be assembled
or disassembled into larger and smaller sizes is at the moment when the user is
spending money on the public blockchain. It is at this time that the user is under the
public eye, and therefore his actions can be verified.

To compare this limitation to fiat money, consider the effect created were Charlie
to cut a $100-dollar bill into smaller pieces. The $100-dollar bill would no longer be
respected as a valid form of currency.

As the word, "UTXO," is not a sonorous word, some users in the Komodo ecosystem
simply refer to UTXOs as "bills." The concept is effectively the same. However, as the
rest of the blockchain industry primarily uses the word "UTXO," we frequently must use this word to maintain a common line of communication. The word UTXO will be
used throughout the rest of this white paper, to keep in line with industry practices.

The UTXO packet can be any size, and the developer of the GUI software decides
on this process. Most importantly, and to reiterate, a UTXO can only be resized during
the process of spending, as this is the moment when the user interacts with the public
blockchain.

To further clarify this, let us return to Charlie’s example with fiat money. Recall
that when Charlie went to purchase a $1-dollar item, he only had $100-dollar bills in
his wallet. He had to give out one $100- dollar bill, and then receive a broken-down
collection of dollar bills in return.

This is exactly how it works with UTXOs. Charlie has a collection of UTXOs in
his digital wallet. When he goes to buy something, he will give out UTXOs until he
surpasses how much he owes, and then the extra change from the last UTXO used
will be broken down and returned to him.

For example, let us suppose that Charlie’s 9.99000999 BTC is comprised of three
UTXOs worth the following values:

+----------------------------+
| UTXOs in Charlie’s Wallet  |
+-----------+----------------+
| UTXO #1:  | 0.50000000 BTC |
+-----------+----------------+
| UTXO #2:  | 0.49000999 BTC |
+-----------+----------------+
| UTXO #3:  | 9.00000000 BTC |
+-----------+----------------+
| Total     | 9.99000999 BTC |
+-----------+----------------+

Charlie now desires to purchase an item that costs 0.60000000 BTC. He will have to
hand out enough UTXOs from his wallet until he covers the costs of this transaction,
just as he would if he were using fiat money. The Bitcoin protocol calculates the
change from the transaction and then returns his change to him.

Remember that there is a fee when spending money on a blockchain. Since we are
using Bitcoin in this example, the fee would be paid to cryptocurrency miners. Let us
imagine that the fee the miners charge Charlie is 999 satoshis.

We begin by looking at how Charlie would see the process of making the purchase,
assuming he does not understand the concept of UTXOs. For now, Charlie only understands how much is in his wallet at the satoshi level as he conducts his transaction:


+--------------------+------------------------------------------------------------------+
| 9.99000999 BTC     | The amount Charlie initially owns                                |
+--------------------+------------------------------------------------------------------+
| (-) 0.60000000 BTC | The amount Charlie sends to the digital cashier for his purchase |
+--------------------+------------------------------------------------------------------+
| (-) 0.00000999 BTC | The network fee paid to miners                                   |
+--------------------+------------------------------------------------------------------+
| 9.39000000 BTC     | The amount left in his wallet                                    |
+--------------------+------------------------------------------------------------------+

This deduction for his purchase all appears very simple to Charlie—a testament to
the Bitcoin protocol’s effective design.

In the background, however, the digital wallet handles the UTXOs and the change
process in a manner as determined by the programmer. In Charlie’s example, let us
assume that it proceeds this way:

+------------------------+---------------------------------------------------------------+
| 0.60000999 BTC         | The total amount that Charlie owes to the cashier and network |
+------------------------+---------------------------------------------------------------+
| **(-) 0.50000000 BTC** | The wallet sends the full value of **UTXO #1** to the digital |
|                        | cashier                                                       |
+------------------------+---------------------------------------------------------------+
| 0.10000999 BTC         | This is the remaining total amount that Charlie still         |
|                        | owes                                                          |
+------------------------+---------------------------------------------------------------+

The wallet now brings out UTXO #2, which is worth 0.49000999 BTC:
This UTXO is broken down or shattered into smaller pieces.

+--------------------+---------------------------------------------------------------------+
| 0.49000999 BTC     | The size of Charlie’s **UTXO #2**, now in the process of change     |
+--------------------+---------------------------------------------------------------------+
| (-) 0.10000000 BTC | This shatter of **UTXO #2** goes to the cashier (payment fulfilled) |
+--------------------+---------------------------------------------------------------------+
| (-) 0.00000999 BTC | This shatter of **UTXO #2** pays the network fee                    |
|                    | to the miners                                                       |
+--------------------+---------------------------------------------------------------------+
| 0.39000000 BTC     | This last shatter now returns to Charlie’s wallet                   |
|                    | as a new UTXO                                                       |
+--------------------+---------------------------------------------------------------------+

Charlie now has one new UTXO in his wallet, and it is worth 0.39000000 BTC:

+----------------------------+
| Charlie’s New Wallet State |
+-----------+----------------+
| UTXO #3:  | 9.00000000 BTC |
+-----------+----------------+
| UTXO #4:  | 0.39000000 BTC |
+-----------+----------------+
| Total     | 9.39000000 BTC |
+-----------+----------------+

If Charlie wants to buy something later, these UTXOs will have to be broken up once
more, according to the costs and programming of the digital wallet. Again, whatever
is left over from his last UTXO comes back to his own wallet as a new UTXO.

Now let us suppose that Charlie receives 0.4 BTC from someone else. In Charlie’s
wallet, he will see a total of 9.79 BTC. However, in his wallet there are now actually
three UTXOs:

+----------------------------+
| Charlie’s New Wallet State |
+-----------+----------------+
| UTXO #3:  | 9.00000000 BTC |
+-----------+----------------+
| UTXO #4:  | 0.39000000 BTC |
+-----------+----------------+
| UTXO #5:  | 0.4000000 BTC  |
+-----------+----------------+
| Total     | 9.79000000 BTC |
+-----------+----------------+

As a result, the number and sizes of UTXOs in Charlie’s wallet will vary over time. He
may have many smaller UTXOs that make up his full balance, or sometimes he might
just have one large UTXO that comprises all of it. For Charlie, it is normally possible
to ignore this since the wallet developer could handle everything automatically.

However, understanding the nature of BarterDEX currently encourages users to
understand UTXOs, as the process relies on their UTXO inventory during trading, as
explained below.

Trading on Barterdex
====================


