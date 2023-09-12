import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

servcie_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=servcie_obj)

driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()
driver.implicitly_wait(10)


course_elem = driver.find_element(By.XPATH, "//span[text()='Courses']")
course1_elem = driver.find_element(By.XPATH, "//span[text()='For Working Professionals']")
course2_elem = driver.find_element(By.XPATH, '//ul[@class="mega-dropdown"]/li/ul/li/a[text()="DevOps(Live)"]')

act_obj=ActionChains(driver)

# mousehover
act_obj.move_to_element(course_elem).move_to_element(course1_elem).move_to_element(course2_elem).click().perform()
verify_page= driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/section/div[3]/div[1]/div[1]/p')
print(verify_page.text)