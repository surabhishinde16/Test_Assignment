Feature: Product Management

  # Scenario for reading a product
  Scenario: Read a product by ID
    Given a product with name "Gadget" and category "Electronics"
    When I request the product by ID
    Then I should receive a product with name "Gadget" and category "Electronics"

  # Scenario for updating a product
  Scenario: Update a product
    Given a product with name "Gadget" and category "Electronics"
    When I update the product with name "Gadget Pro" and category "Home Appliances"
    Then the product name should be "Gadget Pro"
    And the product category should be "Home Appliances"

  # Scenario for deleting a product
  Scenario: Delete a product
    Given a product with name "Gadget" and category "Electronics"
    When I delete the product
    Then the product should no longer exist

  # Scenario for listing all products
  Scenario: List all products
    Given there are 3 products with names "Gadget", "Widget", and "Doodad"
    When I request the list of all products
    Then I should receive a list with 3 products

  # Scenario for searching products by name
  Scenario: Search products 
