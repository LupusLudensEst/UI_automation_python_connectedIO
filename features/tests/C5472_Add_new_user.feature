# Created by rapid at 8/27/2020
Feature: # App's button Background works and after clicking there is a text "Background"

  Scenario: # Click on About Us button. See how many there are submenu buttons.
    # Click on the Background btn.
    # Verify a text "Background" is here
    Given Loginpage
    Then Click on About Us button
    Then Click on the Background button and verify there is a text Background on the newly open page