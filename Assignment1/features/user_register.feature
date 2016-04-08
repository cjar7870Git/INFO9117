Feature: User Register
  As a System Owner
  I want users to be able to register
  so that the system can capture neccessary information
  and identify and verify individual users

  Scenario Outline: New user registers
    Given at the register screen
    When a new user submits a unique <username> and <password>
    Then the system should return "Success" as the authentication status of the user
        Examples:
      | username | password  |
      | chrisfjardine@gmail.com    | HoopyFrood     |
      | CrazyUserName              | CrazyPassword  |
