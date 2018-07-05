****************************
Komodo - API - Documentation
****************************

You can access this API while ``komodod`` is running. Just go to another terminal and run ``./komodo-cli help``.

For help about a particular API option execute ``./komodo-cli help getwalletinfo``

In some of the explanation of API calls if you find ``Zcash`` consider it replaced by ``Komodo`` and ``zcashaddress`` replaced by ``komodoaddress`` 

:doc:`Guide to install Komodo <install-Komodo-manually>`

List of API by Category
=======================

Click any of the api options below to be taken to their summary.
Then navigate using the links in the Navigation bar on the left side. Or press the ``Home`` button on your keyboard to come back to the top again. 
As the docs are full of code samples and command-line outputs, it's best viewed on a laptop/desktop (i.e, any device that is bigger than a handheld).

:ref:`Category: Addressindex <Addressindex>`
--------------------------------------------

:ref:`getaddressbalance`, :ref:`getaddressdeltas`, :ref:`getaddressmempool`, :ref:`getaddresstxids`, :ref:`getaddressutxos`

:ref:`Category: Blockchain <Blockchain>`
----------------------------------------

:ref:`MoMoMdata symbol kmdheight notarized_height`, :ref:`allMoMs kmdstarti kmdendi`, :ref:`calc_MoM height MoMdepth`, :ref:`getbestblockhash`, :ref:`getblock "hash|height" ( verbose )`, :ref:`getblockchaininfo`, :ref:`getblockcount`

:ref:`getblockhash index`, :ref:`getblockhashes timestamp`, :ref:`getblockheader "hash" ( verbose )`, :ref:`getchaintips`, :ref:`getdifficulty`, :ref:`getmempoolinfo`, :ref:`getrawmempool ( verbose )`, :ref:`getspentinfo`, :ref:`gettxout "txid" n ( includemempool )`, :ref:`gettxoutproof ["txid",...] ( blockhash )`, :ref:`gettxoutsetinfo`, :ref:`height_MoM height`, :ref:`kvsearch key`, :ref:`kvupdate key value flags/passphrase`, :ref:`minerids needs height`, :ref:`notaries height timestamp`, :ref:`paxpending needs no args`, :ref:`paxprice "base" "rel" height`, :ref:`paxprices "base" "rel" maxsamples`, :ref:`txMoMproof needs a txid`, :ref:`verifychain ( checklevel numblocks )`, :ref:`verifytxoutproof "proof"`

:ref:`Category: Control <Control>`
----------------------------------

:ref:`getinfo`, :ref:`help ( "command" )`, :ref:`stop <komodo-api-stop>`

:ref:`Category: Disclosure <Disclosure>`
----------------------------------------

:ref:`z_getpaymentdisclosure "txid" "js_index" "output_index" ("message")`, 
:ref:`z_validatepaymentdisclosure "paymentdisclosure"`

:ref:`Category: Generating <Generating>`
----------------------------------------

:ref:`generate numblocks`, :ref:`getgenerate`, :ref:`setgenerate generate ( genproclimit )`

:ref:`Category: Mining <Mining>`
--------------------------------

:ref:`getblocksubsidy height`, :ref:`getblocktemplate ( "jsonrequestobject" )`, :ref:`getlocalsolps`, :ref:`getmininginfo`, :ref:`getnetworkhashps ( blocks height )`, :ref:`getnetworksolps ( blocks height )`, 
:ref:`prioritisetransaction \<txid\> \<priority delta\> \<fee delta\>`, :ref:`submitblock "hexdata" ( "jsonparametersobject" )`

:ref:`Category: Network <Network>`
----------------------------------

:ref:`addnode "node" "add|remove|onetry"`, :ref:`clearbanned`, :ref:`disconnectnode "node"`,
:ref:`getaddednodeinfo dns ( "node" )`, 
:ref:`getconnectioncount`, :ref:`getdeprecationinfo`, :ref:`getnettotals`, :ref:`getnetworkinfo`, 
:ref:`getpeerinfo`, :ref:`listbanned`, :ref:`ping`, :ref:`setban "ip(/netmask)" "add|remove" (bantime) (absolute)`

:ref:`Category: Rawtransactions <Rawtransactions>`
--------------------------------------------------

:ref:`createrawtransaction [{"txid":"id","vout":n},...] {"address":amount,...}`, :ref:`decoderawtransaction "hexstring"`, :ref:`decodescript "hex"`, :ref:`fundrawtransaction "hexstring"`, :ref:`getrawtransaction "txid" ( verbose )`, :ref:`sendrawtransaction "hexstring" ( allowhighfees )`, :ref:`signrawtransaction "hexstring" ( [{"txid":"id","vout":n,"scriptPubKey":"hex","redeemScript":"hex"},...] ["privatekey1",...] sighashtype )`

:ref:`Category: Util <Util>`
----------------------------

:ref:`createmultisig nrequired ["key",...]`, :ref:`estimatefee nblocks`, :ref:`estimatepriority nblocks`, :ref:`invalidateblock "hash"`, :ref:`jumblr_deposit "depositaddress"`, :ref:`jumblr_pause`, :ref:`jumblr_resume`, :ref:`jumblr_secret "secretaddress"`, :ref:`reconsiderblock "hash"`, :ref:`validateaddress "komodoaddress"`, :ref:`verifymessage "komodoaddress" "signature" "message"`, :ref:`z_validateaddress "zaddr"`

:ref:`Category: Wallet <Wallet>`
--------------------------------

:ref:`addmultisigaddress nrequired ["key",...] ( "account" )`, :ref:`backupwallet "destination"`, :ref:`dumpprivkey "komodoaddress"`, :ref:`dumpwallet "filename"`, :ref:`encryptwallet "passphrase"`, :ref:`getaccount "KMD_address"`, :ref:`getaccountaddress "account"`, :ref:`getaddressesbyaccount "account"`, :ref:`getbalance ( "account" minconf includeWatchonly )`, :ref:`getnewaddress ( "account" )`, :ref:`getrawchangeaddress`, :ref:`getreceivedbyaccount "account" ( minconf )`, :ref:`getreceivedbyaddress "KMD_address" ( minconf )`, :ref:`gettransaction "txid" ( includeWatchonly )`, :ref:`getunconfirmedbalance`, :ref:`getwalletinfo`, :ref:`importaddress "address" ( "label" rescan )`, :ref:`importprivkey "komodoprivkey" ( "label" rescan )`, :ref:`importwallet "filename"`, :ref:`keypoolrefill ( newsize )`, :ref:`listaccounts ( minconf includeWatchonly)`, :ref:`listaddressgroupings`, :ref:`listlockunspent`, :ref:`listreceivedbyaccount ( minconf includeempty includeWatchonly)`, :ref:`listreceivedbyaddress ( minconf includeempty includeWatchonly)`, :ref:`listsinceblock ( "blockhash" target-confirmations includeWatchonly)`, :ref:`listtransactions ( "account" count from includeWatchonly)`, :ref:`listunspent ( minconf maxconf  ["address",...] )`, :ref:`lockunspent unlock [{"txid":"txid","vout":n},...]`, :ref:`move "fromaccount" "toaccount" amount ( minconf "comment" )`, :ref:`resendwallettransactions`, :ref:`sendfrom "fromaccount" "toKMDaddress" amount ( minconf "comment" "comment-to" )`, :ref:`sendmany "fromaccount" {"address":amount,...} ( minconf "comment" ["address",...] )`, :ref:`sendtoaddress "KMD_address" amount ( "comment" "comment-to" subtractfeefromamount )`, :ref:`setaccount "KMD_address" "account"`, :ref:`settxfee amount`, :ref:`signmessage "KMD address" "message"`, :ref:`z_exportkey "zaddr"`, :ref:`z_exportviewingkey "zaddr"`, :ref:`z_exportwallet "filename"`, :ref:`z_getbalance "address" ( minconf )`, :ref:`z_getnewaddress`, 
:ref:`z_getoperationresult (["operationid", ...])`, 
:ref:`z_getoperationstatus (["operationid", ...])`, 
:ref:`z_gettotalbalance ( minconf includeWatchonly )`, :ref:`z_importkey "zkey" ( rescan startHeight )`, :ref:`z_importviewingkey "vkey" ( rescan startHeight )`, :ref:`z_importwallet "filename"`, :ref:`z_listaddresses ( includeWatchonly )`, :ref:`z_listoperationids`, :ref:`z_listreceivedbyaddress "address" ( minconf )`, :ref:`z_mergetoaddress ["fromaddress", ...] "toaddress" ( fee ) ( transparent_limit ) ( shielded_limit ) ( memo )`, :ref:`z_sendmany "fromaddress" [{"address":...,"amount":...},...] ( minconf ) ( fee )`, :ref:`z_shieldcoinbase "fromaddress" "tozaddress" ( fee ) ( limit )`, :ref:`zcbenchmark benchmarktype samplecount`, :ref:`zcrawjoinsplit rawtx inputs outputs vpub_old vpub_new`, :ref:`zcrawkeygen`, :ref:`zcrawreceive zcsecretkey encryptednote`, :ref:`zcsamplejoinsplit`

Addressindex
============

getaddressbalance
-----------------

Returns the balance for an address(es) (requires addressindex to be enabled).

Arguments:

::

	{
	  "addresses"
	    [
	      "address"  (string) The base58check encoded address
	      ,...
	    ]
	}

Result:
::

	{
	  "balance"  (string) The current balance in satoshis
	  "received"  (string) The total number of satoshis received (including change)
	}

Examples:

::

	> komodo-cli getaddressbalance '{"addresses": ["12c6DSiU4Rq3P4ZxziKxzrL5LmMBrzjrJX"]}'
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getaddressbalance", "params": [{"addresses": ["12c6DSiU4Rq3P4ZxziKxzrL5LmMBrzjrJX"]}] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getaddressdeltas
----------------

Returns all changes for an address (requires addressindex to be enabled).

Arguments:

::

	{
	  "addresses"
	    [
	      "address"  (string) The base58check encoded address
	      ,...
	    ]
	  "start" (number) The start block height
	  "end" (number) The end block height
	  "chainInfo" (boolean) Include chain info in results, only applies if start and end specified
	}

Result:

::

	[
	  {
	    "satoshis"  (number) The difference of satoshis
	    "txid"  (string) The related txid
	    "index"  (number) The related input or output index
	    "height"  (number) The block height
	    "address"  (string) The base58check encoded address
	  }
	]

Examples:

::

	> komodo-cli getaddressdeltas '{"addresses": ["12c6DSiU4Rq3P4ZxziKxzrL5LmMBrzjrJX"]}'
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getaddressdeltas", "params": [{"addresses": ["12c6DSiU4Rq3P4ZxziKxzrL5LmMBrzjrJX"]}] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getaddressmempool
-----------------

Returns all mempool deltas for an address (requires addressindex to be enabled).

Arguments:

::

	{
	  "addresses"
	    [
	      "address"  (string) The base58check encoded address
	      ,...
	    ]
	}

Result:

::

	[
	  {
	    "address"  (string) The base58check encoded address
	    "txid"  (string) The related txid
	    "index"  (number) The related input or output index
	    "satoshis"  (number) The difference of satoshis
	    "timestamp"  (number) The time the transaction entered the mempool (seconds)
	    "prevtxid"  (string) The previous txid (if spending)
	    "prevout"  (string) The previous transaction output index (if spending)
	  }
	]

Examples:

::

	> komodo-cli getaddressmempool '{"addresses": ["12c6DSiU4Rq3P4ZxziKxzrL5LmMBrzjrJX"]}'
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getaddressmempool", "params": [{"addresses": ["12c6DSiU4Rq3P4ZxziKxzrL5LmMBrzjrJX"]}] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getaddresstxids
---------------

Returns the txids for an address(es) (requires addressindex to be enabled).

Arguments:

::

	{
	  "addresses"
	    [
	      "address"  (string) The base58check encoded address
	      ,...
	    ]
	  "start" (number) The start block height
	  "end" (number) The end block height
	}

Result:

::
	
	[
	  "transactionid"  (string) The transaction id
	  ,...
	]

Examples:

::

	> komodo-cli getaddresstxids '{"addresses": ["12c6DSiU4Rq3P4ZxziKxzrL5LmMBrzjrJX"]}'
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getaddresstxids", "params": [{"addresses": ["12c6DSiU4Rq3P4ZxziKxzrL5LmMBrzjrJX"]}] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getaddressutxos
---------------

Returns all unspent outputs for an address (requires addressindex to be enabled).

Arguments:

::

	{
	  "addresses"
	    [
	      "address"  (string) The base58check encoded address
	      ,...
	    ],
	  "chainInfo"  (boolean) Include chain info with results
	}

Result:

::

	[
	  {
	    "address"  (string) The address base58check encoded
	    "txid"  (string) The output txid
	    "height"  (number) The block height
	    "outputIndex"  (number) The output index
	    "script"  (strin) The script hex encoded
	    "satoshis"  (number) The number of satoshis of the output
	  }
	]

Examples:

::

	> komodo-cli getaddressutxos '{"addresses": ["12c6DSiU4Rq3P4ZxziKxzrL5LmMBrzjrJX"]}'
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getaddressutxos", "params": [{"addresses": ["12c6DSiU4Rq3P4ZxziKxzrL5LmMBrzjrJX"]}] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

Blockchain
==========

MoMoMdata symbol kmdheight notarized_height
-------------------------------------------

``COMING SOON``

allMoMs kmdstarti kmdendi
-------------------------

``COMING SOON``

calc_MoM height MoMdepth
------------------------

``COMING SOON``

getbestblockhash
----------------

Returns the hash of the best (tip) block in the longest block chain.

Result:

::

	"hex"      (string) the block hash hex encoded

Examples:

::

	> komodo-cli getbestblockhash 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getbestblockhash", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getblock "hash|height" ( verbose )
----------------------------------

* If verbose is ``false``, returns a string that is serialized, hex-encoded data for block 'hash|height'.
* If verbose is ``true``, returns an Object with information about block <hash|height>.

Arguments:

::

	1. "hash|height"     (string, required) The block hash or height
	2. verbose           (boolean, optional, default=true) true for a json object, false for the hex encoded data

Result (for verbose = ``true``):

::

        {
            "hash": "hash",       (string) the block hash (same as provided hash)
  "confirmations": n,   (numeric) The number of confirmations, or -1 if the block is not on the main chain
  "size": n,            (numeric) The block size
  "height": n,          (numeric) The block height or index (same as provided height)
  "version": n,         (numeric) The block version
  "merkleroot": "xxxx", (string) The merkle root
  "tx": [               (array of string) The transaction ids
     "transactionid"     (string) The transaction id
     ,...
            ],
            "time": ttt,          (numeric) The block time in seconds since epoch (Jan 1 1970 GMT)
  "nonce": n,           (numeric) The nonce
  "bits": "1d00ffff",   (string) The bits
  "difficulty": x.xxx,  (numeric) The difficulty
  "previousblockhash": "hash",  (string) The hash of the previous block
  "nextblockhash": "hash"       (string) The hash of the next block
        }

Result (for verbose=``false``):

