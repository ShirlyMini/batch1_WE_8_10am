import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servcie_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=servcie_obj)

# driver.get("https://www.geeksforgeeks.org/")
# driver.maximize_window()
# driver.find_element(By.LINK_TEXT, "Community is here").click()
# print(driver.current_window_handle)
# window_id_list = driver.window_handles#--->winodw id in list
# print(window_id_list)
# parent_window=window_id_list[0]
# child_window=window_id_list[1]
#
# driver.switch_to.window(child_window)
# print(driver.title)
# print(driver.current_window_handle)
# driver.close()

#with multiple windows
#
# driver.find_element(By.LINK_TEXT, "Community is here").click()
# driver.find_element(By.LINK_TEXT, "Community is here").click()
# driver.find_element(By.LINK_TEXT, "Community is here").click()
#
# window_id_list = driver.window_handles
# print(window_id_list)
# for id in window_id_list:
#     driver.switch_to.window(id)
#     print(id)
#     print(driver.title)
#     # driver.find_element("d").is_element_preset
#     if "Community" in driver.title:
#         driver.close()

driver.get("https://www.myntra.com/tops")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.XPATH, '//*[@id="desktopSearchResults"]/div[2]/section/ul/li[1]/a/div[1]/div/div/div/picture/img').click()
driver.find_element(By.XPATH, '//*[@id="desktopSearchResults"]/div[2]/section/ul/li[2]/a/div[1]/div/div/div/picture/img').click()
driver.find_element(By.XPATH, '//*[@id="desktopSearchResults"]/div[2]/section/ul/li[3]/a/div[1]/div/div/div/picture/img').click()
driver.find_element(By.XPATH, '//*[@id="desktopSearchResults"]/div[2]/section/ul/li[4]/a/div[1]/div/div/div/picture/img').click()

window_ids = driver.window_handles
# window ids in list[o]--parent window
for id in window_ids[1:]:
    driver.switch_to.window(id)
    price=driver.find_element(By.XPATH, '//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[1]/div/p[1]/span[1]/strong').text
    print(price)
    if int(price[1:])>600:
        driver.save_screenshot("kurta.png")
        driver.close()

