#!/usr/bin/python
# -*- coding:UTF-8 -*-

import socket
import traceback
from datetime import datetime

help_doc = '''
help                - print help_doc .
set <key> <value>   - store the key/value .
get <key>           - get the vaule of <key> .
flushall            - clean the store data . 
exit                - exit connection .
'''

host = '0.0.0.0'
port = 6375

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(10)
print "%s Starting kvserver now...." % datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
storedata = {}
while True:
    conn, addr = sock.accept()
    print "%s connection from %s " % (datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"), addr[0])
    while True:
        senddata = "None"
        try:
            accept_cmd = conn.recv(1024)
            cli_tuple = accept_cmd.split(" ")
            if cli_tuple is None:
                pass
            elif cli_tuple[0] == 'set' and len(cli_tuple) == 3:
                key = cli_tuple[1]
                value = cli_tuple[2]
                storedata[key] = value
                senddata = 'OK'
            elif cli_tuple[0] == 'get' and len(cli_tuple) == 2:
                key = cli_tuple[1]
                senddata = storedata.get(key, 'None')
            elif cli_tuple[0] == 'auth' and len(cli_tuple) == 3:
                pass
            elif accept_cmd == 'exit':
                print "%s %s exit" % (datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"), addr[0])
                break
            elif accept_cmd == 'flushall':
                storedata = {}
            else:
                senddata = help_doc
            conn.sendall(senddata)
        except socket.error:
            break
sock.close()
