# Created by rapid at 10/20/2020
Feature: # C5204 Verify details on LAN section if active

  Scenario: # C5204 Verify details on LAN section if active
    Given Loginpage
    Then Login with the given credentials
    And Go to the Devices page https://devcloud.connectedio.com/devices
    Then Click Add new device button on the right up corner
    Then Fill required Device IMEI field 356961071557824
    And Fill Device Name field if any TVM Test123 jjnkjn
    Then Fill required Serial Number field 1806208A0279
    And Click Save and refresh the page
    Then Success is here - device is on the page
    Then Pay attention to the LAN section. IP address, TX data from last reboot KB, RX data from last reboot KB, MAC address and Pie Chart
    And Delete device