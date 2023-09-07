#!/usr/bin/env python3
from scapy.all import *

source_ip = '10.9.0.1'  # The IP to filter the packets from
destination_port = 23  # The Port number to filter the packets


def print_pkt(pkt):
    is_valid_tcp_pkt = IP in pkt and TCP in pkt

    if is_valid_tcp_pkt:
        pkt.show()


pkt_filter = f"tcp and src host {source_ip} and dst port {destination_port}"
pkt = sniff(iface='br-de2a1d2003ef', filter=pkt_filter, prn=print_pkt)
