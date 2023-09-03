import time

from selenium.webdriver.common.by import By

class loginPage:
    # kindofelem_nameofelem_typelocator
    input_username_id = "Email"
    input_password_id = "Password"
    btn_sumbit_xpath = "//button[contains(text(),'Log in')]"
    link_logout_xpath = "//a[contains(text(),'Logout')]"
    link_logo_id = "//div[@id='ajaxBusy']"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, email):
        self.driver.find_element(By.ID, self.input_username_id).clear()
        self.driver.find_element(By.ID, self.input_username_id).send_keys(email)

    def setUPassword(self, password):
        self.driver.find_element(By.ID, self.input_password_id).clear()
        self.driver.find_element(By.ID, self.input_password_id).send_keys(password)

    def clickLogIn(self):
        self.driver.find_element(By.XPATH, self.btn_sumbit_xpath).click()

    def clickLogOut(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()

    def verifyLogo(self):
        status = self.driver.find_element(By.XPATH, self.link_logo_id).is_displayed()
        return status