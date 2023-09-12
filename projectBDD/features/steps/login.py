from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By



@when('Enter Username "{user}" and Password "{password}"')
def step_impl(context, user, password):
    context.driver.find_element(By.ID, "Email").clear()
    context.driver.find_element(By.ID, "Email").send_keys(user)

    context.driver.find_element(By.ID, "Password").clear()
    context.driver.find_element(By.ID, "Password").send_keys(password)


@when('Click on Submit Button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()

@then('User must successfully enter into the dashboard page')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div[3]/aside/a/img[1]")

@then('verify Dashbord Page "{status}"')
def step_impl(context, status):
    try:
        response = context.driver.find_element(By.XPATH, "/html/body/div[3]/aside/a/img[1]").is_displayed()
    except:
        if status == "False":
            print("Test Executed successfully")
        else:
            assert False
            print("Test Execution Failed")
    else:
        if status == "True" and response == True:
            print("Test Executed successfully")
        else:
            assert False
            print("Test Execution Failed")