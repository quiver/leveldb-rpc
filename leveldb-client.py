# vim: set fileencoding=utf8
'''XML-RPC client for leveldb
'''

import argparse
import cmd
from xmlrpclib import ServerProxy

class Cmd(cmd.Cmd):
    def __init__(self, host, port, *args, **kw):
        cmd.Cmd.__init__(self, *args, **kw)
        self.prompt = '%s:%d> ' % (host, port)
        self.server = ServerProxy('http://%s:%d' % (host, port))

    def do_put(self, arg):
        args =  arg.split()
        if len(args) != 2:
            print "(error) ERR wrong number of arguments for 'put' command"
            return
        key, value = args

        result = self.server.put(key, value)

    def do_get(self, arg):
        args =  arg.split()
        if len(args) != 1:
            print "(error) ERR wrong number of arguments for 'get' command"
            return
        key, = args

        result = self.server.get(key)
        if result:
            print result

    def do_delete(self, arg):
        args =  arg.split()
        if len(args) != 1:
            print "(error) ERR wrong number of arguments for 'delete' command"
            return
        key, = args

        result = self.server.delete(key)

    def do_EOF(self, arg):
        return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, nargs='?', default='localhost')
    parser.add_argument('--port', type=int, nargs='?', default=8000)
    args =  parser.parse_args()

    cmd = Cmd(args.host, args.port)
    cmd.cmdloop()

if __name__ == '__main__':
    main()
