from scapy.all import *
from scapy.layers.l2 import Ether, ARP


# run as root user

def subnet_scanner(start_host=1, end_host=254, subnet="192.168.3."):
    for lsb in range(start_host, end_host):
        ip = subnet + str(lsb)
        # request broadcast address
        arpRequest = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip, hwdst="ff:ff:ff:ff:ff:ff")
        arpResponse = srp1(arpRequest, timeout=1, verbose=0)
        if arpResponse:
            print("IP:" + arpResponse.psrc + "    MAC:" + arpResponse.hwsrc)



if __name__ =="__main__":
	subnet_scanner(start_host=1,end_host=254,subnet="192.168.3.")