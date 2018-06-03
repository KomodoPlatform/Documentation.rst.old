****************************
Komodo - API - Documentation
****************************

You can access this API while ``komodod`` is running. Just go to another terminal and run ``./komodo-cli help``.

For help about a particular API option execute ``./komodo-cli help getwalletinfo``

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

 *Note that when the chain tip is at the last block before a network upgrade activation,*
``consensus.chaintip != consensus.nextblock``.

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

``COMING SOON``

paxprice "base" "rel" height
----------------------------

``COMING SOON``

paxprices "base" "rel" maxsamples
---------------------------------

``COMING SOON``

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



Control
=======

getinfo
-------

help ( "command" )
------------------



.. _komodo-api-stop:

stop
----

Disclosure
==========

z_getpaymentdisclosure "txid" "js_index" "output_index" ("message") 
--------------------------------------------------------------------


z_validatepaymentdisclosure "paymentdisclosure"
-----------------------------------------------


Generating
==========

generate numblocks
------------------


getgenerate
-----------


setgenerate generate ( genproclimit )
-------------------------------------


Mining
======

getblocksubsidy height
----------------------


getblocktemplate ( "jsonrequestobject" )
----------------------------------------


getlocalsolps
-------------


getmininginfo
-------------


getnetworkhashps ( blocks height )
----------------------------------


getnetworksolps ( blocks height )
---------------------------------


prioritisetransaction <txid> <priority delta> <fee delta>
---------------------------------------------------------


submitblock "hexdata" ( "jsonparametersobject" )
------------------------------------------------



Network
=======

addnode "node" "add|remove|onetry"
----------------------------------


clearbanned
-----------


disconnectnode "node" 
----------------------


getaddednodeinfo dns ( "node" )
-------------------------------


getconnectioncount
------------------


getdeprecationinfo
------------------


getnettotals
------------


getnetworkinfo
--------------


getpeerinfo
-----------


listbanned
----------


ping
----


setban "ip(/netmask)" "add|remove" (bantime) (absolute)
-------------------------------------------------------



Rawtransactions
===============

createrawtransaction [{"txid":"id","vout":n},...] {"address":amount,...}
------------------------------------------------------------------------


decoderawtransaction "hexstring"
--------------------------------


decodescript "hex"
------------------


fundrawtransaction "hexstring"
------------------------------


getrawtransaction "txid" ( verbose )
------------------------------------


sendrawtransaction "hexstring" ( allowhighfees )
------------------------------------------------


signrawtransaction "hexstring" ( [{"txid":"id","vout":n,"scriptPubKey":"hex","redeemScript":"hex"},...] ["privatekey1",...] sighashtype )
-----------------------------------------------------------------------------------------------------------------------------------------



Util
====

createmultisig nrequired ["key",...]
------------------------------------


estimatefee nblocks
-------------------


estimatepriority nblocks
------------------------


invalidateblock "hash"
----------------------


jumblr_deposit "depositaddress"
-------------------------------


jumblr_pause
------------


jumblr_resume
-------------


jumblr_secret "secretaddress"
-----------------------------


reconsiderblock "hash"
----------------------


validateaddress "komodoaddress"
-------------------------------


verifymessage "komodoaddress" "signature" "message"
---------------------------------------------------


z_validateaddress "zaddr"
-------------------------



Wallet
======

addmultisigaddress nrequired ["key",...] ( "account" )
------------------------------------------------------


backupwallet "destination"
--------------------------


dumpprivkey "komodoaddress"
---------------------------


dumpwallet "filename"
---------------------


encryptwallet "passphrase"
--------------------------


getaccount "KMD_address"
------------------------


getaccountaddress "account"
---------------------------


getaddressesbyaccount "account"
-------------------------------


getbalance ( "account" minconf includeWatchonly )
-------------------------------------------------


getnewaddress ( "account" )
---------------------------


getrawchangeaddress
-------------------


getreceivedbyaccount "account" ( minconf )
------------------------------------------


getreceivedbyaddress "KMD_address" ( minconf )
----------------------------------------------


gettransaction "txid" ( includeWatchonly )
------------------------------------------


getunconfirmedbalance
---------------------


getwalletinfo
-------------


importaddress "address" ( "label" rescan )
------------------------------------------


importprivkey "komodoprivkey" ( "label" rescan )
------------------------------------------------


importwallet "filename"
-----------------------


keypoolrefill ( newsize )
-------------------------


listaccounts ( minconf includeWatchonly)
----------------------------------------


listaddressgroupings
--------------------


listlockunspent
---------------


listreceivedbyaccount ( minconf includeempty includeWatchonly)
--------------------------------------------------------------


listreceivedbyaddress ( minconf includeempty includeWatchonly)
--------------------------------------------------------------


listsinceblock ( "blockhash" target-confirmations includeWatchonly)
-------------------------------------------------------------------


listtransactions ( "account" count from includeWatchonly)
---------------------------------------------------------


listunspent ( minconf maxconf  ["address",...] )
------------------------------------------------


lockunspent unlock [{"txid":"txid","vout":n},...]
-------------------------------------------------


move "fromaccount" "toaccount" amount ( minconf "comment" )
-----------------------------------------------------------


resendwallettransactions
------------------------


sendfrom "fromaccount" "toKMDaddress" amount ( minconf "comment" "comment-to" )
-------------------------------------------------------------------------------


sendmany "fromaccount" {"address":amount,...} ( minconf "comment" ["address",...] )
-----------------------------------------------------------------------------------


sendtoaddress "KMD_address" amount ( "comment" "comment-to" subtractfeefromamount )
-----------------------------------------------------------------------------------


setaccount "KMD_address" "account"
----------------------------------


settxfee amount
---------------


signmessage "KMD address" "message"
-----------------------------------


z_exportkey "zaddr"
-------------------


z_exportviewingkey "zaddr"
--------------------------


z_exportwallet "filename"
-------------------------


z_getbalance "address" ( minconf )
----------------------------------


z_getnewaddress
---------------


z_getoperationresult (["operationid", ...]) 
---------------------------------------------


z_getoperationstatus (["operationid", ...]) 
---------------------------------------------


z_gettotalbalance ( minconf includeWatchonly )
----------------------------------------------


z_importkey "zkey" ( rescan startHeight )
-----------------------------------------


z_importviewingkey "vkey" ( rescan startHeight )
------------------------------------------------


z_importwallet "filename"
-------------------------


z_listaddresses ( includeWatchonly )
------------------------------------


z_listoperationids
------------------


z_listreceivedbyaddress "address" ( minconf )
---------------------------------------------


z_mergetoaddress ["fromaddress", ...] "toaddress" ( fee ) ( transparent_limit ) ( shielded_limit ) ( memo )
------------------------------------------------------------------------------------------------------------


z_sendmany "fromaddress" [{"address":...,"amount":...},...] ( minconf ) ( fee )
--------------------------------------------------------------------------------


z_shieldcoinbase "fromaddress" "tozaddress" ( fee ) ( limit )
-------------------------------------------------------------


zcbenchmark benchmarktype samplecount
-------------------------------------


zcrawjoinsplit rawtx inputs outputs vpub_old vpub_new
-----------------------------------------------------


zcrawkeygen
-----------


zcrawreceive zcsecretkey encryptednote
--------------------------------------


zcsamplejoinsplit
-----------------


