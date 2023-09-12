import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Chome options

ops=webdriver.ChromeOptions()
ops.add_argument("--start-maximized")
ops.add_argument("--incognito")
ops.add_argument("--headless")

servcie_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=servcie_obj, options=ops)

driver.get("https://books-pwakit.appspot.com/")
#driver.maximize_window()

# CSS, tagname id locator
shadow1= driver.find_element(By.CSS_SELECTOR, "book-app").shadow_root
print(shadow1.find_element(By.CSS_SELECTOR,"div").text)

# driver.get("chrome://settings/")
# #driver.maximize_window()
#
# # CSS, tagname id locator
# shadow1= driver.find_element(By.CSS_SELECTOR, "settings-ui").shadow_root
# shadow2=shadow1.find_element(By.CSS_SELECTOR,"settings-main#main").shadow_root
# shadow3=shadow2.find_element(By.CSS_SELECTOR,"settings-basic-page.cr-centered-card-container").shadow_root
# shadow4=shadow3.find_element(By.CSS_SELECTOR,"settings-people-page").shadow_root
# shadow5=shadow4.find_element(By.CSS_SELECTOR,"cr-link-row#importDataDialogTrigger").shadow_root
#
# print(shadow5.find_element(By.CSS_SELECTOR,"div#label").text)

#task
# chrome://settings/downloads
# get text "Ask where to save each file before downloading"