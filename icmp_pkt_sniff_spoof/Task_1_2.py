#!/usr/bin/env python3

from scapy.all import *

ip_obj = IP()
ip_obj.src = '1.2.3.4'
ip_obj.dst = '10.9.0.5'

icmp_packet = ICMP()

send(ip_obj/icmp_packet)
