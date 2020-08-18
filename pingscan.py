# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 14:30:25 2020

@author: fikirsanat
"""

import os
import platform


from datetime import datetime
#pip install getmac
from getmac import get_mac_address


net = '192.168.1.60'#input("Enter the Network Address: ")
net1= net.split('.')
a = '.'

net2 = net1[0] + a + net1[1] + a + net1[2] + a
st1 = int(input("Enter the Starting Number: "))
en1 = int(input("Enter the Last Number: "))
en1 = en1 + 1
oper = platform.system()

if (oper == "Windows"):
   ping1 = "ping -n 1 "
elif (oper == "Linux"):
   ping1 = "ping -c 1 "
else :
   ping1 = "ping -c 1 "
t1 = datetime.now()
print ("Scanning in Progress:")

for ip in range(st1,en1):
   addr = net2 + str(ip)
   comm = ping1 + addr
   response = os.popen(comm)
   #print(comm)
   for line in response.readlines():
     # print(response) 
      #print(line)

      if (line.count("TTL")):  
         print (addr, "--> Live","Mac Address:",get_mac_address(ip=addr))
         
t2 = datetime.now()
total = t2 - t1
print ("Scanning completed in: ",total)