import time

from selenium import webdriver
from selenium.webdriver.chrome import service
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(service=service.Service("E:\selenium\drivers\chromedriver.exe"))
driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
#driver = webdriver.Chrome()
time.sleep(10)
driver.get("https://google.com")
print(driver.title)
#driver.close()