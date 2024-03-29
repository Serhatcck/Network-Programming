# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 15:47:48 2020

@author: fikirsanat
"""

import dns.resolver,argparse

def lookup(name):
    #A->v4 AAAA->v6  NS->SERVER MX->EMAIL
    for qtype in 'A', 'AAAA', 'CNAME', 'MX', 'NS':
        answer = dns.resolver.query(name,qtype,raise_on_no_answer=False)
        if answer.rrset() is not None:
            print(answer.rrset())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Resolve a name using DNS')
    parser.add_argument('name', help='name that you want to look up in DNS')
    args = parser.parse_args()
    lookup(args.name)