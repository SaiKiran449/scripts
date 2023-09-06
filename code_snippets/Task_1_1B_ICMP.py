#!/usr/bin/env python3
from scapy.all import *
def print_pkt(pkt):
    pkt.show()
pkt = sniff(iface='br-50353f7ab3af', filter='icmp', prn=print_pkt)
