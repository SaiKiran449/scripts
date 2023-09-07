#!/usr/bin/env python3

from scapy.all import *


def spoof(pkt):
    if ICMP in pkt and (pkt[ICMP].type == 8):
        src = pkt[IP].src
        dst = pkt[IP].dst
        seq = pkt[ICMP].seq
        id = pkt[ICMP].id
        load = pkt[Raw].load
        reply = IP(src=dst, dst=src) / ICMP(type=0, id=id, seq=seq) / load
        
        print("Spoofed packet.......")
        print("Source IP:",reply[IP].src)
        print("Destination IP:", reply[IP].dst)

        send(reply, verbose=0)


sniff(iface='br-de2a1d2003ef', filter='icmp and src host 10.9.0.5', prn=spoof)
