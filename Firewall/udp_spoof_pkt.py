#!/usr/bin/python3
from scapy.all import *

print("Sending Spoofed ICMP packet.....")
ip = IP(dst="10.9.0.11")
data="hello\n"
srcport=5000

for i in range (10):
    udp = UDP(sport=srcport, dport=8080)
    srcport +=1
    payload = data + str(i) + '\n'
    pkt = ip/udp/payload
    send(pkt, verbose=0)
