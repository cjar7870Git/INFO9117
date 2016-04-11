Feature: User Register
  As a System Owner
  I want users to be able to register
  so that the system can capture neccessary information
  and identify and verify individual users

  Scenario Outline: New user registers
    Given at the register screen
    When I submit a unique <username> and <password>
    Then the system should return "Success" as the registration status of the user
        Examples:
      | username | password  |
      | _testchrisfjardine@gmail.com    | HoopyFrood     |
      | _testCrazyUserName              | NewPassword  |



  Scenario Outline: User attempts to register existing user name
    Given at the register screen
    When I submit an existing <username> and <password>
    Then the system should return "Fail" as the registration status of the user
        Examples:
      | username | password  |
      | _testCrazyUserName   | NewPassword |


