from scapy.all import sniff, scapy
from scapy.layers import http
from scapy.layers.inet import IP


def process_tcp_packet(packet):
    '''
    Processes a TCP packet, and if it contains an HTTP request, it prints it.
    '''
    if not packet.haslayer(http.HTTPRequest):
        # This packet doesn't contain an HTTP request so we skip it
        return
    http_layer = packet.getlayer(http.HTTPRequest)
    ip_layer = packet.getlayer(IP)
    print(http_layer)
    print('\n{0[src]} just requested a {1[Method]} {1[Host]}{1[Path]}'.format(ip_layer.fields, http_layer.fields))


# Start sniffing the network.
sniff(filter='tcp', prn=process_tcp_packet)
