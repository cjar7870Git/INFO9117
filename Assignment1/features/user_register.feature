Feature: User Register
  As a System Owner
  I want users to be able to register
  so that the system can capture neccessary information
  and identify and verify individual users

  Scenario Outline: New user registers
    Given at the register screen
    When a new user submits their unique <username> and <password>
    Then the system should record the <username> and <password> of the new user
    and return "Success" as the registration status of the user
        Examples:
      | username | password  |
      | test     | test123   |
      | chrisfjardine@gmail.com    | HoopyFrood     |
