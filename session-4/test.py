import requests

base_url = "http://tayanloo.com"
fuzdb = open("fuzzdb-admin.txt","r")
for item in fuzdb.readlines():
    target_url = base_url + item

    response = requests.get(target_url)
    if response.status_code == 200:
        print(target_url)



