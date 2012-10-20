#!/usr/bin/env python3
# UNIX domain Echo client
import socket

def main() :
    PIPE = '/tmp/socket54321'
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    print('Client:Connecting %s.' % repr(PIPE))
    s.connect(PIPE)
    try:
        while True:
            t = input('> ')
            s.send(t.encode())
            print("Client:Send:" + t)
            data = s.recv(1024)
            print('Client:Received:' + data.decode())
    except (EOFError, KeyboardInterrupt):
        pass
    print('Client:Closing.')
    s.close()

main()
