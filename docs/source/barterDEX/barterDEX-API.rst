BarterDEX API Summary by Category
=================================

:doc:`BarterDEX-CLI Installation guide <install-barterDEX-CLI>`

List of API by Category
-----------------------

Click any of the api options below to be taken to their summary.
Then navigate using the links in the Navigation bar on the left side. Or press the ``Home`` button on your keyboard to come back to the top again. 
As the docs are full of code samples and command-line outputs, it's best viewed on a laptop/desktop (i.e, any device that is bigger than a handheld).

:ref:`Category: BarterDEX Operation <BarterDEX Operation>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`client`, :ref:`client-osx`, :ref:`convaddress`, :ref:`debug`, :ref:`disable`, 
:ref:`electrum`, :ref:`enable`, :ref:`getcoin`, :ref:`getcoins`, :ref:`getpeers`, :ref:`getpeersIP`, 
:ref:`help`, :ref:`jpg`, :ref:`millis`, :ref:`notarizations`, :ref:`parselog`, 
:ref:`passphrase`, :ref:`sleep`, :ref:`stop`, :ref:`trust`, :ref:`trusted`

:ref:`Category: BarterDEX Trading <BarterDEX Trading>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`autoprice`, :ref:`buy`, :ref:`getfee`, :ref:`getprices`, 
:ref:`goal`, :ref:`goals`, :ref:`myprice`, :ref:`myprices`, 
:ref:`orderbook`, :ref:`pubkeystats`, :ref:`sell`, 
:ref:`setconfirms`, :ref:`setprice`, :ref:`fomo`, :ref:`dump`

> :ref:`autoprice-the-value-of-a-fund-using-the-fundvalue-api`

> :ref:`autoprice-using-usdpeg`

:ref:`Category: Status/Info <Status/Info>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`getendpoint`, :ref:`pendings`, :ref:`swapstatus`, :ref:`baserelswaps`, 
:ref:`pendingswaps`, :ref:`coinswaps`, :ref:`swapstatus-requestid-quoteid-pending`, :ref:`recentswaps`

:ref:`Category: TradeBots <TradeBots>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`bot_buy`, :ref:`bot_list`, :ref:`bot_pause`, :ref:`bot_resume`, :ref:`bot_sell`, 
:ref:`bot_settings`, :ref:`bot_status`, :ref:`bot_stop`

:ref:`Category: Coin Features <Coin Features>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`balance`, :ref:`balances`, :ref:`calcaddress`, :ref:`fundvalue`, 
:ref:`getrawtransaction`, :ref:`inuse`, :ref:`listtransactions`, 
:ref:`listunspent`, :ref:`secretaddresses`, :ref:`sendrawtransaction`, 
:ref:`supernet`, :ref:`timelock-and-unlockedspend`, 
:ref:`withdraw`, :ref:`eth_withdraw`, :ref:`opreturn`, :ref:`opreturndecrypt`

:ref:`Category: Statistics <Statistics>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`guistats`, :ref:`pricearray`, :ref:`statsdisp`, :ref:`ticker`, :ref:`tradesarray`

:ref:`Category: Revenue Sharing/Operations <Revenue Sharing/Operations>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`dividends`, :ref:`snapshot`, 
:ref:`snapshot-balance`, :ref:`snapshot-loop`

:ref:`InstantDEX-swap` - ``deposit`` & ``claim``

Docker
^^^^^^

Use command line JSON args, either ``"docker":1`` or ``"docker":"<ipaddr>"`` with marketmaker and the request must come from that ip address to be mapped to localhost.

If you have docker installed you can get the BarterDEX API running on Windows, Mac or Linux by running:

.. code-block:: shell

	docker run -e PASSPHRASE="secure passphrase" -p 127.0.0.1:7783:7783 lukechilds/barterdex-api

`GitHub link <https://github.com/lukechilds/docker-barterdex-api>`_

Summary info for each API by Category:


BarterDEX Operation
-------------------

client
^^^^^^

The first API to run which will start barterDEX in client mode. Next script to run is ``setpassphrase``. If you want to close barterDEX, issue ``pkill -15 marketmaker`` every time. This ensures all barterDEX process is killed safely.

Sample File Contents:

.. code-block:: shell

	#!/bin/bash
	source passphrase
	source coins
	./stop
	git pull;
	cp ../exchanges/updateprices .;./updateprices
	cd ..; 
	./m_mm;
	pkill -15 marketmaker; 
	stdbuf -oL $1 ./marketmaker "{\"gui\":\"nogui\",\"client\":1,\"userhome\":\"/${HOME#"/"}\",\"passphrase\":\"$passphrase\",\"coins\":$coins}" &

Fields that can be used: ``gui:nogui`` or ``gui:SimpleUI`` - to identify the CLI/GUI being used to run marketmaker. ``client:1`` - to start marketmaker as client mode. ``"userhome\":\"/${HOME#"/"`` - defines the data dir for barterDEX. DB dir contains PRICES, SWAPS, UNSPENTS and instantdex_deposit (0conf) files. ``passphrase:$passphrase`` - is to set the passphrase to run the marketmaker with, to run and login into marketmaker using WIF (Wallet Import Format) key instead of passphrase. You need to use the WIF key as passphrase inside ``passphrase`` file. barterDEX supports login using WIF Key for all supported coins instead of passphrase. ``wif:1`` - will display the passphrase's WIF during the first api return. ``rpcport:port`` - to change the 7782 port to other open port of choice.

.. _ref-netid:

netid
^^^^^

For the startup JSON default is 0, max is 19240, which should be plenty of p2p networks for a while. Each ``netid`` will operate totally independent of the other netids. The ``rpcport`` field can be used to specify different ones so you can run multiple mm on the same node, but they will be on separate ``netid``. This way you can broadcast the ``marketmaker`` prices to all the netids. You also need to use the same ``netid`` in ``setpassphrase`` script.

Example usage: 

.. code-block:: shell

	./marketmaker "{\"gui\":\"nogui\",\"client\":1, \"userhome\":\"/${HOME#"/"}\", \"passphrase\":\"$passphrase\", \"coins\":$coins, \"netid\":1}"

.. _client-osx:

client_osx
^^^^^^^^^^

It is the same script as above but only for MacOS.

Sample File Contents:

.. code-block:: shell

	#!/bin/bash	
	source passphrase
	source coins
	pkill -15 marketmaker; 
	git pull;
	cd ..; 
	./m_mm;
	./marketmaker "{\"gui\":\"nogui\",\"client\":1, \"userhome\":\"/${HOME#"/"}/Library/Application\ Support\", \"passphrase\":\"$passphrase\", \"coins\":$coins}" &

convaddress
^^^^^^^^^^^

This script should work with p2sh addresses and also with normal addresses to convert. You just have to specify the ``coin``, ``address`` & ``destcoin`` parameter and run.

Sample file contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"convaddress\",\"coin\":\"BTC\",\"address\":\"1KPctPk4Zs4Qbe1x32A5bC1roAnmpvi9Fy\",\"destcoin\":\"KMD\"}"

Sample Output 1:

.. code-block:: json

    {
        "result": "success",
        "coin": "BTC",
        "address": "1KPctPk4Zs4Qbe1x32A5bC1roAnmpvi9Fy",
        "destcoin": "KMD",
        "destaddress": "RTfoxudMAgryfeP9WC9CgiM4ZSFNVM2VvK"
    }	

Sample Output 2:

.. code-block:: json

    {
        "result": "success",
        "coin": "BTC",
        "address": "1KPctPk4Zs4Qbe1x32A5bC1roAnmpvi9Fy",
        "destcoin": "DGB",
        "destaddress": "DPXiReghsGxh8eCYmc9e8xBTgJX5CdnALu"
    }

debug
^^^^^

This script will let you debug if you run into problem with ``marketmaker`` and coins using ``gdb``. This will kill the ``marketmaker`` first, do a ``git pull`` for fresh data and build it again. Once ready, type ``run`` and hit enter to start. In case of marketmaker crash, you can use ``backtrace`` command to find the reason of the crash. To exit from this mode type ``quit`` and hit enter.

Sample File Contents:

.. code-block:: shell

	#!/bin/bash
	source passphrase
	source coins
	pkill -15 marketmaker; 
	git pull;
	cd ..; 
	./m_mm;
	gdb -args ./marketmaker "{\"gui\":\"nogui\",\"client\":1,\"userhome\":\"/${HOME#"/"}\",\"passphrase\":\"$passphrase\",\"coins\":$coins}"

disable
^^^^^^^

This method disables a coin. A disabled coin is not eligible for trading.

Sample File Contents:

.. code-block:: shell

	#!/bin/bash
	source userpass
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":	\"$userpass\",\"method\":\"disable\",\"coin\":\"REVS\"}"

enable
^^^^^^

This method enables a coin by connecting to a locally running 	native coin daemon, otherwise, known as **Native Mode**. To be eligible for trading a coin must be enabled and the daemon should be running. You can edit the sample ``enable`` script file to activate the native coins you want to trade. you can stop it by using the :ref:`disable` script.

Sample File Contents:

.. code-block:: shell

	#!/bin/bash
	source userpass
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"enable\",\"coin\":\"BEER\"}"
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"enable\",\"coin\":\"ETOMIC\"}"
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"enable\",\"coin\":\"PIZZA\"}"
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"enable\",\"coin\":\"REVS\"}"
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"enable\",\"coin\":\"KMD\"}"
	#curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"enable\",\"coin\":\"BTC\"}"
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"enable\",\"coin\":\"CHIPS\"}"
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"enable\",\"coin\":\"SUPERNET\"}"
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"enable\",\"coin\":\"CRYPTO\"}"
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"enable\",\"coin\":\"DEX\"}"
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"enable\",\"coin\":\"BOTS\"}"
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"enable\",\"coin\":\"BET\"}"
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"enable\",\"coin\":\"HODL\"}"
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"enable\",\"coin\":\"MSHARK\"}"
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"enable\",\"coin\":\"MGW\"}"
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"enable\",\"coin\":\"PANGEA\"}"
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"enable\",\"coin\":\"JUMBLR\"}"
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"enable\",\"coin\":\"HUSH\"}"
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"enable\",\"coin\":\"BTCH\"}"

Sample Output:

