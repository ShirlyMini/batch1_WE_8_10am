import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servcie_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=servcie_obj)

driver.get("https://money.rediff.com/gainers")
driver.maximize_window()

no_of_rows=len(driver.find_elements(By.XPATH, "//div[@id='leftcontainer']/table/tbody/tr"))
print(f" no of rows {no_of_rows}")
no_of_col=len(driver.find_elements(By.XPATH, "//div[@id='leftcontainer']/table/tbody/tr[1]/td"))
print(f" no of coloumns {no_of_col}")

# 1. how to all the datas in the console

# for r in range(1, no_of_rows+1):
#     for c in range(1,no_of_col+1):
#         print(driver.find_element(By.XPATH, f"//div[@id='leftcontainer']/table/tbody/tr[{r}]/td[{c}]").text, end="\t")
#     print("\n")

# 2 . get data based on condition
# get the data of specifi stock

# for r in range(1, no_of_rows+1):
#     stock_name=driver.find_element(By.XPATH, f"//div[@id='leftcontainer']/table/tbody/tr[{r}]/td[{1}]").text
#     if "BMW Industries" == stock_name:
#         for c in range(1, no_of_col + 1):
#             print(driver.find_element(By.XPATH, f"//div[@id='leftcontainer']/table/tbody/tr[{r}]/td[{c}]").text)
#         break

# get the stocks below 10rs
# 0-n-1----1 n
for r in range(1, no_of_rows+1):
    stock_price=driver.find_element(By.XPATH, f"//div[@id='leftcontainer']/table/tbody/tr[{r}]/td[{4}]").text
    if float(stock_price.replace(",","")) <= 10:
        for c in range(1, no_of_col + 1):
            print(driver.find_element(By.XPATH, f"//div[@id='leftcontainer']/table/tbody/tr[{r}]/td[{c}]").text, end="\t")
        print("/n")


# task
# get all stocks which having change % above 20%
# static website
# https://cosmocode.io/automation-practice-webtable/