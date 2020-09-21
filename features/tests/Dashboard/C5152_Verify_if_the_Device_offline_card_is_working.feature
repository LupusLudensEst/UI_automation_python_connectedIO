# Created by rapid at 9/20/2020
Feature: # C5152 Verify if the Device offline card is working

  Scenario: # C5152 Verify if the Device offline card is working
    Given Loginpage
    Then Login with the given credentials
    Then Click on DEVICE OFFLINE card
    And https://devcloud.connectedio.com/devices is here
    Then Verify Offline status in FILTERS field is seen