import time
from utilities.readConfig import ReadConfig
from selenium.webdriver.common.by import By
from pageObjects.login import loginPage
from pageObjects.addCustomer import add_customers


class customerInfo(loginPage, add_customers):
    input_email_id="SearchEmail"
    input_firstname_id="SearchFirstName"
    input_lastname_id="SearchLastName"
    btn_search_id = "search-customers"
    table_row_xpath = "//table[@id='customers-grid']/tbody/tr" # no of rows
    # def __init__(self, driver):
    #     self.driver = driver

    def SearchbyEmail(self, email):
        #login
        print(ReadConfig.getUserEmail())
        loginPage.setUsername(self, ReadConfig.getUserEmail())
        loginPage.setUPassword(self, ReadConfig.getUserPassword())
        loginPage.clickLogIn(self)
        #navigate to customerpage
        add_customers.clickCustomerMainMenu(self)
        add_customers.clickCustomerLink(self)
        #search by email
        self.driver.find_element(By.ID,self.input_email_id).send_keys(email)
        self.driver.find_element(By.ID, self.btn_search_id).click()

    def verifyEmail(self, email):
        time.sleep(3)
        row_count = len(self.driver.find_elements(By.XPATH, self.table_row_xpath)) # retuens webelements in list
        print("Row Count", row_count)
        for r in range(1, row_count+1):
            print(self.driver.find_element(By.XPATH, f"//table[@id='customers-grid']/tbody/tr[{r}]/td[2]").text)
            if email == self.driver.find_element(By.XPATH, f"//table[@id='customers-grid']/tbody/tr[{r}]/td[2]").text:
                return True