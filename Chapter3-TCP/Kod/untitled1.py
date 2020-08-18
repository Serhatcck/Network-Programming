# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 12:48:38 2020

@author: fikirsanat
"""


"""
import socket
from pprint import pprint

infolist = socket.getaddrinfo('localhost','ftp')
pprint(infolist)
"""

"""
from socket import getaddrinfo
import socket
"""
"""
print(getaddrinfo(None, 'smtp', 0, socket.SOCK_STREAM, 0, socket.AI_PASSIVE))
print(getaddrinfo(None, 53, 0, socket.SOCK_DGRAM, 0, socket.AI_PASSIVE))

print(getaddrinfo('localhost', 'smtp', 0, socket.SOCK_STREAM, 0))
"""
"""

print(getaddrinfo('iana.org', 'www', 0, socket.SOCK_STREAM, socket.AI_ADDRCONFIG | socket.AI_V4MAPPED))
print(getaddrinfo('iana.org', 'www', 0, socket.SOCK_STREAM, 0))
print(getaddrinfo('iana.org', 'www', 0, socket.SOCK_STREAM, socket.AI_ADDRCONFIG | socket.AI_V4MAPPED | socket.AI_CANONNAME))
"""


import argparse
import dns.resolver

def lookup(name):
    for qtype in 'A','AAA','CNAME','MX','NS':
        answer = dns.resolver.query(name,qtype,raise_on_no_answer=False)
        if answer.rrset is not None:
            print(answer.rrset)
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Resolve a name using DNS')
    parser.add_argument('name', help='name that you want to look up in DNS')
    lookup(parser.parse_args().name)