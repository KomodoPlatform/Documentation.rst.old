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
.. code-block:: json

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
	1. "node"     (string, required) The node (see getpeerinfo for nodes)

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


