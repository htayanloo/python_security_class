from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
import re

driver = webdriver.Chrome(executable_path="/home/hadi/chromedriver")
driver.get("https://spys.one/en/free-proxy-list/")

lines = driver.find_elements_by_xpath("//tr[@class='spy1x']/td")
for line in lines:
    try:
        ip_address = re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",str(line.text))
    except:
        pass
    else:
        temp = line.text.split(":")
        if len(temp)==2:
            print(line.text)
    #print(line.text)

# lines = driver.find_elements_by_xpath("//tr[@class='spy1xx']/td")
# for line in lines:
#     print(line.text)


