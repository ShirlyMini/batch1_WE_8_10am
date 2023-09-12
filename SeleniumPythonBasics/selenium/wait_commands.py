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
#driver.implicitly_wait(10)

wait_obj=WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[Exception])

sign_in_elem = driver.find_element(By.XPATH, '//*[@id="userProfileId"]/a')
assert sign_in_elem.is_displayed()==True

sign_in_elem.click()

check_box_elem = driver.find_element(By.XPATH, '//input[@name="rem" and @type="checkbox"]')
print(check_box_elem.is_selected()) # True
print(check_box_elem.is_enabled())
#time.sleep(10)---# pause #hard wait

#wait_obj.until(EC.presence_of_element_located, (By.XPATH, '//input[@name="rem" and @type="checkbox"]'))
wait_obj.until(EC.element_to_be_selected, (By.XPATH, '//input[@name="rem" and @type="checkbox"]'))
check_box_elem.click() # unselect
print(check_box_elem.is_selected()) # False
if not check_box_elem.is_selected():
    check_box_elem.click() # select
print(check_box_elem.is_selected()) # True