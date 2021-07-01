from scapy.all import *
from scapy.layers import http
from scapy.layers.inet import TCP, IP


def proccess_sniff(packet):
    if packet[TCP].payload:
        if packet[IP].dport == 443:
            print(str(bytes(packet[IP].payload)).split("\n"))
    # if packet.hashlayer(http.HTTPRequest):
    #     print("A")

sniff(iface="eth0",store=False,prn=proccess_sniff,filter="tcp")