::

	"data"             (string) A string that is serialized, hex-encoded data for block 'hash'.

Examples:
::

	> komodo-cli getblock "00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09"
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getblock", "params": ["00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/
	> komodo-cli getblock 12800
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getblock", "params": [12800] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/


getblockchaininfo
-----------------

Returns an object containing various state info regarding block chain processing.

 *Note that when the chain tip is at the last block before a network upgrade activation,* ``consensus.chaintip != consensus.nextblock``.

Result:

::

    {
        "chain": "xxxx",        (string) current network name as defined in BIP70 (main, test, regtest)
  "blocks": xxxxxx,         (numeric) the current number of blocks processed in the server
  "headers": xxxxxx,        (numeric) the current number of headers we have validated
  "bestblockhash": "...", (string) the hash of the currently best block
  "difficulty": xxxxxx,     (numeric) the current difficulty
  "verificationprogress": xxxx, (numeric) estimate of verification progress [0..1
        ]
  "chainwork": "xxxx"     (string) total amount of work in active chain, in hexadecimal
  "commitments": xxxxxx,    (numeric) the current number of note commitments in the commitment tree
  "softforks": [            (array) status of softforks in progress
     {
                "id": "xxxx",        (string) name of softfork
        "version": xx,         (numeric) block version
        "enforce": {           (object) progress toward enforcing the softfork rules for new-version blocks
           "status": xx,       (boolean) true if threshold reached
           "found": xx,        (numeric) number of blocks with the new version found
           "required": xx,     (numeric) number of blocks required to trigger
           "window": xx,       (numeric) maximum size of examined window of recent blocks
                },
                "reject": { ...
                }      (object) progress toward rejecting pre-softfork blocks (same fields as "enforce")
            }, ...
        ],
        "upgrades": {                (object) status of network upgrades
     "xxxx": {                (string) branch ID of the upgrade
        "name": "xxxx",        (string) name of upgrade
        "activationheight": xxxxxx,  (numeric) block height of activation
        "status": "xxxx",      (string) status of upgrade
        "info": "xxxx",        (string) additional information about upgrade
            }, ...
        },
        "consensus": {               (object) branch IDs of the current and upcoming consensus rules
     "chaintip": "xxxxxxxx",   (string) branch ID used to validate the current chain tip
     "nextblock": "xxxxxxxx"   (string) branch ID that the next block will be validated under
        }
    }

Examples:

::

	> komodo-cli getblockchaininfo 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getblockchaininfo", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/


getblockcount
-------------

Returns the number of blocks in the best valid block chain.

Result:

::

	n    (numeric) The current block count

Examples:

::

	> komodo-cli getblockcount 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getblockcount", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getblockhash index
------------------

Returns hash of block in best-block-chain at index provided.

Arguments:

::

	1. index         (numeric, required) The block index

Result:

::

	"hash"         (string) The block hash

Examples:

::

	> komodo-cli getblockhash 1000
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getblockhash", "params": [1000] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getblockhashes timestamp
------------------------

Returns array of hashes of blocks within the timestamp range provided.

Arguments:

::

	1. high         (numeric, required) The newer block timestamp
	2. low          (numeric, required) The older block timestamp
	3. options      (string, required) A json object
    {
      "noOrphans":true   (boolean) will only include blocks on the main chain
      "logicalTimes":true   (boolean) will include logical timestamps with hashes
    }

Result:

::

	[
		  "hash"         (string) The block hash
	]
	[
	  {
	    "blockhash": (string) The block hash
	    "logicalts": (numeric) The logical timestamp
	  }
	]

Examples:

::

	> komodo-cli getblockhashes 1231614698 1231024505
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getblockhashes", "params": [1231614698, 1231024505] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/
	> komodo-cli getblockhashes 1231614698 1231024505 '{"noOrphans":false, "logicalTimes":true}'

getblockheader "hash" ( verbose )
---------------------------------

If verbose is false, returns a string that is serialized, hex-encoded data for blockheader 'hash'.
If verbose is true, returns an Object with information about blockheader <hash>.

Arguments:

::

	1. "hash"          (string, required) The block hash
	2. verbose           (boolean, optional, default=true) true for a json object, false for the hex encoded data

Result (for verbose = true):

::

	{
	  "hash" : "hash",     (string) the block hash (same as provided)
	  "confirmations" : n,   (numeric) The number of confirmations, or -1 if the block is not on the main chain
	  "height" : n,          (numeric) The block height or index
	  "version" : n,         (numeric) The block version
	  "merkleroot" : "xxxx", (string) The merkle root
	  "time" : ttt,          (numeric) The block time in seconds since epoch (Jan 1 1970 GMT)
	  "nonce" : n,           (numeric) The nonce
	  "bits" : "1d00ffff", (string) The bits
	  "difficulty" : x.xxx,  (numeric) The difficulty
	  "previousblockhash" : "hash",  (string) The hash of the previous block
	  "nextblockhash" : "hash"       (string) The hash of the next block
	}

Result (for verbose=false):

::

	"data"             (string) A string that is serialized, hex-encoded data for block 'hash'.

Examples:

::

	> komodo-cli getblockheader "00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09"
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getblockheader", "params": ["00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getchaintips
------------

Return information about all known tips in the block tree, including the main chain as well as orphaned branches.

Result:

::

	[
	  {
	    "height": xxxx,         (numeric) height of the chain tip
	    "hash": "xxxx",         (string) block hash of the tip
	    "branchlen": 0          (numeric) zero for main chain
	    "status": "active"      (string) "active" for the main chain
	  },
	  {
	    "height": xxxx,
	    "hash": "xxxx",
	    "branchlen": 1          (numeric) length of branch connecting the tip to the main chain
	    "status": "xxxx"        (string) status of the chain (active, valid-fork, valid-headers, headers-only, invalid)
	  }
	]

Possible values for status:

::

	1.  "invalid"               This branch contains at least one invalid block
	2.  "headers-only"          Not all blocks for this branch are available, but the headers are valid
	3.  "valid-headers"         All blocks are available for this branch, but they were never fully validated
	4.  "valid-fork"            This branch is not part of the active chain, but is fully validated
	5.  "active"                This is the tip of the active main chain, which is certainly valid

Examples:

::

	> komodo-cli getchaintips 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getchaintips", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/


getdifficulty
-------------

Returns the proof-of-work difficulty as a multiple of the minimum difficulty.

Result:

::

	n.nnn       (numeric) the proof-of-work difficulty as a multiple of the minimum difficulty.

Examples:

::

	> komodo-cli getdifficulty 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getdifficulty", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getmempoolinfo
--------------

Returns details on the active state of the TX memory pool.

Result:

::

	{
	  "size": xxxxx                (numeric) Current tx count
	  "bytes": xxxxx               (numeric) Sum of all tx sizes
	  "usage": xxxxx               (numeric) Total memory usage for the mempool
	}

Examples:

::

	> komodo-cli getmempoolinfo 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getmempoolinfo", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getrawmempool ( verbose )
-------------------------

Returns all transaction ids in memory pool as a json array of string transaction ids.

Arguments:

::

	1. verbose           (boolean, optional, default=false) true for a json object, false for array of transaction ids

Result: (for verbose = false):

::

	[                     (json array of string)
	  "transactionid"     (string) The transaction id
	  ,...
	]

Result: (for verbose = true):

::

	{                           (json object)
	  "transactionid" : {       (json object)
	    "size" : n,             (numeric) transaction size in bytes
	    "fee" : n,              (numeric) transaction fee in ZEC
    	"time" : n,             (numeric) local time transaction entered pool in seconds since 1 Jan 1970 GMT
    	"height" : n,           (numeric) block height when transaction entered pool
    	"startingpriority" : n, (numeric) priority when transaction entered pool
    	"currentpriority" : n,  (numeric) transaction priority now
    	"depends" : [           (array) unconfirmed transactions used as inputs for this transaction
        "transactionid",    (string) parent transaction id
	       ...]
	  }, ...
	}

Examples:

::

	> komodo-cli getrawmempool true
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getrawmempool", "params": [true] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getspentinfo
------------

Returns the txid and index where an output is spent.

Arguments:

::

	{
	  "txid" (string) The hex string of the txid
	  "index" (number) The start block height
	}

Result:

::

	{
	  "txid"  (string) The transaction id
	  "index"  (number) The spending input index
	  ,...
	}

Examples:

::

	> komodo-cli getspentinfo '{"txid": "0437cd7f8525ceed2324359c2d0ba26006d92d856a9c20fa0241106ee5a597c9", "index": 0}'
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getspentinfo", "params": [{"txid": "0437cd7f8525ceed2324359c2d0ba26006d92d856a9c20fa0241106ee5a597c9", "index": 0}] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

gettxout "txid" n ( includemempool )
------------------------------------

Returns details about an unspent transaction output.

Arguments:

::

	1. "txid"       (string, required) The transaction id
	2. n              (numeric, required) vout value
	3. includemempool  (boolean, optional) Whether to include the mempool

Result:

::

	{
	  "bestblock" : "hash",    (string) the block hash
	  "confirmations" : n,       (numeric) The number of confirmations
	  "value" : x.xxx,           (numeric) The transaction value in ZEC
  	"scriptPubKey" : {         (json object)
    	 "asm" : "code",       (string) 
    	 "hex" : "hex",        (string) 
    	 "reqSigs" : n,          (numeric) Number of required signatures
    	 "type" : "pubkeyhash", (string) The type, eg pubkeyhash
    	 "addresses" : [          (array of string) array of Zcash addresses
    	    "zcashaddress"        (string) Zcash address
    	    ,...
    	 ]
  	},
  	"version" : n,              (numeric) The version
  	"coinbase" : true|false     (boolean) Coinbase or not
	}

Examples:

Get unspent transactions

::

	> komodo-cli listunspent 

View the details

::

	> komodo-cli gettxout "txid" 1

As a json rpc call

::

	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "gettxout", "params": ["txid", 1] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

gettxoutproof ["txid",...] ( blockhash )
----------------------------------------

Returns a hex-encoded proof that "txid" was included in a block.

**NOTE:** By default this function only works sometimes. This is when there is an
unspent output in the utxo for this transaction. To make it always work,
you need to maintain a transaction index, using the -txindex command line option or
specify the block in which the transaction is included in manually (by blockhash).

Return the raw transaction data.

Arguments:

::

	1. "txids"       (string) A json array of txids to filter
	    [
	      "txid"     (string) A transaction hash
	      ,...
	    ]
	2. "block hash"  (string, optional) If specified, looks for txid in the block with this hash

Result:

::

	"data"           (string) A string that is a serialized, hex-encoded data for the proof.

gettxoutsetinfo
---------------

Returns statistics about the unspent transaction output set.
Note this call may take some time.

Result:

::

	{
	  "height":n,     (numeric) The current block height (index)
	  "bestblock": "hex",   (string) the best block hash hex
	  "transactions": n,      (numeric) The number of transactions
	  "txouts": n,            (numeric) The number of output transactions
 	 "bytes_serialized": n,  (numeric) The serialized size
	  "hash_serialized": "hash",   (string) The serialized hash
	  "total_amount": x.xxx          (numeric) The total amount
	}

Examples:

::

	> komodo-cli gettxoutsetinfo 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "gettxoutsetinfo", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

height_MoM height
-----------------

``COMING SOON``

kvsearch key
------------

``COMING SOON``

kvupdate key value flags/passphrase
-----------------------------------

``COMING SOON``

minerids needs height
---------------------

``COMING SOON``

notaries height timestamp
-------------------------

``COMING SOON``

paxpending needs no args
------------------------

``DEPRECATED``

paxprice "base" "rel" height
----------------------------

``DEPRECATED``

paxprices "base" "rel" maxsamples
---------------------------------

``DEPRECATED``

txMoMproof needs a txid
-----------------------

``COMING SOON``

verifychain ( checklevel numblocks )
------------------------------------

Verifies blockchain database.

Arguments:

::

	1. checklevel   (numeric, optional, 0-4, default=3) How thorough the block verification is.
	2. numblocks    (numeric, optional, default=288, 0=all) The number of blocks to check.

Result:

::

	true|false       (boolean) Verified or not

Examples:

::

	> komodo-cli verifychain 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "verifychain", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

verifytxoutproof "proof"
------------------------

Verifies that a proof points to a transaction in a block, returning the transaction it commits to
and throwing an RPC error if the block is not in our best chain

Arguments:

::

	1. "proof"    (string, required) The hex-encoded proof generated by gettxoutproof

Result:

::

	["txid"]      (array, strings) The txid(s) which the proof commits to, or empty array if the proof is invalid


Control
=======

getinfo
-------

Returns an object containing various state info.

Result:

::

	{
	  "version": xxxxx,           (numeric) the server version
	  "protocolversion": xxxxx,   (numeric) the protocol version
	  "walletversion": xxxxx,     (numeric) the wallet version
	  "balance": xxxxxxx,         (numeric) the total Zcash balance of the wallet
	  "blocks": xxxxxx,           (numeric) the current number of blocks processed in the server
	  "timeoffset": xxxxx,        (numeric) the time offset
	  "connections": xxxxx,       (numeric) the number of connections
	  "proxy": "host:port",     (string, optional) the proxy used by the server
	  "difficulty": xxxxxx,       (numeric) the current difficulty
	  "testnet": true|false,      (boolean) if the server is using testnet or not
	  "keypoololdest": xxxxxx,    (numeric) the timestamp (seconds since GMT epoch) of the oldest pre-generated key in the key pool
	  "keypoolsize": xxxx,        (numeric) how many new keys are pre-generated
	  "unlocked_until": ttt,      (numeric) the timestamp in seconds since epoch (midnight Jan 1 1970 GMT) that the wallet is unlocked for transfers, or 0 if the wallet is locked
	  "paytxfee": x.xxxx,         (numeric) the transaction fee set in ZEC/kB
	  "relayfee": x.xxxx,         (numeric) minimum relay fee for non-free transactions in ZEC/kB
	  "errors": "..."           (string) any error messages
	}

Examples:

::

	> komodo-cli getinfo 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getinfo", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/


help ( "command" )
------------------

List all commands, or get help for a specified command.

Arguments:

::

	1. "command"     (string, optional) The command to get help on

Result:

::

	"text"     (string) The help text

.. _komodo-api-stop:

stop
----

Stop Komodo server.

Disclosure
==========

z_getpaymentdisclosure "txid" "js_index" "output_index" ("message") 
--------------------------------------------------------------------

Generate a payment disclosure for a given joinsplit output.

**EXPERIMENTAL FEATURE**

**WARNING**: Payment disclosure is currently DISABLED. This call always fails.

Arguments:

::

	1. "txid"            (string, required) 
	2. "js_index"        (string, required) 
	3. "output_index"    (string, required) 
	4. "message"         (string, optional) 

Result:

::

	"paymentdisclosure"  (string) Hex data string, with "zpd:" prefix.

Examples:

