****************************************************************************
Configuration and Installation Instructions for coins supported on BarterDEX
****************************************************************************

The below configurations and installation instructions for various coins supported by BarterDEX have been verified to work by our Test Engineers while testing their Atomic-Swap compatibility through BarterDEX. But these instructions are provided here for reference purpose only and in case of any difficulty installing or configuring any coin that doesn't belong to the Komodo Ecosystem, it is recommended to contact the Support channels/Developers of the particular coin directly.

Do ``CTRL + F`` and search for a coin by its TICKER and then NAME if TICKER doesn't yield results.   

.. note::

	Most ./configure lines contain a specific config that has been used by our Test Engineers which may not be suitable for every system. In most cases, delete everything before ./configure in the same line.

	For Example:
	 CFLAGS="-fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free" CPPFLAGS="-fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free" LDFLAGS="-ltcmalloc_minimal" ./configure --with-incompatible-bdb --with-gui=no --disable-tests --disable-bench --without-miniupnpc --disable-zmq

	Should be edited to:
	 ./configure --with-incompatible-bdb --with-gui=no --disable-tests --disable-bench --without-miniupnpc --disable-zmq

Contabo is the hosting provider for one of the Bob nodes used while testing. The output beneath the word ``Contabo`` is the output from the ``getcoin`` API call on the VPS.

.. contents:: Links
   :depth: 2

888
===

.. include:: coin-configs-install-instructions/888
   :literal:

ABY
===

.. include:: coin-configs-install-instructions/ABY
   :literal:

ADT
===

.. include:: coin-configs-install-instructions/ADT
   :literal:

AE
==

.. include:: coin-configs-install-instructions/AE
   :literal:

AION
====

.. include:: coin-configs-install-instructions/AION
   :literal:

AMB
===

.. include:: coin-configs-install-instructions/AMB
   :literal:

ANN
===

.. include:: coin-configs-install-instructions/ANN
   :literal:

ARC
===

.. include:: coin-configs-install-instructions/ARC
   :literal:

ARG
===

.. include:: coin-configs-install-instructions/ARG
   :literal:

AST
===

.. include:: coin-configs-install-instructions/AST
   :literal:

ATB
===

.. include:: coin-configs-install-instructions/ATB
   :literal:

AXE
===

.. include:: coin-configs-install-instructions/AXE
   :literal:

BAT
===

.. include:: coin-configs-install-instructions/BAT
   :literal:

BAY
===

.. include:: coin-configs-install-instructions/BAY
   :literal:

BCBC
====

.. include:: coin-configs-install-instructions/BCBC
   :literal:

BCH
===

.. include:: coin-configs-install-instructions/BCH
   :literal:

BCO
===

.. include:: coin-configs-install-instructions/BCO
   :literal:

BDL
===

.. include:: coin-configs-install-instructions/BDL
   :literal:

BITSOKO
=======

.. include:: coin-configs-install-instructions/BITSOKO
   :literal:

BLK
===

.. include:: coin-configs-install-instructions/BLK
   :literal:

BLOCK
=====

.. include:: coin-configs-install-instructions/BLOCK
   :literal:

BNB
===

.. include:: coin-configs-install-instructions/BNB
   :literal:

BNT
===

.. include:: coin-configs-install-instructions/BNT
   :literal:

BOX
===

.. include:: coin-configs-install-instructions/BOX
   :literal:

BSD
===

.. include:: coin-configs-install-instructions/BSD
   :literal:

BTA
===

.. include:: coin-configs-install-instructions/BTA
   :literal:

BTC
===

.. include:: coin-configs-install-instructions/BTC
   :literal:

BTCL
====

.. include:: coin-configs-install-instructions/BTCL
   :literal:

BTCP
====

.. include:: coin-configs-install-instructions/BTCP
   :literal:

BTCZ
====

.. include:: coin-configs-install-instructions/BTCZ
   :literal:

BTG
===

.. include:: coin-configs-install-instructions/BTG
   :literal:

BTK
===

.. include:: coin-configs-install-instructions/BTK
   :literal:

BTM
===

