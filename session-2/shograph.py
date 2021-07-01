from scapy.layers.inet import traceroute

res4,unans=traceroute(["217.218.127.128"])
res4.show( )
res4.graph()
