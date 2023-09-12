from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servcie_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=servcie_obj)

#application Command
driver.get("https://www.facebook.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)# security purpose
print(driver.page_source)

# navigator command
driver.get("https://www.geeksforgeeks.org/")
#driver.get("https://www.facebook.com/")
print(driver.back())# ---> facebook page
print(driver.refresh())
print(driver.forward()) # ----> gfg

