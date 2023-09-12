from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servcie_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=servcie_obj)
# driver.get("https://www.facebook.com/")

# CSS selector
# tag and ID

# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc@yahoo.com")

# tag and class
# driver.get("https://www.geeksforgeeks.org/")
# driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR, "a.header-main__signup").click()

# tag and attr

#driver.find_element(By.CSS_SELECTOR, "a[type=button]").click()

# tag/class/attr

driver.get("https://www.facebook.com/")
driver.maximize_window()
#with tag name
#driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_email]").send_keys("abc@yahoo.com")
#driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_pass]").send_keys("abc")
# without tagname
driver.find_element(By.CSS_SELECTOR, ".inputtext[data-testid=royal_email]").send_keys("abc@yahoo.com")
driver.find_element(By.CSS_SELECTOR, ".inputtext[data-testid=royal_pass]").send_keys("abc")

