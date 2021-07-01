import requests

base_url = "http://testphp.vulnweb.com/listproducts.php?cat="
fuzdb = open("fuzzdb-mysql.txt", "r")
for item in fuzdb.readlines():
    target_url = base_url + item
    # print(target_url)
    response = requests.get(target_url)

    if "SQL syntax" in str(response.content):
        print(target_url)

