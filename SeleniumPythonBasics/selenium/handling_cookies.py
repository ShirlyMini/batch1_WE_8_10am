import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

servcie_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=servcie_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

cookies = driver.get_cookies() # --> returning list

# for i in cookies:
#     print(i["name"] +": "+i["value"])

# add new cookies
print("Before adding cookie", len(driver.get_cookies()))
driver.add_cookie({"name": "mycookie", "value": "my_cookie_value_12345"})
print("After adding cookie", len(driver.get_cookies()))
cookies = driver.get_cookies()
for i in cookies:
    print(i["name"] + ":: " + i["value"])

# delete cookies
driver.delete_cookie("mycookie")
print("After deleteing mycookie", len(driver.get_cookies()))
driver.delete_all_cookies()
print("After deleteing all cookie", len(driver.get_cookies()))


