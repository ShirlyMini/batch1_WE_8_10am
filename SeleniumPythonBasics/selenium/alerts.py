import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

driver = webdriver.Edge()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
#
driver.find_element(By.XPATH, "//li[3]/button").click()
get_alert=driver.switch_to.alert
# get text. send input and accpect alert
print(get_alert.text)# get text
time.sleep(5)
get_alert.send_keys("java script alert")# giving input in feild
time.sleep(5)
get_alert.accept()
# get_alert.dismiss()

#task

# https://mypage.rediff.com/---> click go button
# with and without email capture the js prompt msg

# ops=webdriver.ChromeOptions()
# ops.add_argument("--disable--notifications")
#
# servcie_obj = Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=servcie_obj, options=ops)
# driver.get("https://whatmylocation.com/")
# driver.maximize_window()


# authentication popup

# 1) Using url  -- https://admin:admin@the-internet.herokuapp.com/basic_auth

# 2) using autoit

# install pip install pyautoit

# import autoit
# servcie_obj = Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=servcie_obj)
#
# driver.get("https://the-internet.herokuapp.com/basic_auth")
# time.sleep(5)
# autoit.win_wait_active("", 30)
# autoit.send("admin{TAB}")
# autoit.send("admin{ENTER}")

