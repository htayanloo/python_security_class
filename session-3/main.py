import nmap3
import ipaddress

scan = nmap3.Nmap()

result = scan.nmap_os_detection("192.168.3.1")

print(result)
for item in result:
    try:
        temp = ipaddress.IPv4Address(item)
    except:
        pass
    else:
        print(result[item])
