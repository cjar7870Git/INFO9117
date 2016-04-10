Feature: User Register
  As a System Owner
  I want users to be able to register
  so that the system can capture neccessary information
  and identify and verify individual users

  Scenario Outline: New user registers
    Given at the register screen
    When a new user submits a unique <username> and <password>
    Then the system should return "Success" as the registration status of the user
        Examples:
      | username | password  |
      | chrisfjardine@gmail.com    | HoopyFrood     |
      | CrazyUserName              | CrazyPassword  |

  Scenario Outline: User attempts to register existing user name
    Given at the register screen
    When a user submits an existinge <username> and <password>
    Then the system should return "Fail" as the registration status
        Examples:
      | username | password  |
      | CrazyUserName   | CrazyPassword |
