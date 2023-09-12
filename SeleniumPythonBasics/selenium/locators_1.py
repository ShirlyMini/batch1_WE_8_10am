from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servcie_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=servcie_obj)
driver.get("https://www.facebook.com/")

# ID
driver.find_element(By.ID, "email").send_keys("xyz@hotmail.com")

# name
driver.find_element(By.NAME,"pass").send_keys("abcdef")

#linktext
#driver.find_element(By.LINK_TEXT, "Forgotten password?").click()

#partial linktext
#driver.find_element(By.PARTIAL_LINK_TEXT, "password?").click()

# list=driver.find_elements(By.PARTIAL_LINK_TEXT, "password?")
# for i in list:
#     i.click

# classname

# user_pass=driver.find_elements(By.CLASS_NAME, "inputtext")
# print(len(user_pass))
#
# for i in user_pass:
#     i.send_keys("abcdef")

# Tagname
#driver.find_element(By.TAG_NAME, "button").click()

