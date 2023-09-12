Feature: NopCommerce Logo

  Background: Steps to be implemented before each scenario
    Given Launch browser
    When Open nopcommerce page
    And Enter Username "admin@yourstore.com" and Password "admin"
    And Click on Submit Button


  Scenario: Login to NopCommerce app with valid parameter
    Then User must successfully enter into the dashboard page

  Scenario: Login to NopCommerce app and navigate to customer page
    When Click customer menu
    Then Verify the customer page