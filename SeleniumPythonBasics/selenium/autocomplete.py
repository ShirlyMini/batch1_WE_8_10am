import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

servcie_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=servcie_obj)

driver.get("https://demoqa.com/auto-complete")
driver.maximize_window()

wait_obj=WebDriverWait(driver,20)

input_elem = driver.find_element(By.XPATH, '//*[@id="autoCompleteMultipleInput"]')
#print(input_elem.is_enabled())
wait_obj.until(EC.element_to_be_clickable, (By.XPATH, '//*[@id="autoCompleteMultipleInput"]'))
#input_elem.click()
#
#
# act_obj=ActionChains(driver)
# act_obj.send_keys("g").perform()
# act_obj.send_keys(Keys.ENTER).perform()
# #
# act_obj.send_keys("g").perform()
# act_obj.send_keys(Keys.RETURN).perform()
# #
# act_obj.send_keys("g").perform()
# act_obj.send_keys(Keys.RETURN).perform()
# print(driver.find_element(By.XPATH, '//*[@id="autoCompleteMultipleContainer"]/div/div[1]/div[1]/div[1]').text)
# print(driver.find_element(By.XPATH, '//*[@id="autoCompleteMultipleContainer"]/div/div[1]/div[2]/div[1]').text)
# print(driver.find_element(By.XPATH, '//*[@id="autoCompleteMultipleContainer"]/div/div[1]/div[3]/div[1]').text)
######################################

# to Freeze the browser
# ctrl+\ or F8-----> disable javascript execution
# Eventlistern--> blur--> click on revome(remove all properties)--suggestions option
# Eventlistern--> mouseout--> click on revome(remove all properties)--Tooltip
input_elem.send_keys("a")
suggestion_elem = driver.find_elements(By.XPATH, '//*[@id="autoCompleteMultipleContainer"]/div[2]/div/div')
for sug in suggestion_elem:
    print(sug.text)

input_elem.clear()

for i in range(len(suggestion_elem)):
    input_elem.send_keys("a")
    driver.find_element(By.XPATH, '//*[@id="autoCompleteMultipleContainer"]/div[2]/div/div[1]').click()

color_elem = driver.find_elements(By.XPATH, '//*[@id="autoCompleteMultipleContainer"]/div/div[1]/div/div[1]')
for color in color_elem:
    #[black-0, meganta-1, aqua-2] fetchs 2 as index-
    # html index starts from 1-n[black-1, meganta-2, aqua-3]
    print(color.text)
    print(color_elem.index(color))
    if color.text == "Aqua":
        driver.find_element(By.XPATH, f'//*[@id="autoCompleteMultipleContainer"]/div/div[1]/div[{color_elem.index(color)+1}]/div[2]').click()

###################################33

# input_elem.click()
#
#
# act_obj=ActionChains(driver)
# act_obj.send_keys("g").perform()
# act_obj.send_keys(Keys.ARROW_DOWN).perform()
# act_obj.send_keys(Keys.ENTER).perform()


###############################3
# range(5) # 0-4
# list()#
