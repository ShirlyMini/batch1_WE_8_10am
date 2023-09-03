import pytest
from utilities.readConfig import ReadConfig
from utilities.customLogger import Logger
from pageObjects.search_PC import customerInfo


class Test004_Add_Customer_TestSuite:
    log = Logger()

    @pytest.mark.regression
    @pytest.mark.sanity
    def testCase_001_searchcustomer_byemail(self, setup):
        self.log.info("*********Test Case 001 search Customer by Email******")
        self.driver = setup

        self.search_obj = customerInfo(self.driver)
        self.search_obj.SearchbyEmail("arthur_holmes@nopCommerce.com")

        self.log.info("*********Searching for Customer By Email******")
        self.status = self.search_obj.verifyEmail("arthur_holmes@nopCommerce.com")
        print(self.status)
        if self.status == True:
            print("testCase_001_searchcustomer_byemail : Passed")
            self.log.info("Test Case 001 search Customer by Email : Passed")
            self.log.info("*********Test Case 001 search Customer by Email completed ******")
            assert True
        else:
            print("testCase_001_searchcustomer_byemail : Failed")
            self.driver.save_screenshot("./screenShots/testCase_001_searchcustomer_byemail.png")
            self.log.error("Test Case 001 search Customer by Email : Failed")
            self.log.error("*********Test Case 001 search Customer by Email completed ******")
            assert False