.. include:: coin-configs-install-instructions/BTM
   :literal:

BTNX
====

.. include:: coin-configs-install-instructions/BTNX
   :literal:

BTX
===

.. include:: coin-configs-install-instructions/BTX
   :literal:

CDT
===

.. include:: coin-configs-install-instructions/CDT
   :literal:

CENNZ
=====

.. include:: coin-configs-install-instructions/CENNZ
   :literal:

CHIPS
=====

.. include:: coin-configs-install-instructions/CHIPS
   :literal:

CIX
===

.. include:: coin-configs-install-instructions/CIX
   :literal:

CMM
===

.. include:: coin-configs-install-instructions/CMM
   :literal:

CMT
===

.. include:: coin-configs-install-instructions/CMT
   :literal:

CRC
===

.. include:: coin-configs-install-instructions/CRC
   :literal:

CRDS
====

.. include:: coin-configs-install-instructions/CRDS
   :literal:

CREA
====

.. include:: coin-configs-install-instructions/CREA
   :literal:

CRW
===

.. include:: coin-configs-install-instructions/CRW
   :literal:

CS
==

.. include:: coin-configs-install-instructions/CS
   :literal:

CVC
===

.. include:: coin-configs-install-instructions/CVC
   :literal:

DAI
===

.. include:: coin-configs-install-instructions/DAI
   :literal:

DASH
====

.. include:: coin-configs-install-instructions/DASH
   :literal:

DATA
====

.. include:: coin-configs-install-instructions/DATA
   :literal:

DCN
===

.. include:: coin-configs-install-instructions/DCN
   :literal:

DGB
===

.. include:: coin-configs-install-instructions/DGB
   :literal:

DGD
===

.. include:: coin-configs-install-instructions/DGD
   :literal:

DGPT
====

.. include:: coin-configs-install-instructions/DGPT
   :literal:

DNR
===

.. include:: coin-configs-install-instructions/DNR
   :literal:

DNT
===

.. include:: coin-configs-install-instructions/DNT
   :literal:

DOGE
====

.. include:: coin-configs-install-instructions/DOGE
   :literal:

DRGN
====

.. include:: coin-configs-install-instructions/DRGN
   :literal:

DROP
====

.. include:: coin-configs-install-instructions/DROP
   :literal:

DRT
===

.. include:: coin-configs-install-instructions/DRT
   :literal:

DSR
===

.. include:: coin-configs-install-instructions/DSR
   :literal:

EFL
===

.. include:: coin-configs-install-instructions/EFL
   :literal:

ELD
===

.. include:: coin-configs-install-instructions/ELD
   :literal:

ELF
===

.. include:: coin-configs-install-instructions/ELF
   :literal:

EMC2
====

.. include:: coin-configs-install-instructions/EMC2
   :literal:

ENG
===

.. include:: coin-configs-install-instructions/ENG
   :literal:

ENJ
===

.. include:: coin-configs-install-instructions/ENJ
   :literal:

EOS
===

.. include:: coin-configs-install-instructions/EOS
   :literal:

ERC
===

.. include:: coin-configs-install-instructions/ERC
   :literal:

ETHOS
=====

.. include:: coin-configs-install-instructions/ETHOS
   :literal:

FAIR
====

.. include:: coin-configs-install-instructions/FAIR
   :literal:

FLLW
====

.. include:: coin-configs-install-instructions/FLLW
   :literal:

FLO
===

.. include:: coin-configs-install-instructions/FLO
   :literal:

FSN
===

.. include:: coin-configs-install-instructions/FSN
   :literal:

FTC
===

.. include:: coin-configs-install-instructions/FTC
   :literal:

FUN
===

.. include:: coin-configs-install-instructions/FUN
   :literal:

GAME
====

.. include:: coin-configs-install-instructions/GAME
   :literal:

GBX
===

.. include:: coin-configs-install-instructions/GBX
   :literal:

GLD
===

.. include:: coin-configs-install-instructions/GLD
   :literal:

GLT
===

.. include:: coin-configs-install-instructions/GLT
   :literal:

GNO
===

