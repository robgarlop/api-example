Feature: Test Swagger Petstore https://petstore.swagger.io

  Scenario: Get a pet by ID
    Given I set base url to "https://petstore.swagger.io/v2/pet/"
    When I retrieve info of the pet with ID "1"
    Then I should get status code "200"
    And The name should be "doggie"