::

	> komodo-cli z_getpaymentdisclosure 96f12882450429324d5f3b48630e3168220e49ab7b0f066e5c2935a6b88bb0f2 0 0 "refund"
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "z_getpaymentdisclosure", "params": ["96f12882450429324d5f3b48630e3168220e49ab7b0f066e5c2935a6b88bb0f2", 0, 0, "refund"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/


z_validatepaymentdisclosure "paymentdisclosure"
-----------------------------------------------

Validates a payment disclosure.

**EXPERIMENTAL FEATURE**

**WARNING**: Payment disclosure is curretly DISABLED. This call always fails.

Arguments:

::

	1. "paymentdisclosure"     (string, required) Hex data string, with "zpd:" prefix.

Examples:

::

	> komodo-cli z_validatepaymentdisclosure "zpd:706462ff004c561a0447ba2ec51184e6c204..."
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "z_validatepaymentdisclosure", "params": ["zpd:706462ff004c561a0447ba2ec51184e6c204..."] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/


Generating
==========

generate numblocks
------------------

Mine blocks immediately (before the RPC call returns)

**Note**: this function can only be used on the regtest network

Arguments:

::

	1. numblocks    (numeric) How many blocks are generated immediately.

Result:

::

	[ blockhashes ]     (array) hashes of blocks generated

Examples:

Generate 11 blocks

::

	> komodo-cli generate 11


getgenerate
-----------

Return if the server is set to generate coins or not. The default is false.
It is set with the command line argument ``-gen`` (or ``komodo.conf`` setting gen)
It can also be set with the ``setgenerate`` call.

Result:

::

	true|false      (boolean) If the server is set to generate coins or not

Examples:

::
	
	> komodo-cli getgenerate 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getgenerate", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

setgenerate generate ( genproclimit )
-------------------------------------

Set 'generate' true or false to turn generation on or off.
Generation is limited to 'genproclimit' processors, -1 is unlimited.
See the getgenerate call for the current setting.

Arguments:

::

	1. generate         (boolean, required) Set to true to turn on generation, off to turn off.
	2. genproclimit     (numeric, optional) Set the processor limit for when generation is on. Can be -1 for unlimited.

Examples:

Set the generation on with a limit of one processor

::

	> komodo-cli setgenerate true 1

Check the setting

::

	> komodo-cli getgenerate 

Turn off generation

::

	> komodo-cli setgenerate false

Using json rpc

::

	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "setgenerate", "params": [true, 1] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/


Mining
======

getblocksubsidy height
----------------------

Returns block subsidy reward, taking into account the mining slow start and the founders reward, of block at index provided.

Arguments:

::

	1. height         (numeric, optional) The block height.  If not provided, defaults to the current height of the chain.

Result:

::

	{
	  "miner" : x.xxx           (numeric) The mining reward amount in KMD.
	}

Examples:

::

	> komodo-cli getblocksubsidy 1000
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getblockubsidy", "params": [1000] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getblocktemplate ( "jsonrequestobject" )
----------------------------------------

If the request parameters include a ``mode`` key, that is used to explicitly select between the default 'template' request or a 'proposal'.
It returns data needed to construct a block to work on.
See https://en.bitcoin.it/wiki/BIP_0022 for full specification.

Arguments:

::

	1. "jsonrequestobject"       (string, optional) A json object in the following spec
	     {
	       "mode":"template"    (string, optional) This must be set to "template" or omitted
	       "capabilities":[       (array, optional) A list of strings
	           "support"           (string) client side supported feature, 'longpoll', 'coinbasetxn', 'coinbasevalue', 'proposal', 'serverlist', 'workid'
	           ,...
	         ]
	     }


Result:

::

	{
	  "version" : n,                    (numeric) The block version
	  "previousblockhash" : "xxxx",    (string) The hash of current highest block
	  "transactions" : [                (array) contents of non-coinbase transactions that should be included in the next block
	      {
	         "data" : "xxxx",          (string) transaction data encoded in hexadecimal (byte-for-byte)
	         "hash" : "xxxx",          (string) hash/id encoded in little-endian hexadecimal
	         "depends" : [              (array) array of numbers 
	             n                        (numeric) transactions before this one (by 1-based index in 'transactions' list) that must be present in the final block if this one is
	             ,...
	         ],
	         "fee": n,                   (numeric) difference in value between transaction inputs and outputs (in Satoshis); for coinbase transactions, this is a negative Number of the total collected block fees (ie, not including the block subsidy); if key is not present, fee is unknown and clients MUST NOT assume there isn't one
	         "sigops" : n,               (numeric) total number of SigOps, as counted for purposes of block limits; if key is not present, sigop count is unknown and clients MUST NOT assume there aren't any
	         "required" : true|false     (boolean) if provided and true, this transaction must be in the final block
	      }
	      ,...
	  ],
	  "coinbasetxn" : { ...},           (json object) information for coinbase transaction
	  "target" : "xxxx",               (string) The hash target
	  "mintime" : xxx,                   (numeric) The minimum timestamp appropriate for next block time in seconds since epoch (Jan 1 1970 GMT)
	  "mutable" : [                      (array of string) list of ways the block template may be changed 
	     "value"                         (string) A way the block template may be changed, e.g. 'time', 'transactions', 'prevblock'
	     ,...
	  ],
	  "noncerange" : "00000000ffffffff",   (string) A range of valid nonces
	  "sigoplimit" : n,                 (numeric) limit of sigops in blocks
	  "sizelimit" : n,                  (numeric) limit of block size
	  "curtime" : ttt,                  (numeric) current timestamp in seconds since epoch (Jan 1 1970 GMT)
	  "bits" : "xxx",                 (string) compressed target of next block
	  "height" : n                      (numeric) The height of the next block
	}

Examples:

::

	> komodo-cli getblocktemplate 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getblocktemplate", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getlocalsolps
-------------

Returns the average local solutions per second since this node was started.
This is the same information shown on the metrics screen (if enabled).

Result:

	xxx.xxxxx     (numeric) Solutions per second average

Examples:

::

	> komodo-cli getlocalsolps 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getlocalsolps", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getmininginfo
-------------

Returns a json object containing mining-related information.

Result:

::

	{
	  "blocks": nnn,             (numeric) The current block
	  "currentblocksize": nnn,   (numeric) The last block size
	  "currentblocktx": nnn,     (numeric) The last block transaction
	  "difficulty": xxx.xxxxx    (numeric) The current difficulty
	  "errors": "..."          (string) Current errors
	  "generate": true|false     (boolean) If the generation is on or off (see getgenerate or setgenerate calls)
	  "genproclimit": n          (numeric) The processor limit for generation. -1 if no generation. (see getgenerate or setgenerate calls)
	  "localsolps": xxx.xxxxx    (numeric) The average local solution rate in Sol/s since this node was started
	  "networksolps": x          (numeric) The estimated network solution rate in Sol/s
	  "pooledtx": n              (numeric) The size of the mem pool
	  "testnet": true|false      (boolean) If using testnet or not
	  "chain": "xxxx",         (string) current network name as defined in BIP70 (main, test, regtest)
	}

Examples:

::

	> komodo-cli getmininginfo 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getmininginfo", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getnetworkhashps ( blocks height )
----------------------------------

**DEPRECATED** - left for backwards-compatibility. Use getnetworksolps instead.

Returns the estimated network solutions per second based on the last n blocks.
Pass in [blocks] to override # of blocks, -1 specifies over difficulty averaging window.
Pass in [height] to estimate the network speed at the time when a certain block was found.

Arguments:

::

	1. blocks     (numeric, optional, default=120) The number of blocks, or -1 for blocks over difficulty averaging window.
	2. height     (numeric, optional, default=-1) To estimate at the time of the given height.

Result:

::

	x             (numeric) Solutions per second estimated

Examples:

::

	> komodo-cli getnetworkhashps 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getnetworkhashps", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getnetworksolps ( blocks height )
---------------------------------

Returns the estimated network solutions per second based on the last n blocks.
Pass in [blocks] to override # of blocks, -1 specifies over difficulty averaging window.
Pass in [height] to estimate the network speed at the time when a certain block was found.

Arguments:

::

	1. blocks     (numeric, optional, default=120) The number of blocks, or -1 for blocks over difficulty averaging window.
	2. height     (numeric, optional, default=-1) To estimate at the time of the given height.

Result:

::

	x             (numeric) Solutions per second estimated

Examples:

::

	> komodo-cli getnetworksolps 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getnetworksolps", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

prioritisetransaction <txid> <priority delta> <fee delta>
---------------------------------------------------------

Accepts the transaction into mined blocks at a higher (or lower) priority

Arguments:

::

	1. "txid"       (string, required) The transaction id.
	2. priority delta (numeric, required) The priority to add or subtract.
                  The transaction selection algorithm considers the tx as it would have a higher priority.
                  (priority of a transaction is calculated: coinage * value_in_satoshis / txsize) 
	3. fee delta      (numeric, required) The fee value (in satoshis) to add (or subtract, if negative).
                  The fee is not actually paid, only the algorithm for selecting transactions into a block
                  considers the transaction as it would have paid a higher (or lower) fee.

Result:

::

	true              (boolean) Returns true

Examples:

::

	> komodo-cli prioritisetransaction "txid" 0.0 10000
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "prioritisetransaction", "params": ["txid", 0.0, 10000] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

submitblock "hexdata" ( "jsonparametersobject" )
------------------------------------------------

Attempts to submit new block to network.
The 'jsonparametersobject' parameter is currently ignored.
See https://en.bitcoin.it/wiki/BIP_0022 for full specification.

Arguments:

::

	1. "hexdata"    (string, required) the hex-encoded block data to submit
	2. "jsonparametersobject"     (string, optional) object of optional parameters

::

	    {
	      "workid" : "id"    (string, optional) if the server provided a workid, it MUST be included with submissions
	    }

Result:

::

	"duplicate" - node already has valid copy of block
	"duplicate-invalid" - node already has block, but it is invalid
	"duplicate-inconclusive" - node already has block but has not validated it
	"inconclusive" - node has not validated the block, it may not be on the node's current best chain
	"rejected" - block was rejected as invalid

For more information on submitblock parameters and results, see: https://github.com/bitcoin/bips/blob/master/bip-0022.mediawiki#block-submission

Examples:

::

	> komodo-cli submitblock "mydata"
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "submitblock", "params": ["mydata"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/


Network
=======

addnode "node" "add|remove|onetry"
----------------------------------

Attempts add or remove a node from the addnode list.
Or try a connection to a node once.

Arguments:
::

	1. "node"     (string, required) The node (see getpeerinfo for nodes)
	2. "command"  (string, required) 'add' to add a node to the list, 'remove' to remove a node from the list, 'onetry' to try a connection to the node once

Examples:

::

	> komodo-cli addnode "192.168.0.6:8233" "onetry"
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "addnode", "params": ["192.168.0.6:8233", "onetry"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

clearbanned
-----------

Clear all banned IPs.

Examples:

::

	> komodo-cli clearbanned 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "clearbanned", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

disconnectnode "node" 
----------------------

Immediately disconnects from the specified node.

Arguments:

::

	1."node"     (string, required) The node (see getpeerinfo for nodes)

Examples:

::

	> komodo-cli disconnectnode "192.168.0.6:8233"
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "disconnectnode", "params": ["192.168.0.6:8233"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getaddednodeinfo dns ( "node" )
-------------------------------

Returns information about the given added node, or all added nodes
(note that onetry addnodes are not listed here)
If dns is false, only a list of added nodes will be provided,
otherwise connected information will also be available.

Arguments:

::

	1. dns        (boolean, required) If false, only a list of added nodes will be provided, otherwise connected information will also be available.
	2. "node"   (string, optional) If provided, return information about this specific node, otherwise all nodes are returned.

Result:

::

	[
	  {
	    "addednode" : "192.168.0.201",   (string) The node ip address
	    "connected" : true|false,          (boolean) If connected
	    "addresses" : [
	       {
	         "address" : "192.168.0.201:8233",  (string) The Zcash server host and port
	         "connected" : "outbound"           (string) connection, inbound or outbound
	       }
	       ,...
	     ]
	  }
	  ,...
	]

Examples:

::

	> komodo-cli getaddednodeinfo true
	> komodo-cli getaddednodeinfo true "192.168.0.201"
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getaddednodeinfo", "params": [true, "192.168.0.201"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getconnectioncount
------------------

Returns the number of connections to other nodes.

Result:

::

	n          (numeric) The connection count

Examples:

::

	> komodo-cli getconnectioncount 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getconnectioncount", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getdeprecationinfo
------------------

Returns an object containing current version and deprecation block height. Applicable only on mainnet.

Result:

::

	{
	  "version": xxxxx,                      (numeric) the server version
	  "subversion": "/MagicBean:x.y.z[-v]/",     (string) the server subversion string
	  "deprecationheight": xxxxx,            (numeric) the block height at which this version will deprecate and shut down (unless -disabledeprecation is set)
	}

Examples:

::

	> komodo-cli getdeprecationinfo 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getdeprecationinfo", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getnettotals
------------

Returns information about network traffic, including bytes in, bytes out,
and current time.

Result:

::

	{
	  "totalbytesrecv": n,   (numeric) Total bytes received
	  "totalbytessent": n,   (numeric) Total bytes sent
	  "timemillis": t        (numeric) Total cpu time
	}

Examples:

::

	> komodo-cli getnettotals 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getnettotals", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getnetworkinfo
--------------

Returns an object containing various state info regarding P2P networking.

Result:

::

	{
	  "version": xxxxx,                      (numeric) the server version
	  "subversion": "/MagicBean:x.y.z[-v]/",     (string) the server subversion string
	  "protocolversion": xxxxx,              (numeric) the protocol version
	  "localservices": "xxxxxxxxxxxxxxxx", (string) the services we offer to the network
	  "timeoffset": xxxxx,                   (numeric) the time offset
	  "connections": xxxxx,                  (numeric) the number of connections
	  "networks": [                          (array) information per network
	  {
	    "name": "xxx",                     (string) network (ipv4, ipv6 or onion)
	    "limited": true|false,               (boolean) is the network limited using -onlynet?
	    "reachable": true|false,             (boolean) is the network reachable?
	    "proxy": "host:port"               (string) the proxy that is used for this network, or empty if none
	  }
	  ,...
	  ],
	  "relayfee": x.xxxxxxxx,                (numeric) minimum relay fee for non-free transactions in ZEC/kB
	  "localaddresses": [                    (array) list of local addresses
	  {
	    "address": "xxxx",                 (string) network address
	    "port": xxx,                         (numeric) network port
	    "score": xxx                         (numeric) relative score
	  }
	  ,...
	  ]
	  "warnings": "..."                    (string) any network warnings (such as alert messages) 
	}

Examples:

::

	> komodo-cli getnetworkinfo 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getnetworkinfo", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getpeerinfo
-----------

Returns data about each connected network node as a json array of objects.

Result:

::

	[
	  {
	    "id": n,                   (numeric) Peer index
	    "addr":"host:port",      (string) The ip address and port of the peer
	    "addrlocal":"ip:port",   (string) local address
	    "services":"xxxxxxxxxxxxxxxx",   (string) The services offered
	    "lastsend": ttt,           (numeric) The time in seconds since epoch (Jan 1 1970 GMT) of the last send
	    "lastrecv": ttt,           (numeric) The time in seconds since epoch (Jan 1 1970 GMT) of the last receive
	    "bytessent": n,            (numeric) The total bytes sent
	    "bytesrecv": n,            (numeric) The total bytes received
	    "conntime": ttt,           (numeric) The connection time in seconds since epoch (Jan 1 1970 GMT)
	    "timeoffset": ttt,         (numeric) The time offset in seconds
	    "pingtime": n,             (numeric) ping time
	    "pingwait": n,             (numeric) ping wait
	    "version": v,              (numeric) The peer version, such as 170002
	    "subver": "/MagicBean:x.y.z[-v]/",  (string) The string version
	    "inbound": true|false,     (boolean) Inbound (true) or Outbound (false)
	    "startingheight": n,       (numeric) The starting height (block) of the peer
	    "banscore": n,             (numeric) The ban score
	    "synced_headers": n,       (numeric) The last header we have in common with this peer
	    "synced_blocks": n,        (numeric) The last block we have in common with this peer
	    "inflight": [
	       n,                        (numeric) The heights of blocks we're currently asking from this peer
	       ...
	    ]
	  }
	  ,...
	]

Examples:

::

	> komodo-cli getpeerinfo 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getpeerinfo", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

listbanned
----------

List all banned IPs/Subnets.

Examples:

::

	> komodo-cli listbanned 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listbanned", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

ping
----

Requests that a ping be sent to all other nodes, to measure ping time.
Results provided in getpeerinfo, pingtime and pingwait fields are decimal seconds.
Ping command is handled in queue with all other commands, so it measures processing backlog, not just network ping.

Examples:

::

	> komodo-cli ping 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "ping", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

setban "ip(/netmask)" "add|remove" (bantime) (absolute)
-------------------------------------------------------

Attempts add or remove a IP/Subnet from the banned list.

Arguments:

::

	1. "ip(/netmask)" (string, required) The IP/Subnet (see getpeerinfo for nodes ip) with a optional netmask (default is /32 = single ip)
	2. "command"      (string, required) 'add' to add a IP/Subnet to the list, 'remove' to remove a IP/Subnet from the list
	3. "bantime"      (numeric, optional) time in seconds how long (or until when if [absolute] is set) the ip is banned (0 or empty means using the default time of 24h which can also be overwritten by the -bantime startup argument)
	4. "absolute"     (boolean, optional) If set, the bantime must be a absolute timestamp in seconds since epoch (Jan 1 1970 GMT)

Examples:

	> komodo-cli setban "192.168.0.6" "add" 86400
	> komodo-cli setban "192.168.0.0/24" "add"
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "setban", "params": ["192.168.0.6", "add" 86400] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

Rawtransactions
===============

createrawtransaction [{"txid":"id","vout":n},...] {"address":amount,...}
------------------------------------------------------------------------

Create a transaction spending the given inputs and sending to the given addresses.
Returns hex-encoded raw transaction.
*Note that the transaction's inputs are not signed, and
it is not stored in the wallet or transmitted to the network.*

Arguments:

::

	1. "transactions"        (string, required) A json array of json objects
	     [
	       {
	         "txid":"id",  (string, required) The transaction id
	         "vout":n        (numeric, required) The output number
	       }
	       ,...
	     ]
	2. "addresses"           (string, required) a json object with addresses as keys and amounts as values
	    {
	      "address": x.xxx   (numeric, required) The key is the Zcash address, the value is the ZEC amount
	      ,...
	    }

Result:

::

	"transaction"            (string) hex string of the transaction

Examples:

	> komodo-cli createrawtransaction "[{\"txid\":\"myid\",\"vout\":0}]" "{\"address\":0.01}"
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "createrawtransaction", "params": ["[{\"txid\":\"myid\",\"vout\":0}]", "{\"address\":0.01}"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

decoderawtransaction "hexstring"
--------------------------------

Return a JSON object representing the serialized, hex-encoded transaction.

Arguments:

::

	1. "hex"      (string, required) The transaction hex string

Result:

::

	{
	  "txid" : "id",        (string) The transaction id
	  "overwintered" : bool   (boolean) The Overwintered flag
	  "version" : n,          (numeric) The version
	  "versiongroupid": "hex"   (string, optional) The version group id (Overwintered txs)
	  "locktime" : ttt,       (numeric) The lock time
	  "expiryheight" : n,     (numeric, optional) Last valid block height for mining transaction (Overwintered txs)
	  "vin" : [               (array of json objects)
	     {
	       "txid": "id",    (string) The transaction id
	       "vout": n,         (numeric) The output number
	       "scriptSig": {     (json object) The script
	         "asm": "asm",  (string) asm
	         "hex": "hex"   (string) hex
	       },
	       "sequence": n     (numeric) The script sequence number
	     }
	     ,...
	  ],
	  "vout" : [             (array of json objects)
	     {
	       "value" : x.xxx,            (numeric) The value in ZEC
	       "n" : n,                    (numeric) index
	       "scriptPubKey" : {          (json object)
	         "asm" : "asm",          (string) the asm
	         "hex" : "hex",          (string) the hex
	         "reqSigs" : n,            (numeric) The required sigs
	         "type" : "pubkeyhash",  (string) The type, eg 'pubkeyhash'
	         "addresses" : [           (json array of string)
	           "t12tvKAXCxZjSmdNbao16dKXC8tRWfcF5oc"   (string) zcash address
	           ,...
	         ]
	       }
	     }
	     ,...
	  ],
	  "vjoinsplit" : [        (array of json objects, only for version >= 2)
	     {
	       "vpub_old" : x.xxx,         (numeric) public input value in KMD
	       "vpub_new" : x.xxx,         (numeric) public output value in KMD
	       "anchor" : "hex",         (string) the anchor
	       "nullifiers" : [            (json array of string)
	         "hex"                     (string) input note nullifier
	         ,...
	       ],
	       "commitments" : [           (json array of string)
	         "hex"                     (string) output note commitment
	         ,...
	       ],
	       "onetimePubKey" : "hex",  (string) the onetime public key used to encrypt the ciphertexts
	       "randomSeed" : "hex",     (string) the random seed
	       "macs" : [                  (json array of string)
	         "hex"                     (string) input note MAC
	         ,...
	       ],
	       "proof" : "hex",          (string) the zero-knowledge proof
	       "ciphertexts" : [           (json array of string)
	         "hex"                     (string) output note ciphertext
	         ,...
	       ]
	     }
	     ,...
	  ],
	}
	
Examples:

::

	> komodo-cli decoderawtransaction "hexstring"
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "decoderawtransaction", "params": ["hexstring"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

decodescript "hex"
------------------

Decode a hex-encoded script.

Arguments:

::

	1. "hex"     (string) the hex encoded script

Result:

::

	{
	  "asm":"asm",   (string) Script public key
	  "hex":"hex",   (string) hex encoded public key
	  "type":"type", (string) The output type
	  "reqSigs": n,    (numeric) The required signatures
	  "addresses": [   (json array of string)
	     "address"     (string) Zcash address
	     ,...
	  ],
	  "p2sh","address" (string) script address
	}

Examples:

::

	> komodo-cli decodescript "hexstring"
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "decodescript", "params": ["hexstring"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

fundrawtransaction "hexstring"
------------------------------

Add inputs to a transaction until it has enough in value to meet its out value.
This will not modify existing inputs, and will add one change output to the outputs.
Note that inputs which were signed may need to be resigned after completion since in/outputs have been added.
The inputs added will not be signed, use signrawtransaction for that.

Arguments:

::

	1. "hexstring"    (string, required) The hex string of the raw transaction

Result:

::

	{
	  "hex":       "value", (string)  The resulting raw transaction (hex-encoded string)
	  "fee":       n,         (numeric) The fee added to the transaction
	  "changepos": n          (numeric) The position of the added change output, or -1
	}
	"hex"             

Examples:

Create a transaction with no inputs

::

	> komodo-cli createrawtransaction "[]" "{\"myaddress\":0.01}"

Add sufficient unsigned inputs to meet the output value

::

	> komodo-cli fundrawtransaction "rawtransactionhex"

Sign the transaction

::

	> komodo-cli signrawtransaction "fundedtransactionhex"

Send the transaction

::

	> komodo-cli sendrawtransaction "signedtransactionhex"

getrawtransaction "txid" ( verbose )
------------------------------------

**NOTE**: By default this function only works sometimes. This is when the tx is in the mempool
or there is an unspent output in the utxo for this transaction. To make it always work,
you need to maintain a transaction index, using the ``-txindex`` command line option.

Return the raw transaction data.

If ``verbose=0``, returns a string that is serialized, hex-encoded data for 'txid'.
If ``verbose`` is non-zero, returns an Object with information about 'txid'.

Arguments:

::

	1. "txid"      (string, required) The transaction id
	2. verbose       (numeric, optional, default=0) If 0, return a string, other return a json object

Result (if verbose is not set or set to 0):

::

	"data"      (string) The serialized, hex-encoded data for 'txid'

Result (if verbose > 0):

::

	{
	  "hex" : "data",       (string) The serialized, hex-encoded data for 'txid'
	  "txid" : "id",        (string) The transaction id (same as provided)
	  "version" : n,          (numeric) The version
	  "locktime" : ttt,       (numeric) The lock time
	  "expiryheight" : ttt,   (numeric, optional) The block height after which the transaction expires
	  "vin" : [               (array of json objects)
	     {
	       "txid": "id",    (string) The transaction id
	       "vout": n,         (numeric) 
	       "scriptSig": {     (json object) The script
	         "asm": "asm",  (string) asm
	         "hex": "hex"   (string) hex
	       },
	       "sequence": n      (numeric) The script sequence number
	     }
	     ,...
	  ],
	  "vout" : [              (array of json objects)
	     {
	       "value" : x.xxx,            (numeric) The value in ZEC
	       "n" : n,                    (numeric) index
	       "scriptPubKey" : {          (json object)
	         "asm" : "asm",          (string) the asm
	         "hex" : "hex",          (string) the hex
	         "reqSigs" : n,            (numeric) The required sigs
	         "type" : "pubkeyhash",  (string) The type, eg 'pubkeyhash'
    	     "addresses" : [           (json array of string)
    	       "zcashaddress"          (string) Zcash address
    	       ,...
    	     ]
    	   }
    	 }
    	 ,...
	  ],	
	  "vjoinsplit" : [        (array of json objects, only for version >= 2)
	     {
	       "vpub_old" : x.xxx,         (numeric) public input value in KMD
	       "vpub_new" : x.xxx,         (numeric) public output value in KMD
	       "anchor" : "hex",         (string) the anchor
	       "nullifiers" : [            (json array of string)
	         "hex"                     (string) input note nullifier
	         ,...
	       ],
	       "commitments" : [           (json array of string)
	         "hex"                     (string) output note commitment
	         ,...
	       ],
	       "onetimePubKey" : "hex",  (string) the onetime public key used to encrypt the ciphertexts
	       "randomSeed" : "hex",     (string) the random seed
	       "macs" : [                  (json array of string)
	         "hex"                     (string) input note MAC
	         ,...
	       ],
	       "proof" : "hex",          (string) the zero-knowledge proof
	       "ciphertexts" : [           (json array of string)
	         "hex"                     (string) output note ciphertext
	         ,...
	       ]
	     }
	     ,...
	  ],
	  "blockhash" : "hash",   (string) the block hash
	  "confirmations" : n,      (numeric) The confirmations
	  "time" : ttt,             (numeric) The transaction time in seconds since epoch (Jan 1 1970 GMT)
	  "blocktime" : ttt         (numeric) The block time in seconds since epoch (Jan 1 1970 GMT)
	}

Examples:

::

	> komodo-cli getrawtransaction "mytxid"
	> komodo-cli getrawtransaction "mytxid" 1
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getrawtransaction", "params": ["mytxid", 1] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

sendrawtransaction "hexstring" ( allowhighfees )
------------------------------------------------

Submits raw transaction (serialized, hex-encoded) to local node and network.

Also see createrawtransaction and signrawtransaction calls.

Arguments:

::

	1. "hexstring"    (string, required) The hex string of the raw transaction)
	2. allowhighfees    (boolean, optional, default=false) Allow high fees

Result:

::

	"hex"             (string) The transaction hash in hex

Examples:

Create a transaction

::

	> komodo-cli createrawtransaction "[{\"txid\" : \"mytxid\",\"vout\":0}]" "{\"myaddress\":0.01}"

Sign the transaction, and get back the hex

::

	> komodo-cli signrawtransaction "myhex"

Send the transaction (signed hex)

::

	> komodo-cli sendrawtransaction "signedhex"

As a json rpc call

::

	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "sendrawtransaction", "params": ["signedhex"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/


signrawtransaction "hexstring" ( [{"txid":"id","vout":n,"scriptPubKey":"hex","redeemScript":"hex"},...] ["privatekey1",...] sighashtype )
-----------------------------------------------------------------------------------------------------------------------------------------

Sign inputs for raw transaction (serialized, hex-encoded).
The second optional argument (may be null) is an array of previous transaction outputs that
this transaction depends on but may not yet be in the block chain.
The third optional argument (may be null) is an array of base58-encoded private
keys that, if given, will be the only keys used to sign the transaction.


Arguments:

::

	1. "hexstring"     (string, required) The transaction hex string
	2. "prevtxs"       (string, optional) An json array of previous dependent transaction outputs
	     [               (json array of json objects, or 'null' if none provided)
	       {
	         "txid":"id",             (string, required) The transaction id
	         "vout":n,                  (numeric, required) The output number
	         "scriptPubKey": "hex",   (string, required) script key
	         "redeemScript": "hex",   (string, required for P2SH) redeem script
	         "amount": value            (numeric, required) The amount spent
	       }
	       ,...
	    ]
	3. "privatekeys"     (string, optional) A json array of base58-encoded private keys for signing
	    [                  (json array of strings, or 'null' if none provided)
	      "privatekey"   (string) private key in base58-encoding
	      ,...
	    ]
	4. "sighashtype"     (string, optional, default=ALL) The signature hash type. Must be one of
	       "ALL"
	       "NONE"
	       "SINGLE"
	       "ALL|ANYONECANPAY"
	       "NONE|ANYONECANPAY"
	       "SINGLE|ANYONECANPAY"
	
Result:

::

	{
	  "hex" : "value",           (string) The hex-encoded raw transaction with signature(s)
	  "complete" : true|false,   (boolean) If the transaction has a complete set of signatures
	  "errors" : [                 (json array of objects) Script verification errors (if there are any)
	    {
	      "txid" : "hash",           (string) The hash of the referenced, previous transaction
	      "vout" : n,                (numeric) The index of the output to spent and used as input
	      "scriptSig" : "hex",       (string) The hex-encoded signature script
	      "sequence" : n,            (numeric) Script sequence number
	      "error" : "text"           (string) Verification or signing error related to the input
	    }
	    ,...
	  ]
	}

Examples:

::

	> komodo-cli signrawtransaction "myhex"
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "signrawtransaction", "params": ["myhex"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

Util
====

createmultisig nrequired ["key",...]
------------------------------------

Creates a multi-signature address with n signature of m keys required.
It returns a json object with the address and redeemScript.

Arguments:

::

	1. nrequired      (numeric, required) The number of required signatures out of the n keys or addresses.
	2. "keys"       (string, required) A json array of keys which are Zcash addresses or hex-encoded public keys

::

     [
       "key"    (string) Zcash address or hex-encoded public key
       ,...
     ]

Result:

::

	{
	  "address":"multisigaddress",  (string) The value of the new multisig address.
	  "redeemScript":"script"       (string) The string value of the hex-encoded redemption script.
	}

Examples:

Create a multisig address from 2 addresses

::

	> komodo-cli createmultisig 2 "[\"t16sSauSf5pF2UkUwvKGq4qjNRzBZYqgEL5\",\"t171sgjn4YtPu27adkKGrdDwzRTxnRkBfKV\"]"

As a json rpc call

::

	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "createmultisig", "params": [2, "[\"t16sSauSf5pF2UkUwvKGq4qjNRzBZYqgEL5\",\"t171sgjn4YtPu27adkKGrdDwzRTxnRkBfKV\"]"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

estimatefee nblocks
-------------------

Estimates the approximate fee per kilobyte
needed for a transaction to begin confirmation
within nblocks blocks.

Arguments:

::

	1. nblocks     (numeric)

Result:

::

	n :    (numeric) estimated fee-per-kilobyte

	-1.0 is returned if not enough transactions and blocks have been observed to make an estimate.

Example:

::

	> komodo-cli estimatefee 6

estimatepriority nblocks
------------------------

Estimates the approximate priority
a zero-fee transaction needs to begin confirmation
within nblocks blocks.

Arguments:

::

	1. nblocks     (numeric)

Result:

::

	n :    (numeric) estimated priority

	-1.0 is returned if not enough transactions and blocks have been observed to make an estimate.

Example:

::

	> komodo-cli estimatepriority 6

invalidateblock "hash"
----------------------

Permanently marks a block as invalid, as if it violated a consensus rule.

Arguments:

::

	1. hash   (string, required) the hash of the block to mark as invalid

Result:

Examples:

::

	> komodo-cli invalidateblock "blockhash"
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "invalidateblock", "params": ["blockhash"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

jumblr_deposit "depositaddress"
-------------------------------

For usage look at :doc:`using-JUMBLR`

jumblr_pause
------------

For usage look at :doc:`using-JUMBLR`

jumblr_resume
-------------

For usage look at :doc:`using-JUMBLR`

jumblr_secret "secretaddress"
-----------------------------

For usage look at :doc:`using-JUMBLR`

reconsiderblock "hash"
----------------------

Removes invalidity status of a block and its descendants, reconsider them for activation.
This can be used to undo the effects of invalidateblock.

Arguments:

::

	1. hash   (string, required) the hash of the block to reconsider

Result:

Examples:

::

	> komodo-cli reconsiderblock "blockhash"
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "reconsiderblock", "params": ["blockhash"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

validateaddress "komodoaddress"
-------------------------------

Return information about the given Zcash address.

Arguments:

::

	1. "zcashaddress"     (string, required) The Zcash address to validate

Result:

::

	{
	  "isvalid" : true|false,         (boolean) If the address is valid or not. If not, this is the only property returned.
	  "address" : "zcashaddress",   (string) The Zcash address validated
	  "scriptPubKey" : "hex",       (string) The hex encoded scriptPubKey generated by the address
	  "ismine" : true|false,          (boolean) If the address is yours or not
	  "isscript" : true|false,        (boolean) If the key is a script
	  "pubkey" : "publickeyhex",    (string) The hex value of the raw public key
	  "iscompressed" : true|false,    (boolean) If the address is compressed
	  "account" : "account"         (string) DEPRECATED. The account associated with the address, "" is the default account
	}

Examples:

::

	> komodo-cli validateaddress "1PSSGeFHDnKNxiEyFrD1wcEaHr9hrQDDWc"
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "validateaddress", "params": ["1PSSGeFHDnKNxiEyFrD1wcEaHr9hrQDDWc"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

verifymessage "komodoaddress" "signature" "message"
---------------------------------------------------

Verify a signed message

Arguments:

::

	1. "zcashaddress"    (string, required) The Zcash address to use for the signature.
	2. "signature"       (string, required) The signature provided by the signer in base 64 encoding (see signmessage).
	3. "message"         (string, required) The message that was signed.

Result:

::

	true|false   (boolean) If the signature is verified or not.

Examples:

Unlock the wallet for 30 seconds

::

	> komodo-cli walletpassphrase "mypassphrase" 30

Create the signature

::

	> komodo-cli signmessage "t14oHp2v54vfmdgQ3v3SNuQga8JKHTNi2a1" "my message"

Verify the signature

::

	> komodo-cli verifymessage "t14oHp2v54vfmdgQ3v3SNuQga8JKHTNi2a1" "signature" "my message"

As json rpc

::

	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "verifymessage", "params": ["t14oHp2v54vfmdgQ3v3SNuQga8JKHTNi2a1", "signature", "my message"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

z_validateaddress "zaddr"
-------------------------

Return information about the given z address.

Arguments:

::

	1. "zaddr"     (string, required) The z address to validate

Result:

::

	{
	  "isvalid" : true|false,      (boolean) If the address is valid or not. If not, this is the only property returned.
	  "address" : "zaddr",         (string) The z address validated
	  "ismine" : true|false,       (boolean) If the address is yours or not
	  "payingkey" : "hex",         (string) The hex value of the paying key, a_pk
	  "transmissionkey" : "hex",   (string) The hex value of the transmission key, pk_enc
	}

Examples:

::

	> komodo-cli z_validateaddress "zcWsmqT4X2V4jgxbgiCzyrAfRT1vi1F4sn7M5Pkh66izzw8Uk7LBGAH3DtcSMJeUb2pi3W4SQF8LMKkU2cUuVP68yAGcomL"
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "z_validateaddress", "params": ["zcWsmqT4X2V4jgxbgiCzyrAfRT1vi1F4sn7M5Pkh66izzw8Uk7LBGAH3DtcSMJeUb2pi3W4SQF8LMKkU2cUuVP68yAGcomL"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/


Wallet
======

addmultisigaddress nrequired ["key",...] ( "account" )
------------------------------------------------------

Add a nrequired-to-sign multisignature address to the wallet.
Each key is a Komodo address or hex-encoded public key.
If 'account' is specified (DEPRECATED), assign address to that account.

Arguments:

::

	1. nrequired        (numeric, required) The number of required signatures out of the n keys or addresses.
	2. "keysobject"   (string, required) A json array of Zcash addresses or hex-encoded public keys
	     [
	       "address"  (string) Zcash address or hex-encoded public key
	       ...,
	     ]
	3. "account"      (string, optional) DEPRECATED. If provided, MUST be set to the empty string "" to represent the default account. Passing any other string will result in an error.

Result:

::

	"zcashaddress"  (string) A Zcash address associated with the keys.

Examples:

Add a multisig address from 2 addresses

::

	> komodo-cli addmultisigaddress 2 "[\"t16sSauSf5pF2UkUwvKGq4qjNRzBZYqgEL5\",\"t171sgjn4YtPu27adkKGrdDwzRTxnRkBfKV\"]"

As json rpc call

::

	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "addmultisigaddress", "params": [2, "[\"t16sSauSf5pF2UkUwvKGq4qjNRzBZYqgEL5\",\"t171sgjn4YtPu27adkKGrdDwzRTxnRkBfKV\"]"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

backupwallet "destination"
--------------------------

Safely copies wallet.dat to destination filename

Arguments:

::

	1. "destination"   (string, required) The destination filename, saved in the directory set by -exportdir option.

Result:

::

	"path"             (string) The full path of the destination file

Examples:

::

	> komodo-cli backupwallet "backupdata"
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "backupwallet", "params": ["backupdata"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

dumpprivkey "komodoaddress"
---------------------------

Reveals the private key corresponding to 'komodoaddress'.
Then the importprivkey can be used with this output

Arguments:

::

	1. "zcashaddress"   (string, required) The zcash address for the private key

Result:

::

	"key"                (string) The private key

Examples:

::

	> komodo-cli dumpprivkey "myaddress"
	> komodo-cli importprivkey "mykey"
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "dumpprivkey", "params": ["myaddress"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/


dumpwallet "filename"
---------------------

Dumps taddr wallet keys in a human-readable format.  Overwriting an existing file is not permitted.

Arguments:

::

	1. "filename"    (string, required) The filename, saved in folder set by zcashd -exportdir option

Result:

::

	"path"           (string) The full path of the destination file

Examples:

::

	> komodo-cli dumpwallet "test"
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "dumpwallet", "params": ["test"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

encryptwallet "passphrase"
--------------------------

**WARNING**: Wallet encryption is **DISABLED**. This call always fails.

Encrypts the wallet with ``passphrase``. This is for first time encryption.
After this, any calls that interact with private keys such as sending or signing 
will require the passphrase to be set prior the making these calls.
Use the ``walletpassphrase`` call for this, and then ``walletlock`` call.
If the wallet is already encrypted, use the ``walletpassphrasechange`` call.
Note that this will shutdown the server.

Arguments:

::

	1. "passphrase"    (string) The pass phrase to encrypt the wallet with. It must be at least 1 character, but should be long.

Examples:

Encrypt you wallet

::

	> komodo-cli encryptwallet "my pass phrase"

Now set the passphrase to use the wallet, such as for signing or sending Zcash

::

	> komodo-cli walletpassphrase "my pass phrase"

Now we can so something like sign

::

	> komodo-cli signmessage "zcashaddress" "test message"

Now lock the wallet again by removing the passphrase

::

	> komodo-cli walletlock 

As a json rpc call

::

	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "encryptwallet", "params": ["my pass phrase"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/


getaccount "KMD_address"
------------------------

**DEPRECATED**. Returns the account associated with the given address.

Arguments:

1. "komodoaddress"  (string, required) The Komodo address for account lookup.

Result:

::

	"accountname"        (string) the account address

Examples:

::

	> komodo-cli getaccount "t14oHp2v54vfmdgQ3v3SNuQga8JKHTNi2a1"
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getaccount", "params": ["t14oHp2v54vfmdgQ3v3SNuQga8JKHTNi2a1"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getaccountaddress "account"
---------------------------

**DEPRECATED**. Returns the current Komodo address for receiving payments to this account.

Arguments:

::

	1. "account"       (string, required) MUST be set to the empty string "" to represent the default account. Passing any other string will result in an error.

Result:

	"komodoaddress"   (string) The account Komodo address

Examples:

::

	> komodo-cli getaccountaddress 
	> komodo-cli getaccountaddress ""
> komodo-cli getaccountaddress "myaccount"
> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getaccountaddress", "params": ["myaccount"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getaddressesbyaccount "account"
-------------------------------

**DEPRECATED**. Returns the list of addresses for the given account.

Arguments:

::

	1. "account"  (string, required) MUST be set to the empty string "" to represent the default account. Passing any other string will result in an error.

Result:

::

	[                     (json array of string)
	  "zcashaddress"  (string) a Zcash address associated with the given account
	  ,...
	]

Examples:

::

	> komodo-cli getaddressesbyaccount "tabby"
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getaddressesbyaccount", "params": ["tabby"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getbalance ( "account" minconf includeWatchonly )
-------------------------------------------------

Returns the server's total available balance.

Arguments:

::

	1. "account"      (string, optional) DEPRECATED. If provided, it MUST be set to the empty string "" or to the string "*", either of which will give the total available balance. Passing any other string will result in an error.
	2. minconf          (numeric, optional, default=1) Only include transactions confirmed at least this many times.
	3. includeWatchonly (bool, optional, default=false) Also include balance in watchonly addresses (see 'importaddress')

Result:

::

	amount              (numeric) The total amount in ZEC received for this account.

Examples:

The total amount in the wallet

::

	> komodo-cli getbalance 

The total amount in the wallet at least 5 blocks confirmed

::

	> komodo-cli getbalance "*" 6

As a json rpc call

::

	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getbalance", "params": ["*", 6] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getnewaddress ( "account" )
---------------------------

Returns a new Komodo address for receiving payments.

Arguments:

::

	1. "account"        (string, optional) DEPRECATED. If provided, it MUST be set to the empty string "" to represent the default account. Passing any other string will result in an error.

Result:

::

	"zcashaddress"    (string) The new Zcash address

Examples:

::

	> komodo-cli getnewaddress 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getnewaddress", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getrawchangeaddress
-------------------

Returns a new Komodo address, for receiving change.
This is for use with raw transactions, NOT normal use.

Result:

::

	"address"    (string) The address

Examples:

::

	> komodo-cli getrawchangeaddress 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getrawchangeaddress", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getreceivedbyaccount "account" ( minconf )
------------------------------------------

**DEPRECATED**. Returns the total amount received by addresses with <account> in transactions with at least [minconf] confirmations.

Arguments:

::

	1. "account"      (string, required) MUST be set to the empty string "" to represent the default account. Passing any other string will result in an error.
	2. minconf          (numeric, optional, default=1) Only include transactions confirmed at least this many times.

Result:

::

	amount              (numeric) The total amount in ZEC received for this account.

Examples:

Amount received by the default account with at least 1 confirmation

::

	> komodo-cli getreceivedbyaccount ""

Amount received at the tabby account including unconfirmed amounts with zero confirmations

::

	> komodo-cli getreceivedbyaccount "tabby" 0

The amount with at least 6 confirmation, very safe

::

	> komodo-cli getreceivedbyaccount "tabby" 6

As a json rpc call

::

	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getreceivedbyaccount", "params": ["tabby", 6] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getreceivedbyaddress "KMD_address" ( minconf )
----------------------------------------------

Returns the total amount received by the given Zcash address in transactions with at least minconf confirmations.

Arguments:

::

	1. "zcashaddress"  (string, required) The Zcash address for transactions.
	2. minconf             (numeric, optional, default=1) Only include transactions confirmed at least this many times.

Result:

::

	amount   (numeric) The total amount in ZEC received at this address.

Examples:

The amount from transactions with at least 1 confirmation

::

	> komodo-cli getreceivedbyaddress "t14oHp2v54vfmdgQ3v3SNuQga8JKHTNi2a1"

The amount including unconfirmed transactions, zero confirmations

::

	> komodo-cli getreceivedbyaddress "t14oHp2v54vfmdgQ3v3SNuQga8JKHTNi2a1" 0

The amount with at least 6 confirmations, very safe

::

	> komodo-cli getreceivedbyaddress "t14oHp2v54vfmdgQ3v3SNuQga8JKHTNi2a1" 6

As a json rpc call

::

> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getreceivedbyaddress", "params": ["t14oHp2v54vfmdgQ3v3SNuQga8JKHTNi2a1", 6] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/


gettransaction "txid" ( includeWatchonly )
------------------------------------------

Get detailed information about in-wallet transaction <txid>

Arguments:

::

	1. "txid"    (string, required) The transaction id
	2. "includeWatchonly"    (bool, optional, default=false) Whether to include watchonly addresses in balance calculation and details[]

Result:

::

	{
	  "amount" : x.xxx,        (numeric) The transaction amount in ZEC
	  "confirmations" : n,     (numeric) The number of confirmations
	  "blockhash" : "hash",  (string) The block hash
	  "blockindex" : xx,       (numeric) The block index
	  "blocktime" : ttt,       (numeric) The time in seconds since epoch (1 Jan 1970 GMT)
	  "txid" : "transactionid",   (string) The transaction id.
	  "time" : ttt,            (numeric) The transaction time in seconds since epoch (1 Jan 1970 GMT)
	  "timereceived" : ttt,    (numeric) The time received in seconds since epoch (1 Jan 1970 GMT)
	  "details" : [
	    {
	      "account" : "accountname",  (string) DEPRECATED. The account name involved in the transaction, can be "" for the default account.
	      "address" : "zcashaddress",   (string) The Zcash address involved in the transaction
	      "category" : "send|receive",    (string) The category, either 'send' or 'receive'
	      "amount" : x.xxx                  (numeric) The amount in ZEC
	      "vout" : n,                       (numeric) the vout value
	    }
	    ,...
	  ],
	  "vjoinsplit" : [
	    {
	      "anchor" : "treestateref",          (string) Merkle root of note commitment tree
	      "nullifiers" : [ string, ...]      (string) Nullifiers of input notes
	      "commitments" : [ string, ...]     (string) Note commitments for note outputs
	      "macs" : [ string, ...]            (string) Message authentication tags
	      "vpub_old" : x.xxx                  (numeric) The amount removed from the transparent value pool
	      "vpub_new" : x.xxx,                 (numeric) The amount added to the transparent value pool
	    }
	    ,...
	  ],
	  "hex" : "data"         (string) Raw data for transaction
	}

Examples:

::

	> komodo-cli gettransaction "1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d"
	> komodo-cli gettransaction "1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d" true
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "gettransaction", "params": ["1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

getunconfirmedbalance
---------------------

Returns the server's total unconfirmed balance

getwalletinfo
-------------

Returns an object containing various wallet state info.

Result:

::

	{
	  "walletversion": xxxxx,     (numeric) the wallet version
	  "balance": xxxxxxx,         (numeric) the total confirmed balance of the wallet in ZEC
	  "unconfirmed_balance": xxx, (numeric) the total unconfirmed balance of the wallet in ZEC
	  "immature_balance": xxxxxx, (numeric) the total immature balance of the wallet in ZEC
	  "txcount": xxxxxxx,         (numeric) the total number of transactions in the wallet
	  "keypoololdest": xxxxxx,    (numeric) the timestamp (seconds since GMT epoch) of the oldest pre-generated key in the key pool
	  "keypoolsize": xxxx,        (numeric) how many new keys are pre-generated
	  "unlocked_until": ttt,      (numeric) the timestamp in seconds since epoch (midnight Jan 1 1970 GMT) that the wallet is unlocked for transfers, 	or 0 if the wallet is locked
	  "paytxfee": x.xxxx,         (numeric) the transaction fee configuration, set in KMD/KB
	}

Examples:

::

	> komodo-cli getwalletinfo 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getwalletinfo", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/


importaddress "address" ( "label" rescan )
------------------------------------------

Adds an address or script (in hex) that can be watched as if it were in your wallet but cannot be used to spend.

Arguments:

::

	1. "address"          (string, required) The address
	2. "label"            (string, optional, default="") An optional label
	3. rescan               (boolean, optional, default=true) Rescan the wallet for transactions

**Note**: This call can take minutes to complete if rescan is true.

Examples:

Import an address with rescan
> komodo-cli importaddress "myaddress"

Import using a label without rescan
> komodo-cli importaddress "myaddress" "testing" false

As a JSON-RPC call
> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "importaddress", "params": ["myaddress", "testing", false] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/


importprivkey "komodoprivkey" ( "label" rescan )
------------------------------------------------

Adds a private key (as returned by dumpprivkey) to your wallet.

Arguments:

::

	1. "zcashprivkey"   (string, required) The private key (see dumpprivkey)
	2. "label"            (string, optional, default="") An optional label
	3. rescan               (boolean, optional, default=true) Rescan the wallet for transactions

Note: This call can take minutes to complete if rescan is true.

Examples:

Dump a private key

::

	> komodo-cli dumpprivkey "myaddress"

Import the private key with rescan

::


	> komodo-cli importprivkey "mykey"

Import using a label and without rescan

::

	> komodo-cli importprivkey "mykey" "testing" false

As a JSON-RPC call

::

	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "importprivkey", "params": ["mykey", "testing", false] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

importwallet "filename"
-----------------------

Imports taddr keys from a wallet dump file (see dumpwallet).

Arguments:

::

	1. "filename"    (string, required) The wallet file

Examples:

Dump the wallet

::

	> komodo-cli dumpwallet "nameofbackup"

Import the wallet

::

	> komodo-cli importwallet "path/to/exportdir/nameofbackup"

Import using the json rpc call

::

> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "importwallet", "params": ["path/to/exportdir/nameofbackup"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

keypoolrefill ( newsize )
-------------------------

Fills the keypool.

Arguments

::

	1. newsize     (numeric, optional, default=100) The new keypool size

Examples:

::

	> komodo-cli keypoolrefill 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "keypoolrefill", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

listaccounts ( minconf includeWatchonly)
----------------------------------------

**DEPRECATED**. Returns Object that has account names as keys, account balances as values.

Arguments:

::

	1. minconf          (numeric, optional, default=1) Only include transactions with at least this many confirmations
	2. includeWatchonly (bool, optional, default=false) Include balances in watchonly addresses (see 'importaddress')

Result:

::

	{                      (json object where keys are account names, and values are numeric balances
	  "account": x.xxx,  (numeric) The property name is the account name, and the value is the total balance for the account.
	  ...
	}

Examples:

List account balances where there at least 1 confirmation

::

	> komodo-cli listaccounts 

List account balances including zero confirmation transactions

::

	> komodo-cli listaccounts 0

List account balances for 6 or more confirmations

::

	> komodo-cli listaccounts 6

As json rpc call

::

	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listaccounts", "params": [6] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/


listaddressgroupings
--------------------

Lists groups of addresses which have had their common ownership
made public by common use as inputs or as the resulting change
in past transactions

Result:

::

	[
	  [
	    [
	      "zcashaddress",     (string) The zcash address
	      amount,                 (numeric) The amount in ZEC
	      "account"             (string, optional) The account (DEPRECATED)
	    ]
	    ,...
	  ]
	  ,...
	]

Examples:

::

	> komodo-cli listaddressgroupings 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listaddressgroupings", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

listlockunspent
---------------

Returns list of temporarily unspendable outputs.
See the lockunspent call to lock and unlock transactions for spending.

Result:

::

	[
	  {
	    "txid" : "transactionid",     (string) The transaction id locked
	    "vout" : n                      (numeric) The vout value
	  }
	  ,...
	]

Examples:

List the unspent transactions

::

	> komodo-cli listunspent 

Lock an unspent transaction

::

	> komodo-cli lockunspent false "[{\"txid\":\"a08e6907dbbd3d809776dbfc5d82e371b764ed838b5655e72f463568df1aadf0\",\"vout\":1}]"

List the locked transactions

::

	> komodo-cli listlockunspent 

Unlock the transaction again

::

	> komodo-cli lockunspent true "[{\"txid\":\"a08e6907dbbd3d809776dbfc5d82e371b764ed838b5655e72f463568df1aadf0\",\"vout\":1}]"

As a json rpc call

::

	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listlockunspent", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/


listreceivedbyaccount ( minconf includeempty includeWatchonly)
--------------------------------------------------------------

**DEPRECATED**. List balances by account.

Arguments:

::

	1. minconf      (numeric, optional, default=1) The minimum number of confirmations before payments are included.
	2. includeempty (boolean, optional, default=false) Whether to include accounts that haven't received any payments.
	3. includeWatchonly (bool, optional, default=false) Whether to include watchonly addresses (see 'importaddress').

Result:

::

	[
	  {
	    "involvesWatchonly" : true,   (bool) Only returned if imported addresses were involved in transaction
	    "account" : "accountname",  (string) The account name of the receiving account
	    "amount" : x.xxx,             (numeric) The total amount received by addresses with this account
	    "confirmations" : n           (numeric) The number of confirmations of the most recent transaction included
	  }
	  ,...
	]

Examples:

::

	> komodo-cli listreceivedbyaccount 
	> komodo-cli listreceivedbyaccount 6 true
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listreceivedbyaccount", "params": [6, true, true] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

listreceivedbyaddress ( minconf includeempty includeWatchonly)
--------------------------------------------------------------

List balances by receiving address.

Arguments:

::

	1. minconf       (numeric, optional, default=1) The minimum number of confirmations before payments are included.
	2. includeempty  (numeric, optional, default=false) Whether to include addresses that haven't received any payments.
	3. includeWatchonly (bool, optional, default=false) Whether to include watchonly addresses (see 'importaddress').

Result:

::

	[
	  {
	    "involvesWatchonly" : true,        (bool) Only returned if imported addresses were involved in transaction
	    "address" : "receivingaddress",  (string) The receiving address
	    "account" : "accountname",       (string) DEPRECATED. The account of the receiving address. The default account is "".
	    "amount" : x.xxx,                  (numeric) The total amount in ZEC received by the address
	    "confirmations" : n                (numeric) The number of confirmations of the most recent transaction included
	  }
	  ,...
	]

Examples:

::

	> komodo-cli listreceivedbyaddress 
	> komodo-cli listreceivedbyaddress 6 true
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listreceivedbyaddress", "params": [6, true, true] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

listsinceblock ( "blockhash" target-confirmations includeWatchonly)
-------------------------------------------------------------------

Get all transactions in blocks since block [blockhash], or all transactions if omitted

Arguments:

::
	
	1. "blockhash"   (string, optional) The block hash to list transactions since
	2. target-confirmations:    (numeric, optional) The confirmations required, must be 1 or more
	3. includeWatchonly:        (bool, optional, default=false) Include transactions to watchonly addresses (see 'importaddress')

Result:

::

	{
	  "transactions": [
  	  "account":"accountname",       (string) DEPRECATED. The account name associated with the transaction. Will be "" for the default account.
  	  "address":"zcashaddress",    (string) The Zcash address of the transaction. Not present for move transactions (category = move).
  	  "category":"send|receive",     (string) The transaction category. 'send' has negative amounts, 'receive' has positive amounts.
  	  "amount": x.xxx,          (numeric) The amount in ZEC. This is negative for the 'send' category, and for the 'move' category for moves 
                                          outbound. It is positive for the 'receive' category, and for the 'move' category for inbound funds.
    	"vout" : n,               (numeric) the vout value
	    "fee": x.xxx,             (numeric) The amount of the fee in ZEC. This is negative and only available for the 'send' category of transactions.
	    "confirmations": n,       (numeric) The number of confirmations for the transaction. Available for 'send' and 'receive' category of transactions.
	    "blockhash": "hashvalue",     (string) The block hash containing the transaction. Available for 'send' and 'receive' category of transactions.
	    "blockindex": n,          (numeric) The block index containing the transaction. Available for 'send' and 'receive' category of transactions.
	    "blocktime": xxx,         (numeric) The block time in seconds since epoch (1 Jan 1970 GMT).
	    "txid": "transactionid",  (string) The transaction id. Available for 'send' and 'receive' category of transactions.
    	"time": xxx,              (numeric) The transaction time in seconds since epoch (Jan 1 1970 GMT).
	    "timereceived": xxx,      (numeric) The time received in seconds since epoch (Jan 1 1970 GMT). Available for 'send' and 'receive' category of transactions.
	    "comment": "...",       (string) If a comment is associated with the transaction.
	    "to": "...",            (string) If a comment to is associated with the transaction.
	  ],
	  "lastblock": "lastblockhash"     (string) The hash of the last block
	}

Examples:

::

	> komodo-cli listsinceblock 
	> komodo-cli listsinceblock "000000000000000bacf66f7497b7dc45ef753ee9a7d38571037cdb1a57f663ad" 6
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listsinceblock", "params": ["000000000000000bacf66f7497b7dc45ef753ee9a7d38571037cdb1a57f663ad", 6] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/


listtransactions ( "account" count from includeWatchonly)
---------------------------------------------------------

Returns up to 'count' most recent transactions skipping the first 'from' transactions for account 'account'.

Arguments:

::

	1. "account"    (string, optional) DEPRECATED. The account name. Should be "*".
	2. count          (numeric, optional, default=10) The number of transactions to return
	3. from           (numeric, optional, default=0) The number of transactions to skip
	4. includeWatchonly (bool, optional, default=false) Include transactions to watchonly addresses (see 'importaddress')

Result:

::

	[
	  {
	    "account":"accountname",       (string) DEPRECATED. The account name associated with the transaction. 
	                                                It will be "" for the default account.
	    "address":"zcashaddress",    (string) The Zcash address of the transaction. Not present for 
	                                                move transactions (category = move).
	    "category":"send|receive|move", (string) The transaction category. 'move' is a local (off blockchain)
	                                                transaction between accounts, and not associated with an address,
	                                                transaction id or block. 'send' and 'receive' transactions are 
	                                                associated with an address, transaction id and block details
	    "amount": x.xxx,          (numeric) The amount in ZEC. This is negative for the 'send' category, and for the
	                                         'move' category for moves outbound. It is positive for the 'receive' category,
	                                         and for the 'move' category for inbound funds.
	    "vout" : n,               (numeric) the vout value
	    "fee": x.xxx,             (numeric) The amount of the fee in ZEC. This is negative and only available for the 
	                                         'send' category of transactions.
	    "confirmations": n,       (numeric) The number of confirmations for the transaction. Available for 'send' and 
	                                         'receive' category of transactions.
	    "blockhash": "hashvalue", (string) The block hash containing the transaction. Available for 'send' and 'receive'
	                                          category of transactions.
	    "blockindex": n,          (numeric) The block index containing the transaction. Available for 'send' and 'receive'
	                                          category of transactions.
	    "txid": "transactionid", (string) The transaction id. Available for 'send' and 'receive' category of transactions.
	    "time": xxx,              (numeric) The transaction time in seconds since epoch (midnight Jan 1 1970 GMT).
	    "timereceived": xxx,      (numeric) The time received in seconds since epoch (midnight Jan 1 1970 GMT). Available 
	                                          for 'send' and 'receive' category of transactions.
	    "comment": "...",       (string) If a comment is associated with the transaction.
	    "otheraccount": "accountname",  (string) For the 'move' category of transactions, the account the funds came 
	                                          from (for receiving funds, positive amounts), or went to (for sending funds,
	                                          negative amounts).
	    "size": n,                (numeric) Transaction size in bytes
	  }
	]

Examples:

List the most recent 10 transactions in the systems

::

	> komodo-cli listtransactions 

List transactions 100 to 120

::

	> komodo-cli listtransactions "*" 20 100

As a json rpc call

::

	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listtransactions", "params": ["*", 20, 100] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/


listunspent ( minconf maxconf  ["address",...] )
------------------------------------------------

Returns array of unspent transaction outputs
with between minconf and maxconf (inclusive) confirmations.
Optionally filter to only include txouts paid to specified addresses.
Results are an array of Objects, each of which has:
{txid, vout, scriptPubKey, amount, confirmations}

Arguments:

::

	1. minconf          (numeric, optional, default=1) The minimum confirmations to filter
	2. maxconf          (numeric, optional, default=9999999) The maximum confirmations to filter
	3. "addresses"    (string) A json array of Zcash addresses to filter

	    [
	      "address"   (string) Zcash address
	      ,...
	    ]
	
Result:

::

	[                   (array of json object)
	  {
	    "txid" : "txid",        (string) the transaction id 
	    "vout" : n,               (numeric) the vout value
	    "generated" : true|false  (boolean) true if txout is a coinbase transaction output
	    "address" : "address",  (string) the Zcash address
	    "account" : "account",  (string) DEPRECATED. The associated account, or "" for the default account
	    "scriptPubKey" : "key", (string) the script key
	    "amount" : x.xxx,         (numeric) the transaction amount in ZEC
	    "confirmations" : n       (numeric) The number of confirmations
	  }
	  ,...
	]

Examples:

::

	> komodo-cli listunspent 
	> komodo-cli listunspent 6 9999999 "[\"t1PGFqEzfmQch1gKD3ra4k18PNj3tTUUSqg\",\"t1LtvqCaApEdUGFkpKMM4MstjcaL4dKg8SP\"]"
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "listunspent", "params": [6, 9999999 "[\"t1PGFqEzfmQch1gKD3ra4k18PNj3tTUUSqg\",\"t1LtvqCaApEdUGFkpKMM4MstjcaL4dKg8SP\"]"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/


lockunspent unlock [{"txid":"txid","vout":n},...]
-------------------------------------------------

Updates list of temporarily unspendable outputs.
Temporarily lock (unlock=false) or unlock (unlock=true) specified transaction outputs.
A locked transaction output will not be chosen by automatic coin selection, when spending Zcash.
Locks are stored in memory only. Nodes start with zero locked outputs, and the locked output list
is always cleared (by virtue of process exit) when a node stops or fails.
Also see the listunspent call

Arguments:

::

	1. unlock            (boolean, required) Whether to unlock (true) or lock (false) the specified transactions
	2. "transactions"  (string, required) A json array of objects. Each object the txid (string) vout (numeric)
	     [           (json array of json objects)
	       {
	         "txid":"id",    (string) The transaction id
	         "vout": n         (numeric) The output number
	       }
	       ,...
	     ]

Result:

::

	true|false    (boolean) Whether the command was successful or not

Examples:

List the unspent transactions

::

	> komodo-cli listunspent 

Lock an unspent transaction

::

	> komodo-cli lockunspent false "[{\"txid\":\"a08e6907dbbd3d809776dbfc5d82e371b764ed838b5655e72f463568df1aadf0\",\"vout\":1}]"

List the locked transactions

::

	> komodo-cli listlockunspent 

Unlock the transaction again

::

	> komodo-cli lockunspent true "[{\"txid\":\"a08e6907dbbd3d809776dbfc5d82e371b764ed838b5655e72f463568df1aadf0\",\"vout\":1}]"

As a json rpc call

::

	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "lockunspent", "params": [false, "[{\"txid\":\"a08e6907dbbd3d809776dbfc5d82e371b764ed838b5655e72f463568df1aadf0\",\"vout\":1}]"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

move "fromaccount" "toaccount" amount ( minconf "comment" )
-----------------------------------------------------------

**DEPRECATED**. Move a specified amount from one account in your wallet to another.

Arguments:

::

	1. "fromaccount"   (string, required) MUST be set to the empty string "" to represent the default account. Passing any other string will result in an error.
	2. "toaccount"     (string, required) MUST be set to the empty string "" to represent the default account. Passing any other string will result in an error.
	3. amount            (numeric) Quantity of ZEC to move between accounts.
	4. minconf           (numeric, optional, default=1) Only use funds with at least this many confirmations.
	5. "comment"       (string, optional) An optional comment, stored in the wallet only.

Result:

::

	true|false           (boolean) true if successful.

Examples:

Move 0.01 ZEC from the default account to the account named tabby

::

	> komodo-cli move "" "tabby" 0.01

Move 0.01 ZEC timotei to akiko with a comment and funds have 6 confirmations

::

	> komodo-cli move "timotei" "akiko" 0.01 6 "happy birthday!"

As a json rpc call

::
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "move", "params": ["timotei", "akiko", 0.01, 6, "happy birthday!"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/


resendwallettransactions
------------------------

Immediately re-broadcast unconfirmed wallet transactions to all peers.
Intended only for testing; the wallet code periodically re-broadcasts
automatically.

Returns array of transaction ids that were re-broadcast.

sendfrom "fromaccount" "toKMDaddress" amount ( minconf "comment" "comment-to" )
-------------------------------------------------------------------------------

**DEPRECATED** (use sendtoaddress). Sent an amount from an account to a Zcash address.
The amount is a real and is rounded to the nearest 0.00000001.

Arguments:

::

	1. "fromaccount"       (string, required) MUST be set to the empty string "" to represent the default account. Passing any other string will result in an error.
	2. "tozcashaddress"  (string, required) The Zcash address to send funds to.
	3. amount                (numeric, required) The amount in ZEC (transaction fee is added on top).
	4. minconf               (numeric, optional, default=1) Only use funds with at least this many confirmations.
	5. "comment"           (string, optional) A comment used to store what the transaction is for. 
	                                     This is not part of the transaction, just kept in your wallet.
	6. "comment-to"        (string, optional) An optional comment to store the name of the person or organization 
                                     to which you're sending the transaction. This is not part of the transaction, 
                                     it is just kept in your wallet.

Result:

::

	"transactionid"        (string) The transaction id.

Examples:

Send 0.01 ZEC from the default account to the address, must have at least 1 confirmation

::

	> komodo-cli sendfrom "" "t1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0.01

Send 0.01 from the tabby account to the given address, funds must have at least 6 confirmations

::

	> komodo-cli sendfrom "tabby" "t1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0.01 6 "donation" "seans outpost"

As a json rpc call

::

	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "sendfrom", "params": ["tabby", "t1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", 0.01, 6, "donation", "seans outpost"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/


sendmany "fromaccount" {"address":amount,...} ( minconf "comment" ["address",...] )
-----------------------------------------------------------------------------------

Send multiple times. Amounts are double-precision floating point numbers.

Arguments:

::

	1. "fromaccount"         (string, required) MUST be set to the empty string "" to represent the default account. Passing any other string will result in an error.
	2. "amounts"             (string, required) A json object with addresses and amounts
	    {
	      "address":amount   (numeric) The Zcash address is the key, the numeric amount in ZEC is the value
	      ,...
	    }
	3. minconf                 (numeric, optional, default=1) Only use the balance confirmed at least this many times.
	4. "comment"             (string, optional) A comment
	5. subtractfeefromamount   (string, optional) A json array with addresses.
	                           The fee will be equally deducted from the amount of each selected address.
	                           Those recipients will receive less Zcash than you enter in their corresponding amount field.
	                           If no addresses are specified here, the sender pays the fee.
	    [
	      "address"            (string) Subtract fee from this address
	      ,...
	    ]

Result:

::

	"transactionid"          (string) The transaction id for the send. Only 1 transaction is created regardless of 
                                    the number of addresses.

Examples:

Send two amounts to two different addresses:

::

	> komodo-cli sendmany "" "{\"t14oHp2v54vfmdgQ3v3SNuQga8JKHTNi2a1\":0.01,\"t1353tsE8YMTA4EuV7dgUXGjNFf9KpVvKHz\":0.02}"

Send two amounts to two different addresses setting the confirmation and comment:

::

	> komodo-cli sendmany "" "{\"t14oHp2v54vfmdgQ3v3SNuQga8JKHTNi2a1\":0.01,\"t1353tsE8YMTA4EuV7dgUXGjNFf9KpVvKHz\":0.02}" 6 "testing"

Send two amounts to two different addresses, subtract fee from amount:

::

	> komodo-cli sendmany "" "{\"t14oHp2v54vfmdgQ3v3SNuQga8JKHTNi2a1\":0.01,\"t1353tsE8YMTA4EuV7dgUXGjNFf9KpVvKHz\":0.02}" 1 "" "[\"t14oHp2v54vfmdgQ3v3SNuQga8JKHTNi2a1\",\"t1353tsE8YMTA4EuV7dgUXGjNFf9KpVvKHz\"]"

As a json rpc call

::

	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "sendmany", "params": ["", "{\"t14oHp2v54vfmdgQ3v3SNuQga8JKHTNi2a1\":0.01,\"t1353tsE8YMTA4EuV7dgUXGjNFf9KpVvKHz\":0.02}", 6, "testing"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

sendtoaddress "KMD_address" amount ( "comment" "comment-to" subtractfeefromamount )
-----------------------------------------------------------------------------------

Send an amount to a given address. The amount is a real and is rounded to the nearest 0.00000001

Arguments:

::

	1. "komodoaddress"  (string, required) The Komodo address to send to.
	2. "amount"      (numeric, required) The amount in Komodo to send. eg 0.1
	3. "comment"     (string, optional) A comment used to store what the transaction is for. 
	                             This is not part of the transaction, just kept in your wallet.
	4. "comment-to"  (string, optional) A comment to store the name of the person or organization 
	                             to which you're sending the transaction. This is not part of the 
	                             transaction, just kept in your wallet.
	5. subtractfeefromamount  (boolean, optional, default=false) The fee will be deducted from the amount being sent.
	                             The recipient will receive less Zcash than you enter in the amount field.

Result:

::

	"transactionid"  (string) The transaction id.

Examples:

::

	> komodo-cli sendtoaddress "t1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0.1
	> komodo-cli sendtoaddress "t1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0.1 "donation" "seans outpost"
	> komodo-cli sendtoaddress "t1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" 0.1 "" "" true
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "sendtoaddress", "params": ["t1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", 0.1, "donation", "seans outpost"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

setaccount "KMD_address" "account"
----------------------------------

**DEPRECATED**. Sets the account associated with the given address.

Arguments:

::

	1. "zcashaddress"  (string, required) The Zcash address to be associated with an account.
	2. "account"         (string, required) MUST be set to the empty string "" to represent the default account. Passing any other string will result in an error.

Examples:

::

	> komodo-cli setaccount "t14oHp2v54vfmdgQ3v3SNuQga8JKHTNi2a1" "tabby"
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "setaccount", "params": ["t14oHp2v54vfmdgQ3v3SNuQga8JKHTNi2a1", "tabby"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

settxfee amount
---------------

Set the transaction fee per kB.

Arguments:

::

	1. amount         (numeric, required) The transaction fee in ZEC/kB rounded to the nearest 0.00000001

Result

::

	true|false        (boolean) Returns true if successful

Examples:

::

	> komodo-cli settxfee 0.00001
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "settxfee", "params": [0.00001] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

signmessage "KMD address" "message"
-----------------------------------

Sign a message with the private key of an address

Arguments:

::

	1. "zcashaddress"  (string, required) The Zcash address to use for the private key.
	2. "message"         (string, required) The message to create a signature of.

Result:

::

	"signature"          (string) The signature of the message encoded in base 64

Examples:

Unlock the wallet for 30 seconds

::

	> komodo-cli walletpassphrase "mypassphrase" 30

Create the signature

::

	> komodo-cli signmessage "t14oHp2v54vfmdgQ3v3SNuQga8JKHTNi2a1" "my message"

Verify the signature

::

	> komodo-cli verifymessage "t14oHp2v54vfmdgQ3v3SNuQga8JKHTNi2a1" "signature" "my message"

As json rpc

::

	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "signmessage", "params": ["t14oHp2v54vfmdgQ3v3SNuQga8JKHTNi2a1", "my message"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/


z_exportkey "zaddr"
-------------------

Reveals the zkey corresponding to 'zaddr'.
Then the z_importkey can be used with this output

Arguments:

::

	1. "zaddr"   (string, required) The zaddr for the private key

Result:

::

	"key"                  (string) The private key

Examples:

::

	> komodo-cli z_exportkey "myaddress"
	> komodo-cli z_importkey "mykey"
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "z_exportkey", "params": ["myaddress"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

z_exportviewingkey "zaddr"
--------------------------

Reveals the viewing key corresponding to 'zaddr'.
Then the z_importviewingkey can be used with this output

Arguments:

::

	1. "zaddr"   (string, required) The zaddr for the viewing key

Result:

::

	"vkey"                  (string) The viewing key

Examples:

	> komodo-cli z_exportviewingkey "myaddress"
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "z_exportviewingkey", "params": ["myaddress"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

z_exportwallet "filename"
-------------------------

Exports all wallet keys, for taddr and zaddr, in a human-readable format.  Overwriting an existing file is not permitted.

Arguments:

::

	1. "filename"    (string, required) The filename, saved in folder set by zcashd -exportdir option

Result:

	"path"           (string) The full path of the destination file

Examples:

::

	> komodo-cli z_exportwallet "test"
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "z_exportwallet", "params": ["test"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

z_getbalance "address" ( minconf )
----------------------------------

Returns the balance of a taddr or zaddr belonging to the node’s wallet.

``CAUTION``: If address is a watch-only zaddr, the returned balance may be larger than the actual balance,
because spends cannot be detected with incoming viewing keys.

Arguments:

::

	1. "address"      (string) The selected address. It may be a transparent or private address.
	2. minconf          (numeric, optional, default=1) Only include transactions confirmed at least this many times.

Result:

::

	amount              (numeric) The total amount in KMD received for this address.

Examples:

The total amount received by address "myaddress"

::

	> komodo-cli z_getbalance "myaddress"

The total amount received by address "myaddress" at least 5 blocks confirmed

::

	> komodo-cli z_getbalance "myaddress" 5

As a json rpc call

::

	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "z_getbalance", "params": ["myaddress", 5] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

z_getnewaddress
---------------

Returns a new zaddr for receiving payments.

Arguments:

Result:

::
	
	"zcashaddress"    (string) The new zaddr

Examples:

::

	> komodo-cli z_getnewaddress 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "z_getnewaddress", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

z_getoperationresult (["operationid", ...]) 
---------------------------------------------

Retrieve the result and status of an operation which has finished, and then remove the operation from memory.

Arguments:

::

	1. "operationid"         (array, optional) A list of operation ids we are interested in.  If not provided, examine all operations known to the node.

Result:

::

	"    [object, ...]"      (array) A list of JSON objects

Examples:

::

	> komodo-cli z_getoperationresult '["operationid", ... ]'
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "z_getoperationresult", "params": ['["operationid", ...]'] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

z_getoperationstatus (["operationid", ...]) 
---------------------------------------------

Get operation status and any associated result or error data.  The operation will remain in memory.

Arguments:

::

	1. "operationid"         (array, optional) A list of operation ids we are interested in.  If not provided, examine all operations known to the node.

Result:

::

	"    [object, ...]"      (array) A list of JSON objects

Examples:

::

	> komodo-cli z_getoperationstatus '["operationid", ... ]'
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "z_getoperationstatus", "params": ['["operationid", ...]'] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

z_gettotalbalance ( minconf includeWatchonly )
----------------------------------------------

Return the total value of funds stored in the node’s wallet.

**CAUTION**: If the wallet contains watch-only zaddrs, the returned private balance may be larger than the actual balance,
because spends cannot be detected with incoming viewing keys.

Arguments:

::

	1. minconf          (numeric, optional, default=1) Only include private and transparent transactions confirmed at least this many times.
	2. includeWatchonly (bool, optional, default=false) Also include balance in watchonly addresses (see 'importaddress' and 'z_importviewingkey')

Result:

::

	{
	  "transparent": xxxxx,     (numeric) the total balance of transparent funds
	  "private": xxxxx,         (numeric) the total balance of private funds
	  "total": xxxxx,           (numeric) the total balance of both transparent and private funds
	}

Examples:

The total amount in the wallet

::

	> komodo-cli z_gettotalbalance 

The total amount in the wallet at least 5 blocks confirmed

::

	> komodo-cli z_gettotalbalance 5

As a json rpc call

::

	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "z_gettotalbalance", "params": [5] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

z_importkey "zkey" ( rescan startHeight )
-----------------------------------------

Adds a zkey (as returned by z_exportkey) to your wallet.

Arguments:

::

	1. "zkey"             (string, required) The zkey (see z_exportkey)
	2. rescan             (string, optional, default="whenkeyisnew") Rescan the wallet for transactions - can be "yes", "no" or "whenkeyisnew"
	3. startHeight        (numeric, optional, default=0) Block height to start rescan from

**Note**: This call can take minutes to complete if rescan is true.

Examples:

Export a zkey

::

	> komodo-cli z_exportkey "myaddress"

Import the zkey with rescan

::

	> komodo-cli z_importkey "mykey"

Import the zkey with partial rescan

::

	> komodo-cli z_importkey "mykey" whenkeyisnew 30000

Re-import the zkey with longer partial rescan

::

	> komodo-cli z_importkey "mykey" yes 20000

As a JSON-RPC call

::

	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "z_importkey", "params": ["mykey", "no"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

z_importviewingkey "vkey" ( rescan startHeight )
------------------------------------------------

Adds a viewing key (as returned by z_exportviewingkey) to your wallet.

Arguments:

::

	1. "vkey"             (string, required) The viewing key (see z_exportviewingkey)
	2. rescan             (string, optional, default="whenkeyisnew") Rescan the wallet for transactions - can be "yes", "no" or "whenkeyisnew"
	3. startHeight        (numeric, optional, default=0) Block height to start rescan from

**Note**: This call can take minutes to complete if rescan is true.

Examples:

Import a viewing key

::

	> komodo-cli z_importviewingkey "vkey"

Import the viewing key without rescan

::

	> komodo-cli z_importviewingkey "vkey", no

Import the viewing key with partial rescan

::

	> komodo-cli z_importviewingkey "vkey" whenkeyisnew 30000

Re-import the viewing key with longer partial rescan

::

	> komodo-cli z_importviewingkey "vkey" yes 20000

As a JSON-RPC call

::

	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "z_importviewingkey", "params": ["vkey", "no"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

z_importwallet "filename"
-------------------------

Imports taddr and zaddr keys from a wallet export file (see z_exportwallet).

Arguments:

::

	1. "filename"    (string, required) The wallet file

Examples:

Dump the wallet

::

	> komodo-cli z_exportwallet "nameofbackup"

Import the wallet

::

	> komodo-cli z_importwallet "path/to/exportdir/nameofbackup"

Import using the json rpc call

::

	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "z_importwallet", "params": ["path/to/exportdir/nameofbackup"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

z_listaddresses ( includeWatchonly )
------------------------------------

Returns the list of zaddr belonging to the wallet.

Arguments:

::

	1. includeWatchonly (bool, optional, default=false) Also include watchonly addresses (see 'z_importviewingkey')

Result:

::

	[                     (json array of string)
	  "zaddr"           (string) a zaddr belonging to the wallet
	  ,...
	]

Examples:

::

	> komodo-cli z_listaddresses 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "z_listaddresses", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

z_listoperationids
------------------

Returns the list of operation ids currently known to the wallet.

Arguments:

::

	1. "status"         (string, optional) Filter result by the operation's state e.g. "success".

Result:

::

	[                     (json array of string)
	  "operationid"       (string) an operation id belonging to the wallet
	  ,...
	]

Examples:

::

	> komodo-cli z_listoperationids 
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "z_listoperationids", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

z_listreceivedbyaddress "address" ( minconf )
---------------------------------------------

Return a list of amounts received by a zaddr belonging to the node’s wallet.

Arguments:

::

	1. "address"      (string) The private address.
	2. minconf          (numeric, optional, default=1) Only include transactions confirmed at least this many times.

Result:

::

	{
	  "txid": xxxxx,     (string) the transaction id
	  "amount": xxxxx,   (numeric) the amount of value in the note
	  "memo": xxxxx,     (string) hexademical string representation of memo field
	}

Examples:

::

	> komodo-cli z_listreceivedbyaddress "ztfaW34Gj9FrnGUEf833ywDVL62NWXBM81u6EQnM6VR45eYnXhwztecW1SjxA7JrmAXKJhxhj3vDNEpVCQoSvVoSpmbhtjf"
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "z_listreceivedbyaddress", "params": ["ztfaW34Gj9FrnGUEf833ywDVL62NWXBM81u6EQnM6VR45eYnXhwztecW1SjxA7JrmAXKJhxhj3vDNEpVCQoSvVoSpmbhtjf"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

z_mergetoaddress ["fromaddress", ...] "toaddress" ( fee ) ( transparent_limit ) ( shielded_limit ) ( memo )
------------------------------------------------------------------------------------------------------------

**WARNING**: z_mergetoaddress is DISABLED but can be enabled as an experimental feature.

Merge multiple UTXOs and notes into a single UTXO or note.  Coinbase UTXOs are ignored; use ``z_shieldcoinbase``
to combine those into a single note.

This is an asynchronous operation, and UTXOs selected for merging will be locked.  If there is an error, they
are unlocked.  The RPC call `listlockunspent` can be used to return a list of locked UTXOs.

The number of UTXOs and notes selected for merging can be limited by the caller.  If the transparent limit
parameter is set to zero, the -mempooltxinputlimit option will determine the number of UTXOs.  Any limit is
constrained by the consensus rule defining a maximum transaction size of 100000 bytes.

Arguments:

::
	
	1. fromaddresses         (string, required) A JSON array with addresses.
    	                     The following special strings are accepted inside the array:
    	                         - "*": Merge both UTXOs and notes from all addresses belonging to the wallet.
    	                         - "ANY_TADDR": Merge UTXOs from all t-addrs belonging to the wallet.
    	                         - "ANY_ZADDR": Merge notes from all z-addrs belonging to the wallet.
    	                     If a special string is given, any given addresses of that type will be ignored.
    	[
    	  "address"          (string) Can be a t-addr or a z-addr
    	  ,...
    	]
	2. "toaddress"           (string, required) The t-addr or z-addr to send the funds to.
	3. fee                   (numeric, optional, default=0.0001) The fee amount to attach to this transaction.
	4. transparent_limit     (numeric, optional, default=50) Limit on the maximum number of UTXOs to merge.  Set to 0 to use node option -mempooltxinputlimit.
	4. shielded_limit        (numeric, optional, default=10) Limit on the maximum number of notes to merge.  Set to 0 to merge as many as will fit in the transaction.
	5. "memo"                (string, optional) Encoded as hex. When toaddress is a z-addr, this will be stored in the memo field of the new note.

Result:

::

	{
	  "remainingUTXOs": xxx               (numeric) Number of UTXOs still available for merging.
	  "remainingTransparentValue": xxx    (numeric) Value of UTXOs still available for merging.
	  "remainingNotes": xxx               (numeric) Number of notes still available for merging.
	  "remainingShieldedValue": xxx       (numeric) Value of notes still available for merging.
	  "mergingUTXOs": xxx                 (numeric) Number of UTXOs being merged.
	  "mergingTransparentValue": xxx      (numeric) Value of UTXOs being merged.
	  "mergingNotes": xxx                 (numeric) Number of notes being merged.
	  "mergingShieldedValue": xxx         (numeric) Value of notes being merged.
	  "opid": xxx          (string) An operationid to pass to z_getoperationstatus to get the result of the operation.
	}

Examples:

::

	> komodo-cli z_mergetoaddress '["t1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd"]' ztfaW34Gj9FrnGUEf833ywDVL62NWXBM81u6EQnM6VR45eYnXhwztecW1SjxA7JrmAXKJhxhj3vDNEpVCQoSvVoSpmbhtjf
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "z_mergetoaddress", "params": [["t1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd"], "ztfaW34Gj9FrnGUEf833ywDVL62NWXBM81u6EQnM6VR45eYnXhwztecW1SjxA7JrmAXKJhxhj3vDNEpVCQoSvVoSpmbhtjf"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

z_sendmany "fromaddress" [{"address":...,"amount":...},...] ( minconf ) ( fee )
--------------------------------------------------------------------------------

Send multiple times. Amounts are double-precision floating point numbers.
Change from a taddr flows to a new taddr address, while change from zaddr returns to itself.
When sending coinbase UTXOs to a zaddr, change is not allowed. The entire value of the UTXO(s) must be consumed.
Currently, the maximum number of zaddr outputs is 54 due to transaction size limits.

Arguments:

::

	1. "fromaddress"         (string, required) The taddr or zaddr to send the funds from.
	2. "amounts"             (array, required) An array of json objects representing the amounts to send.
	    [{
	      "address":address  (string, required) The address is a taddr or zaddr
	      "amount":amount    (numeric, required) The numeric amount in KMD is the value
	      "memo":memo        (string, optional) If the address is a zaddr, raw data represented in hexadecimal string format
	    }, ...]
	3. minconf               (numeric, optional, default=1) Only use funds confirmed at least this many times.
	4. fee                   (numeric, optional, default=0.0001) The fee amount to attach to this transaction.

Result:

::

	"operationid"          (string) An operationid to pass to z_getoperationstatus to get the result of the operation.

Examples:

::

	> komodo-cli z_sendmany "t1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" '[{"address": "ztfaW34Gj9FrnGUEf833ywDVL62NWXBM81u6EQnM6VR45eYnXhwztecW1SjxA7JrmAXKJhxhj3vDNEpVCQoSvVoSpmbhtjf" ,"amount": 5.0}]'
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "z_sendmany", "params": ["t1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", [{"address": "ztfaW34Gj9FrnGUEf833ywDVL62NWXBM81u6EQnM6VR45eYnXhwztecW1SjxA7JrmAXKJhxhj3vDNEpVCQoSvVoSpmbhtjf" ,"amount": 5.0}]] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

z_shieldcoinbase "fromaddress" "tozaddress" ( fee ) ( limit )
-------------------------------------------------------------

Shield transparent coinbase funds by sending to a shielded zaddr.  This is an asynchronous operation and utxos
selected for shielding will be locked.  If there is an error, they are unlocked.  The RPC call `listlockunspent`
can be used to return a list of locked utxos.  The number of coinbase utxos selected for shielding can be limited
by the caller.  If the limit parameter is set to zero, the -mempooltxinputlimit option will determine the number
of uxtos.  Any limit is constrained by the consensus rule defining a maximum transaction size of 100000 bytes.

Arguments:

::

	1. "fromaddress"         (string, required) The address is a taddr or "*" for all taddrs belonging to the wallet.
	2. "toaddress"           (string, required) The address is a zaddr.
	3. fee                   (numeric, optional, default=0.0001) The fee amount to attach to this transaction.
	4. limit                 (numeric, optional, default=50) Limit on the maximum number of utxos to shield.  Set to 0 to use node option -mempooltxinputlimit.

Result:

::

	{
	  "remainingUTXOs": xxx       (numeric) Number of coinbase utxos still available for shielding.
	  "remainingValue": xxx       (numeric) Value of coinbase utxos still available for shielding.
	  "shieldingUTXOs": xxx        (numeric) Number of coinbase utxos being shielded.
	  "shieldingValue": xxx        (numeric) Value of coinbase utxos being shielded.
	  "opid": xxx          (string) An operationid to pass to z_getoperationstatus to get the result of the operation.
	}

Examples:

::

	> komodo-cli z_shieldcoinbase "t1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd" "ztfaW34Gj9FrnGUEf833ywDVL62NWXBM81u6EQnM6VR45eYnXhwztecW1SjxA7JrmAXKJhxhj3vDNEpVCQoSvVoSpmbhtjf"
	> curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "z_shieldcoinbase", "params": ["t1M72Sfpbz1BPpXFHz9m3CdqATR44Jvaydd", "ztfaW34Gj9FrnGUEf833ywDVL62NWXBM81u6EQnM6VR45eYnXhwztecW1SjxA7JrmAXKJhxhj3vDNEpVCQoSvVoSpmbhtjf"] }' -H 'content-type: text/plain;' http://127.0.0.1:7771/

zcbenchmark benchmarktype samplecount
-------------------------------------

Runs a benchmark of the selected type samplecount times,
returning the running times of each sample.

Output: 

::

	[
	  {
	    "runningtime": runningtime
	  },
	  {
	    "runningtime": runningtime
	  }
	  ...
	]

zcrawjoinsplit rawtx inputs outputs vpub_old vpub_new
-----------------------------------------------------

  inputs: a JSON object mapping {note: zcsecretkey, ...}
  outputs: a JSON object mapping {zcaddr: value, ...}

**DEPRECATED**. Splices a joinsplit into rawtx. Inputs are unilaterally confidential.
Outputs are confidential between sender/receiver. The vpub_old and
vpub_new values are globally public and move transparent value into
or out of the confidential value store, respectively.

Note: The caller is responsible for delivering the output enc1 and
enc2 to the appropriate recipients, as well as signing rawtxout and
ensuring it is mined. (A future RPC call will deliver the confidential
payments in-band on the blockchain.)

Output: 

::

	{
	  "encryptednote1": enc1,
	  "encryptednote2": enc2,
	  "rawtxn": rawtxout
	}

zcrawkeygen
-----------

**DEPRECATED**. Generate a zcaddr which can send and receive confidential values.

Output: 

::

	{
	  "zcaddress": zcaddr,
	  "zcsecretkey": zcsecretkey,
	  "zcviewingkey": zcviewingkey,
	}

zcrawreceive zcsecretkey encryptednote
--------------------------------------

**DEPRECATED**. Decrypts encryptednote and checks if the coin commitments
are in the blockchain as indicated by the "exists" result.

Output: 

::

	{
	  "amount": value,
	  "note": noteplaintext,
	  "exists": exists
	}

zcsamplejoinsplit
-----------------

Perform a joinsplit and return the JSDescription.
