********************************************
Calculate Komodo rewards using an npm module  
********************************************

This module has been created by `Luke Childs <https://github.com/lukechilds>`__ a developer in the Komodo ecosystem.

    * **Source code**: https://github.com/atomiclabs/get-komodo-rewards
    * **npm module**: https://www.npmjs.com/package/get-komodo-rewards

Install
=======

.. code-block:: shell

    npm install get-komodo-rewards

Usage
=====

Pass in a utxo object and an integer of the ``accrued rewards`` in satoshis will be returned.

.. code-block:: js

    const getKomodoRewards = require('get-komodo-rewards');

    const utxo = {
      tiptime: 1552292091,
      locktime: 1552248193,
      height: 1263192,
      satoshis: 3206795322480
    };

    const rewards = getKomodoRewards(utxo);
    // 205000320

.. tip::

    * ``tiptime`` should be the current tiptime from komodod.
    * If you don't have access to this, you can use a client-side generated ``UNIX timestamp`` at the cost of slightly reduced accuracy. If you do this, use **a timestamp ~10 minutes in the past** to avoid over calculating the rewards and creating an invalid transaction.

API
===

getKomodoRewards(utxo)
----------------------

Returns the accrued rewards in satoshis.

+------+----------+------------------------------------------------------------+
| Name | Type     | Description                                                |
+======+==========+============================================================+
| utxo | (Object) | An object containing the following properties of the UTXO. |
+------+----------+------------------------------------------------------------+

Keys of the ``utxo`` object
^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------+----------+------------------------------------------------------------+
| Name     | Type     | Description                                                |
+==========+==========+============================================================+
| tiptime  | (number) | The current tiptime of the Komodo blockchain.              |
+----------+----------+------------------------------------------------------------+
| locktime | (number) | The locktime value of the UTXO.                            |
+----------+----------+------------------------------------------------------------+
| height   | (number) | The height of the UTXO.                                    |
+----------+----------+------------------------------------------------------------+
| satoshis | (number) | The value of the UTXO in satoshis.                         |
+----------+----------+------------------------------------------------------------+

License
-------

MIT © Atomic Labs

MIT © Luke Childs    