.. code-block:: json

    [{
        "coin": "KMD",
        "installed": true,
        "height": 706875,
        "balance": 1231.55116115,
        "KMDvalue": 1231.55116115,
        "status": "active",
        "electrum": "electrum1.cipig.net:10001",
        "smartaddress": "RANyPgfZZLhSjQB9jrzztSw66zMMYDZuxQ",
        "rpc": "127.0.0.1:7771",
        "pubtype": 60,
        "p2shtype": 85,
        "wiftype": 188,
        "txfee": 1000,
        "zcredits": 1000,
        "zdebits": {
            "swaps": [{
                "iambob": 1,
                "aliceid": 14646443851645911040,
                "requestid": 1531405035,
                "quoteid": 668442874,
                "base": "KMD",
                "satoshis": 398119479,
                "rel": "BTCH",
                "destsatoshis": 996001000,
                "price": 2.50176404,
                "finished": 0,
                "bobneeds_dPoW": 1,
                "bob_dPoWheight": 687380,
                "aliceneeds_dPoW": 1,
                "alice_dPoWheight": 0,
                "kmdvalue": 3.98119479
            }, {
                "iambob": 0,
                "aliceid": 7500808088360189952,
                "requestid": 2426472678,
                "quoteid": 3136038708,
                "base": "KMD",
                "satoshis": 170727131,
                "rel": "MSHARK",
                "destsatoshis": 30001000,
                "price": 0.17572485,
                "finished": 1518455358,
                "bobneeds_dPoW": 706621,
                "bob_dPoWheight": 687380,
                "aliceneeds_dPoW": 20948,
                "alice_dPoWheight": 14108,
                "kmdvalue": 1.72646183
            }, {
                "iambob": 0,
                "aliceid": 10968666690691268608,
                "requestid": 769582120,
                "quoteid": 492899755,
                "base": "KMD",
                "satoshis": 57319224,
                "rel": "MSHARK",
                "destsatoshis": 10001000,
                "price": 0.17447898,
                "finished": 1518455358,
                "bobneeds_dPoW": 706644,
                "bob_dPoWheight": 687380,
                "aliceneeds_dPoW": 20963,
                "alice_dPoWheight": 14108,
                "kmdvalue": 0.57552564
            }, {
                "iambob": 0,
                "aliceid": 3325348207487614976,
                "requestid": 1461677939,
                "quoteid": 3994513936,
                "base": "KMD",
                "satoshis": 57334419,
                "rel": "MSHARK",
                "destsatoshis": 10001000,
                "price": 0.17443274,
                "finished": 1518455358,
                "bobneeds_dPoW": 706648,
                "bob_dPoWheight": 687380,
                "aliceneeds_dPoW": 20965,
                "alice_dPoWheight": 14108,
                "kmdvalue": 0.57552564
            }, {
                "iambob": 0,
                "aliceid": 3949043092670119936,
                "requestid": 868202615,
                "quoteid": 2718753539,
                "base": "KMD",
                "satoshis": 40174013,
                "rel": "MSHARK",
                "destsatoshis": 7001000,
                "price": 0.17426688,
                "finished": 1518455358,
                "bobneeds_dPoW": 706662,
                "bob_dPoWheight": 687380,
                "aliceneeds_dPoW": 20972,
                "alice_dPoWheight": 14108,
                "kmdvalue": 0.40288521
            }, {
                "iambob": 0,
                "aliceid": 1187687474903711744,
                "requestid": 1035974224,
                "quoteid": 4214136299,
                "base": "KMD",
                "satoshis": 40170553,
                "rel": "MSHARK",
                "destsatoshis": 7001000,
                "price": 0.17428189,
                "finished": 1518455358,
                "bobneeds_dPoW": 706665,
                "bob_dPoWheight": 687380,
                "aliceneeds_dPoW": 20975,
                "alice_dPoWheight": 14108,
                "kmdvalue": 0.40288521
            }, {
                "iambob": 0,
                "aliceid": 3361541373681205248,
                "requestid": 1030751685,
                "quoteid": 1769312982,
                "base": "KMD",
                "satoshis": 40197682,
                "rel": "MSHARK",
                "destsatoshis": 7001000,
                "price": 0.17416427,
                "finished": 1518455358,
                "bobneeds_dPoW": 706665,
                "bob_dPoWheight": 687380,
                "aliceneeds_dPoW": 20982,
                "alice_dPoWheight": 14108,
                "kmdvalue": 0.40288521
            }, {
                "iambob": 0,
                "aliceid": 16301556677736726528,
                "requestid": 1082032834,
                "quoteid": 977860445,
                "base": "KMD",
                "satoshis": 40191021,
                "rel": "MSHARK",
                "destsatoshis": 7001000,
                "price": 0.17419313,
                "finished": 1518455358,
                "bobneeds_dPoW": 706669,
                "bob_dPoWheight": 687380,
                "aliceneeds_dPoW": 20991,
                "alice_dPoWheight": 14108,
                "kmdvalue": 0.40288521
            }, {
                "iambob": 0,
                "aliceid": 12486716361556295680,
                "requestid": 131073424,
                "quoteid": 554811147,
                "base": "KMD",
                "satoshis": 57472918,
                "rel": "MSHARK",
                "destsatoshis": 10001000,
                "price": 0.17401239,
                "finished": 1518455358,
                "bobneeds_dPoW": 706718,
                "bob_dPoWheight": 687380,
                "aliceneeds_dPoW": 21033,
                "alice_dPoWheight": 14108,
                "kmdvalue": 0.57552564
            }, {
                "iambob": 0,
                "aliceid": 13831903913886154752,
                "requestid": 3159266235,
                "quoteid": 2688690321,
                "base": "KMD",
                "satoshis": 57143474,
                "rel": "MSHARK",
                "destsatoshis": 10001000,
                "price": 0.17501561,
                "finished": 1518455358,
                "bobneeds_dPoW": 706715,
                "bob_dPoWheight": 687380,
                "aliceneeds_dPoW": 21029,
                "alice_dPoWheight": 14108,
                "kmdvalue": 0.57552564
            }, {
                "iambob": 0,
                "aliceid": 10301729584199958528,
                "requestid": 1213522022,
                "quoteid": 54249754,
                "base": "KMD",
                "satoshis": 57528414,
                "rel": "MSHARK",
                "destsatoshis": 10001000,
                "price": 0.17384453,
                "finished": 1518455358,
                "bobneeds_dPoW": 706719,
                "bob_dPoWheight": 687380,
                "aliceneeds_dPoW": 21038,
                "alice_dPoWheight": 14108,
                "kmdvalue": 0.57552564
            }, {
                "iambob": 0,
                "aliceid": 8232914266839056384,
                "requestid": 4081601584,
                "quoteid": 412356287,
                "base": "KMD",
                "satoshis": 57494778,
                "rel": "MSHARK",
                "destsatoshis": 10001000,
                "price": 0.17394623,
                "finished": 0,
                "bobneeds_dPoW": 1,
                "bob_dPoWheight": 687380,
                "aliceneeds_dPoW": 1,
                "alice_dPoWheight": 14108,
                "kmdvalue": 0.57552564
            }, {
                "iambob": 0,
                "aliceid": 9209632436025032704,
                "requestid": 3537842224,
                "quoteid": 3725087089,
                "base": "KMD",
                "satoshis": 21597791,
                "rel": "MSHARK",
                "destsatoshis": 3747597,
                "price": 0.17351760,
                "finished": 1518455358,
                "bobneeds_dPoW": 706758,
                "bob_dPoWheight": 687380,
                "aliceneeds_dPoW": 21082,
                "alice_dPoWheight": 14108,
                "kmdvalue": 0.21566225
            }, {
                "iambob": 0,
                "aliceid": 8233074053957746688,
                "requestid": 2261166303,
                "quoteid": 22701758,
                "base": "KMD",
                "satoshis": 21597177,
                "rel": "MSHARK",
                "destsatoshis": 3746456,
                "price": 0.17346970,
                "finished": 1518455358,
                "bobneeds_dPoW": 706765,
                "bob_dPoWheight": 687380,
                "aliceneeds_dPoW": 21091,
                "alice_dPoWheight": 14108,
                "kmdvalue": 0.21559659
            }, {
                "iambob": 0,
                "aliceid": 6122187997339189248,
                "requestid": 1197866694,
                "quoteid": 488405108,
                "base": "KMD",
                "satoshis": 115069202,
                "rel": "MSHARK",
                "destsatoshis": 20001000,
                "price": 0.17381714,
                "finished": 1518455358,
                "bobneeds_dPoW": 706766,
                "bob_dPoWheight": 687380,
                "aliceneeds_dPoW": 21093,
                "alice_dPoWheight": 14108,
                "kmdvalue": 1.15099373
            }, {
                "iambob": 0,
                "aliceid": 14721798049184415744,
                "requestid": 739807218,
                "quoteid": 364988835,
                "base": "KMD",
                "satoshis": 115164687,
                "rel": "MSHARK",
                "destsatoshis": 20001000,
                "price": 0.17367303,
                "finished": 1518455358,
                "bobneeds_dPoW": 706773,
                "bob_dPoWheight": 687380,
                "aliceneeds_dPoW": 21101,
                "alice_dPoWheight": 14108,
                "kmdvalue": 1.15099373
            }, {
                "iambob": 0,
                "aliceid": 15764304953332531200,
                "requestid": 2360598697,
                "quoteid": 3777086736,
                "base": "KMD",
                "satoshis": 57519187,
                "rel": "MSHARK",
                "destsatoshis": 10001000,
                "price": 0.17387241,
                "finished": 0,
                "bobneeds_dPoW": 1,
                "bob_dPoWheight": 687380,
                "aliceneeds_dPoW": 1,
                "alice_dPoWheight": 14108,
                "kmdvalue": 0.57552564
            }, {
                "iambob": 0,
                "aliceid": 15764470458444021760,
                "requestid": 1183002364,
                "quoteid": 2238731236,
                "base": "KMD",
                "satoshis": 20796927,
                "rel": "MSHARK",
                "destsatoshis": 3600230,
                "price": 0.17311355,
                "finished": 1518455358,
                "bobneeds_dPoW": 706822,
                "bob_dPoWheight": 687380,
                "aliceneeds_dPoW": 21145,
                "alice_dPoWheight": 14108,
                "kmdvalue": 0.20718175
            }, {
                "iambob": 0,
                "aliceid": 15223997733381865472,
                "requestid": 1894968837,
                "quoteid": 948074537,
                "base": "KMD",
                "satoshis": 20806039,
                "rel": "MSHARK",
                "destsatoshis": 3594169,
                "price": 0.17274642,
                "finished": 1518456523,
                "bobneeds_dPoW": 706844,
                "bob_dPoWheight": 687380,
                "aliceneeds_dPoW": 21189,
                "alice_dPoWheight": 14108,
                "kmdvalue": 0.20683295
            }],
            "pendingswaps": 14.49513794
        }
    }]
    [{
        "coin": "SUPERNET",
        "installed": true,
        "height": 85017,
        "balance": 0.94386703,
        "KMDvalue": 35.77755890,
        "status": "active",
        "smartaddress": "RANyPgfZZLhSjQB9jrzztSw66zMMYDZuxQ",
        "rpc": "127.0.0.1:11341",
        "pubtype": 60,
        "p2shtype": 85,
        "wiftype": 188,
        "txfee": 1000
    }]
    [{
        "coin": "BOTS",
        "installed": true,
        "height": 14118,
        "balance": 8.61219046,
        "KMDvalue": 95.90388479,
        "status": "active",
        "electrum": "electrum1.cipig.net:10007",
        "smartaddress": "RANyPgfZZLhSjQB9jrzztSw66zMMYDZuxQ",
        "rpc": "127.0.0.1:11964",
        "pubtype": 60,
        "p2shtype": 85,
        "wiftype": 188,
        "txfee": 1000
    }]
    [{
        "coin": "BET",
        "installed": true,
        "height": 16555,
        "balance": 36.65094825,
        "KMDvalue": 0,
        "status": "active",
        "electrum": "electrum1.cipig.net:10012",
        "smartaddress": "RANyPgfZZLhSjQB9jrzztSw66zMMYDZuxQ",
        "rpc": "127.0.0.1:14250",
        "pubtype": 60,
        "p2shtype": 85,
        "wiftype": 188,
        "txfee": 1000
    }]
    [{
        "coin": "MSHARK",
        "installed": true,
        "height": 21221,
        "balance": 61.90419488,
        "KMDvalue": 356.23889156,
        "status": "active",
        "smartaddress": "RANyPgfZZLhSjQB9jrzztSw66zMMYDZuxQ",
        "rpc": "127.0.0.1:8846",
        "pubtype": 60,
        "p2shtype": 85,
        "wiftype": 188,
        "txfee": 1000
    }]
    [{
        "coin": "BTCH",
        "installed": true,
        "height": 17922,
        "balance": 1890.26497637,
        "KMDvalue": 1085.25152617,
        "status": "active",
        "smartaddress": "RANyPgfZZLhSjQB9jrzztSw66zMMYDZuxQ",
        "rpc": "127.0.0.1:8800",
        "pubtype": 60,
        "p2shtype": 85,
        "wiftype": 188,
        "txfee": 1000
    }]
	
getcoin
^^^^^^^

This method will show coin data including smartaddress, balance etc. Do NOT use ``getcoin`` to get balance in SPV mode, use the ``balance`` API.

Sample File Contents:

.. code-block:: shell


	#!/bin/bash
	source userpass
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"getcoin\",\"coin\":\"LTC\"}"

Sample Output:

.. code-block:: json

    {
        "result": "success",
        "enabled": 5,
        "disabled": 88,
        "coin": {
            "coin": "BTCH",
            "installed": true,
            "height": 17914,
            "balance": 1890.26497637,
            "KMDvalue": 1060.52748251,
            "status": "active",
            "smartaddress": "RANyPgfZZLhSjQB9jrzztSw66zMMYDZuxQ",
            "rpc": "127.0.0.1:8800",
            "pubtype": 60,
            "p2shtype": 85,
            "wiftype": 188,
            "txfee": 1000
        }
    }

getcoins
^^^^^^^^

This will display the list of all coins that barterDEX supports. It will list both disabled and enabled coins. Along with the status of the coin, this function will also display your smartaddress for that given coin. This method does not need user defined inputs and will just display all the coins.

Sample File Contents:

.. code-block:: shell

	#!/bin/bash
	source userpass
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"getcoins\"}"

Sample Output:

.. code-block:: json

     [{
             "coin": "BTC",
             "height": 0,
             "status": "inactive",
             "smartaddress": "15XAhHK4ULofD6BTckrCWK6XSkCjscX7jj",
             "rpc": "127.0.0.1:8332",
             "pubtype": 0,
             "p2shtype": 5,
             "wiftype": 128,
             "txfee": 0
         },
         {
             "coin": "KMD",
             "height": 538355,
             "status": "active",
             "smartaddress": "RDoMmoCM5AcEH6Yf5vqKbqRjD1fLcQHuWb",
             "rpc": "127.0.0.1:7771",
             "pubtype": 60,
             "p2shtype": 85,
             "wiftype": 188,
             "txfee": 10000
         }
     ]
 
getpeers
^^^^^^^^

The ``./getpeers`` script prints the connected nodes available to trade in the network.

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"getpeers\"}"

Sample Output:

.. code-block:: json

     [{
             "ipaddr": "5.9.253.202",
             "port": 7783,
             "session": 1508151814
         },
         {
             "ipaddr": "5.9.253.195",
             "port": 7783,
             "session": 1508151804
         },
         {
             "ipaddr": "5.9.253.196",
             "port": 7783,
             "session": 0
         },
         {
             "ipaddr": "5.9.253.197",
             "port": 7783,
             "session": 0
         },
         {
             "ipaddr": "5.9.253.198",
             "port": 7783,
             "session": 0
         },
         {
             "ipaddr": "5.9.253.199",
             "port": 7783,
             "session": 0
         },
         {
             "ipaddr": "5.9.253.200",
             "port": 7783,
             "session": 0
         },
         {
             "ipaddr": "5.9.253.201",
             "port": 7783,
             "session": 0
         },
         {
             "ipaddr": "5.9.253.203",
             "port": 7783,
             "session": 0
         }
     ]

getpeersIP
^^^^^^^^^^

The ``./getpeersIP`` script prints all the connected nodes, their ``port`` and ``session`` number.

Sample File Contents:

.. code-block:: shell

	curl --url "http://5.9.253.195:7783" --data "{\"method\":\"getpeers\"}"
	curl --url "http://5.9.253.196:7783" --data "{\"method\":\"getpeers\"}"
	curl --url "http://5.9.253.197:7783" --data "{\"method\":\"getpeers\"}"
	curl --url "http://5.9.253.198:7783" --data "{\"method\":\"getpeers\"}"
	curl --url "http://5.9.253.199:7783" --data "{\"method\":\"getpeers\"}"
	curl --url "http://5.9.253.200:7783" --data "{\"method\":\"getpeers\"}"
	curl --url "http://5.9.253.201:7783" --data "{\"method\":\"getpeers\"}"
	curl --url "http://5.9.253.202:7783" --data "{\"method\":\"getpeers\"}"
	curl --url "http://5.9.253.203:7783" --data "{\"method\":\"getpeers\"}"
	curl --url "http://5.9.253.204:7783" --data "{\"method\":\"getpeers\"}"

Sample Output:

.. code-block:: json

	[{
	        "ipaddr": "5.9.253.195",
	        "port": 7783,
	        "session": 1508151804
	    },
	    {
	        "ipaddr": "5.9.253.196",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.197",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.198",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.199",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.200",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.201",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.203",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.202",
	        "port": 7783,
	        "session": 0
	    }
	]
	[{
	        "ipaddr": "5.9.253.196",
	        "port": 7783,
	        "session": 1508151807
	    },
	    {
	        "ipaddr": "5.9.253.195",
	        "port": 7783,
	        "session": 1508151804
	    },
	    {
	        "ipaddr": "5.9.253.197",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.198",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.199",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.200",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.201",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.203",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.202",
	        "port": 7783,
	        "session": 0
	    }
	]
	[{
	        "ipaddr": "5.9.253.197",
	        "port": 7783,
	        "session": 1508151808
	    },
	    {
	        "ipaddr": "5.9.253.195",
	        "port": 7783,
	        "session": 1508151804
	    },
	    {
	        "ipaddr": "5.9.253.196",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.198",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.199",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.200",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.201",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.203",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.202",
	        "port": 7783,
	        "session": 0
	    }
	]
	[{
	        "ipaddr": "5.9.253.198",
	        "port": 7783,
	        "session": 1508151809
	    },
	    {
	        "ipaddr": "5.9.253.195",
	        "port": 7783,
	        "session": 1508151804
	    },
	    {
	        "ipaddr": "5.9.253.196",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.197",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.199",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.200",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.201",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.203",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.202",
	        "port": 7783,
	        "session": 0
	    }
	]
	[{
	        "ipaddr": "5.9.253.199",
	        "port": 7783,
	        "session": 1508151809
	    },
	    {
	        "ipaddr": "5.9.253.195",
	        "port": 7783,
	        "session": 1508151804
	    },
	    {
	        "ipaddr": "5.9.253.196",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.197",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.198",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.200",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.201",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.203",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.202",
	        "port": 7783,
	        "session": 0
	    }
	]
	[{
	        "ipaddr": "5.9.253.200",
	        "port": 7783,
	        "session": 1508151812
	    },
	    {
	        "ipaddr": "5.9.253.195",
	        "port": 7783,
	        "session": 1508151804
	    },
	    {
	        "ipaddr": "5.9.253.196",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.197",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.198",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.199",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.201",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.203",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.202",
	        "port": 7783,
	        "session": 0
	    }
	]
	[{
	        "ipaddr": "5.9.253.201",
	        "port": 7783,
	        "session": 1508151813
	    },
	    {
	        "ipaddr": "5.9.253.195",
	        "port": 7783,
	        "session": 1508151804
	    },
	    {
	        "ipaddr": "5.9.253.196",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.197",
	        "po###barterDEX Trading###rt": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.198",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.199",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.200",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.203",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.202",
	        "port": 7783,
	        "session": 0
	    }
	]
	[{
	        "ipaddr": "5.9.253.202",
	        "port": 7783,
	        "session": 1508151814
	    },
	    {
	        "ipaddr": "5.9.253.195",
	        "port": 7783,
	        "session": 1508151804
	    },
	    {
	        "ipaddr": "5.9.253.196",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.197",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.198",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.199",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.200",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.201",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.203",
	        "port": 7783,
	        "session": 0
	    }
	]
	[{
	        "ipaddr": "5.9.253.203",
	        "port": 7783,
	        "session": 1508151814
	    },
	    {
	        "ipaddr": "5.9.253.195",
	        "port": 7783,
	        "session": 1508151804
	    },
	    {
	        "ipaddr": "5.9.253.196",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.197",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.198",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.199",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.200",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.201",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.202",
	        "port": 7783,
	        "session": 0
	    }
	]
	[{
	        "ipaddr": "5.9.253.197",
	        "port": 7783,
	        "session": 1506966021
	    },
	    {
	        "ipaddr": "5.9.253.195",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.196",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.199",
	        "port": 7783,
	        "session": 1506966023
	    },
	    {
	        "ipaddr": "5.9.253.201",
	        "port": 7783,
	        "session": 1506966027
	    },
	    {
	        "ipaddr": "5.9.253.202",
	        "port": 7783,
	        "session": 1506966028
	    },
	    {
	        "ipaddr": "5.9.253.200",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.203",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "5.9.253.198",
	        "port": 7783,
	        "session": 0
	    },
	    {
	        "ipaddr": "82.7.169.222",
	        "port": 7783,
	        "session": 0
	    }
	]


help
^^^^

The ``./help`` API will display a list of all the available API available on barterDEX and usage options.

Sample File Contents:

.. code-block:: shell

	#!/bin/bash
	source userpass
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"help\"}"

Sample Output:

