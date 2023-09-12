import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


servcie_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=servcie_obj)

# driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
# driver.maximize_window()
#
# driver.switch_to.frame("packageListFrame") # name attr
# driver.find_element(By.XPATH, "/html/body/main/ul/li[1]/a").click()
# driver.switch_to.default_content()
#
# driver.switch_to.frame("packageFrame")
# driver.find_element(By.XPATH, "/html/body/main/div/section[1]/ul/li[13]/a/span").click()
# driver.switch_to.default_content()
#
# driver.switch_to.frame("classFrame")
# driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[6]/a").click()
# print(driver.find_element(By.XPATH, "/html/body/main/div[1]/h1").text)

# innerframes

# driver.get("https://ui.vision/demo/webtest/frames/")
# driver.maximize_window()
#
# outer_frame_elem = driver.find_element(By.XPATH, "//frameset/frameset/frame[2]")
# driver.switch_to.frame(outer_frame_elem)
# print(driver.find_element(By.XPATH, "//center/p").text)
# inner_frame_elem = driver.find_element(By.XPATH, "//iframe")
# driver.switch_to.frame(inner_frame_elem)
# print(driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div[1]/div[1]/div/div[2]/div[1]/div').text)

# task

# https://demo.automationtesting.in/Frames.html