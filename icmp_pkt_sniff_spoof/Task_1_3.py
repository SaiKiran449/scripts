#!/usr/bin/env python3
from scapy.all import *

ip_obj = IP()
ip_obj.dst = '8.8.8.8'  # The destination IP address
ip_obj.ttl = 1

icmp_pkt = ICMP()

is_pkt_dropped = True
total_routers = 0

while is_pkt_dropped:
    response = sr1(ip_obj/icmp_pkt, timeout=2, verbose=False)

    is_packet_dropped_by_router = response and response.type == 11 and response.code == 0
    if is_packet_dropped_by_router:
        # Checks if the packet is dropped by the router with time exceeded message
        total_routers = total_routers + 1
        print(f"{total_routers} {response.src}")
        ip_obj.ttl = ip_obj.ttl + 1
    else:
        is_pkt_dropped = False
