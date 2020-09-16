# Created by rapid at 9/15/2020
Feature: # C5125 Change_password

  Scenario: # C5125_Change_password and verify the message is displayed: "Success."
    Given Loginpage
    Then Login with the given credentials
    Then Go to the "Change Password" page https://devcloud.connectedio.com/profile/change-password
    And Verify https://devcloud.connectedio.com/profile/change-password is open
    Then Enter the old password in the field "New Password" manicpiano731
    And Enter the old password in the field "Confirm New Password" manicpiano731
    Then Click on the button "Save"
    And Verify the words Old and new password cannot be same. is here
