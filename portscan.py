# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 14:53:58 2020

@author: fikirsanat
"""

import pyfiglet 
import sys 
import socket 
from datetime import datetime 
   

ascii_banner = pyfiglet.figlet_format("IFS") 
print(ascii_banner) 

target='192.168.1.60'
  
# Add Banner  
print("-" * 50) 
print("Scanning Target: " + target) 
print("Scanning started at:" + str(datetime.now())) 
print("-" * 50) 
   

try:
        # will scan ports between 1 to 65,535 
    for port in range(0,50): 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        socket.setdefaulttimeout(1) 
              
            # returns an error indicator 
        result = s.connect_ex((target,port)) 
        print('Port {} is checked'.format(port))
        if result ==0: 
            print("Port {} is open".format(port)) 
        s.close() 
    #Ctrl+C
except KeyboardInterrupt: 
        print("\n Exitting Program !!!!") 
        sys.exit() 
except socket.gaierror: 
        print("\n Hostname Could Not Be Resolved !!!!") 
        sys.exit() 
except socket.error: 
        print("\ Server not responding !!!!") 
        sys.exit() 
          
        