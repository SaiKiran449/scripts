#!/bin/bash

iptables -A FORWARD -i eth0 -d 192.168.60.5 -p tcp --dport 23 -j ACCEPT
iptables -A FORWARD -i eth1 -s 192.168.60.5 -p tcp --sport 23 -j ACCEPT

iptables -A FORWARD -p tcp -j DROP
iptables -P FORWARD ACCEPT
