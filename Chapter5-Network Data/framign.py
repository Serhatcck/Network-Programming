# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 13:37:02 2020

@author: fikirsanat
"""
import socket 
from argparse import ArgumentParser


def server(address):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sock.bind(address)
    sock.listen(1)
    
    print('Run this script in another windows with"-c"to connect')
    print('Listening at',sock.getsockname())
    sc,sockname = sock.accept()
    print('Accept connection from',sockname)
    sc.shutdown(socket.SHUT_WR)
    message = b''
    while True:
        more = sc.recv(8192)
        
        if not more:
            print('Received zero bytes - end of file')
            break
        print('Received {} bytes '.format(len(more)))
        message += more
    
    print('Message:\n')
    print(message.decode('ascii'))
    sc.close()
    sock.close()
    
def client(address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    sock.shutdown(socket.SHUT_RD)
    sock.sendall(b'Beautiful is better than ugly.\n')
    sock.sendall(b'Explicit is better than implicit.\n')
    sock.sendall(b'Simple is better than complex.\n')
    sock.close()
    
if __name__ == '__main__':
    parser = ArgumentParser(description='Transmit & receive a data stream')
    parser.add_argument('hostname', nargs='?', default='127.0.0.1',help='IP address or hostname (default: %(default)s)')
    parser.add_argument('-c', action='store_true', help='run as the client')
    parser.add_argument('-p', type=int, metavar='port', default=1060,help='TCP port number (default: %(default)s)')
    args = parser.parse_args()
    function = client if args.c else server
    function((args.hostname, args.p))