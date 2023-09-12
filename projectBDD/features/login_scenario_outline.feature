Feature: NopCommerce login

  Scenario Outline: Login to NopCommerce app with valid parameter
    Given Launch browser
    When Open nopcommerce page
    And Enter Username "<username>" and Password "<password>"
    And Click on Submit Button
    Then verify Dashbord Page "<status>"

    Examples:
      | username            | password | status |
      | admin@yourstore.com | admin    | True   |
      | admin@yourstore.com | admin123 | False   |
      | abc@yourstore.com   | abc123   | False  |
      | xyz@mystore.com     | mystore  | False  |