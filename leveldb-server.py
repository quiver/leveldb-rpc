# vim: set fileencoding=utf8
'''XML-RPC server for leveldb
'''
import argparse
from SimpleXMLRPCServer import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler

import leveldb

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class LevelDBMethod(object):
    def __init__(self, datadir):
        self.db = leveldb.LevelDB(datadir)

    def put(self, key, value):
        return self.db.Put(key, value)
    
    def get(self, key):
        try:
            return self.db.Get(key)
        except KeyError, err:
            return ''
    
    def delete(self, key):
        return self.db.Delete(key)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, nargs='?', default=8000)
    parser.add_argument('--datadir', type=str, nargs='?', default='data')
    args =  parser.parse_args()

    # Create server
    server = SimpleXMLRPCServer(("localhost", args.port),
                                requestHandler=RequestHandler,
                                allow_none=True)
    server.register_introspection_functions()
    server.register_instance(LevelDBMethod(args.datadir))
    server.serve_forever()

if __name__ == '__main__':
    main()
