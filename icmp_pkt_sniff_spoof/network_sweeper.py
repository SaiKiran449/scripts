#!/usr/bin/env python3

from scapy.all import *
import sys


def sweep_network(network):
    """
    This function will ping each IP address in the given network and determine if it's online
    :param network: 
    :return: List of online host IP Addresses
    """
    online_hosts = []
    for host_count in range(1, 11):
        ip_address = "{SUBNET}.{HOST_NUMBER}".format(SUBNET=network, HOST_NUMBER=host_count)
        icmp_request = IP(dst=ip_address) / ICMP()
        icmp_response = sr1(icmp_request, timeout=1, verbose=False)
        
        is_host_online = icmp_response and icmp_response.haslayer(ICMP) and icmp_response[ICMP].type == 0
        if is_host_online:
            online_hosts.append(ip_address)

    return online_hosts


def validate_the_input(len_of_args):
    if len_of_args != 2:
        sys.exit(1)


validate_the_input(len_of_args=len(sys.argv))

subnet = sys.argv[1]
online_hosts = sweep_network(subnet)

if online_hosts:
    print("The following hosts are online")
    for host in online_hosts:
        print(f"{host}")
else:
    print("Couldn't find any online hosts in the given subnet")
