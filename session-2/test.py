from scapy.all import sniff, scapy
from scapy.layers import http
from scapy.layers.inet import IP


def packet_ana(packet):
    if not packet.haslayer(http.HTTPRequest):
        return
    http_layer = packet.getlayer(http.HTTPRequest)
    ip_layer = packet.getlayer(IP)
    print(http_layer)


sniff(filter='tcp', prn=packet_ana)
