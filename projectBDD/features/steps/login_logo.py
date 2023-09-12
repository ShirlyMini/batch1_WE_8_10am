from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('Launch browser')
def step_impl(context):
    context.driver=webdriver.Chrome()


@when('Open nopcommerce page')
def step_impl(context):
    context.driver.get("https://admin-demo.nopcommerce.com/")


@then('Verify the presence of logo')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[1]/h1")


@then('Close browser')
def step_impl(context):
    context.driver.close()
