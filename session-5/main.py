import requests
from bs4 import BeautifulSoup
import re

"""
pip3 install requests[socks]
"""

session = requests.Session()
session.headers.update({'User-agent':'Custome user agent'})
response = session.get("https://spys.one/en/free-proxy-list/")

soup = BeautifulSoup(response.content,'html.parser')
temp = soup.find_all(attrs={"onmouseover":"this.style.background='#002424'"})

proxy_list =[]

for item in temp:
    all_td = item.findAll('td')
    #ip_address = re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",str(all_td[0].text))
    #print(ip_address.group())
    proxy_server ={
        "ip":all_td[0].text,
        "type":all_td[1].text,
        "anony":all_td[2].text,
        "country":all_td[3].text,
        "hostname":all_td[4].text,
        "latency":all_td[5].text,
        "speed":all_td[6].text,
        "uptime":all_td[7].text,
        "check_date":all_td[8].text,
    }
    proxy_list.append(proxy_server)



print(proxy_list)
for item in proxy_list:
    print(item)
#
# proxies ={
#     "http":"socks5://127.0.0.1:8080",
#     "https":"http://127.0.0.1:8080",
# }
#
# requests.get("https://spys.one/en/free-proxy-list/",proxies=proxies)