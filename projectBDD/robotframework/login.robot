*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary
Library           xlutilites.py

*** Variables ***
${url}     https://admin-demo.nopcommerce.com/
${BROWSER}        Chrome
${xl_path}    .//LoginData.xlsx
${sheet}    Sheet1

*** Test Cases ***
Valid Login
    #[setup]
    Open Browser To Login Page
    ${user}    xlutilites.Read Data    ${xl_path}     ${sheet}    2    1
    Input Username    ${user}
    ${pass}    xlutilites.Read Data    ${xl_path}     ${sheet}    2    2
    Input Password    ${pass}
    Submit Credentials
    Welcome Page Should Be Open
    [Teardown]    Close Browser

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${url}    ${BROWSER}
    Title Should Be    Your store. Login

Input Username
    [Arguments]    ${username}
    Input Text    Email    ${username}    clear=True

Input Password
    [Arguments]    ${password}
    Input Text    Password    ${password}    clear=True

Submit Credentials
    Click Button    //button[@type='submit']

Welcome Page Should Be Open
    Title Should Be    Dashboard / nopCommerce administration