# Created by rapid at 9/12/2020
Feature: # Login_enter the incorrect password

  Scenario: # Login_enter the valid but incorrect password and verify Invalid Login or Password is here
    Given Loginpage
    Then Enter valid, and the correct email address in the line "Email address" vadim@mailinator.com
    Then Enter the valid but incorrect password in the line "Password" manicpiano731_wrong
    Then Verify Invalid Login or Password is on login pop_up