.. code-block:: json

	{
        "result": " available localhost RPC commands: 
        setprice(base, rel, price, broadcast = 1)
        autoprice(base, rel, fixed, minprice, maxprice, margin, refbase, refrel, factor, offset) *
        goal(coin = * , val = < autocalc > )
        myprice(base, rel)
        enable(coin)
        disable(coin)
        notarizations(coin)
        statsdisp(starttime = 0, endtime = 0, gui = , pubkey = , base = , rel = )
        ticker(base = , rel = )
        tradesarray(base, rel, starttime = < now > -timescale * 1024, endtime = < now > , timescale = 60) - > [timestamp, high, low, open, close, relvolume, basevolume, aveprice, numtrades]
        pricearray(base, rel, starttime = 0, endtime = 0, timescale = 60) - > [timestamp, avebid, aveask, highbid, lowask]
        getrawtransaction(coin, txid)
        inventory(coin, reset = 0, [passphrase = ])
        lastnonce()
        buy(base, rel, price, relvolume, timeout = 10, duration = 3600, nonce)
        sell(base, rel, price, basevolume, timeout = 10, duration = 3600, nonce)
        withdraw(coin, outputs[])
        sendrawtransaction(coin, signedtx)
        swapstatus(pending = 0, fast = 0)
        swapstatus(coin, limit = 10)
        swapstatus(base, rel, limit = 10)
        swapstatus(requestid, quoteid, pending = 0, fast = 0)
        recentswaps(limit = 3)
        notarizations(coin)
        public API: getcoins()
        getcoin(coin)
        portfolio()
        getpeers()
        passphrase(passphrase, gui, netid = 0, seednode = )
        listunspent(coin, address)
        setconfirms(coin, numconfirms, maxconfirms = 6)
        trust(pubkey, trust)# positive to trust, 0 for normal, negative to blacklist
        balance(coin, address)
        balances(address)
        fundvalue(address = , holdings = [], divisor = 0)
        orderbook(base, rel, duration = 3600)
        getprices()
        inuse()
        getmyprice(base, rel)
        getprice(base, rel)
        //sendmessage(base=coin, rel=, pubkey=zero, <argjson method2>)
        //getmessages(firsti=0, num=100)
        //deletemessages(firsti=0, num=100)
        secretaddresses(prefix = 'secretaddress', passphrase, num = 10, pubtype = 60, taddr = 0)
        electrum(coin, ipaddr, port)
        snapshot(coin, height)
        snapshot_balance(coin, height, addresses[])
        dividends(coin, height, < args > )
        stop()
        bot_list()
        bot_statuslist()
        bot_buy(base, rel, maxprice, relvolume) - > botid
        bot_sell(base, rel, minprice, basevolume) - > botid
        bot_settings(botid, newprice, newvolume)
        bot_status(botid)
        bot_stop(botid)
        bot_pause(botid)
        calcaddress(passphrase, coin = KMD)
        convaddress(coin, address, destcoin)
        instantdex_deposit(weeks, amount, broadcast = 1)
        instantdex_claim()
        timelock(coin, duration, destaddr = (tradeaddr), amount)
        unlockedspend(coin, txid)
        opreturndecrypt(coin, txid, passphrase)
        getendpoint()
        jpg(srcfile, destfile, power2 = 7, password, data = , required, ind = 0)"}

jpg
^^^

barterDEX supports password encrypting data into a .jpg. The dest image is virtually indistinguishable from the original. Best to use a raw .jpg you created with a camera and not some file from the internet. As from the internet, it can be compared as to what bits are changed and in that case the encrypted rawdata will be visible.

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"password\":\"123\",\"ind\":3453,\"userpass\":\"$userpass\",\"method\":\"jpg\",\"srcfile\":\"/root/boost_1_64_0/libs/gil/doc/doxygen/images/monkey_steps.jpg\",\"destfile\":\"dest.jpg\",\"power2\":3,\"data\":\"68656c6c6f20776f726c64\",\"required\":88}"

To write into a .jpg file, specify password, srcfile, destfile, data (hexstring) and required number of bits, power2. The same values of power2, password and required are needed to extract the data. 

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"password\":\"123\",\"userpass\":\"$userpass\",\"method\":\"jpg\",\"srcfile\":\"dest.jpg\",\"power2\":3,\"required\":88}" 

Just the name of the image, power2 are required along with the password.

Sample Output:

.. code-block:: shell

	47007d0d6e91a7844e14f685153c71f57b20f79b3d0204009eb1bcef0000000000000000000000000000000067622f82d97186d2c561f7abd6880b8d692563b8c71b1ab299e525 encoded .71
	47007d0d6e91a7844e14f685153c71f57b20f79b3d0204009eb1bcef0000000000000000000000000000000067622f82d97186d2c561f7abd6880b8d692563b8c71b1ab299e525 restored
	68656c6c6f20776f726c64 VERIFIED decryption .11 ind.3453 msglen .71 required .568 New DCT coefficients successfully written to dest.jpg, capacity 35672 modifiedrows .1 / 114 emit .568 
	{
        "result": "success",
        "modifiedrows": 1,
        "outputfile": "dest.jpg",
        "power2": 3,
        "capacity": 35672,
        "required": 88,
        "ind": 65535,
        "decoded": "3a4e7dc2785e40d58b8784"
    }
	47007d0d6e91a7844e14f685153c71f57b20f79b3d0204009eb1bcef0000000000000000000000000000000067622f82d97186d2c561f7abd6880b8d692563b8c71b1ab299e525 restored {
        "result": "success",
        "modifiedrows": 0,
        "power2": 3,
        "capacity": 35672,
        "required": 88,
        "ind": 3453,
        "decoded": "68656c6c6f20776f726c64"
    }

millis
^^^^^^

``millis`` is a new debug API. James put the millis display in the swaploop, which is once per 10 minutes.

Sample File Content:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"millis\"}"

Sample Output:

.. image:: /_static/images/millis-sample-output.png
   :align: center
                      
notarizations
^^^^^^^^^^^^^

This script will display coin notarization status for a specified coin. Use the script like this ``./notarizations KMD``, ``./notarizations REVS``, etc.

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"notarizations\",\"coin\":\"$1\"}"

Sample Output:

.. code-block:: json

    {
        "result": "success",
        "coin": "KMD",
        "lastnotarization": 553573,
        "bestheight": 553578
    }

parselog
^^^^^^^^

``./parselog`` will parse the stats.log file, just the incremental since last time.

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"parselog\"}"

Sample Output:

.. code-block:: json

	{
	    "result": "success",
	    "newlines": 0,
	    "request": 0,
	    "reserved": 0,
	    "connect": 0,
	    "connected": 0,
	    "duplicates": 0,
	    "parse_errors": 0,
	    "uniques": 0,
	    "tradestatus": 0,
	    "unknown": 0
	}

passphrase
^^^^^^^^^^

This method helps the GUI build to take input of the passphrase and generate userpass. This is the second API to run in BarterDEX. On the first call it will display the userpass value at the top of output.

Sample File Content:

.. code-block:: shell

	#!/bin/bash
	source userpass
	source passphrase
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"1d8b27b21efabcd96571cd56f91a40fb9aa4cc623d273c63bf9223dc6f8cd81f\",\"method\":\"passphrase\",\"passphrase\":\"$passphrase\",\"gui\":\"nogui\"}"

sleep
^^^^^

``sleep`` API is to create a call with definite duration. What the below example scritps does is, it starts sleep async and it gets queued. While that is happening, we do 2 orderbooks, which immediately return. After 10 seconds the sleep is done and the normal command queue completes and the getcoin is executed. This changes the serialized nature of calls. So, it might destabilize things, but by being limited to orderbook and portfolio the risk is very small. New API can be added to the whitelisted fast calls, by testing it with a ``"fast":1``.

Sample file content:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"queueid\":1,\"userpass\":\"$userpass\",\"method\":\"sleep\",\"seconds\":10}" &
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"orderbook\",\"base\":\"REVS\",\"rel\":\"KMD\"}"
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"orderbook\",\"base\":\"REVS\",\"rel\":\"KMD\"}"
	curl --url "http://127.0.0.1:7783" --data "{\"queueid\":2,\"userpass\":\"$userpass\",\"method\":\"getcoin\",\"coin\":\"REVS\",\"rel\":\"KMD\"}"

stop
^^^^

This method will stop ``barterDEX``.

Sample File Content:

.. code-block:: shell

	#!/bin/bash
	source userpass
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"stop\"}"

trust
^^^^^

Make your pubkey trusted by using this ``./trust`` method. You need to add your pubkey after the command. If you want the pubkey to be not trusted use \"trust\":-1. -1 means dont trust, 1 means to trust. This API works immediately.

Sample File Contents:

.. code-block:: shell

	echo "usage: ./trust <pubkey>"
	source userpass
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"pubkey\":\"$1\",\"method\":\"trust\",\"trust\":1}"

Sample Output:

.. code-block:: shell

	usage: ./trust <pubkey>
	{"result":"success"}

trusted
^^^^^^^

This method will display the ``pubkey`` you made trusted. No need to edit the file.

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"trusted\"}"

Sample Output:

.. code-block:: shell

	[
  		"040f1d2d5d12027afa2cec30477312e225b0d24c77cc4aa08d3fffe51277b904"
	]

barterDEX Trading
-----------------

Default timeout for a trade is 10 seconds, which means if no response, must wait 10 seconds between trade requests. It will generate an error if Alice tries to submit a trade while a previous request is pending.

However if the other side responds, you can do another trade and we are seeing virtually instant responses from the live FR (Full Relay) nodes.

Trade Negotiation Sequence:
^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

	Alice submits a "request" to the Bob node.
	Now we are in a pending state for up to 10 seconds.
	Bob responds with a "reserved", which releases Alice from the pending state.
	For the request that comes back, Alice can reject it or accept it and send a "connect" message.
	Finally Bob returns a "connected" message and the atomic swap begins.

James has also added automated broadcast of any setprices, which will occur automatically when you do a buy/sell for the coin you are buying with, as long as you are not using Electrum.

To be a bob, you need the native coin. With the pruning of the orderbook to most recent 2 minutes, it required the setprice to be called regularly. 

This function is internalized, so a single setprice is all that is needed. If you want to "cancel" it you can setprice to 0. GUI can now post bob orders if you have native coins enabled.

Using the ``buy/sell`` api is a fill or kill (except partial fills are allowed) and to put a limit order, ``autoprice`` needs to be used. The ``autoprice`` is a bit tricky to use, make sure you don't make the example backwards.

Note: To fully cancel an autotrade, ``setprice 0`` needs to be called twice, once with ``base/rel`` and then with ``rel/base``, since there are actually 2 prices (bid and ask).

autoprice
^^^^^^^^^

``autoprice`` is a very powerful API and it allows you to specify the price for a specific trading pair that is automatically updated as the market price of it changes. barterDEX uses external price sources (Bittrex, Cryptopia, Coinmarketcap) to get up to date prices. You can use fixed price instead of ``margin`` or use autoprice based on coinmarketcap. For now, it is a relatively simple set of things you can do with the following fields (``base, rel, fixed, minprice, maxprice, margin, refbase, refrel, factor, offset``).

Sample File Contents:

.. code-block:: shell

	#!/bin/bash
	margin=0.05
	source userpass
	
	# KMD/BTC must be first as other prices depend on it
	#curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"autoprice\",\"base\":\"KMD\",\"rel\":\"BTC\",\"margin\":$margin,\"refbase\":\"komodo\",\"refrel\":\"coinmarketcap\"}"
	#curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"autoprice\",\"base\":\"BTC\",\"rel\":\"KMD\",\"fixed\":0.00025,\"margin\":$margin}"
	#curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"autoprice\",\"base\":\"KMD\",\"rel\":\"BTC\",\"fixed\":4000,\"margin\":$margin}"
	curl --url "http://127.0.0.1:7783" --data "{\"minprice\":0.0003,\"maxprice\":0.001,\"userpass\":\"$userpass\",\"method\":\"autoprice\",\"base\":\"KMD\",\"rel\":\"BTC\",\"margin\":0.05,\"refbase\":\"komodo\",\"refrel\":\"coinmarketcap\"}"
	
	./auto_chipskmd
	./auto_chipsbtc

	#curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"autoprice\",\"base\":\"KMD\",\"rel\":\"MNZ\",\"offset\":0.0,\"refbase\":\"KMD\",\"refrel\":\"BTC\",\"factor\":15000,\"margin\":-0.2}"
	
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"autoprice\",\"base\":\"HUSH\",\"rel\":\"KMD\",\"margin\":$margin,\"refbase\":\"hush\",\"refrel\":\"coinmarketcap\"}"
	#curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"autoprice\",\"base\":\"KMD\",\"rel\":\"BTCH\",\"offset\":0.0,\"refbase\":\"KMD\",\"refrel\":\"HUSH\",\"factor\":1.44,\"buymargin\":0.05,\"sellmargin\":0.05}"
	#curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"autoprice\",\"base\":\"BTCH\",\"rel\":\"KMD\",\"offset\":0.0,\"refbase\":\"HUSH\",\"refrel\":\"KMD\",\"factor\":0.7,\"buymargin\":0.05,\"sellmargin\":0.05}"

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"autoprice\",\"base\":\"BEER\",\"rel\":\"PIZZA\",\"fixed\":0.0001,\"margin\":0.00001}"
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"autoprice\",\"base\":\"BEER\",\"rel\":\"ETOMIC\",\"fixed\":10,\"margin\":0.00001}"

	source crypto
	source trackbtc

	#source jumblr
	#source trackbtc

	source pangea
	source trackbtc
	
	source bet
	source trackbtc
	
	#source revs
	#source trackbtc

	sharkholdings="{\"coin\":\"iota\",\"balance\":1500000}, {\"coin\":\"komodo\",\"balance\":120000}, {\"coin\":\"bitcoin-cash\",\"balance\":1200}, {\"coin\":\"bitcoin\",\"balance\":100}"
	curl --url "http://127.0.0.1:7783" --data "{\"base\":\"MSHARK\",\"rel\":\"KMD\",\"fundvalue_bid\":\"NAV_KMD\",\"fundvalue_ask\":\"assetNAV_KMD\",\"userpass\":\"$userpass\",\"method\":\"autoprice\",\"margin\":$margin,\"address\":\"RTu3JZZKLJTcfNwBa19dWRagEfQq49STqC\",\"holdings\":[$sharkholdings],\"divisor\":1400000}"

	curl --url "http://127.0.0.1:7783" --data "{\"margin\":$margin,\"base\":\"SUPERNET\",\"rel\":\"KMD\",\"fundvalue_bid\":\"NAV_KMD\",\"fundvalue_ask\":\"NAV_KMD\",\"userpass\":\"$userpass\",\"method\":\"autoprice\",\"address\":\"RRyyejME7LRTuvdziWsXkAbSW1fdiohGwK\",\"holdings\":[{\"coin\":\"iota\",\"balance\":11000000}, {\"coin\":\"stratis\",\"balance\":1300000}, {\"coin\":\"zcash\",\"balance\":0.10000}, {\"coin\":\"syscoin\",\"balance\":20000000}, {\"coin\":\"waves\",\"balance\":700000}, {\"coin\":\"bitcoin\",\"balance\":600}, {\"coin\":\"bitcoin-cash\",\"balance\":1500}, {\"coin\":\"heat-ledger\",\"balance\":2323851 }, {\"coin\":\"decred\",\"balance\":0.20000}, {\"coin\":\"vericoin\",\"balance\":2199368 }, {\"coin\":\"byteball\",\"balance\":4238}, {\"coin\":\"iocoin\",\"balance\":0.150000}, {\"coin\":\"quantum-resistant-ledger\",\"balance\":0.375000}, {\"coin\":\"chips\",\"balance\":2577006 }, {\"coin\":\"hush\",\"balance\":100000 }, {\"coin\":\"mobilego\",\"balance\":100000 }],\"divisor\":612529}"

	curl --url "http://127.0.0.1:7783" --data "{\"margin\":$margin,\"base\":\"HODL\",\"rel\":\"KMD\",\"fundvalue_bid\":\"assetNAV_KMD\",\"fundvalue_ask\":\"assetNAV_KMD\",\"userpass\":\"$userpass\",\"method\":\"autoprice\",\"address\":\"RNcUaMUEFLxVwtTo7rgruhwYanGk1jTkeU\",\"holdings\":[{\"coin\":\"siacoin\",\"balance\":185000000,\"comment\":\"using siafunds equal to million siacoin\"}],\"divisor\":10000000}"
	
	dexholdings="{\"coin\":\"blocknet\",\"balance\":2500000}"
	
	curl --url "http://127.0.0.1:7783" --data "{\"base\":\"DEX\",\"rel\":\"KMD\",\"margin\":$margin,\"fundvalue_bid\":\"assetNAV_KMD\",\"fundvalue_ask\":\"assetNAV_KMD\",\"userpass\":\"$userpass\",\"method\":\"autoprice\",\"address\":\"RThtXup6Zo7LZAi8kRWgjAyi1s4u6U9Cpf\",\"holdings\":[$dexholdings],\"divisor\":1000000}"

	curl --url "http://127.0.0.1:7783" --data "{\"base\":\"BOTS\",\"rel\":\"KMD\",\"margin\":$margin,\"fundvalue_bid\":\"assetNAV_KMD\",\"fundvalue_ask\":\"assetNAV_KMD\",\"userpass\":\"$userpass\",\"method\":\"autoprice\",\"address\":\"RNdqHx26GWy9bk8MtmH1UiXjQcXE4RKK2P\",\"holdings\":[$dexholdings],\"divisor\":3333333}"

	curl --url "http://127.0.0.1:7783" --data "{\"base\":\"JUMBLR\",\"rel\":\"KMD\",\"margin\":$margin,\"fundvalue_bid\":\"assetNAV_KMD\",\"fundvalue_ask\":\"assetNAV_KMD\",\"userpass\":\"$userpass\",\"method\":\"autoprice\",\"address\":\"RGhxXpXSSBTBm9EvNsXnTQczthMCxHX91t\",\"holdings\":[$dexholdings],\"divisor\":3333333}"

	curl --url "http://127.0.0.1:7783" --data "{\"base\":\"MGW\",\"rel\":\"KMD\",\"margin\":$margin,\"fundvalue_bid\":\"assetNAV_KMD\",\"fundvalue_ask\":\"assetNAV_KMD\",\"userpass\":\"$userpass\",\"method\":\"autoprice\",\"holdings\":[$dexholdings],\"divisor\":13000000}"

	curl --url "http://127.0.0.1:7783" --data "{\"base\":\"REVS\",\"rel\":\"KMD\",\"margin\":$margin,\"fundvalue_bid\":\"assetNAV_KMD\",\"fundvalue_ask\":\"assetNAV_KMD\",\"userpass\":\"$userpass\",\"method\":\"autoprice\",\"holdings\":[$dexholdings],\"divisor\":9000000}"

Sample Output:

::

	{
		  "result": "success"
	},
	{
		  "result": "success"
	}
	.......

Knowledge Base:
"""""""""""""""

``refbase`` and ``refrel`` allow you to specify a different base/rel pair as the basis for the price, if there is no ``refbase`` and ``refrel``, the the base/rel price from external sources is used as the starting point. This is calculated approximately once per minute and a set price done automatically:
::

	setprice of (1. + margin) * ((price * factor) + offset)

The margin is usually set to 0.01 for 1% profit margin. using factor and offset it is possible to map a starting price to a standard multiple.

There is also a minprice field which sets the absolute minimum (post calculation) price that is accepted.

Example ``autoprice`` script using coinmarketcap prices.
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"minprice\":0.00002,\"maxprice\":0.0001,\"userpass\":\"$userpass\",\"method\":\"autoprice\",\"base\":\"CHIPS\",\"rel\":\"BTC\",\"margin\":0.05,\"refbase\":\"chips\",\"refrel\":\"coinmarketcap\"}"

or

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"minprice\":0.04,\"maxprice\":0.1,\"userpass\":\"$userpass\",\"method\":\"autoprice\",\"base\":\"CHIPS\",\"rel\":\"KMD\",\"margin\":0.05,\"refbase\":\"chips\",\"refrel\":\"coinmarketcap\"}"

.. _autoprice-the-value-of-a-fund-using-the-fundvalue-api:

``autoprice`` the value of a fund, ie. using the ``fundvalue`` api
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The way to do is it start with the ``fundvalue`` api call, then change the ``method`` to ``autoprice``. Add ``base`` and ``rel`` and most importantly ``fundvalue_bid`` and ``fundvalue_ask`` that will be values in the return of the fundvalue call. Additionally, ``margin`` is applied. This sounds complicated and it is, but now MSHARK, HODL and even SUPERNET are running using this autoprice. The following sample content is an example how to use it.

Sample File Content:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"base\":\"MSHARK\",\"rel\":\"KMD\",\"fundvalue_bid\":\"NAV_KMD\",\"fundvalue_ask\":\"assetNAV_KMD\",\"userpass\":\"$userpass\",\"method\":\"autoprice\",\"address\":\"RTu3JZZKLJTcfNwBa19dWRagEfQq49STqC\",\"holdings\":[{\"coin\":\"iota\",\"balance\":5000000}],\"divisor\":1400000}"

Sample Output:

.. code-block:: json

	{
		"result":"success"
	}

.. _autoprice-using-usdpeg:

autoprice using usdpeg
""""""""""""""""""""""

There is a way for autoprice coinmarketcap to do USD pegs for orderbooks denominated in any coin. The syntax is pretty arbitrary but it works.

Make sure the ``usdpeg`` is set to non-zero. In that case put in the orderbook BACKWARDS (dont ask me why, it just works only in this way) for the coin that is the coinmarketcap refbase. Based on the example it is KMD so base KMD and rel OOT, will create OOT/KMD orderbooks using factor 0.15 (fifteen cents) denominated in KMD. The example script used different margins for buymargin and sellmargin, so it works for dICO scenario (allow people to sell back but at a steep loss) and also it is backwards (dont ask me why).

What this means is if you do a base DOGE rel OOT and refbase dogecoin, it should maintain an orderbook in DOGE pegged to the 15 cents price. Any CMC coin can be used. If you want to change the price, change the value of ``factor`` accordingly.

Sample File Content:

.. code-block:: shell

	#!/bin/bash
	source userpass
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"autoprice\",\"base\":\"KMD\",\"rel\":\"OOT\",\"factor\":0.15,\"buymargin\":0.0001,\"sellmargin\":0.2,\"refbase\":\"komodo\",\"refrel\":\"coinmarketcap\",\"usdpeg\":1}"

Sample Output:

.. code-block:: json

	{
		"result":"success"
	}

buy
^^^

In simple terms, this command will post a buy order. If there is a matching order in the orderbooks, then this will automatically start a trade. If a match is not found, a bid order will be added in the orderbook. Buy fills asks from the orderbook using relvolume. Trade request will last as long as defined in the 'timeout' field.

Call 'recentswaps' to check the status of the trade request. Alice side does not give feedback about expired trade request, unless a 'recentswaps' call is done.

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"buy\",\"base\":\"MNZ\",\"rel\":\"KMD\",\"relvolume\":0.005,\"price\":0.172}"

Knowledge Base:
"""""""""""""""

``base:`` the currency you want to buy ``rel:`` the currency you are paying with ``price:`` the max price you are willing to pay for 1 base ``relvolume:`` the amount of rel you want to trade ``timeout:`` the amount of time Alice or Bob should wait for payment. Default: 10 seconds (might be deprecated in future) ``duration:`` after the specified duration it wont be displayed

Sample Output:

.. code-block:: json

    {
        "result": "success",
        "swaps": [
            [
                45030989,
                41860326
            ],
            [
                264022270,
                1424922977
            ],
            [
                3882191272,
                3366340834
            ]
        ],
        "pending": {
            "expiration": 1509564162,
            "timeleft": 15,
            "requestid": 0,
            "quoteid": 0,
            "bob": "MNZ",
            "base": "MNZ",
            "basevalue": 0.02803687,
            "alice": "KMD",
            "rel": "KMD",
            "relvalue": 0.0048,
            "aliceid": 7785695213943587000
        }
    }

electrum
^^^^^^^^

This method enables a coin by connecting to the specified electrumx server. For this method running a native node and blockchain download is not necessary. You need to edit the file with coin name and IP address and port for the coin. For a list of electrumx server check this link http://pad.supernet.org/electrum-servers

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"electrum\",\"coin\":\"KMD\",\"ipaddr\":\"electrum1.cipig.net\",\"port\":10001}"
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"electrum\",\"coin\":\"MNZ\",\"ipaddr\":\"electrum1.cipig.net\",\"port\":10002}"
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"electrum\",\"coin\":\"REVS\",\"ipaddr\":\"electrum1.cipig.net\",\"port\":10003}"
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"electrum\",\"coin\":\"JUMBLR\",\"ipaddr\":\"electrum1.cipig.net\",\"port\":10004}"
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"electrum\",\"coin\":\"SUPERNET\",\"ipaddr\":\"electrum1.cipig.net\",\"port\":10005}"
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"electrum\",\"coin\":\"DEX\",\"ipaddr\":\"electrum1.cipig.net\",\"port\":10006}"
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"electrum\",\"coin\":\"BOTS\",\"ipaddr\":\"electrum1.cipig.net\",\"port\":10007}"
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"electrum\",\"coin\":\"CRYPTO\",\"ipaddr\":\"electrum1.cipig.net\",\"port\":10008}"
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"electrum\",\"coin\":\"HODL\",\"ipaddr\":\"electrum1.cipig.net\",\"port\":10009}"

getfee
^^^^^^

``getfee`` API will display network tx fee based on that time. This should only be required for BTC, all other coins are hardcoded.

Sample file content:

.. code-block:: shell

	#!/bin/bash
	source userpass
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":	\"$userpass\",\"method\":\"getfee\",\"coin\":\"BTC\"}"

Sample file output:

.. code-block:: json

	{
		"result":"success",
		"coin":"BTC",
		"txfee":0.00020000
	}

getprices
^^^^^^^^^

The ``./getprices`` API lists all currently available trading pairs and its current prices. You need to specify a ``base`` and ``rel`` coin if you need a specific pair price.

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"getprices\",\"coin\":\"KMD\"}"

Sample Output:

.. code-block:: json

    [{
        "pubkey": "040f1d2d5d12027afa2cec30477312e225b0d24c77cc4aa08d3fffe51277b904",
        "rmd160": "8784673d815a20300412a9010b72e771963d45b6",
        "pubsecp": "03829863f4ed7660fbf62b2f84b0e655f523a33f23a1f681107d2a2942987584b1",
        "timestamp": 1508160175,
        "asks": [
            [
                "BTC",
                "KMD",
                3304.53174512
            ],
            [
                "KMD",
                "BTC",
                0.00030268
            ],
            [
                "KMD",
                "REVS",
                0.78551134
            ],
            [
                "KMD",
                "JUMBLR",
                0.10432527
            ],
            [
                "KMD",
                "HUSH",
                1.17931676
            ],
            [
                "REVS",
                "KMD",
                1.29051134
            ],
            [
                "JUMBLR",
                "KMD",
                9.77904977
            ],
            [
                "HUSH",
                "KMD",
                0.86507888
            ]
        ]
    }]

goal
^^^^

The ``./goal`` command is basically the automatic trading tool of the API. When you execute this command, orders will be set until the goals are reached. The idea is that you set the goal for each coin and if you have more than the goal for a specific coin, it will allow sales of that coin. If you have less than the goal percentage, it will allow buys of that coin.

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"goal\",\"coin\":\"KMD\",\"val\":99}"
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"goal\",\"coin\":\"BTC\",\"val\":10}"
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"goal\",\"coin\":\"REVS\",\"val\":1}"

Sample Output:

.. code-block:: json

    {
        "result": "success",
        "kmd_equiv": 29.03290329,
        "buycoin": "KMD",
        "buyforce": 125.75072424,
        "sellcoin": "DGB",
        "sellforce": -412.28377122,
        "portfolio": [{
                "coin": "BTC",
                "address": "15XAhHK4ULofD6BTckrCWK6XSkCjscX7jj",
                "amount": 0,
                "price": 3315.35638637,
                "kmd_equiv": 0,
                "perc": 0,
                "goal": 10,
                "goalperc": 9.09090909,
                "relvolume": 0,
                "force": 82.6446281,
                "balanceA": 0,
                "valuesumA": 0,
                "balanceB": 0,
                "valuesumB": 0,
                "balance": 0
            },
            {
                "coin": "KMD",
                "address": "RDoMmoCM5AcEH6Yf5vqKbqRjD1fLcQHuWb",
                "amount": 22.87390295,
                "price": 1,
                "kmd_equiv": 22.87390295,
                "perc": 78.78613696,
                "goal": 99,
                "goalperc": 90,
                "relvolume": 0,
                "force": 125.75072424,
                "balanceA": 22.6448,
                "valuesumA": 22.87390295,
                "aliceutil": 98.99840901,
                "balanceB": 22.6448,
                "valuesumB": 22.87390295,
                "balance": 22.87390295,
                "bobutil": 98.99840901
            },
            {
                "coin": "DGB",
                "address": "D9fGEYFhmkhwk6N4MLqm45G8Ksw3E2AmTR",
                "amount": 919,
                "price": 0.00670185,
                "kmd_equiv": 6.15900034,
                "perc": 21.21386304,
                "goal": 1,
                "goalperc": 0.90909091,
                "relvolume": 186.60085587,
                "force": -412.28377122,
                "balanceA": 479.499,
                "valuesumA": 919,
                "aliceutil": 52.17616975,
                "balanceB": 479.499,
                "valuesumB": 919,
                "balance": 919,
                "bobutil": 52.17616975
            }
        ]
    }

goals
^^^^^

Displays the goal percentage for each coin and their status.

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"goal\"}"

Sample Output:

.. code-block:: json

    {
        "result": "success",
        "kmd_equiv": 28.98048555,
        "buycoin": "BTC",
        "buyforce": 625,
        "sellcoin": "KMD",
        "sellforce": -2908.30091422,
        "base": "BTC",
        "rel": "KMD",
        "relvolume": 12.33191136,
        "portfolio": [{
                "coin": "BTC",
                "address": "15XAhHK4ULofD6BTckrCWK6XSkCjscX7jj",
                "amount": 0,
                "price": 3321.5219084,
                "kmd_equiv": 0,
                "perc": 0,
                "goal": 25,
                "goalperc": 25,
                "relvolume": 0,
                "force": 625,
                "balanceA": 0,
                "valuesumA": 0,
                "balanceB": 0,
                "valuesumB": 0,
                "balance": 0
            },
            {
                "coin": "KMD",
                "address": "RDoMmoCM5AcEH6Yf5vqKbqRjD1fLcQHuWb",
                "amount": 22.87391037,
                "price": 1,
                "kmd_equiv": 22.87391037,
                "perc": 78.92866505,
                "goal": 25,
                "goalperc": 25,
                "relvolume": 12.33559451,
                "force": -2908.30091422,
                "balanceA": 22.6448,
                "valuesumA": 22.87391037,
                "aliceutil": 98.9983769,
                "balanceB": 22.6448,
                "valuesumB": 22.87391037,
                "balance": 22.87391037,
                "bobutil": 98.9983769
            },
            {
                "coin": "ZEC",
                "address": "t1NPmhcjCSfbFojEMZBfKe8CShQPpkcn4W7",
                "amount": 0,
                "price": 135.89703925,
                "kmd_equiv": 0,
                "perc": 0,
                "goal": 25,
                "goalperc": 25,
                "relvolume": 0,
                "force": 625,
                "balanceA": 0,
                "valuesumA": 0,
                "balanceB": 0,
                "valuesumB": 0,
                "balance": 0
            },
            {
                "coin": "DGB",
                "address": "D9fGEYFhmkhwk6N4MLqm45G8Ksw3E2AmTR",
                "amount": 919,
                "price": 0.0066448,
                "kmd_equiv": 6.10657518,
                "perc": 21.07133495,
                "goal": 25,
                "goalperc": 25,
                "relvolume": 0,
                "force": 15.43440909,
                "balanceA": 479.499,
                "valuesumA": 919,
                "aliceutil": 52.17616975,
                "balanceB": 479.499,
                "valuesumB": 919,
                "balance": 919,
                "bobutil": 52.17616975
            }
        ]
    }

myprice
^^^^^^^

Shows number of bids andprices you set for a given coin. Your wallet must be active to display the prices.

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"myprice\",\"base\":\"REVS\",\"rel\":\"KMD\"}"

Sample Output:

.. code-block:: json

	{
	  "base": "REVS",
	  "rel": "KMD",
	  "bid": 2,
	  "ask": 0
	}

myprices
^^^^^^^^

``./myprices`` shows numer of bids and ask for your ``./buy`` coin pair.

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"myprices\"}"

Sample Output:

.. code-block:: json

    [{
            "base": "KMD",
            "rel": "REVS",
            "bid": 0,
            "ask": 0.5
        },
        {
            "base": "REVS",
            "rel": "KMD",
            "bid": 2,
            "ask": 0
        }
    ]

orderbook
^^^^^^^^^

Displays bid/ask for a specific coin/asset pair. You can display multiple pairs, just need to edit the file and add more line. The ``numutxos/minvolume/maxvolume`` are the state of your local ``utxo`` cache. It might or might not be 100% accurate. Also, if all ``0``'s it could be that it hasn't been queried yet. Even if all zeros, it is possible, even likely that there are actually ``utxo`` available.

If you do an ``./orderbook``, it will start fetching the details from the best prices. You can do ``listunspent`` for a specific address, but it is not possible to know for sure what trades are possible, especially as there are other nodes that might be going after the same ``utxo``. Specifically doing a ``listunspent`` api will also fetch the details, also doing a trade will fetch the details as well. James uses just in time fetching to get the ``utxo`` data. This way we don't flood the network with data for ``utxo`` info.

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"orderbook\",\"base\":\"DGB\",\"rel\":\"KMD\"}"

Sample Output:

.. code-block:: json

    {
        "bids": [
            {
                "coin": "KMD",
                "address": "RB8yufv3YTfdzYnwz5paNnnDynGJG6WsqD",
                "price": 0.00492739,
                "numutxos": 13,
                "minvolume": 0.072,
                "maxvolume": 0.76,
                "pubkey": "8adbf9d5de4fb49ec1fca9ca3f28ba384715752de1197c9cddbb756c3d2a1a7c",
                "age": 16
            },
            {
                "coin": "KMD",
                "address": "RHPBQQpjVqpwWC8NrpAxdoRQAkigA2zjRo",
                "price": 0.00487791,
                "numutxos": 5,
                "minvolume": 0.00016002,
                "maxvolume": 96,
                "pubkey": "22aaf8e3686d31ee9f5ebe61c97231114717aee943ef01cc58e9f843ddad0240",
                "age": 53
            }
        ],
        "numbids": 2,
        "asks": [
            {
                "coin": "DGB",
                "address": "D6ztNQyQF3mMTYcMFVq1q2cd6eXzqPKGc8",
                "price": 0.00532946,
                "numutxos": 38,
                "minvolume": 0.00586622,
                "maxvolume": 2.20800448,
                "pubkey": "8adbf9d5de4fb49ec1fca9ca3f28ba384715752de1197c9cddbb756c3d2a1a7c",
                "age": 16
            },
            {
                "coin": "DGB",
                "address": "DDF5s9t6CRveyBwn8EBQ63FoHczNsyFsFi",
                "price": 0.0053779,
                "numutxos": 3,
                "minvolume": 0.67844886,
                "maxvolume": 7.06141621,
                "pubkey": "22aaf8e3686d31ee9f5ebe61c97231114717aee943ef01cc58e9f843ddad0240",
                "age": 53
            }
        ],
        "numasks": 2,
        "base": "DGB",
        "rel": "KMD",
        "timestamp": 1508410319
    }

portfolio
^^^^^^^^^

Shows all active coin information and value. Such as, smartaddress, balance, current price per coin in barterDEX, KMD equivalent balance, percentage of your portfolio goal. You don’t need to edit or change the script for it work. It will get information from your active wallets and display them.

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"portfolio\"}"

Sample Output:

.. code-block:: json

    {
        "result": "success",
        "kmd_equiv": 29.09215302,
        "buycoin": "KMD",
        "buyforce": 129.37341083,
        "sellcoin": "DGB",
        "sellforce": -418.82246271,
        "base": "ZEC",
        "rel": "DGB",
        "relvolume": 189.62190318,
        "portfolio": [
            {
                "coin": "BTC",
                "address": "15XAhHK4ULofD6BTckrCWK6XSkCjscX7jj",
                "amount": 0,
                "price": 3351.92820521,
                "kmd_equiv": 0,
                "perc": 0,
                "goal": 10,
                "goalperc": 9.09090909,
                "relvolume": 0,
                "force": 82.6446281,
                "balanceA": 0,
                "valuesumA": 0,
                "balanceB": 0,
                "valuesumB": 0,
                "balance": 0
            },
            {
                "coin": "KMD",
                "address": "RDoMmoCM5AcEH6Yf5vqKbqRjD1fLcQHuWb",
                "amount": 22.87392545,
                "price": 1,
                "kmd_equiv": 22.87392545,
                "perc": 78.62575669,
                "goal": 99,
                "goalperc": 90,
                "relvolume": 0,
                "force": 129.37341083,
                "balanceA": 22.6448,
                "valuesumA": 22.87392545,
                "aliceutil": 98.99831163,
                "balanceB": 22.6448,
                "valuesumB": 22.87392545,
                "balance": 22.87392545,
                "bobutil": 98.99831163
            },
            {
                "coin": "DGB",
                "address": "D9fGEYFhmkhwk6N4MLqm45G8Ksw3E2AmTR",
                "amount": 919,
                "price": 0.0067663,
                "kmd_equiv": 6.21822757,
                "perc": 21.37424331,
                "goal": 1,
                "goalperc": 0.90909091,
                "relvolume": 188.07475055,
                "force": -418.82246271,
                "balanceA": 479.499,
                "valuesumA": 919,
                "aliceutil": 52.17616975,
                "balanceB": 479.499,
                "valuesumB": 919,
                "balance": 919,
                "bobutil": 52.17616975
            }
        ]
    }

sell
^^^^

This script is completely opposite of ``buy`` and uses the same parameters. Edit the file with specific coin pair name, volume and price.

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"sell\",\"base\":\"KMD\",\"rel\":\"BTC\",\"basevolume\":10.0,\"price\":0.0005}"

Sample Output:

.. code-block:: json

	{
	  	"result": "success"
	}

setconfirms
^^^^^^^^^^^

This will allow each node to set the number of required confirms on a coin by coin basis. During the atomic swap, each side sends to the other the required confirms and the "protocol" is that both sides use the bigger value.

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"setconfirms\",\"coin\":\"DGB\",\"numconfirms\":1}"

Sample Output:

.. code-block:: json

	{
		  "result": "success"
	}

setprice
^^^^^^^^

To create a bob ``utxo`` (or an ask order) you need to first set the price. To set price you need to edit the ``./setprice`` script in the ``dexscripts`` folder

Note: To fully cancel an autotrade, ``setprice 0`` needs to be called twice, once with ``base/rel`` and then with ``rel/base``, since there are actually 2 prices (bid and ask). Doing ``setprice 0`` for an order made with ``coinmarketcap api`` call doesn't end it. It is likely as it has two ``0``'s and you can only set one ``0`` at a time. The only way to stop an order made with ``coinmarketcap api`` is to kill ``marketmaker``.

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"setprice\",\"base\":\"KMD\",\"rel\":\"REVS\",\"price\":0.5}"

Sample Output:

.. code-block:: json

	{
  		"result": "success"
	}

fomo
^^^^

``fomo`` Fear of missing out API will allow you buy for your specified relvol at the best current orderbook price. Orderbook has to be visible for this API to work. When using ``fomo`` you won't get the best price. No need to ``fomo`` if you are able to do normal ordermatch. It adds 5% to the orderbook entry that is the biggest that fits.

Sample file content:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"buy\",\"base\":\"KMD\",\"rel\":\"HODL\",\"fomo\":40.00038}"

dump
^^^^

As the name suggests, you can use ``dump`` API to dump the coins you want to at current orderbook price. Orderbook has to be visible for this API to work.

Sample file content:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"sell\",\"base\":\"KMD\",\"rel\":\"HODL\",\"dump\":40.00038}"

pubkeystats
^^^^^^^^^^^
Sample File Content:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"statsdisp\",\"starttime\":0,\"endtime\":0,\"pubkey\":\"a2593155464e37fcc88245780240a412a38cf3d316809445aad73f4e7789187d\"}"

Status/Info
-----------

getendpoint
^^^^^^^^^^^

There is a new websockets realtime events to the barterDEX API family, ``getendpoint``. It returns a nanomsg NN_PAIR endpoint that if you connect to it. You get an event stream, with hopefully all the relevant events, especially about the change in state of swap. The even stream is started as soon as the ``getendpoint`` API is called.

There is also a new mode for marketmaker: ``./marketmaker events`` which we should run in a new terminal. This should connect to the endpoint created by ``getendpoint`` API call. This will simply launch a new process and printout all the events. It will be like the console spew of printouts so you might want to ``nohup`` it and then ``grep`` to find things. This allows GUI to be done in an event driven way. Any command can add a ``"queueid":nn`` with a non-zero ``nn`` and it will queue the command. Its completion will arrive in the nanomsg event stream with the ``queueid`` and the result.

Sample File Content:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"getendpoint\"}"

Sample Output:

.. code-block:: json

    {
        "result": "success",
        "endpoint": "ws://127.0.0.1:5555",
        "socket": 20,
        "sockopt": 0
    }

pendings
^^^^^^^^

``./pendings`` is a special case of ``statsdisp`` and will display all the pending swaps. Using ``recentswaps`` API is better suitable for most usecases.

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"statsdisp\",\"starttime\":2000000000,\"endtime\":2000000000}"

Sample Output:

.. code-block:: json

    {
        "result": "success",
        "newlines": 0,
        "swaps": [
            {
                "aliceid": "7276253190735921153",
                "src": "30eb3d952f66eba2df0100b97d6707257cf91dc8c8b0237cfb7c3aa70dc52d4d",
                "base": "REVS",
                "basevol": 0.13338748,
                "dest": "1282417c4e7d5bb870067f5c05ffe87a0d8c8ce9956befff560e92b7c8d23741",
                "rel": "KMD",
                "relvol": 0.1505,
                "price": 1.12913831,
                "requestid": 2339417255,
                "quoteid": 1177391651,
                "line": "2017-10-30T16:16:00Z (nogui).(nogui) 0    connected    7276253190735921153: (0.13338748  REVS) -> (0.15050000   KMD) 1.12913831 finished.0 expired.0"
            }
        ],
        "volumes": [
            {
                "coin": "KMD",
                "srcvol": 0,
                "destvol": 0.1505,
                "numtrades": 1,
                "total": 0.1505
            },
            {
                "coin": "REVS",
                "srcvol": 0.13338748,
                "destvol": 0,
                "numtrades": 1,
                "total": 0.13338748
            }
        ],
        "request": 4,
        "reserved": 2,
        "connect": 4,
        "connected": 1,
        "duplicates": 4,
        "parse_errors": 0,
        "uniques": 1,
        "tradestatus": 0,
        "unknown": 0
    }

swapstatus
^^^^^^^^^^

This will display the swap status for your trades along with ``requestid`` and ``quoteid``. This API also helps unstuck swaps and help claim funds if the swap wasn't successfully completed. In order to claim stuck funds, remove all ``.finished`` file, start barterDEX, add coins and issue this script.

These available API options are described below:

::

	swapstatus(pending=0)
	swapstatus(coin, limit=10)
	swapstatus(base, rel, limit=10)
	swapstatus(requestid, quoteid, pending=0)

The base/rel swapstatus will scan ALL your historical swaps and that could take a very long time. There is a new parameter for the ``swapstatus`` API, ``fast:1``. You can use this flag with swapstatus for ``base/rel``, ``requestid/quoteid`` for faster and optimised performance while getting the response. 2 different example scripts:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"pending\":1,\"userpass\":\"$userpass\",\"method\":\"swapstatus\", \"base\":\"CHIPS\", \"rel\":\"KMD\", \"fast\":1}"

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"swapstatus\",\"requestid\":2291973695,\"quoteid\":3387529385}, \"fast\":1}"

This is very helpful when you have so many swap files in DB/SWAPS dir.

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"swapstatus\"}"

Sample Output:

.. code-block:: json

    {
        "result": "success",
        "swaps": [
            {
                "status": "realtime",
                "requestid": 157581336,
                "quoteid": 2717912442
            },
            {
                "status": "realtime",
                "requestid": 2050117881,
                "quoteid": 263483411
            }
        ]
    }

pendingswaps
^^^^^^^^^^^^

This way you can see what swaps are still pending. This uses ``pending=1`` arg to ``swapstatus`` method.

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"swapstatus\",\"pending\":1}"

Sample Output:

.. code-block:: json

        {
            "result": "success",
            "swaps": [
                {
                    "expiration": 1512738286,
                    "tradeid": 4038861795,
                    "requestid": 1887485571,
                    "quoteid": 2755902417,
                    "iambob": 0,
                    "Bgui": "",
                    "Agui": "nogui",
                    "gui": "nogui",
                    "bob": "BTC",
                    "srcamount": 0.02555775,
                    "bobtxfee": 0.00212221,
                    "alice": "KMD",
                    "destamount": 95,
                    "alicetxfee": 0.0001,
                    "aliceid": "9807693779256541185",
                    "sentflags": [
                        "bobspend",
                        "bobpayment",
                        "alicepayment",
                        "bobdeposit",
                        "myfee",
                        "bobrefund"
                    ],
                    "values": [
                        0.02343554,
                        0,
                        0.02555775,
                        95.0002,
                        0.02875246,
                        0,
                        0.12226512,
                        0.0279102,
                        0,
                        0,
                        0
                    ],
                    "result": "success",
                    "status": "finished",
                    "finishtime": 1512839121,
                    "bobdeposit": "ec1e73395a7bd855bcf3afe58b0b1d478532ef398f2df68d2d10424e9d36743f",
                    "alicepayment": "d3edb95bb9f3bd898f8b655398c5ab0ae86bc90d14176068096b6111eb201a05",
                    "bobpayment": "9ff00880871d1474474378a4b9fc445ec13367be51a7b797a3cc76c1c4da52b6",
                    "paymentspent": "0000000000000000000000000000000000000000000000000000000000000000",
                    "Apaymentspent": "1fd16aaf9a41e44efe30bf01087470b9db3cf287b0b7a2634b25b97601e2acda",
                    "depositspent": "27d774b0765eee97f7423785a4c80d3cea36adaccb5fa9f4fa5fe0e8fa68bfbe",
                    "method": "tradestatus"
                }
            ]
        }

coinswaps
^^^^^^^^^

This method uses ``swapstatus`` for a spcific coin.

Sample File Content:

.. code-block:: shell

	#!/bin/bash
	source userpass
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"swapstatus\",\"coin\":\"CHIPS\"}"

baserelswaps
^^^^^^^^^^^^

This method uses the ``swapstatus`` API and displays base/rel swapstatus. 

Sample File Content:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"swapstatus\",\"base\":\"MNZ\",\"rel\":\"KMD\"}"

.. _swapstatus-requestid-quoteid-pending:

``swapstatus(requestid, quoteid, pending=0)``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can get more information about the swaps by quering with ``requestid`` and ``quoteid``. This API helps query about stuck swap and helps them unstuck. The sample file looks like below. ``pending=0`` is optional.

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"swapstatus\",\"requestid\":157581336,\"quoteid\":2717912442}"

The sample result is below:

.. code-block:: json

    {
        "requestid": 157581336,
        "quoteid": 2717912442,
        "iambob": 0,
        "bob": "REVS",
        "srcamount": 1.79816276,
        "bobtxfee": 0.0001,
        "alice": "KMD",
        "destamount": 2,
        "alicetxfee": 0.0001,
        "sentflags": [
            "alicespend",
            "bobpayment",
            "alicepayment",
            "bobdeposit",
            "myfee"
        ],
        "values": [
            1.79806276,
            0,
            1.79816276,
            2.0001,
            2.0229331,
            0,
            0.002674,
            0,
            0,
            0,
            0
        ],
        "result": "success",
        "status": "finished",
        "bobdeposit": "6f36a465184f9c2a377dc7a338ff24c1096c97a7cc13aa3a8e3cf2bd46d88c03",
        "alicepayment": "7221eb0ac7cb9985cd580d82310a1f95b4e47617597c1b747d7840e776d73a93",
        "bobpayment": "7a05b28041b112178ecf5d532a18ff8e75d280fec8a7bc4511fce0215a3c66d3",
        "paymentspent": "9a541250257346de1b7d5b4ca11814b2df7098b750af23d0fad5b245c5435110",
        "Apaymentspent": "0000000000000000000000000000000000000000000000000000000000000000",
        "depositspent": "0000000000000000000000000000000000000000000000000000000000000000"
    }

recentswaps
^^^^^^^^^^^

This api returns up to "limit" in reverse order the swaps on the node and the current pending swap (if any) so you can see what trade might happen.

'limit' = the number of latest swaps to be visible in output.

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"recentswaps\",\"limit\":1}"

Sample Output:

.. code-block:: json

    {
        "result": "success",
        "swaps": [
            [
                2779577435,
                2461904533
            ],
            [
                932852928,
                3189912026
            ]
        ],
        "pending": {
            "expiration": 1508343494,
            "timeleft": 5,
            "base": "",
            "basevalue": 0,
            "rel": "",
            "relvalue": 0
        }
    }

TradeBots
---------

bot_buy
^^^^^^^

Starts a auto tradebot to do the trading for you. ``maxprice`` is the highest price you want to pay for 1 base, ``relvolume`` is the total amount of coins you want to spend.

Sample file contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"bot_buy\",\"base\":\"MNZ\",\"rel\":\"KMD\",\"maxprice\":3,\"relvolume\":10.0}"

Sample output:

.. code-block:: json

    {
        "result": "success",
        "name": "buy_MNZ_KMD.1509539940",
        "botid": 3601212692,
        "started": 1509539940,
        "action": "buy",
        "base": "MNZ",
        "rel": "KMD",
        "maxprice": 3,
        "totalrelvolume": 10,
        "totalbasevolume": 3.33333333,
        "trades": []
    }

bot_list
^^^^^^^^

This script will display a list of all ``botid``\ s that you used.

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"bot_list\"}"

Sample Output:

::

	[
	  2833291137,
	  3601212692,
	  2712409213
	]

bot_pause
^^^^^^^^^

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"bot_pause\",\"botid\":$1}"

Sample usage: ``./bot_resume 3601212692`` # here **3601212692** is the ``botid`` from ``./bot_buy`` or ``./bot_sell`` script output.

Sample Output:

.. code-block:: json

	{
		"result":"success"
	}

bot_resume
^^^^^^^^^^

Resumes a paused tradebot.

Sample file contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"bot_resume\",\"botid\":$1}"

Sample Usage: ``./bot_resume 3601212692`` # here **3601212692** is the ``botid`` from ``./bot_buy`` or ``./bot_sell`` script output.

Sample Output:

.. code-block:: json

    {
        "result": "success"
    }

bot_sell
^^^^^^^^

Place a sell order using tradebots. ``minprice`` is the lowest you will sell for 1 coin, ``basevolume`` is the total amount of coins you want to sell.

Sample file contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"bot_sell\",\"base\":\"REVS\",\"rel\":\"KMD\",\"minprice\":2,\"basevolume\":5.0}"

Sample Output:

.. code-block:: json

    {
        "result": "success",
        "name": "sell_MNZ_KMD.1509549405",
        "botid": 2247122510,
        "started": 1509549405,
        "action": "sell",
        "base": "MNZ",
        "rel": "KMD",
        "minprice": 2,
        "totalbasevolume": 5,
        "totalrelvolume": 10,
        "trades": []
    }

bot_settings
^^^^^^^^^^^^

``./bot_settings`` allows you to change price or volume after starting the ``bot_buy`` or ``bot_sell``.

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"bot_settings\",\"botid\":$1,\"newprice\":$1,\"newvolume\":$2}"

Sample Usage:

``./bot_settings 2247122510 3 6`` # here **2247122510** is ``botid`` and 3 is the ``new price``, 6 is the ``new volume``

Sample Outputs:

.. code-block:: json

    {
        "result": "success",
        "name": "sell_MNZ_KMD.1509549405",
        "botid": 2247122510,
        "started": 1509549405,
        "paused": 1509549517,
        "action": "sell",
        "base": "MNZ",
        "rel": "KMD",
        "minprice": 2247122510,
        "totalbasevolume": 0,
        "totalrelvolume": 3,
        "aveprice": 2,
        "volume": 4,
        "trades": [
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {}
        ],
        "completed": 4,
        "percentage": 149808167333.3333,
        "pending": 6,
        "pendingprice": 2,
        "pendingvolume": 6
    }

bot_status
^^^^^^^^^^

Tradebot status. Use ``botid`` after the ``./bot_status`` script.

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"bot_status\",\"botid\":$1}"

Sample Usage: ``./bot_status 3601212692`` # here **3601212692** is the ``botid`` from ``./bot_buy`` or ``./bot_sell`` script output.

Sample Output:

.. code-block:: json

    {
        "result": "success",
        "name": "buy_MNZ_KMD.1509542273",
        "botid": 2384827585,
        "started": 1509542273,
        "paused": 1509542452,
        "action": "buy",
        "base": "MNZ",
        "rel": "KMD",
        "maxprice": 0.21,
        "totalrelvolume": 0.1,
        "totalbasevolume": 0.47619048,
        "aveprice": 0.20486144,
        "volume": 0.0672,
        "trades": [
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {}
        ],
        "completed": 7,
        "percentage": 67.2,
        "pending": 4,
        "pendingprice": 0.20633316,
        "pendingvolume": 0.0387
    }

bot_statuslist
^^^^^^^^^^^^^^

Displays the status of all bots.

Sample File Content:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"bot_statuslist\"}"

bot_stop
^^^^^^^^

To stop the tradebots. Use ``botid`` from your buy or sell order.

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"bot_stop\",\"botid\":$1}"

Sample usage: ``./bot_stop 3601212692`` # here **3601212692** is the ``botid`` from ``./bot_buy`` or ``./bot_sell`` script output.

Sample Output:

.. code-block:: json

    {
        "result": "success"
    }

Coin Features
-------------

balance
^^^^^^^

This will display the balance of a specific smartaddress for barterDEX trading. The idea of the barterDEX balance are, ``utxo``. That are "hot" / "live" ready for trading. It is the analogue of funds in an exchange account. This will not show your full wallet balance, and you wouldn't want the exchange account balance to show the amount of all your coins, including the ones not deposited in the exchange. Edit the file with coin ``name`` and ``smartaddress`` and it will display balance of your smartaddress(s).

KMD balance will display ``zcredits`` as well.

Sample File Contents:

.. code-block:: shell

	#!/bin/bash
	source userpass
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"balance\",\"coin\":\"KMD\",\"address\":\"RHV2As4rox97BuE3LK96vMeNY8VsGRTmBj\"}"

Sample Output:

.. code-block:: json

    {
        "result": "success",
        "coin": "KMD",
        "address": "RANyPgfZZLhSjQB9jrzztSw66zMMYDZuxQ",
        "balance": 360.33996021,
        "zcredits": 0,
        "zdebits": {
            "swaps": [],
            "pendingswaps": 0
        }
    } {
        "result": "success",
        "coin": "REVS",
        "address": "RANyPgfZZLhSjQB9jrzztSw66zMMYDZuxQ",
        "balance": 39.10219798
    } {
        "result": "success",
        "coin": "BTC",
        "address": "126nKAnGxWtsfPoxGh1snvbtLitkstZbvV",
        "balance": 0.00400000
    }

balances
^^^^^^^^

This method will display balance of all active coins in your wallet. No need to use a curl script for a specific coin and address.

Sample File Content:

.. code-block:: shell

	#!/bin/bash
	source userpass
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"balances\"}"

Sample Output:

.. code-block:: json

    [
        {
            "coin": "BTC",
            "balance": 0.00400000
        },
        {
            "coin": "KMD",
            "balance": 360.33996021
        },
        {
            "coin": "MNZ",
            "balance": 55.70756040
        },
        {
            "coin": "REVS",
            "balance": 39.10219798
        },
        {
            "coin": "JUMBLR",
            "balance": 1.12038776
        },
        {
            "coin": "SUPERNET",
            "balance": 0.91430900
        },
        {
            "coin": "PANGEA",
            "balance": 1
        },
        {
            "coin": "DEX",
            "balance": 1
        },
        {
            "coin": "BET",
            "balance": 1
        },
        {
            "coin": "CRYPTO",
            "balance": 1
        },
        {
            "coin": "HODL",
            "balance": 1
        },
        {
            "coin": "BOTS",
            "balance": 1
        },
        {
            "coin": "COQUI",
            "balance": 10.85596031
        }
    ]

calcaddress
^^^^^^^^^^^

Useful to get your private key for specific seed passphrase for any supported coin or asset except ETH & ERC20 tokens for now. Edit the passphrase section and change the word ``default`` with your own seed passphrase and coin name. We used Digibyte (DGB) as example.

Sample File Content:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"calcaddress\",\"passphrase\":\"default\",\"coin\":\"DGB\"}"

Sample Output: This output is based on the passphrase ``default``. Change that to your seed passphrase to get your desired private key.

.. code-block:: json

    {
        "passphrase": "default",
        "pubsecp": "03562035ac51f940b7f6e1e390df91fb0fe7f59f99acf8f6f389d9472a14797b5f",
        "coinaddr": "DKRQHUtFhFfViZPCcCut3uB45cATTXXBMh",
        "p2shaddr": "3FyKfmS3wk5bGiu2ziauvmNPLzisePpY3W",
        "privkey": "30a8eec1ce19687d132fe29051dca629d164e2c4958ba141d5f4133a33f0684f",
        "wif": "KxrJKHQ7phDnVnsbs2XEZUeWxjH3zSG6SzftyQGfojEG7ZkU9Zsn"
    }

fundvalue
^^^^^^^^^

``fundvalue`` will process ``"holdings":[]`` array and also do an internal balances api call if ``address`` is specified. This will only work for watchonly addresses that have been rescanned and with active coins. In order for external addresses to work, you need to have ``importaddress`` and ``rescan`` done, for obvious reasons, in native mode. SPV mode should just work without that.

Sample File Content:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"fundvalue\",\"address\":\"RRyyejME7LRTuvdziWsXkAbSW1fdiohGwK\"}"

Sample Output:

.. code-block:: json

    {
        "holdings": [
            {
                "coin": "KMD",
                "KMD": 6000000
            },
            {
                "coin": "REVS",
                "error": "no price source"
            },
            {
                "coin": "JUMBLR",
                "KMD": 4177502.22193679
            },
            {
                "coin": "SUPERNET",
                "error": "no price source"
            },
            {
                "coin": "PANGEA",
                "error": "no price source"
            },
            {
                "coin": "DEX",
                "error": "no price source"
            },
            {
                "coin": "BET",
                "error": "no price source"
            },
            {
                "coin": "CRYPTO",
                "error": "no price source"
            },
            {
                "coin": "HODL",
                "error": "no price source"
            },
            {
                "coin": "MSHARK",
                "error": "no price source"
            },
            {
                "coin": "BOTS",
                "error": "no price source"
            }
        ],
        "fundvalue": 10177502.22193679
    }

getrawtransaction
^^^^^^^^^^^^^^^^^

barterDEX now has ``getrawtransaction`` API for any installed coin and will use Electrum or native depending on whether electrum was called, that should help us directly issue Electrum for the oversized txid and directly cause any overflows.

Sample File Content:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"getrawtransaction\",\"coin\":\"KMD\",\"txid\":\"107a2683abbfa9188f78e17d3bcba66ece5bd7cbe105ab5bbaae79364159e84d\"}"

inuse
^^^^^

This API will return you all the UTXOs that are locked for swaps. The UTXOs that are locked for swaps are not spendable until they become free. The lock is basically for about 2 minutes, after that the UTXOs becomes free.

Sample File Content:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"inuse\"}"

Sample Output:

.. code-block:: json

    [
        {
            "expiration": 1520277125,
            "txid": "74a9f85dc372c3941bdfa7bc517f209db11c2fbdf7c83df3f4c8ccf15afa9e75",
            "vout": 1
        },
        {
            "expiration": 1520277125,
            "txid": "46f021a999b5f62fc42afeb431d09c85a2f2bc113aa23b5142cafb868a877bd0",
            "vout": 1
        }
    ]

listtransactions
^^^^^^^^^^^^^^^^

This API just passes through the call to native mode and filters out any with a different address. For spv it just returns the SPV history.

Sample File Content:

.. code-block:: shell

	#!/bin/bash
	source userpass
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"listtransactions\",\"coin\":\"JUMBLR\",\"address\":\"RANyPgfZZLhSjQB9jrzztSw66zMMYDZuxQ\"}"

Sample output using Native mode:

.. code-block:: json

    [
        {
            "account": "",
            "address": "RANyPgfZZLhSjQB9jrzztSw66zMMYDZuxQ",
            "category": "receive",
            "amount": 0.26042583,
            "vout": 0,
            "confirmations": 8904,
            "blockhash": "00009eeaa7458a5d781830c166158481fda6ae039450607f90e239d839694050",
            "blockindex": 2,
            "blocktime": 1521983789,
            "txid": "2ff201697e8486865638d35f4de796ce025ec72734c4053a6b835dfb50340ca9",
            "walletconflicts": [],
            "time": 1521983789,
            "timereceived": 1522155873,
            "vjoinsplit": [],
            "size": 300
        },
        {
            "account": "",
            "address": "RANyPgfZZLhSjQB9jrzztSw66zMMYDZuxQ",
            "category": "receive",
            "amount": 0.00203615,
            "vout": 1,
            "confirmations": 5955,
            "blockhash": "00000e1d26d1e13cb9c9456f2f2112fd2c3079fbdf66a88dbbf96db6114aecfe",
            "blockindex": 1,
            "blocktime": 1522161804,
            "txid": "2235aa0b2beed7b2a79619df044912af3baec026cda6a4eb00c9de5b6a1f6788",
            "walletconflicts": [],
            "time": 1522161801,
            "timereceived": 1522161801,
            "vjoinsplit": [],
            "size": 223
        },
        {
            "account": "",
            "address": "RANyPgfZZLhSjQB9jrzztSw66zMMYDZuxQ",
            "category": "send",
            "amount": -0.00203615,
            "vout": 1,
            "fee": -1e-05,
            "confirmations": 5955,
            "blockhash": "00000e1d26d1e13cb9c9456f2f2112fd2c3079fbdf66a88dbbf96db6114aecfe",
            "blockindex": 1,
            "blocktime": 1522161804,
            "txid": "2235aa0b2beed7b2a79619df044912af3baec026cda6a4eb00c9de5b6a1f6788",
            "walletconflicts": [],
            "time": 1522161801,
            "timereceived": 1522161801,
            "vjoinsplit": [],
            "size": 223
        },
        {
            "involvesWatchonly": true,
            "account": "",
            "address": "RANyPgfZZLhSjQB9jrzztSw66zMMYDZuxQ",
            "category": "receive",
            "amount": 14.4499848,
            "vout": 0,
            "confirmations": 4278,
            "blockhash": "0000f759c96b9c866e6417bb3c653e323feea999ce1dabcc27c007f72543f14c",
            "blockindex": 1,
            "blocktime": 1522261902,
            "txid": "6b2b506cffe3423e25d3519c64a5279213993e0d235ff89cbb3bf53be7a727fb",
            "walletconflicts": [],
            "time": 1522261807,
            "timereceived": 1522261807,
            "vjoinsplit": [],
            "size": 300
        },
        {
            "involvesWatchonly": true,
            "account": "",
            "address": "RANyPgfZZLhSjQB9jrzztSw66zMMYDZuxQ",
            "category": "send",
            "amount": -14.4499848,
            "vout": 0,
            "fee": -1e-05,
            "confirmations": 4278,
            "blockhash": "0000f759c96b9c866e6417bb3c653e323feea999ce1dabcc27c007f72543f14c",
            "blockindex": 1,
            "blocktime": 1522261902,
            "txid": "6b2b506cffe3423e25d3519c64a5279213993e0d235ff89cbb3bf53be7a727fb",
            "walletconflicts": [],
            "time": 1522261807,
            "timereceived": 1522261807,
            "vjoinsplit": [],
            "size": 300
        }
    ]

Sample output using SPV mode:

.. code-block:: json

            [
                {
                    "tx_hash": "7c536b8f3d1e33f110ae62399f181b4c5af9a16938b1ecef59f48c226dd2a9be",
                    "height": 8285
                },
                {
                    "tx_hash": "f3169db98c3b7263130d8d0d91aa17df361b76737f8df8363e3b4caeb1afaa55",
                    "height": 8288
                },
                {
                    "tx_hash": "24874d70f3cfa5ae3a1c31916af7bdc6cb6d6fe5d428a12873c373db703bd101",
                    "height": 8833
                },
                {
                    "tx_hash": "9281bcfc9c3262cb3e6d8440fd0250357a8660a24aa22abeca8ce7512c0cf111",
                    "height": 9012
                },
                {
                    "tx_hash": "c3561504f2ce0af8f5c63fa01424d6acb5576caddfa543dc3e16301d51f744f6",
                    "height": 9013
                },
                {
                    "tx_hash": "dce11261eaae611347a5967ea727f0bc0a3ee87e11250ad2ef0758a999d7e920",
                    "height": 9602
                },
                {
                    "tx_hash": "afc2fd0991bdef89da2cd1018c86ab56a5989c6f2b1d4e40861e88bc6125cbec",
                    "height": 10076
                }
            ]

listunspent
^^^^^^^^^^^

barterDEX uses ``utxo`` pairs instead of total balance to do the trading. For this the balance has be broken down and fund the address using 1x, 1.2x & 0.1x ratio. It is due to the nature of atomic swap protocol that is bartering specific utxo and the need for two utxo per atomic swap. **Analogy: If you need a quarter and a dime, exactly to make a purchase, is it possible to use just a single coin? barterDEX is swapping PAIRS (as in two) utxos.** ``./listunspent`` Gives similar output like your coin wallet. It will list all the unspent transactions (``utxo``) you have in a given coin wallet smartaddress.

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"listunspent\",\"coin\":\"CHIPS\",\"address\":\"RDoMmoCM5AcEH6Yf5vqKbqRjD1fLcQHuWb\"}"

Sample Output:

.. code-block:: json

    [
        {
            "tx_hash": "873e12d89eb9a25c1c40f0301b77414da0567982e3a06ce55a3501ff726bd253",
            "tx_pos": 1,
            "height": 534479,
            "value": "1251800000"
        },
        {
            "tx_hash": "8a62bb10f700c16629a52ad0dc8c730490de3038e30af82b1a706c91f337d968",
            "tx_pos": 1,
            "height": 535408,
            "value": "11000000"
        },
        {
            "tx_hash": "8848abd97daca43c702dbb176dac50d85261449c808f19324f5be1b4a495ad69",
            "tx_pos": 1,
            "height": 535379,
            "value": "11000000"
        },
        {
            "tx_hash": "79684e9c19c996292ad4a25c9dc05c89a3a9243af1b83727362bb2e2f92e08f6",
            "tx_pos": 1,
            "height": 534027,
            "value": "1012700000"
        }
    ]

secretaddresses
^^^^^^^^^^^^^^^

It will display secret 10 addresses with their private keys for a given ``pubtype``. You can change the ``num``, ``pubtype`` etc by editing the script.

Sample File Contents:

.. code-block:: shell

	echo "usage: ./secretaddresses 'passphrase'"

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"secretaddresses\",\"num\":16,\"passphrase\":\"$1\"}"

Sample Output:

.. code-block:: shell

	usage: ./secretaddresses 'passphrase'
	{"R9oeSNXqR499PFz2BgUeZJvSsp331TFDYi":"UxKrG3xxxxxx",
	"RX7sUCvxV45LmrmVRvkbm8kUedFqhXgqtt":"UuNeHYexxxxxx",
	"RRKf3RnmbNDnCfC6P7HHYNBJuRrVxEm7Db":"UsXUNtmxxxxxx",
	"RSo6exWzMbnGnwM4b3WcT1MvxvnRuRSURP":"UsFuDaWxxxxxx",
	"RRve3cdBJPF2dcT6uD8gT2Bfhg7ZU9krFU":"Uw1Xbcoxxxxxx",
	"REkV8JMBuLFTjYH93QfJ4UpmoLw85LomP4":"UpYxoFMxxxxxx",
	"RKJ6vpCTYjDCoyrLyuxJRvjiraM5ZEwos5":"Urin6VUxxxxxx",
	"RDHo38pWxDEvqx99C2aJhprHQwf9bYoKRE":"UuNsFyBxxxxxx",
	"RLGRaoQ7FCu8dk653CMR4nLiRnfYZiXb7D":"UvT2utaxxxxxx",
	"RJABFzJzBNoPUGZrMBcBfL5UqYjY8hptJU":"UsoAJqRxxxxxx",
	"RN2TRHQBFWMB9G1MkHKdYbg4oU7ToxRTdB":"UqNiGgAxxxxxx",
	"RJYuYeXAnWoVPbgHpc1rtxkoBWFCtzib1E":"Uqeaxmzxxxxxx",
	"RXkZYAD13G89foJbN7uHpD2A2oZJaDTMzr":"UqejSkPxxxxxx",
	"RUfuMah7a9QXar5XcJpage4S7jtoiL99Kv":"Uq7e4Hdxxxxxx",
	"RTS385Ny2feDBgLGzrAPRw2Q7u5jpv9jZs":"UvUcSEPxxxxxx",
	"RP7haeUQv56FW9X6W1rRbhbqvXPyvX23Fi":"UpqRcKMxxxxxx"}

sendrawtransaction
^^^^^^^^^^^^^^^^^^

This method will broadcast a raw transaction over the network. Uses tx-hex from ``./withdraw`` API output.

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"sendrawtransaction\",\"coin\":\"KMD\",\"signedtx\":\"$1\"}"

supernet
^^^^^^^^

``supernet`` script uses the ``balances`` API and returs all SuperNET aseet balances along with KMD for a specific address. In order for external addresses to work, you need to have ``importaddress`` and ``rescan`` done, for obvious reasons, in native mode. SPV mdoe just works without that.

Sample File Content:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"balances\",\"address\":\"RRyyejME7LRTuvdziWsXkAbSW1fdiohGwK\"}"

Sample Output:

.. code-block:: json

    [
        {
            "coin": "KMD",
            "balance": 6000000
        },
        {
            "coin": "REVS",
            "balance": 6335.95500000
        },
        {
            "coin": "JUMBLR",
            "balance": 239022.38900000
        },
        {
            "coin": "SUPERNET",
            "balance": 6335.95500000
        },
        {
            "coin": "PANGEA",
            "balance": 602828.14640000
        },
        {
            "coin": "DEX",
            "balance": 257733
        },
        {
            "coin": "BET",
            "balance": 2688
        },
        {
            "coin": "CRYPTO",
            "balance": 320754.73700000
        },
        {
            "coin": "HODL",
            "balance": 70000
        },
        {
            "coin": "MSHARK",
            "balance": 385403.90000000
        },
        {
            "coin": "BOTS",
            "balance": 288157
        }
    ]

.. _timelock-and-unlockedspend:

timelock and unlockedspend
^^^^^^^^^^^^^^^^^^^^^^^^^^

BarterDEX now has a coin agnostic timelock/unlock mechanism. Of course the coin will need to support CLTV or it wont work. The timelock will work partially, but the unlockspend will NOT. Test with small amount. Don't confuse these APIs with 0conf deposit and claim.

Sample file content:

``timelock``

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"timelock\",\"coin\":\"KMD\",\"duration\":1000,\"amount\":1}"

``unlockedspend``

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"unlockedspend\",\"coin\":\"KMD\",\"txid\":\"e858e382a816b4cab22e3fd3e29901c7ef497cd1fdad7683314cc9187eca34fd\"}"

``timelock`` API is pretty simple, just specify coin, duration in seconds and the amount. An extra txfee will be added to amount so the unlockspend can send the specified amount. there is an optional ``destaddr`` field that will allow you to send to any address. Like ``withdraw``, ``timelock`` will not actually broadcast the tx, so you need to use ``sendrawtransaction`` to actually broadcast it.

Once its broadcast, and the time lock expires, you can do an ``unlockedspend`` using just the coin and the txid. The requirement is that it must be sent to your smartaddress that you are logged into and it will only just unlock and send to yourself.

withdraw
^^^^^^^^

To withdraw, you just need to specify the array of outputs and the coin. It returns the ``rawtx``, the signed transaction in ``hex`` the ``txid`` and if it was complete or not. All inputs are assumed to be standard pay to ``pubkeyhash``, having other non-standard ``utxo`` will make it create invalid rawtx. Withdrawing ETH/ERC20 tokens works using different parameters (please see :ref:`eth_withdraw`,).

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"withdraw\",\"coin\":\"KMD\",\"outputs\":[{\"RUgW6fLfVsLJ87Ng4zJTqNedJSKYQ9ToAf\":0.001}, {\"RUgW6fLfVsLJ87Ng4zJTqNedJSKYQ9ToAf\":0.002}],\"broadcast\":1}"

Sample Output:

::

    {
        "method": "withdraw",
        "coin": "KMD",
        "outputs": [
            {
                "RUgW6fLfVsLJ87Ng4zJTqNedJSKYQ9ToAf": 0.00100000
            },
            {
                "RUgW6fLfVsLJ87Ng4zJTqNedJSKYQ9ToAf": 0.00200000
            }
        ]
    } -> f6b04d157c007bf688822a73c754934f53cf28516f64dc64372fa397789e9ce1
	{
        "rawtx": "0100000001b5384fc2f0b737a17239eaf2172bf24c4f410f720e672c3f56a9b5a8e0b33a910100000000ffffffff03a0860100000000001976a914d4d2ffc812cdce0c30c5184e8ea1deb7bfeb5b3888ac400d0300000000001976a914d4d2ffc812cdce0c30c5184e8ea1deb7bfeb5b3888ac06771300000000001976a91459fdba29ea85c65ad90f6d38f7a6646476b26b1688ac7dd4e359",
        "hex": "0100000001b5384fc2f0b737a17239eaf2172bf24c4f410f720e672c3f56a9b5a8e0b33a91010000006b483045022100df405fe4f79e66052a952968b93ed3f56b2fc75908a90c70d9d409b4da45996902200b9136063fcdb0bfdfeb09801d2fcbb0658236d69135711a20ac4aa50c8d3bf0012102ebc786cb83de8dc3922ab83c21f3f8a2f3216940c3bf9da43ce39e2a3a882c92ffffffff03a0860100000000001976a914d4d2ffc812cdce0c30c5184e8ea1deb7bfeb5b3888ac400d0300000000001976a914d4d2ffc812cdce0c30c5184e8ea1deb7bfeb5b3888ac06771300000000001976a91459fdba29ea85c65ad90f6d38f7a6646476b26b1688ac7dd4e359",
        "txid": "f6b04d157c007bf688822a73c754934f53cf28516f64dc64372fa397789e9ce1",
        "complete": true
    }

If the last output is doing a withdraw to the smartaddress, it is combined with change. Here are two sample console output below. The first one is withdrawing 10 KMD to the same smartaddress. Second one is 10 & 10.0001 KMD withdraw to the same smartaddress. The last output is increased by 0.0001 & change combined in both example.

::

	vout.0 10.00010000 -> total 10.00020000
	dustcombine.0 numpre.0 min0.(nil) min1.(nil) numutxos.172 amount 10.00020000
	minutes.381 tiptime.1514745296 locktime.1514722428
	46bbfbe93ebfc0a9262143193fe50d5c9ce5c2739da768ce8b5ec919ffaa570f/0 40.01342800 interest 0.00122360 -> sum 0.00122360
	numunspents.171 vini.0 value 40.01342800, total 40.01342800 remains -30.01322800 interest 0.00122360 sum 0.00122360 46bbfbe93ebfc0a9262143193fe50d5c9ce5c2739da768ce8b5ec919ffaa570f/v0
	set inuse until 1514746673 lag.600 for 46bbfbe93ebfc0a9262143193fe50d5c9ce5c2739da768ce8b5ec919ffaa570f/v0
	change 30.01445160 = total 40.01465160 - amount 10.00020000, adjust 0.00000000 numvouts.1
	combine last vout 10.00010000 with change 30.01445160
	LP_withdraw.KMD {"method":"withdraw","coin":"KMD","outputs":[{"RANyPgfZZLhSjQB9jrzztSw66zMMYDZuxQ":10.00010000}]} -> d3f32d814e20edcbc0c654eec79d0399b38b907ecc8cb9418da17a543d299e17

::

	vout.0 10.00000000 -> total 10.00010000
	vout.1 10.00010000 -> total 20.00020000
	dustcombine.0 numpre.0 min0.(nil) min1.(nil) numutxos.172 amount 20.00020000
	numunspents.171 vini.0 value 40.01455160, total 40.01455160 remains -20.01435160 interest 0.00000000 sum 0.00000000 d3f32d814e20edcbc0c654eec79d0399b38b907ecc8cb9418da17a543d299e17/v0
	set inuse until 1514747480 lag.600 for d3f32d814e20edcbc0c654eec79d0399b38b907ecc8cb9418da17a543d299e17/v0
	change 20.01435160 = total 40.01455160 - amount 20.00020000, adjust 0.00000000 numvouts.2
	combine last vout 10.00010000 with change 20.01435160
	LP_withdraw.KMD {"method":"withdraw","coin":"KMD","outputs":[{"RANyPgfZZLhSjQB9jrzztSw66zMMYDZuxQ":10}, {"RANyPgfZZLhSjQB9jrzztSw66zMMYDZuxQ":10.00010000}]} -> f24361b13b7f0188ea422572b882c0df50bef2a33bf8aed7bf0776946332cece

eth_withdraw
^^^^^^^^^^^^
This method is required to withdraw ETH/ERC20 coin/tokens. Similar functionality to ``withdraw`` for Bitcoin protocol based coins.

.. code-block:: shell

	curl --url "http://127.0.0.1:7783 " --data "{\"userpass\":\"$userpass\",\"method\":\"eth_withdraw\",\"coin\":\"DEC8\",\"to\":\"0xbAB36286672fbdc7B250804bf6D14Be0dF69fa29\",\"amount\":1000}"

opreturn
^^^^^^^^

``OP_RETURN`` is just built into the ``withdraw`` API. If an ``"opreturn":"<hex>"`` is defined, it will create an OP_RETURN with the binary of the hex. Without ``outputs`` value, it will return ``{"error":"withdraw needs to have outputs"}``. There is encryption to the opreturn mode of withdraw. Basically if you specify a non-null passphrase, it encrypts with that passphrase and you will need that passphrase to decode it. The second parameter in the first example script is the passphrase. So, if you don't specify it, it is unencrypted.

3 different sample scripts:

.. code-block:: shell

	curl -X POST --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"withdraw\",\"coin\":\"COQUI\",\"passphrase\":\"$2\", \"opreturn\":\"$(echo -n "$1" | od -A n -t x1 | perl -pe 's/\W+//g')\"}"

.. code-block:: shell

	curl -X POST --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"withdraw\",\"coin\":\"COQUI\",\"outputs\":[{\"RGCVXhUxepCxh77thy7XgMrQ5XU9u7SWSR\":0.01}], \"opreturn\":\"$(echo -n "$1" | od -A n -t x1 | perl -pe 's/\W+//g')\"}"

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"withdraw\",\"coin\":\"KMD\",\"outputs\":[{\"RANyPgfZZLhSjQB9jrzztSw66zMMYDZuxQ\":$1}], \"opreturn\":\"deadbeef\"}"

Sample Output:

.. code-block:: json

    {
        "rawtx": "01000000029059515dd331b448b213c12e607b4f104a025f9461d1c094d98010a06406b62d0100000000ffffffff6843fc7a13218df69cd7e03c64af2cefae7b1121ed55206da21c57d5665c8b640100000000ffffffff02565c1700000000001976a9140c1007fc1f406a0a519886c0e59327e9c43a634088ac0000000000000000066a04deadbeef1a69a05a",
        "hex": "01000000029059515dd331b448b213c12e607b4f104a025f9461d1c094d98010a06406b62d010000006b483045022100d80b9fcf9561c889bcdbab79d2215e1fe66118ad1c1d1e8ec5421ced6b2de2ad02206ef83ed458e974ecc8fa9b667e34ab571b06f5e62dd83bff37c00ab5e372bdef012103fe754763c176e1339a3f62ee6b9484720e17ee4646b65a119e9f6370c7004abcffffffff6843fc7a13218df69cd7e03c64af2cefae7b1121ed55206da21c57d5665c8b64010000006b483045022100ec7c86079d1ce7512a835d81cedd850028e297ce22841ae925d5aceaff6f5e78022045a09dcad77f0bcc6d9d85f27ca9c13ba407c0c7968f85c50887b231067050e3012103fe754763c176e1339a3f62ee6b9484720e17ee4646b65a119e9f6370c7004abcffffffff02565c1700000000001976a9140c1007fc1f406a0a519886c0e59327e9c43a634088ac0000000000000000066a04deadbeef1a69a05a",
        "tx": {
            "version": 1,
            "locktime": 1520462106,
            "vin": [
                {
                    "txid": "2db60664a01080d994c0d161945f024a104f7b602ec113b248b431d35d515990",
                    "vout": 1,
                    "scriptPubKey": {
                        "hex": "76a9140c1007fc1f406a0a519886c0e59327e9c43a634088ac"
                    }
                },
                {
                    "txid": "648b5c66d5571ca26d2055ed21117baeef2caf643ce0d79cf68d21137afc4368",
                    "vout": 1,
                    "scriptPubKey": {
                        "hex": "76a9140c1007fc1f406a0a519886c0e59327e9c43a634088ac"
                    }
                }
            ],
            "vout": [
                {
                    "satoshis": "1530966",
                    "scriptPubKey": {
                        "hex": "76a9140c1007fc1f406a0a519886c0e59327e9c43a634088ac"
                    }
                },
                {
                    "satoshis": "0",
                    "scriptPubKey": {
                        "hex": "6a04deadbeef"
                    }
                }
            ]
        },
        "txid": "4e2a338232d13643cdbd6fb0c47d649b9c1842284a78ab6ca9cf03088f3dc0cc",
        "complete": true
    }

opreturndecrypt
^^^^^^^^^^^^^^^

This method will decrypt the encrypted :ref:`OP_RETURN <opreturn>` easily.

Sample File Content:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"opreturndecrypt\",\"coin\":\"KMD\",\"txid\":\"06e59c6e9217ef1e526a1419e231e5f927689765feab9cd48167e089301f6fc2\",\"passphrase\":\"test\"}"

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"opreturndecrypt\",\"coin\":\"KMD\",\"txid\":\"34bf4bc2247e43c0c6a2223b79d3f1a3e9962102fb4a563612e5bbb91fb85348\",\"passphrase\":\"test\"}"

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"opreturndecrypt\",\"coin\":\"KMD\",\"txid\":\"a9e94e6890d6998b3c2b89685e8c7c2b9e380a53fb813192701d0966480807eb\",\"passphrase\":\"test\"}"

Sample Output:

.. code-block:: json

    {
        "coin": "KMD",
        "opreturntxid": "06e59c6e9217ef1e526a1419e231e5f927689765feab9cd48167e089301f6fc2",
        "opreturn": "6a4c4c4c0058501c2c290f7241932a8b4614b844bae28cc3117eeb79d5c0c900000000000000000000000000000000a30dc015ac4e4085f0cdb2c7cc24bca01d771449912d2982d7e9401ef52e5a81",
        "result": "success",
        "decrypted": "68656c6c6f2c20776f726c6474657374",
        "original": "hello, worldtest"
    }

.. code-block:: json

    {
        "coin": "KMD",
        "opreturntxid": "34bf4bc2247e43c0c6a2223b79d3f1a3e9962102fb4a563612e5bbb91fb85348",
        "opreturn": "6a4c4d4d00215bb9fee0d7685c5fcf913f4da4fab726104b1b242d5226939b00000000000000000000000000000000cc5eedec8e34b68726ff77cad0558659333fee18e5b63f8ef259444f66f185e62e",
        "result": "success",
        "decrypted": "68656c6c6f2c20776f726c647465737431",
        "original": "hello, worldtest1"
    }

.. code-block:: json

    {
        "coin": "KMD",
        "opreturntxid": "a9e94e6890d6998b3c2b89685e8c7c2b9e380a53fb813192701d0966480807eb",
        "opreturn": "6a4b4b0057a7b6c2ac0354f967534060bc3719a687bedc3b4741c3c64b7d00000000000000000000000000000000fe4170681aab23ba044516812bc5fe9dd5adb3a2f05fbc8d46e7be69f02040",
        "result": "success",
        "decrypted": "68656c6c6f2c20776f726c64746573",
        "original": "hello, worldtes"
    }

All three recreated the original string passed into the :ref:`opreturn` script. This functionality should allow apps to easily created and retrieve encrypted ``OP_RETURN``.

Statistics
----------

guistats
^^^^^^^^

``guistats`` method is for GUI apps to display statistics, based on the ``statsdisp`` API.

Sample File Content:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"statsdisp\",\"starttime\":0,\"endtime\":0,\"gui\":\"SimpleUI\"}"

pricearray
^^^^^^^^^^

pricearray will display statistical price data based on timescale.

Sample File Content:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"pricearray\",\"base\":\"REVS\",\"rel\":\"KMD\",\"timescale\":300}"

This will output the data in an order of ``[timestamp, avebid, aveask, highbid, lowask]``

Sample output:

::

	[
	 [1510603500, 1.40944454, 1.40944453, 3.13224635, 1.07003092],
	 [1510603800, 1.50064727, 1.50064726, 3.13224635, 1.07003092],
	 [1510604100, 1.50064727, 1.50064726, 3.13224635, 1.07003092],
	 [1510607100, 1.44868382, 1.44868381, 3.13224635, 1.07003092],
	 [1510607400, 1.50064727, 1.50064726, 3.13224635, 1.07003092],
	 [1510607700, 1.52877070, 1.52877069, 3.13224635, 1.07003092],
	 [1510608000, 1.55019807, 1.55019806, 3.13224635, 1.09860370],
	 [1510608300, 1.57205536, 1.57205536, 3.13224635, 1.09860370],
	 [1510608600, 1.30344136, 1.30344135, 1.76975636, 1.17393764],
	 [1510611600, 1.21488583, 1.21488582, 1.25583401, 1.17393764],
	 [1510611900, 1.25661049, 1.25661048, 1.34097978, 1.17393764]
	]

statsdisp
^^^^^^^^^

``statsdisp`` processes the ``stats.log`` file on your node. It will display the swaps as best as it can figure out the unique number of swaps, you can set specific ``starttime`` and ``endtime``. If not specified, will display all. If both are the same time from the future, it will display only the pending stats.

This is a very good feature as it can identify any node that is trying to do too many trades at once

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"statsdisp\",\"starttime\":0,\"endtime\":0}"

Sample Output:

.. code-block:: json

    {
        "result": "success",
        "newlines": 0,
        "request": 0,
        "reserved": 0,
        "connect": 0,
        "connected": 0,
        "duplicates": 0,
        "parse_errors": 0,
        "uniques": 0,
        "tradestatus": 0,
        "unknown": 0
    }

ticker
^^^^^^

``ticker`` API returns trades for the previous 24hours. You can set ``base/rel`` optionally. Most useful for price and marketcap statistics.

Sample File Content:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"ticker\",\"base\":\"REVS\",\"rel\":\"KMD\"}"

Sample Output:

.. code-block:: json

    [
        {
            "timestamp": 1513174486,
            "KMD": 4.02827942,
            "CHIPS": 80.00010000,
            "price": 19.85962036
        },
        {
            "timestamp": 1513168630,
            "KMD": 0.07448089,
            "MNZ": 0.25609997,
            "price": 3.43846549
        },
        {
            "timestamp": 1513166465,
            "CRYPTO": 44.00844307,
            "KMD": 500.00010000,
            "price": 11.36145851
        },
        {
            "timestamp": 1513158008,
            "KMD": 463.91820708,
            "SUPERNET": 10.00010000,
            "price": 0.02155574
        }
    ]

tradesarray
^^^^^^^^^^^

``tradesarray`` will display statistical trade data based on timescale in seconds.

Sample File Content:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"tradesarray\",\"base\":\"REVS\",\"rel\":\"KMD\",\"timescale\":120}"

This will output the data in an order of ``[timestamp, high, low, open, close, relvolume, basevolume, aveprice, numtrades]``

Sample output:

.. code-block:: shell

	[
	 [1511480400, 1.27614172, 1.27614172, 1.27614172, 1.27614172, 0.04990000, 0.03910224, 1.27614172, 1],
	 [1511480520, 1.97936698, 1.36595231, 1.97936698, 1.36595231, 0.09980000, 0.06174137, 1.61642024, 2],
	 [1511480640, 2.11837065, 2.11837065, 2.11837065, 2.11837065, 0.04990000, 0.02355584, 2.11837065, 1],
	 [1511481840, 1.63195519, 1.55147942, 1.63195519, 1.55147942, 0.09980000, 0.06273967, 1.59070011, 2],
	 [1511481960, 1.82528276, 1.82528276, 1.82528276, 1.82528276, 0.04990000, 0.02733823, 1.82528276, 1],
	 [1511482680, 1.77777461, 1.77777461, 1.77777461, 1.77777461, 0.04990000, 0.02806880, 1.77777461, 1]]

Revenue Sharing/Operations
--------------------------

dividends
^^^^^^^^^

This script will allow users / organizations to send dividends for any specific coins/asstets

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"dividends\",\"coin\":\"KMD\",\"height\":$1,\"prefix\":\"fiat/jumblr sendtoaddress\",\"suffix\":\"\",\"dividend\":50000,\"dust\":1}"

snapshot
^^^^^^^^

The name says it all, snapshot will take a snap of the blockchain for a specified coin/asset on a certain block height for sending dividends or airdrop.

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"snapshot\",\"coin\":\"KMD\",\"height\":$1}"

.. _snapshot-balance:

snapshot_balance
^^^^^^^^^^^^^^^^

This API will display the snapshot balance of a specific coin address after snapshot taken on a specific block height. You need to have jq installed (https://stedolan.github.io/jq/).

Sample File Contents:

.. code-block:: shell

	ht=$1
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"snapshot_balance\",\"coin\":\"KMD\",\"height\":$ht,\"addresses\":[\"RSAzPFzgTZHNcxLNLdGyVPbjbMA8PRY7Ss\", \"RBgD5eMGwZppid4x7PTEC2Wg1AzvxbsQqB\"]}"

.. _snapshot-loop:

snapshot_loop
^^^^^^^^^^^^^

This API is used to automate snapshot process for coins/assets at given block height and certain number thereafter. You can configure the script to run on certain block height increments.

Sample File Contents:

.. code-block:: shell

	ht=$1
	while true
	do
	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"snapshot\",\"coin\":\"KMD\",\"height\":$ht}"
	#ht=`komodo-cli getinfo | jq .blocks`
	ht=$(( $ht + 1000 ))
	echo next height $ht
	sleep 1
	done

.. _InstantDEX-swap:

InstantDEX SWAP
---------------

Fastest swaps are here now as InstantDEX Swap. All nodes can be doing this at the same time, any ``bob`` to any ``alice``. All you need to have is some amount of KMD deposit for dynamic trust. It does require a deposit that matches your trade size.

If you are selling 20 at at time, deposit 20. If you are selling 50 at a time, deposit 50. And, you can trade without any deposit if you want to wait for coin confirmations. Use ``InstantDEX`` swap, just wait for deposit coin confirmations, you can sell all. The deposit just has to cover the amount you have pending in swaps, not anything regarding your total amount.

You can see your balance using the regular ``balance`` API. After verification your ``zcredits`` will be displayed with your KMD balance like this:

.. code-block:: json

    {
        "result": "success",
        "coin": "KMD",
        "address": "RANyPgfZZLhSjQB9jrzztSw66zMMYDZuxQ",
        "balance": 363.94840658,
        "zcredits": 50
    }

instantdex_deposit
^^^^^^^^^^^^^^^^^^

You can ``deposit`` KMD using the following script into b addresses which will accrue interest as well. This will allow you to do InstantDEX swaps which finishes a swap within 5-20 seconds. The more KMD you deposit for InstantDEX trading, the more limit you can have. It is a timelocked deposit, keeps the honest traders honest. Gives other traders the assurance that you have a valid deposit to cover any hack attempt.

``instantdex_deposit`` the values are 1 to 52 weeks and the amount (minimum of 10.0001). These figures are calibrated to the 5% APR, ie. 1 weeks interest is approx the BOTS 0.1% fee, 52 weeks is the most the 5% APR accrues, 10.0001 KMD is min required for interest. It can take few minutes (about 10 confirmations) for the Bob nodes to recognise you. This creates a dynamic trust between nodes and swaps are faster. Just issue normal buy and the Bob nodes will respond with InstantDEX swaps.

It creates a binary file in DB with the unique deposit txids on an append only basis. The first time, it seeds it with the contents of the existing ``instantdex.json`` files. from the deposits file the ``instantdex_address_append.json`` is directly created and the ``instantdex.json`` file is created by removing the already spent deposits.

Sample script:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"instantdex_deposit\",\"weeks\":1,\"amount\":10.0001,\"broadcast\":1}"

``weeks:1`` means it will be there for 300 hours or 1 week time. Don't set to ``week:0`` unless you are only testing.

Sample Output:

.. code-block:: json

    {
        "rawtx": "01000000014c9758944771d62c731f9b06246ccd3301ea0e198a6bdbdcb22csdffasdc7010fgdfg00ffffffff0300ca9asdf17a914d9da8esdfsfbe957273f842617132c361546e7b8743420f00000000001976a91492816449164623c4e744009923356ff4832ba388ac998e6d07000000001976a9140c1007fc1f406a0a519886c0e59327e9c43a634088ac2b08175a",
        "hex": "01000000014c9758944771d62c731f9b06246ccd3301ea0e1123jdsfbdcb22ce18d5daf0dc7010000006a473044022044b87624341cb4c01cdce88b592fadcf725d3e88315c2cd35a8d6a66d81ea035022047f372108e264634d610227e9c8ba69399e1609f7a37af1470b47ce6d0bde3b4012103fe754763c176e1339a3f62ee6b9484720e17ee4646b65a119e9f6370c7004abcffffffff0300ca9a3b0000000017a914d9da8e493573be957273f842617132c361546e7b8743420f00000000001976a914928104f862284623c4e744009923356ff4832ba388ac998e6d07000000001976a9140c1007fc1f406a0a519886c0e59327e9c43a634088ac2b08175a",
        "tx": {
            "version": 1,
            "locktime": 1511458859,
            "vin": [
                {
                    "txid": "c70daf5d8de12cb2dcdb6b8a190eea0133cd6c24069b1f732cd671479458974c",
                    "vout": 1,
                    "scriptPubKey": {
                        "hex": "76a9140c1007fc1f406a0a519886c0e59327e9c43a634088ac"
                    }
                }
            ],
            "vout": [
                {
                    "satoshis": "1000000000",
                    "scriptPubKey": {
                        "hex": "a914d9da8e493573be957273f842617132c361546e7b87"
                    }
                },
                {
                    "satoshis": "1000003",
                    "scriptPubKey": {
                        "hex": "76a914928104f862284623c4e744009923356ff4832ba388ac"
                    }
                },
                {
                    "satoshis": "124620441",
                    "scriptPubKey": {
                        "hex": "76a9140c1007fc1f406a0a519886c0e59327e9c43a634088ac"
                    }
                }
            ]
        },
        "txid": "a01b85233259e62edcaf3c171c97de0d2977ce88ae172b9b11809da9757e218c",
        "complete": true,
        "address": "bYbB9P5XG5j1Jr5nbD2nL5jt54WwPEzADd",
        "expiration": 1512201600,
        "deposit": 10,
        "result": "success",
        "broadcast": "a01b85233259e62edcaf3c171c97de0d2977ce88ae172b9b11809da9757e218c"
    }

claim
^^^^^

**For 0conf deposits claim can take extra time. The extra time can be up to a week as it operates on a weekly cycle. Best is to make the 0conf deposit on Saturdays. Friday is safest anywhere in the world.**

After the deposit is **expired**, you can claim at any time, though it is rounded up to the next week boundary. You need to use ``./claim`` API to claim your 0conf deposit (``zcredits``) back. All of your deposits are secured as long as you have the txid handy. If you use ``week:0`` you need to save the details of timestamp and the ``b`` address that the funds were sent in order to use with the ``./claim`` script to claim it back.

::

	Minutes or hours is not long enough. Remember, the point here is to resolve any blockchain attacks.

``claim`` API will display the balance of the 0conf deposit ``txid`` along with interest and wait time to claim. This will claim the deposit instantly if it already expired and ready to claim.

Sample File Contents:

.. code-block:: shell

	curl --url "http://127.0.0.1:7783" --data "{\"userpass\":\"$userpass\",\"method\":\"instantdex_claim\"}"

Output:

.. code-block:: json

    {
        "result": "success",
        "claimed": 0,
        "txids": [
            {
                "txid": "d5705d948a5a4e0171acec3eb718ca1421ef998b37d0af5c37ac3b440898aef5",
                "deposit": 1000,
                "interest": 10.78139269,
                "waittime": 25702320
            }
        ]
    }

Manually Enable 0conf deposits to work with the GUI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You need to put the ``txid`` of the 0conf / instantdex deposit in an ``instantdex.json`` and/or ``instantdex_address.json`` file inside ``DB`` dir. If the file is not preset in the DB folder, create the file manually. The DB dir is located ``C:/Users/<username>/AppData/Roaming/BarterDEX/DB`` in Windows and ``~/.BarterDEX/DB`` in Linux. The content inside the JSON file should look like following:

**1 txid**

::

	["d5705d948a5a4e0171acec3eb718ca1421ef998b37d0af5c37ac3b440898aef5"]

**2 or more txid**

::

	[	
		"d5705d948a5a4e0171acec3eb718ca1421ef998b37d0af5c37ac3b440898aef5",
		"bd2087d431bb9af6213e73efc58e3384227edcf4827e1cf83f3c153e512a9e1f"
	]

**[Note: If you are using Windows, please use 1 txid at a time. Claim for multiple txid may not work together. Claim single txid each time.]**

Then delete any deposit.address binary file for your address i.e.: ``deposits.RPZVpjptzfZnFZZoLnuSbfLexjtkhe6uvn``, all this is in DB dir. **Don't delete any dir in here.**

Next time you start BarterDEX, it should then generate a ``deposits.<address>`` with the binary of the txid and necessary files. If Electrum mode does not work for you, try with native KMD wallet.

::
	
	Negative ``zcredits balance`` is the balance being used for 0conf trade, will be available after the next notarized block.


