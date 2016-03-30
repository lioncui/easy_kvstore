#!/usr/bin/python
# -*- coding:UTF-8 -*-

import socket
import traceback
import sys

def connect_kvserver(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
        sock.connect((host, port))
        while True:
            try:
                cli = raw_input('%s:6375> ' % server)
                sock.sendall(cli)
                if cli == "exit":
                    break
                receive = sock.recv(1024)
                if receive != 'None':
                    print receive
            except KeyboardInterrupt:
                sock.sendall('exit')
                print "\nKeyboardInterrupt - Exit"
                break
        sock.close()
    except:
        print "Connection %s %s failed.." % (host, port)

if __name__ == '__main__':
    try:
        server = sys.argv[1]
    except IndexError:
        server = 'localhost'
    try:
        port = int(sys.argv[2])
    except Exception as e:
        port = 6375
    connect_kvserver(server, port)

