#!/usr/bin/env python3

from scapy.all import *


def print_pkt(pkt):
    """
    This function takes the packet as input and prints its properties
    :param pkt: Packet sniffed by scapy
    :return: None
    """
    pkt.show()


def sniff_packets(network):
    """
    This function filters the packets that has either src or dst of the provided network
    using Berkeley Packet Filter (BPF).
    References: https://biot.com/capstats/bpf.html https://scapy.readthedocs.io/en/latest/usage.html
    :param network: Network Number
    :return: Returns the packed sniffed
    """
    sniffed_packets = sniff(filter="dst net " + network + " or src net " + network, prn=print_pkt)
    return sniffed_packets


subnet = '153.91.1.0/24'  # UCM subnet
sniff_packets(subnet)
