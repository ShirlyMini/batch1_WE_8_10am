import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
print(os.getcwd())
location=os.getcwd()

def edge_setup():
    from selenium.webdriver.edge.service import Service
    servcie_obj = Service("E:\selenium\drivers\msedgedriver.exe")

    preferences = {"download.default_directory":location,
                   "plugins.always_open_pdf_externally": True,
                   "download.prompt_for_download": False}
    #preferences = {"download.default_directory":r"C:\Users\user\PycharmProjects\pythonselenium\venv\selenium"}

    ops = webdriver.EdgeOptions()
    ops.UseChromium = True
    ops.add_experimental_option("prefs", preferences)
    driver = webdriver.Edge(service=servcie_obj)#, options=ops)
    return driver

driver = edge_setup()
# driver.get("edge://settings/downloads")
#
# driver.find_element(By.XPATH, '//input[@aria-label="Open Office files in the browser"]').click()
# time.sleep(2)
#
# driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
# driver.maximize_window()
#
# driver.find_element(By.XPATH, '//*[@id="table-files"]/tbody/tr[1]/td[5]/a').click()


## pdf download
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@id="table-files"]/tbody/tr[1]/td[5]/a').click()
time.sleep(10)


pyautogui.hotkey('ctrl', 's')
time.sleep(5)
pyautogui.typewrite(location+"pyautoit_download.pdf")
pyautogui.press('enter')