#!/bin/bash

iptables -A FORWARD -i eth0 -d 192.168.60.5 -p tcp --dport 23 --syn -j ACCEPT
iptables -A FORWARD -i eth1 -p tcp --syn -j ACCEPT
iptables -A FORWARD -p tcp -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -p tcp -j DROP
iptables -P FORWARD ACCEPT
