# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 16:49:10 2020

@author: fikirsanat
"""

import sys
from scapy.all import *


ip_basligi =IP(dst='192.168.1.60',src='192.168.1.38',ttl=20)
icmp_basligi = ICMP(type=8,code=0)
icmp_paketi = ip_basligi/icmp_basligi
response = send(icmp_paketi)

print(response) 



