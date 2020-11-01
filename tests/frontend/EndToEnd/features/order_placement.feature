Feature: Place order
  @order
  Scenario: As new user I am able to place new order
    Given I go to the page homepage
    When I click on Beanie item
    And I click on Add to cart
    And I click on View cart
    And I verify cart page opens
    And I click on free shipping
#    And I click on the proceed to checkout
#    And I verify checkout page is loaded
#    And I click on the cash on delivery
#    And I fill in the billing details form
#    And I click on the place order
#    Then order confirmation page should load with correct data