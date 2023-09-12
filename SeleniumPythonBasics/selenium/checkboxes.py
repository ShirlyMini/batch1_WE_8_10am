from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


servcie_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=servcie_obj)
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

# raido_btn
# radio_btn_elem=driver.find_element(By.CSS_SELECTOR,"#male")
# radio_btn_elem.click()
# print(radio_btn_elem.is_selected())

#check_box example

check_box_elems=driver.find_elements(By.XPATH,'//input[@type="checkbox" and contains(@id,"day")]')

print(len(check_box_elems))

for elem in check_box_elems: # select only sunday,satu, mod
    #if elem.get_attribute("id") in ["sunday", "monday"]:
    #    elem.click()
    elem.click()

for elem in check_box_elems:
    if elem.is_selected() and elem.get_attribute("id") in ["sunday", "monday"]:
        elem.click() # unselect