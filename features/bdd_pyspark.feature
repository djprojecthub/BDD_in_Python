@fixture.spark.session
  Feature: Buy and sell

    Scenario: Buy some items listed in a Data table
      Given I have 10 rupees
      And I have 0 items
      When I buy the following items
          | Label | Quantity | Price |
          | Coffee| 3        | 1     |
          | Cake  | 1        | 3     |
          | Tea   | 2        | 0.5   |
      Then I should have 7 items in all
      And I should have 3 rupees left

    Scenario: Sell some items (no stock check)
      Given I have 2 rupees
      And I have 2 items
      When I sell the following items
          | Label     | Quantity | Price |
          | Chocolate |   1      |   3   |
      Then I should have 1 items in all
      And I should have 5 rupees left