#! /usr/bin/python3
from scapy.all import *
import time

src_ip = "192.168.70.7"
dst_ip = "192.168.60.5"

print('Sending spoofed packet')

pkt = IP(src=src_ip, dst=dst_ip)/ICMP()

while True:
    send(pkt)
    print('ICMP: {} --> {}'.format(src_ip, dst_ip))
    time.sleep(1)
