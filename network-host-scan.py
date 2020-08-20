# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 13:42:33 2020

@author: fikirsanat
"""

import sys
import os
import platform
from datetime import datetime
from getmac import get_mac_address
import requests
from threading import Thread
import queue
import time




ip_address = queue.Queue()
mac_address_que = queue.Queue()
oper = platform.system()



print ("-->System:"+platform.system())
print ("-->Version:"+platform.version())
print ("-->Machine:"+platform.machine())
print("")
print ("Scanning Hosts:")



def gethostname(mac_address):
     url = 'https://api.macvendors.com/'+mac_address
     res = requests.get(url)
     return res.text


def scan1(que):
    while True:    
        ip = que.get()
        comm = ping1 + ip
        response = os.popen(comm)
        for line in response.readlines():
           if (line.count("TTL")):  
               mac_address = get_mac_address(ip=ip)
               mac_address_que.put(ip+'?'+mac_address)
               
        
        que.task_done()


def get_mac_name(que):
    while True:
        info=que.get()
       
        info2= info.split('?')
        ipadress=info2[0]
        this_mac_address=info2[1]
        time.sleep(2)
        print(ipadress+' Is Live : Mac Address-->'+this_mac_address+"-->"+gethostname(this_mac_address))
        que.task_done()



if __name__=='__main__':

    try:
    
        net = '192.168.1.60'#input("Enter the Network Address: ")
        net1= net.split('.')
        a = '.'
        
        net2 = net1[0] + a + net1[1] + a + net1[2] + a
        
        
        st1 = 0
        en1 = 50
    
        t1 = datetime.now()
    
    
        
        
        if (oper == "Windows"):
           ping1 = "ping -n 1 "
        elif (oper == "Linux"):
           ping1 = "ping -c 1 "
        else :
           ping1 = "ping -c 1 "
        
       
        
        for i in range(st1,en1):
            ip_address.put(net2+str(i))
            
        
        for i in range(30):
            t = Thread(target=scan1,args=(ip_address,))
            t.daemon = True
            t.start()
        
        
        
        
        ip_address.join()
        
        t = Thread(target=get_mac_name,args=(mac_address_que,))
        t.daemon = True
        t.start()
        
        
        mac_address_que.join()
        
        t2 = datetime.now()
        total = t2 - t1
        
        print("Scanning completed in: ",total)
        print("Press any key for close")
        close=input()
        
    
    except KeyboardInterrupt: 
        print("\n Exitting Program !!!!") 
        sys.exit() 
   


         
