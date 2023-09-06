#!/usr/bin/env python3
import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = sys.argv[1]
port = int(sys.argv[2])

if sock.connect_ex((ip, port)):
    print('Port', port, 'is closed')
else:
    print('Port', port, 'is open')

