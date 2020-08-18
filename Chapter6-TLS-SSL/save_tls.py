# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 14:22:20 2020

@author: fikirsanat
"""
"""

runfile('C:/Users/fikirsanat/Documents/Network Programming/Chapter6-TLS-SSL/save_tls.py',args="-s localhost.pem localhost 1060 " ,wdir='C:/Users/fikirsanat/Documents/Network Programming/Chapter6-TLS-SSL')


runfile('C:/Users/fikirsanat/Documents/Network Programming/Chapter6-TLS-SSL/save_tls.py',args="-a ca.crt localhost 1060 " ,wdir='C:/Users/fikirsanat/Documents/Network Programming/Chapter6-TLS-SSL')
"""

import argparse,socket,ssl

def client(host,port,cafile=None):
    purpose = ssl.Purpose.SERVER_AUTH
    context = ssl.create_default_context(purpose, cafile=cafile)
    
    raw_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    raw_sock.connect((host, port))
    print('Connected to host {!r} and port {}'.format(host, port))
    ssl_sock = context.wrap_socket(raw_sock, server_hostname=host)
    
    while True:
        data = ssl_sock.recv(1024)
        if not data:
            break
        print(repr(data))
        
def server(host,port,certfile,cafile=None):
    purpose = ssl.Purpose.CLIENT_AUTH
    context = ssl.create_default_context(purpose, cafile=cafile)
    context.load_cert_chain(certfile)
    
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind((host, port))
    listener.listen(1)
    print('Listening at interface {!r} and port {}'.format(host, port))
    raw_sock, address = listener.accept()
    print('Connection from host {!r} and port {}'.format(*address))
    ssl_sock = context.wrap_socket(raw_sock, server_side=True)
    ssl_sock.sendall('Simple is better than complex.'.encode('ascii'))
    ssl_sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Safe TLS client and server')
    parser.add_argument('host', help='hostname or IP address')
    parser.add_argument('port', type=int, help='TCP port number')
    parser.add_argument('-a', metavar='cafile', default=None,
                        help='authority: path to CA certificate PEM file')
    parser.add_argument('-s', metavar='certfile', default=None,
                        help='run as server: path to server PEM file')
    args = parser.parse_args()
    if args.s:
        server(args.host, args.port, args.s, args.a)
    else:
        client(args.host, args.port, args.a)