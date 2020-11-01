@my_account_smoke
Feature: My account smoke tests

  Scenario: Valid user should be able to login
    Given I go to the page my account
    When I type registered email into username field
    And I type valid password into password field
    And I click on the Log in
    Then User should be logged in

  @test
  Scenario Outline: User with invalid credentials should get appropriate error message
    Given I go to the page my account
    When I type <email type> into username field
    And I type invalid password into password field
    And I click on the Log in
    Then User should get <message type>

    Examples:
      | email type         | message type           |
      | registered email   | wrong password message |
      | unregistered email | invalid email message  |