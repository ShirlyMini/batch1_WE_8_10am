from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servcie_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=servcie_obj)
driver.get("https://www.facebook.com/")
driver.maximize_window()

input_elem=driver.find_element(By.ID,"email")

input_elem.send_keys("abc.gmail.com")
print(f"using text:{input_elem.text}") # works only for innertext
print(f"using get attribute:{input_elem.get_attribute('value')}")
print(f"using get attribute:{input_elem.get_attribute('id')}")

input_elem.clear()
print("After Clear...")
print(f"using text:{input_elem.text}") # works only for innertext
print(f"using get attribute:{input_elem.get_attribute('value')}")
input_elem.send_keys("xyz@gmail.com")
print("After Clear passing input...")
print(f"using text:{input_elem.text}") # works only for innertext
print(f"using get attribute:{input_elem.get_attribute('value')}")
driver.quit()