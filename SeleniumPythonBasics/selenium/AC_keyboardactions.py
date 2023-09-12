import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

servcie_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=servcie_obj)

driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()
driver.implicitly_wait(20)

driver.find_element(By.XPATH, '//*[@id="userProfileId"]/a').click()
driver.find_element(By.XPATH, '//label[contains(text(),"Sign Up")]').click()
user_elem = driver.find_element(By.XPATH, '//*[@id="email"]')
pass_elem = driver.find_element(By.XPATH, '//*[@id="reg-password"]')
org_elem = driver.find_element(By.XPATH, '//*[@id="organization"]')

user_elem.send_keys("abc@gmail.com")

act_obj=ActionChains(driver)

#ctrl+a &ctl+c

act_obj.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform() #selected
act_obj.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform() # copy
act_obj.send_keys(Keys.TAB) # go to next feild

#ctl+V
act_obj.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform() #paste
act_obj.send_keys(Keys.TAB) # go to next feild


act_obj.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform() #paste
act_obj.send_keys(Keys.TAB) # go to next feild