.. include:: coin-configs-install-instructions/GNO
   :literal:

GPN
===

.. include:: coin-configs-install-instructions/GPN
   :literal:

GRLC
====

.. include:: coin-configs-install-instructions/GRLC
   :literal:

GRS
===

.. include:: coin-configs-install-instructions/GRS
   :literal:

GTO
===

.. include:: coin-configs-install-instructions/GTO
   :literal:

GUP
===

.. include:: coin-configs-install-instructions/GUP
   :literal:

HMQ
===

.. include:: coin-configs-install-instructions/HMQ
   :literal:

HODLC
=====

.. include:: coin-configs-install-instructions/HODLC
   :literal:

HTML
====

.. include:: coin-configs-install-instructions/HTML
   :literal:

HUC
===

.. include:: coin-configs-install-instructions/HUC
   :literal:

HUSH
====

.. include:: coin-configs-install-instructions/HUSH
   :literal:

HXX
===

.. include:: coin-configs-install-instructions/HXX
   :literal:

HYD
===

.. include:: coin-configs-install-instructions/HYD
   :literal:

I0C
===

.. include:: coin-configs-install-instructions/I0C
   :literal:

ICN
===

.. include:: coin-configs-install-instructions/ICN
   :literal:

ICX
===

.. include:: coin-configs-install-instructions/ICX
   :literal:

IND
===

.. include:: coin-configs-install-instructions/IND
   :literal:

INN
===

.. include:: coin-configs-install-instructions/INN
   :literal:

IOP
===

.. include:: coin-configs-install-instructions/IOP
   :literal:

IOST
====

.. include:: coin-configs-install-instructions/IOST
   :literal:

JOI
===

.. include:: coin-configs-install-instructions/JOI
   :literal:

KIN
===

.. include:: coin-configs-install-instructions/KIN
   :literal:

KMD
===

.. include:: coin-configs-install-instructions/KMD
   :literal:

KNC
===

.. include:: coin-configs-install-instructions/KNC
   :literal:

KNG
===

.. include:: coin-configs-install-instructions/KNG
   :literal:

KREDS
=====

.. include:: coin-configs-install-instructions/KREDS
   :literal:

LBC
===

.. include:: coin-configs-install-instructions/LBC
   :literal:

LIKE
====

.. include:: coin-configs-install-instructions/LIKE
   :literal:

LINK
====

.. include:: coin-configs-install-instructions/LINK
   :literal:

LOOM
====

.. include:: coin-configs-install-instructions/LOOM
   :literal:

LRC
===

.. include:: coin-configs-install-instructions/LRC
   :literal:

LTC
===

.. include:: coin-configs-install-instructions/LTC
   :literal:

LTZ
===

.. include:: coin-configs-install-instructions/LTZ
   :literal:

LUN
===

.. include:: coin-configs-install-instructions/LUN
   :literal:

LYS
===

.. include:: coin-configs-install-instructions/LYS
   :literal:

MAC
===

.. include:: coin-configs-install-instructions/MAC
   :literal:

MAGA
====

.. include:: coin-configs-install-instructions/MAGA
   :literal:

MAN
===

.. include:: coin-configs-install-instructions/MAN
   :literal:

MANA
====

.. include:: coin-configs-install-instructions/MANA
   :literal:

MCO
===

.. include:: coin-configs-install-instructions/MCO
   :literal:

MGO
===

.. include:: coin-configs-install-instructions/MGO
   :literal:

MKR
===

.. include:: coin-configs-install-instructions/MKR
   :literal:

MLM
===

.. include:: coin-configs-install-instructions/MLM
   :literal:

MMX
===

.. include:: coin-configs-install-instructions/MMX
   :literal:

MNX
===

.. include:: coin-configs-install-instructions/MNX
   :literal:

MONA
====

.. include:: coin-configs-install-instructions/MONA
   :literal:

MOON
====

.. include:: coin-configs-install-instructions/MOON
   :literal:

MTL
===

.. include:: coin-configs-install-instructions/MTL
   :literal:

MUE
===

.. include:: coin-configs-install-instructions/MUE
   :literal:

MYB
===

.. include:: coin-configs-install-instructions/MYB
   :literal:

NAS
===

.. include:: coin-configs-install-instructions/NAS
   :literal:

NAV
===

.. include:: coin-configs-install-instructions/NAV
   :literal:

NMC
===

.. include:: coin-configs-install-instructions/NMC
   :literal:

NMR
===

.. include:: coin-configs-install-instructions/NMR
   :literal:

NOAH
====

.. include:: coin-configs-install-instructions/NOAH
   :literal:

NULS
====

.. include:: coin-configs-install-instructions/NULS
   :literal:

OCC
===

.. include:: coin-configs-install-instructions/OCC
   :literal:

OCT
===

.. include:: coin-configs-install-instructions/OCT
   :literal:

OMG
===

.. include:: coin-configs-install-instructions/OMG
   :literal:

ONNI
====

.. include:: coin-configs-install-instructions/ONNI
   :literal:

PAC
===

.. include:: coin-configs-install-instructions/PAC
   :literal:

PAT
===

.. include:: coin-configs-install-instructions/PAT
   :literal:

PAY
===

.. include:: coin-configs-install-instructions/PAY
   :literal:

PCL
===

.. include:: coin-configs-install-instructions/PCL
   :literal:

PGN
===

.. include:: coin-configs-install-instructions/PGN
   :literal:

PIVX
====

.. include:: coin-configs-install-instructions/PIVX
   :literal:

POLIS
=====

.. include:: coin-configs-install-instructions/POLIS
   :literal:

POLY
====

.. include:: coin-configs-install-instructions/POLY
   :literal:

POWR
====

.. include:: coin-configs-install-instructions/POWR
   :literal:

PRL
===

.. include:: coin-configs-install-instructions/PRL
   :literal:

PURA
====

.. include:: coin-configs-install-instructions/PURA
   :literal:

PURC
====

.. include:: coin-configs-install-instructions/PURC
   :literal:

PYRO
====

.. include:: coin-configs-install-instructions/PYRO
   :literal:

QBIT
====

.. include:: coin-configs-install-instructions/QBIT
   :literal:

QSP
===

.. include:: coin-configs-install-instructions/QSP
   :literal:

QTUM
====

.. include:: coin-configs-install-instructions/QTUM
   :literal:

R

.. include:: coin-configs-install-instructions/R
   :literal:

RCN
===

.. include:: coin-configs-install-instructions/RCN
   :literal:

RDN
===

.. include:: coin-configs-install-instructions/RDN
   :literal:

REP
===

.. include:: coin-configs-install-instructions/REP
   :literal:

REQ
===

.. include:: coin-configs-install-instructions/REQ
   :literal:

RHOC
====

.. include:: coin-configs-install-instructions/RHOC
   :literal:

RLC
===

.. include:: coin-configs-install-instructions/RLC
   :literal:

RLTY
====

.. include:: coin-configs-install-instructions/RLTY
   :literal:

ROGER
=====

.. include:: coin-configs-install-instructions/ROGER
   :literal:

RVN
===

.. include:: coin-configs-install-instructions/RVN
   :literal:

RVT
===

.. include:: coin-configs-install-instructions/RVT
   :literal:

SALT
====

.. include:: coin-configs-install-instructions/SALT
   :literal:

SAN
===

.. include:: coin-configs-install-instructions/SAN
   :literal:

SANC
====

.. include:: coin-configs-install-instructions/SANC
   :literal:

SCRIV
=====

.. include:: coin-configs-install-instructions/SCRIV
   :literal:

SEQ
===

.. include:: coin-configs-install-instructions/SEQ
   :literal:

SIB
===

.. include:: coin-configs-install-instructions/SIB
   :literal:

SMART
=====

.. include:: coin-configs-install-instructions/SMART
   :literal:

SMC
===

.. include:: coin-configs-install-instructions/SMC
   :literal:

SNT
===

.. include:: coin-configs-install-instructions/SNT
   :literal:

SPANK
=====

.. include:: coin-configs-install-instructions/SPANK
   :literal:

