import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

servcie_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=servcie_obj)

driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
driver.implicitly_wait(10)

right_click=driver.find_element(By.XPATH,'//span[text()="right click me"]')
paste_elem = driver.find_element(By.XPATH,"//span[text()='Paste']")
double_click=driver.find_element(By.XPATH,'//button')

act_obj=ActionChains(driver)

act_obj.move_to_element(right_click).context_click(right_click).move_to_element(paste_elem).context_click(paste_elem).perform()

get_alrt=driver.switch_to.alert
print(get_alrt.text)
get_alrt.accept()

act_obj.double_click(double_click).perform()

get_alrt=driver.switch_to.alert
print(get_alrt.text)
get_alrt.accept()

