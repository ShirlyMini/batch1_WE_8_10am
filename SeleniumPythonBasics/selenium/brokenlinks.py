from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import requests


servcie_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=servcie_obj)
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

#driver.find_element(By.LINK_TEXT, "Errorcode 400").click()
# error_code_url=driver.find_element(By.XPATH, '//div[@id="maintext"]/div[1]/ul/li[1]/a').get_attribute("href")
# print(error_code_url)
# print(requests.head(error_code_url))# get the error code or response
#print(driver.title)

# if requests.head(error_code_url) == "<Response [400]>":
#     pass

error_link_elems=driver.find_elements(By.XPATH, '//a')
print(len(error_link_elems))
for elem in error_link_elems:
    url=elem.get_attribute("href")
    print(url)
    try:
        code = requests.head(url)
        print(code)
        if code.status_code>=400:
            print(f"{url} = invalid")
        else:
            print(f"{url} = valid")
    except Exception as e:
        print(f"{url} = invalid", e)

