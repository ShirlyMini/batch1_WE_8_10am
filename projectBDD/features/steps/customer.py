from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@when('Click customer menu')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p").click()
    context.driver.find_element(By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p").click()

@then('Verify the customer page')
def step_impl(context):
    text_from_page = context.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/form[1]/div/h1").text
    if text_from_page == "Customers":
        assert True
    else:
        assert False
