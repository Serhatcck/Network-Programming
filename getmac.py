# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 16:15:11 2020

@author: fikirsanat
"""

from getmac import get_mac_address

eth_mac = get_mac_address(interface="eth0")
win_mac = get_mac_address(interface="Ethernet 3")
ip_mac = get_mac_address(ip="192.168.0.1")
ip6_mac = get_mac_address(ip6="::1")
host_mac = get_mac_address(hostname="localhost")
updated_mac = get_mac_address(ip="10.0.0.1", network_request=True)