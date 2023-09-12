# import datetime
# mytime = datetime.datetime.now()
# #04/01/2021 #mm/dd/yyyy
# current_time = mytime.strftime("%m/%d/%Y")
# print(current_time)
# #year month date time min sec millisec
# mytime = datetime.datetime(2023, 1, 4, 9, 30, 39)
# print(mytime.strftime('%m/%d/%Y'))
# # # 14 January 2023
# # print(mytime.strftime("%d %B %Y"))

# use sendkeys if html page is showing input tag
import datetime


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

servcie_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=servcie_obj)
wait_obj=WebDriverWait(driver,20)
driver.get("https://www.globalsqa.com/demo-site/datepicker/#Simple%20Date%20Picker")
driver.maximize_window()
frame_elem = driver.find_element(By.XPATH, '//*[@id="post-2661"]/div[2]/div/div/div[1]/p/iframe')
driver.switch_to.frame(frame_elem)

wait_obj.until(EC.element_to_be_clickable, (By.XPATH,'//input[@id="datepicker"]'))
driver.find_element(By.XPATH,'//input[@id="datepicker"]').click()

month=driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/div/span[1]').text
Year=driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/div/span[2]').text
#mytime = datetime.datetime.now()
mytime = datetime.datetime(2024, 2, 15)
next_xpath='//*[@id="ui-datepicker-div"]/div/a[2]/span'
prev_xpath='//*[@id="ui-datepicker-div"]/div/a[1]/span'

if Year == mytime.strftime("%Y"):
    if month == mytime.strftime("%B"):
        date = mytime.strftime("%d")
        driver.find_element(By.XPATH,rf'//*[@id="ui-datepicker-div"]/table/tbody/tr/td/a[text()="{date.rstrip("0")}"]').click()

if Year != mytime.strftime("%Y"):
    while int(Year)<int(mytime.strftime("%Y")):
        driver.find_element(By.XPATH,next_xpath).click()
        if driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/div/span[2]').text == mytime.strftime("%Y"):
            break
    month = driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/div/span[1]').text
    while month != mytime.strftime("%B"):
        driver.find_element(By.XPATH, next_xpath).click()
        if driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/div/span[1]').text == mytime.strftime("%B"):
            break
    date = mytime.strftime("%d")
    driver.find_element(By.XPATH,rf'//*[@id="ui-datepicker-div"]/table/tbody/tr/td/a[text()="{date.rstrip("0")}"]').click()


time.sleep(15)
driver.quit()