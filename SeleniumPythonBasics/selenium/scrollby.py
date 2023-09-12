import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

servcie_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=servcie_obj)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
driver.implicitly_wait(10)

print(driver.execute_script("return window.pageYOffset;"))

# scroll to offset y off

# driver.execute_script("window.scrollBy(0,3000)","")
# print(driver.execute_script("return window.pageYOffset;"))

# scroll until element

# flag = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img')
# driver.execute_script("arguments[0].scrollIntoView();",flag)
# print(driver.execute_script("return window.pageYOffset;"))

# scroll to bottom
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")
time.sleep(5)
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)","")