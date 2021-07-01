import dns
import dns.resolver


hosts =["sanjesh.org"]

for host in hosts:
    print(host)
    ip = dns.resolver.resolve(host,"MX")
    for item in ip:
        print(item)

