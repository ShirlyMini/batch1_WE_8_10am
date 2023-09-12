import pytest
from selenium import webdriver
from utilities.readConfig import ReadConfig

@pytest.fixture()
def setup(browser):
    BaseURL = ReadConfig.getApplicationURL()
    if browser=="chrome":
        from selenium.webdriver.chrome.service import Service
        service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser=="edge":
        from selenium.webdriver.edge.service import Service
        service_obj = Service(r"E:\selenium\drivers\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
    elif browser=="firefox":
        from selenium.webdriver.firefox.service import Service
        service_obj = Service(r"E:\selenium\drivers\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    else:
        from selenium.webdriver.chrome.service import Service
        service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    driver.get(BaseURL)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def setup_grid(browser):
    BaseURL = ReadConfig.getApplicationURL()
    if browser=="chrome":
        option=webdriver.ChromeOptions()
    elif browser=="edge":
        option=webdriver.EdgeOptions()
    elif browser=="firefox":
        option=webdriver.FirefoxOptions()
    else:
        option=webdriver.ChromeOptions()

    driver = webdriver.Remote(
        command_executor=r"http://192.168.1.4:4444/wd/hub",
        options=option)
    driver.get(BaseURL)
    driver.maximize_window()
    yield driver
    driver.quit()

###To get command line input###
def pytest_addoption(parser):  # this will get the values from CLI
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return browser value to setup method
    #print(request.config.getoption("--browser"))
    return request.config.getoption("--browser")


###HTML Report###
def pytest_configure(config):
    config._metadata = {
        "Tester": "shirly",
        "Module Name": "customers",
        "Project Name": "nopcommerce",
    }