#!/usr/bin/env python3
from scapy.all import *

source_ip = '10.9.0.1' # The IP to filter the packets from
destination_port = 23 # The Port number to filter the packets

def print_pkt(pkt):
    is_valid_tcp_pkt = IP in pkt and TCP in pkt

    if is_valid_tcp_pkt:
        is_telnet_pkt = pkt[IP].src == source_ip and pkt[TCP].dport == destination_port
        if is_telnet_pkt:
            pkt.show()

pkt = sniff(iface='br-50353f7ab3af', filter='tcp', prn=print_pkt)
