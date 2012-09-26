#!/usr/bin/env python3
# UNIX domain Echo client
import socket

def main() :
    PIPE = '/tmp/socket54321'
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    print('Connecting %s.' % repr(PIPE))
    s.connect(PIPE)
    try:
        while True:
            t = input('> ')
            s.send(t.encode())
            data = s.recv(1024)
            print('Received:' + data.decode())
    except (EOFError, KeyboardInterrupt):
        pass
    print('Closing.')
    s.close()

main()
