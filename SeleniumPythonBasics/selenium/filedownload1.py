from selenium import webdriver
from selenium.webdriver.common.by import By
import os
print(os.getcwd())
location=os.getcwd()

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    servcie_obj = Service("E:\selenium\drivers\chromedriver.exe")
    preferences = {"download.default_directory":location, "plugins.always_open_pdf_externally":True}
    #preferences = {"download.default_directory":r"C:\Users\user\PycharmProjects\pythonselenium\venv\selenium"}

    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)
    driver = webdriver.Chrome(service=servcie_obj, options=ops)
    return driver

def edge_setup():
    from selenium.webdriver.edge.service import Service
    servcie_obj = Service("E:\selenium\drivers\msedgedriver.exe")
    preferences = {"download.default_directory":location,
                   "plugins.always_open_pdf_externally": True,
                   "download.prompt_for_download": False}
    #preferences = {"download.default_directory":r"C:\Users\user\PycharmProjects\pythonselenium\venv\selenium"}

    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs", preferences)
    driver = webdriver.Edge(service=servcie_obj, options=ops)
    return driver

def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    servcie_obj = Service("E:\selenium\drivers\geckodriver.exe")
    #preferences = {"download.default_directory": location, "plugins.always_open_pdf_externally": True}
    # preferences = {"download.default_directory":r"C:\Users\user\PycharmProjects\pythonselenium\venv\selenium"}

    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/pdf")
    ops.set_preference("bowser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.download.folderList", 2)  # 0-desktop,1-downloadfolder,2-desiredloc
    ops.set_preference("browser.download.dir", location)  # onlythefolderlistis2
    ops.set_preference("pdfjs.disabled", True)
    driver = webdriver.Firefox(service=servcie_obj, options=ops)
    return driver

driver = edge_setup()
#driver = chrome_setup()
#driver = firefox_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@id="table-files"]/tbody/tr[1]/td[5]/a').click()


