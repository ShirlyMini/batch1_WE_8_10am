from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servcie_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=servcie_obj)
driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()
# findelement

# with locator matching single elem

# elem = driver.find_element(By.XPATH, "//ul[@id='hslider']//a[contains(text(), 'Python')]")
# print(elem.text)
# # with locator matching multiple elem
# elem = driver.find_element(By.XPATH, '//ul[@id="hslider"]//a')
# print(elem.text)
# invalid locator
# elem = driver.find_element(By.XPATH, '//ul[@id="acdbjcnx"]//a')
# print(elem.text) # NoSuchElementException

#findelements

# with locator matching single elem

# elem = driver.find_elements(By.XPATH, "//ul[@id='hslider']//a[contains(text(), 'Python')]")
# print(elem[0].text)
#
# # with locator matching multiple elem
# elem = driver.find_elements(By.XPATH, '//ul[@id="hslider"]//a')
# print(len(elem))
#
# for i in elem:
#     print(i.text)

# invalid

elem = driver.find_elements(By.XPATH, '//ul[@id="adrefss"]//a')
print(elem)