import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

servcie_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=servcie_obj)

driver.get("https://www.foundit.in/")
driver.maximize_window()

driver.find_element(By.XPATH, '//*[@id="heroSection-container"]/div[3]/div[2]/div[2]').click()
#driver.find_element(By.ID, 'file-upload').send_keys(r"C:\Users\user\PycharmProjects\pythonselenium\venv\selenium\file-sample_150kB.pdf")
driver.find_element(By.ID, 'file-upload').send_keys(r"E:\FITA\tracker.txt")