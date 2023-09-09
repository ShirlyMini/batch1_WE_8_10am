import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from utilities.readConfig import ReadConfig
from utilities.customLogger import Logger
from pageObjects.login import loginPage


class Test001_Login_TestSuite:
    log = Logger()

    @pytest.mark.regression
    @pytest.mark.sanity
    def testCase_001_login(self, setup_grid):
        self.log.info("*********Test Case 001 Login******")
        self.driver = setup_grid
        self.log.info("*********successfully lauched appliaction******")
        self.lp_obj = loginPage(self.driver)
        # self.lp_obj.setUsername("admin@yourstore.com")
        self.lp_obj.setUsername(ReadConfig.getUserEmail())
        # self.lp_obj.setUPassword("admin")
        self.lp_obj.setUPassword(ReadConfig.getUserPassword())
        self.log.info("*********Login to application******")
        self.lp_obj.clickLogIn()

        if self.driver.title == "Dashboard / nopCommerce administration":
            self.lp_obj.clickLogOut()
            if self.driver.title == "Your store. Login":
                print("testCase_001_login : Passed")
                self.log.info("Test Case 001 Login : Passed")
                self.log.info("*********Test Case 001 Login completed ******")
                #self.driver.close()
                assert True
            else:
                print("testCase_001_login : Failed: check logout function")
                self.driver.save_screenshot("./screenShots/testCase_001_login.png")
                self.log.error("Test Case 001 Login : Failed: check logout function ")
                self.log.error("*********Test Case 001 Login completed ******")
                #self.driver.close()
                assert False
        else:
            print("testCase_001_login : Failed: check login function")
            self.driver.save_screenshot("./screenShots/testCase_001_login.png")
            self.log.error("Test Case 001 Login : Failed: check login function")
            self.log.error("*********Test Case 001 Login completed ******")
            #self.driver.close()
            assert False

    @pytest.mark.sanity
    def testCase_002_appLogo(self, setup_grid):
        self.log.info("*********Test Case 002 application Logo******")
        self.driver = setup_grid
        self.log.info("*********successfully lauched appliaction******")
        self.lp_obj = loginPage(self.driver)
        self.lp_obj.setUsername(ReadConfig.getUserEmail())
        self.lp_obj.setUPassword(ReadConfig.getUserPassword())
        self.log.info("*********Login to application******")
        self.lp_obj.clickLogIn()
        self.log.info("*********Verify application Logo******")
        self.status = self.lp_obj.verifyLogo()
        print(self.status)
        if self.status == True:
            print("testCase_002_appLogo : Passed")
            self.log.info("Test Case 002 Application Logo : Passed")
            self.log.info("*********Test Case 002 Application Logo completed ******")
            #self.driver.close()
            assert True
        else:
            print("testCase_002_appLogo : Failed")
            self.driver.save_screenshot("./screenShots/testCase_002_appLogo.png")
            self.log.error("Test Case 002 Application Logo : Failed")
            self.log.error("*********Test Case 002 Application Logo completed ******")
            #self.driver.close()
            assert False
