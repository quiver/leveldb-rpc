LevelDB RPC
===========
LevelDB RPC is an XML-RPC based interface for LevelDB.

## Installation

* install leveldb (http://code.google.com/p/leveldb/)
* install py-leveldb (http://code.google.com/p/py-leveldb/)

## Getting Started

Currently, only following methods are supported:
* 'put'
* 'get'
* 'delete'

### start an XMl-RPC server
  $ python leveldb-server.py

You can also specify port number or data directory:

  $ python leveldb-server.py --port=8080 --datadir=testdir

### start an XMl-RPC client
  $ python leveldb-client.py
  localhost:8000> get foo
  localhost:8000> put foo bar
  localhost:8000> get foo
  bar
  localhost:8000> delete foo
  localhost:8000> <CTRL-D>
  $ 

You can also specify hostname or port number:

  $ python leveldb-client.py --host=hostname --port=8080