SPK
===

.. include:: coin-configs-install-instructions/SPK
   :literal:

SRN
===

.. include:: coin-configs-install-instructions/SRN
   :literal:

STAK
====

.. include:: coin-configs-install-instructions/STAK
   :literal:

STORJ
=====

.. include:: coin-configs-install-instructions/STORJ
   :literal:

STORM
=====

.. include:: coin-configs-install-instructions/STORM
   :literal:

STRM41
======

.. include:: coin-configs-install-instructions/STRM41
   :literal:

STWY
====

.. include:: coin-configs-install-instructions/STWY
   :literal:

SUB
===

.. include:: coin-configs-install-instructions/SUB
   :literal:

SWT
===

.. include:: coin-configs-install-instructions/SWT
   :literal:

SXC
===

.. include:: coin-configs-install-instructions/SXC
   :literal:

SYS
===

.. include:: coin-configs-install-instructions/SYS
   :literal:

THETA
=====

.. include:: coin-configs-install-instructions/THETA
   :literal:

TIME
====

.. include:: coin-configs-install-instructions/TIME
   :literal:

TRC
===

.. include:: coin-configs-install-instructions/TRC
   :literal:

TRX
===

.. include:: coin-configs-install-instructions/TRX
   :literal:

TUSD
====

.. include:: coin-configs-install-instructions/TUSD
   :literal:

UCASH
=====

.. include:: coin-configs-install-instructions/UCASH
   :literal:

UFO
===

.. include:: coin-configs-install-instructions/UFO
   :literal:

UIS
===

.. include:: coin-configs-install-instructions/UIS
   :literal:

USDT
====

.. include:: coin-configs-install-instructions/USDT
   :literal:

VEN
===

.. include:: coin-configs-install-instructions/VEN
   :literal:

VIA
===

.. include:: coin-configs-install-instructions/VIA
   :literal:

VIVO
====

.. include:: coin-configs-install-instructions/VIVO
   :literal:

VOT
===

.. include:: coin-configs-install-instructions/VOT
   :literal:

VRSC
====

.. include:: coin-configs-install-instructions/VRSC
   :literal:

VRT
===

.. include:: coin-configs-install-instructions/VRT
   :literal:

VSL
===

.. include:: coin-configs-install-instructions/VSL
   :literal:

VTC
===

.. include:: coin-configs-install-instructions/VTC
   :literal:

WAVI
====

.. include:: coin-configs-install-instructions/WAVI
   :literal:

WAX
===

.. include:: coin-configs-install-instructions/WAX
   :literal:

WINGS
=====

.. include:: coin-configs-install-instructions/WINGS
   :literal:

WTC
===

.. include:: coin-configs-install-instructions/WTC
   :literal:

XCG
===

.. include:: coin-configs-install-instructions/XCG
   :literal:

XMCC
====

.. include:: coin-configs-install-instructions/XMCC
   :literal:

XMY
===

.. include:: coin-configs-install-instructions/XMY
   :literal:

XOV
===

.. include:: coin-configs-install-instructions/XOV
   :literal:

XRE
===

.. include:: coin-configs-install-instructions/XRE
   :literal:

XSG
===

.. include:: coin-configs-install-instructions/XSG
   :literal:

XSN
===

.. include:: coin-configs-install-instructions/XSN
   :literal:

XZC
===

.. include:: coin-configs-install-instructions/XZC
   :literal:

ZCL
===

.. include:: coin-configs-install-instructions/ZCL
   :literal:

ZEC
===

.. include:: coin-configs-install-instructions/ZEC
   :literal:

ZEL
===

.. include:: coin-configs-install-instructions/ZEL
   :literal:

ZER
===

.. include:: coin-configs-install-instructions/ZER
   :literal:

ZET
===

.. include:: coin-configs-install-instructions/ZET
   :literal:

ZIL
===

.. include:: coin-configs-install-instructions/ZIL
   :literal:

ZOI
===

.. include:: coin-configs-install-instructions/ZOI
   :literal:

ZRX
===

.. include:: coin-configs-install-instructions/ZRX
   :literal:

