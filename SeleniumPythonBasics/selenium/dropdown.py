from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


servcie_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=servcie_obj)
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

# dropdown_elems=driver.find_elements(By.XPATH, '//select[@class="custom-select"]/option')
# for elem in dropdown_elems:
#     print(elem.text)
#     if elem.text=="Italy":
#         elem.click()

dropdown_elem=driver.find_element(By.XPATH, '//select[@class="custom-select"]')
country_dd=Select(dropdown_elem)
country_dd.select_by_visible_text("Sweden")
country_dd.select_by_index(3)
for i in country_dd.options:
    print(i.text)

#print(country_dd.options[0].text)