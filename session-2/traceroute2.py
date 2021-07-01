from scapy.layers.inet import traceroute

res4,unans=traceroute(["8.8.8.8","4.2.2.4","1.1.1.1"])
res4.show( )
