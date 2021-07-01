import pywifi
import time

from pywifi import const

wifi = pywifi.PyWiFi()
print(wifi.interfaces())
iface = wifi.interfaces()[0]

iface.scan()
for i in iface.scan_results():
    print(i.ssid)