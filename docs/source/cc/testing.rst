************************************************
Using the Contracts on a Komodo based Blockchain
************************************************

Currently there are four contracts that can be used on any blockchain created using Komodo. They are:

	* Tokens
	* Faucet
	* Rewards
	* Dice

To use the contracts on the blockchain, the start command of the chain should contain the parameter ``-ac-cc`` and it should be greater than `0`.

A brief overview of the ``-ac-cc`` parameter:

.. code-block:: shell
 
		* A chain with -ac_cc=N with N > 0, will have CC active
		* If N is 1, then it just enables CC
		* if N is >= 2 and <= 100, it allows for non-fungible cross chain contracts within all the chains with the same N value
		* if N >= 101, then it forms a cluster of all the chains with the same N value where the base tokens in all the chains in that cluster are fungible via the burn protocol

To test the contracts: 

	* Compile Komodo
	* Navigate to ``src`` directory, start the test chain with your ``pubkey`` and issue the SmartContract RPC commands. All the instructions to get you started are below. For a more elaborate explanation creating a new blockchain using Komodo see: :doc:`/komodo/create-Komodo-Assetchain` 

 .. code-block:: shell

	#Install dependencies

	cd ~
	sudo apt-get update
	sudo apt-get upgrade -y
	sudo apt-get install build-essential pkg-config libc6-dev m4 g++-multilib autoconf libtool ncurses-dev unzip git python zlib1g-dev wget bsdmainutils automake libboost-all-dev libssl-dev libprotobuf-dev protobuf-compiler libgtest-dev libqt4-dev libqrencode-dev libdb++-dev ntp ntpdate nano software-properties-common curl libcurl4-gnutls-dev cmake clang

	git clone https://github.com/nanomsg/nanomsg
	cd nanomsg
	cmake . -DNN_TESTS=OFF -DNN_ENABLE_DOC=OFF
	make -j2
	sudo make install
	sudo ldconfig

	#Build Komodo

	cd ~
	git clone https://github.com/jl777/komodo
	cd komodo
	git checkout jl777
	./zcutil/fetch-params.sh
	./zcutil/build.sh -j$(nproc)

	#Start the Test Chain	

	cd ~/komodo/src
	./komodod -ac_cc=1 -ac_name=<CHAIN_NAME> -addressindex=1 -spentindex=1 -ac_supply=1000 -ac_reward=10000000000000 -pubkey=<your_pub_key> -addnode=195.201.20.230 -addnode=195.201.137.5 -addnode=195.201.20.230 -addnode=94.130.224.11 &


