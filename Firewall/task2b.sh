#!/bin/bash

iptables -A FORWARD -i eth0 -p icmp --icmp-type echo-request -j DROP
iptables -A FORWARD -i eth1 -p icmp --icmp-type echo-request -j ACCEPT
iptables -A FORWARD -p icmp --icmp-type echo-reply -j ACCEPT
iptables -P FORWARD DROP
