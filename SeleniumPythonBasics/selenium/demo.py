import unittest
from selenium import webdriver


class SearchEnginesTest(unittest.TestCase):
    def test_google(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com/")
        print("Title of the page is ", self.driver.title)
        self.driver.close()


def test_bing(self):
    self.driver = webdriver.Chrome()
    self.driver.get("https://www.bing.com/")
    print("Title of the page is ", self.driver.title)
    self.driver.close()


if __name__ == "__main__":
    unittest.main()