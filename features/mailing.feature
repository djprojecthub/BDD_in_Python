Feature: Sending a newsletter to the customer
  # Rule: Only people who purchased a product get the newsletter

  Scenario: Newsletter is sent to people who purchased at least one product
    Given Diwakar purchased a product
    When we generate newsletter recipients
    Then Diwakar is on the list

  Scenario: Subscriber with no purchases don't receive the newsletter
    Given Akansha bought no products
    When we generate newsletter recipients
    Then Bob is not on the list

  # Rule: Use only the most recent purchase

  Scenario: People who purchased more than one product receive only one message
    Given Diwakar purchased a product
    And Diwakar purchased another product
    When we generate newsletter recipients
    Then Diwakar is on the list only once

  Scenario: Newsletter mentions only the most recent purchase
    Given Diwakar purchased a product
    And Diwakar