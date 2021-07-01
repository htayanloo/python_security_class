import requests

BASE_URL = "https://api.shodan.io/"

def shodan_search_host(token,target,minify=False):
    seach_url = f"shodan/host/{target}?key={token}"
    result = requests.get(f"{BASE_URL}{seach_url}&minify={minify}").json()
    return result

print(shodan_search_host(token="zoXb9dtd58puobXboaEfYjMi7X14rjwG",target="8.8.8.8",minify=True))