Feature: NopCommerce Logo

  Scenario: Logo presence on NopCommerce login
    Given Launch browser
    When Open nopcommerce page
    Then Verify the presence of logo
    And Close browser

  Scenario: Login to NopCommerce app with valid parameter
    Given Launch browser
    When Open nopcommerce page
    And Enter Username "admin@yourstore.com" and Password "admin"
    And Click on Submit Button
    Then User must successfully enter into the dashboard page
