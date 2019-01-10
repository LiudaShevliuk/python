#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import random

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
names = ('Liuda', 'Tania', 'Vlad', 'Yura')
phrases = ('How old are you?',
           'Where are you from?',
           'Nice weather, isn\'t it?',
           'How are you?',
           'Tell me smth about yourself')
hello = True

host = '127.0.0.1'
port = 9999

serversocket.bind((host, port))

serversocket.listen(5)
print('The server is waiting for connection')

clientsocket, addr = serversocket.accept()
print('Got a connection from {}'.format(addr))

while True:
    if hello:
        clientsocket.send('Hello! My name is Jack and your\'s?'.encode('utf-8'))
        hello = False

    client_answer = clientsocket.recv(1024)
    print(client_answer.decode('utf-8'))

    if client_answer.decode('utf-8') in names:
        clientsocket.send('Nice to meet you '.encode('utf-8') \
                          + client_answer +'\n'.encode('utf-8'))
        continue
    elif client_answer.decode('utf-8') == "How are you?":
        clientsocket.send('Perfect!\n'.encode('utf-8'))
        continue
    elif client_answer.decode('utf-8') == "Goodbye":
        clientsocket.send('Bye, have a nice day!\n'.encode('utf-8'))
        break
    else:
        clientsocket.send(random.choice(phrases).encode('utf-8') \
                          + '\n'.encode('utf-8'))
        continue
   
clientsocket.close()

