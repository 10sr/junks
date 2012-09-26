#!/usr/bin/env python3
# UNIX domain Echo server
import socket
import os

def main() :
    PIPE = '/tmp/socket54321'
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s.bind(PIPE)
    s.listen(1)
    conn, addr = s.accept()
    print('Connected.')
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print('Echoing:' + data.decode())
        conn.send(data)
    print('Closing.')
    conn.close()
    os.unlink(PIPE)

main()
