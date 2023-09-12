# selenium 3.x architecture
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#driver = webdriver.Chrome("E:\selenium\drivers\chromedriver.exe")
#driver = webdriver.Chrome(executable_path="E:\selenium\drivers\chromedriver.exe")

#driver = webdriver.Chrome()


#selenium 4.x
#servcie_obj = Service("E:\selenium\drivers\chromedriver.exe")
#driver = webdriver.Chrome(service=servcie_obj)



# without downloading the webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
# service_obj=Service(ChromeDriverManager().install())
# driver=webdriver.Chrome(service=service_obj)
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service

#driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
service_obj=Service(EdgeChromiumDriverManager().install())
driver=webdriver.Edge(service=service_obj)
driver.get("https://www.geeksforgeeks.org/") # drivers version should match

