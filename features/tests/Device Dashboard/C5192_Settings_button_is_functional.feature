# Created by rapid at 10/12/2020
Feature: # C5192 Settings button is functional

  Scenario: # C5192 Settings button is functional
    Given Loginpage
    Then Login with the given credentials
    And Go to the Devices page https://devcloud.connectedio.com/devices
    Then Click Add new device button on the right up corner
    Then Fill required Device IMEI field 356961071557824
    And Fill Device Name field if any TVM Test123 jjnkjn
    Then Fill required Serial Number field 1806208A0279
    And Click Save and refresh the page
    Then Success is here - device is on the page
    Then Choose any device with IMEI number which is highlighted in blue active IMEI number and click on an active IMEI number
    Then Click on Settings button in right up corner and verify it has Reboot item in the drop-down menu