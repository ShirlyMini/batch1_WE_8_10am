import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


servcie_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=servcie_obj)
driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()
driver.find_element(By.XPATH,"//span[contains(text(),'Community is here')]").click() # new window ill get opened
time.sleep(10)
#driver.quit() # closes all windows # will kill browser
driver.close() # closes driver focuse (window handels) # wont kill brower
