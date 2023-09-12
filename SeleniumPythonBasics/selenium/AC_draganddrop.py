import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

servcie_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=servcie_obj)

# driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
# driver.maximize_window()
# driver.implicitly_wait(20)

# source_elem = driver.find_element(By.ID, "box6")
# destination_elem = driver.find_element(By.ID, "box106")
#
# act_obj=ActionChains(driver)
#
# act_obj.drag_and_drop(source_elem, destination_elem).perform()

# drag and drop by offset
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()
driver.implicitly_wait(20)

l2r_slider_elem=driver.find_element(By.XPATH, '//*[@id="slider-range"]/span[1]')
r2l_slider_elem=driver.find_element(By.XPATH, '//*[@id="slider-range"]/span[2]')
print(l2r_slider_elem.location) #{'x': 59, 'y': 250} # add values with x offset
print(r2l_slider_elem.location) #{'x': 545, 'y': 250}# subract values with x offset

act_obj=ActionChains(driver)
act_obj.drag_and_drop_by_offset(l2r_slider_elem, 100, 0).perform()
print(l2r_slider_elem.location)


act_obj.drag_and_drop_by_offset(r2l_slider_elem, -150, 0).perform()
print(r2l_slider_elem.location)


