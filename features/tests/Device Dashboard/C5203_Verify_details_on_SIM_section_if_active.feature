# Created by rapid at 10/19/2020
Feature: # C5203 Verify details on SIM section if active

  Scenario: # C5203 Verify details on SIM section if active
    Given Loginpage
    Then Login with the given credentials
    And Go to the Devices page https://devcloud.connectedio.com/devices
    Then Click Add new device button on the right up corner
    Then Fill required Device IMEI field 356961071557824
    And Fill Device Name field if any TVM Test123 jjnkjn
    Then Fill required Serial Number field 1806208A0279
    And Click Save and refresh the page
    Then Success is here - device is on the page
    Then Verify that the following details displayed: SIM IP address, SIM TX data from last reboot KB, SIM RX data from last reboot KB, SIM ICC number, SIM APN and SIM Pie Chart
    And Delete device