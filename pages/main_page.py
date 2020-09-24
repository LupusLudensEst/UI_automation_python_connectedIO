from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from random import randint
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

# Locators
LOGIN_EMAIL = (By.XPATH, "//input[@placeholder='Email address']")
LOGIN_PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
LOGIN_BTN = (By.CSS_SELECTOR, "button.btn.btn-primary.text-uppercase.w-100.font-weight-bold.gradient-btn.shadow-1.border-0")
POP_UP_WNDW_OK_BTN = (By.XPATH, "//div[@class='swal2-actions']//button[@class='swal2-confirm btn btn-outline-primary btn-sm btn-custom swal2-styled']")
# USERS = (By.CSS_SELECTOR, "i.fa.fa-users")
USERS = (By.XPATH, "(//a[@class='ng-star-inserted'])[4]")
QUICK_ACTIONS = (By.XPATH, "//div[@class='btn-group action-button dropdown']//span[contains(text(), 'Quick actions')]")
ADD_MENU = (By.CSS_SELECTOR, "i.fa.fa-user-plus")
FIRST_NAME = (By.XPATH, "//input[@formcontrolname='firstName']")
LAST_NAME = (By.XPATH, "//input[@formcontrolname='lastName']")
EMAIL = (By.XPATH, "//input[@formcontrolname='email']")
TELEPHONE = (By.XPATH, "//input[@formcontrolname='telephone']")
SELECT_ROLE = (By.ID, "role")
ADDRESS_1 = (By.XPATH, "//input[@formcontrolname='address1']")
ADDRESS_2 = (By.XPATH, "//input[@formcontrolname='address2']")
CITY = (By.XPATH, "//input[@formcontrolname='city']")
ZIP_CODE = (By.XPATH, "//input[@formcontrolname='zipCode']")
COUNTRY = (By.CSS_SELECTOR, "select.form-control.ng-touched.ng-dirty.ng-valid")
STATE = (By.XPATH, "//select[@formcontrolname='state']")
ADD_BTN = (By.CSS_SELECTOR, "button.btn.btn-sm.btn-primary.px-4.py-2.text-uppercase")
TEXT_HR = (By.XPATH, "//td[@style='text-align: left;']")
ADMIN = (By.XPATH, "//b[contains(text(), 'admin')]")
USER = (By.XPATH, "//b[contains(text(), 'user')]")
THREE_DOTS = (By.ID, "dropdownBasic1")
DELETE_BTN = (By.XPATH, "//div[@class='dropdown']//a[contains(text(), 'Delete')]")
DELETE_OK_BTN = (By.CSS_SELECTOR, "button.swal2-confirm.btn.btn-outline-primary.btn-sm.btn-custom.swal2-styled")
INVLD_LGN_PSWRD_HR = (By.XPATH, "//div[contains(text(), 'Invalid Login or Password')]")
# CLCK_TRNGL = (By.CSS_SELECTOR, "i.fas.fa-chevron-right")
CLCK_TRNGL = (By.XPATH, "//button[@class='d-block btn-togglr']")
USR_NM = (By.CSS_SELECTOR, "a.dropdown-toggle.user-name")
LGT_BTN = (By.CSS_SELECTOR, "i.fas.fa-power-off")
CLCK_LGT = (By.CSS_SELECTOR, "a.icon-menu.d-none.d-sm-block")
CHNG_PSWD = (By.XPATH, "//i[@class='fas fa-unlock-alt']")
NW_VLD_PSWD = (By.XPATH, "//input[@placeholder='New Password']")
CNFRM_NW_VLD_PSWD = (By. XPATH, "//input[@placeholder='Confirm New Password']")
SV_BTN = (By.CSS_SELECTOR, "i.fa.fa-save.mr-1")
SCSS_TXT_HR = (By.CSS_SELECTOR, "span.alert.w-100.alert-warning")
DVC_ONLN_TXT = (By.XPATH, "(//div[@class='card overflowhidden number-chart d-flex flex-column'])[1]")
DVC_ONLN = (By.CSS_SELECTOR, "div.number>span")
DVC_OFFLN_TAB = (By.XPATH, "(//div[@class='body information-card'])[2]")
INVNTR = (By.XPATH, "(//div[@class='body information-card'])[3]")
ALRT_NTFCTN = (By.XPATH, "(//div[@class='body information-card'])[4]")
DT_USG = (By.XPATH, "//h6[@class='tile-title text-uppercase']")
DT_USG_DTLS = (By.XPATH, "(//h2[@class='ng-tns-c6-0'])[1]")
NTFCTNS_ALRTS = (By.XPATH, "(//h2[@class='ng-tns-c6-0'])[2]")
GRPS = (By.XPATH, "(//h2[@class='ng-tns-c6-0'])[3]")
SGNL_STRNTH = (By.XPATH, "(//h2[@class='ng-tns-c6-0'])[4]")
DVC_LCTN = (By.XPATH, "//div[@class='col-6']//h2[@class='ng-tns-c6-0']")
DVC_MNGMNT_PRTL = (By.XPATH, "//h5[@class='fw-300 m-0 pl-4 text-truncate']")
ONLN_HERE = (By.CSS_SELECTOR, "span.pr-2")
DVCS_TBL = (By.XPATH, "//input[@name='checkbox1']")
NO_DATA = (By.XPATH, "//div[@class='no-data']")
# DVCS_OFFLN = (By.XPATH, "//div[@class='col col2 dvice_offline']//h6[contains(text(), 'DEVICE OFFLINE')]")
DVCS_OFFLN = (By.XPATH, "(//div[@class='card overflowhidden number-chart d-flex flex-column'])[2]")
OFFLN_TXT = (By.XPATH, "//span[@class='pr-2']")
DVC_OFFLN = (By.CSS_SELECTOR, "div.number>span")
DVCS_TBL_EMPT = (By.XPATH, "(//div[@class='fancy-checkbox devicelist-checkbox select-all'])[2]")
INVNTR_ELMNT = (By.CSS_SELECTOR, "div.card.overflowhidden.number-chart.d-flex.flex-column")
INVNTR_TXT = (By.CSS_SELECTOR, "span.pr-2")

class MainPage(Page):

    # Add new user
    def lgn_w_gn_crdntls(self):
        wait = WebDriverWait(self.driver, 10)
        # 2. Send Login e-mail
        wait.until(EC.presence_of_element_located(LOGIN_EMAIL)).clear()
        wait.until(EC.presence_of_element_located(LOGIN_EMAIL)).send_keys('gurovvic@gmail.com') # vadim@mailinator.com
        # 3. Send Password
        wait.until(EC.presence_of_element_located(LOGIN_PASSWORD)).clear()
        wait.until(EC.presence_of_element_located(LOGIN_PASSWORD)).send_keys('MyUSA2016!@') # manicpiano731
        # 4. Click on Login button
        wait.until(EC.element_to_be_clickable(LOGIN_BTN)).click()
        # 5. Click on pop-window OK button
        wait.until(EC.element_to_be_clickable(POP_UP_WNDW_OK_BTN)).click()
        sleep(4)

    def clck_usrs_btn(self):
        wait = WebDriverWait(self.driver, 10)
        # 6. Click on Users button
        wait.until(EC.element_to_be_clickable(USERS)).click()

    def clck_qck_actns_btn(self):
        wait = WebDriverWait(self.driver, 10)
        # 7. Click on Quick Actions button
        wait.until(EC.element_to_be_clickable(QUICK_ACTIONS)).click()

    def slct_add_drp_dwn_mn(self):
        wait = WebDriverWait(self.driver, 10)
        # 8. Click on Add button
        wait.until(EC.element_to_be_clickable(ADD_MENU)).click()

    def fll_rqrd_flds(self):
        wait = WebDriverWait(self.driver, 10)
        # 9. Fill out the First Name field
        wait.until(EC.presence_of_element_located(FIRST_NAME)).clear()
        wait.until(EC.presence_of_element_located(FIRST_NAME)).send_keys('Roman')

        # 10. Fill out the Last Name field
        wait.until(EC.presence_of_element_located(LAST_NAME)).clear()
        wait.until(EC.presence_of_element_located(LAST_NAME)).send_keys('Ivanov')

        # Generators of password, name and email
        password = str(randint(999, 9999))
        name = 'name' + password
        email = (name + '@sample.com')

        # 11. Fill out the Email field
        wait.until(EC.presence_of_element_located(EMAIL)).clear()
        wait.until(EC.presence_of_element_located(EMAIL)).send_keys(email)

        # 12. Fill out the Telephone field
        wait.until(EC.presence_of_element_located(TELEPHONE)).clear()
        wait.until(EC.presence_of_element_located(TELEPHONE)).send_keys('7895678956')

        # 13. Choose admin in the drop-down menu
        element = wait.until(EC.visibility_of_element_located((SELECT_ROLE)))
        select = Select(element)
        select.select_by_value("admin")

        # 14. Fill out the Adress1 field
        wait.until(EC.presence_of_element_located(ADDRESS_1)).clear()
        wait.until(EC.presence_of_element_located(ADDRESS_1)).send_keys('1933, 84 street')

        # 14. Fill out the Adress2 field
        wait.until(EC.presence_of_element_located(ADDRESS_2)).clear()
        wait.until(EC.presence_of_element_located(ADDRESS_2)).send_keys('Just test')

        # 15. Fill out the City field
        wait.until(EC.presence_of_element_located(CITY)).clear()
        wait.until(EC.presence_of_element_located(CITY)).send_keys('Brooklyn')

        # 16. Fill out the Zip Code field
        wait.until(EC.presence_of_element_located(ZIP_CODE)).clear()
        wait.until(EC.presence_of_element_located(ZIP_CODE)).send_keys('11214')

        # 17. Choose Select Country in the drop-down menu United States
        wait.until(EC.element_to_be_clickable(COUNTRY)).click()
        wait.until(EC.presence_of_element_located(COUNTRY)).send_keys('United States')

        # 18. Choose Select State in the drop-down menu New York
        wait.until(EC.element_to_be_clickable(STATE)).click()
        wait.until(EC.presence_of_element_located(STATE)).send_keys('New York')

    def clck_n_add_btn(self):
        wait = WebDriverWait(self.driver, 10)
        # 19. Click on Add button
        wait.until(EC.element_to_be_clickable(ADD_BTN)).click()

    def vrf_usr_is_hr(self, text_hr):
        wait = WebDriverWait(self.driver, 10)
        expected_text = text_hr
        actual_text = wait.until(EC.presence_of_element_located((TEXT_HR))).text
        assert expected_text in actual_text
        print(f'Expected {text_hr}, and got "{actual_text}" ')
        sleep(10)
        # End of the above code
        sleep(2)

    def admns_n_usrs(self):
        # 7. Make sure there are at list two Admins and one User role in the list of users
        wait = WebDriverWait(self.driver, 15)
        expected_text = 'ADMIN'
        actual_text = wait.until(EC.presence_of_element_located((ADMIN))).text
        assert expected_text in actual_text
        print(f'Expected {expected_text}, and got: "{actual_text}" ')
        len_admins = len(wait.until(EC.presence_of_all_elements_located((ADMIN))))
        print(f'Admins: {len_admins}, type: {type(len_admins)}')
        if len_admins < 2:
            print(f'ADMINS < 2, NOT OK, there is: {len_admins} admin, add to 2 admins')
            # Driver quit
            self.driver.quit()
        else:
            print(f'ADMINS >=2, OK, there are: {len_admins} admins')

            expected_text = 'USER'
            actual_text = wait.until(EC.presence_of_element_located((USER))).text
            assert expected_text in actual_text
            print(f'Expected {expected_text}, and got: "{actual_text}" ')
            len_users = len(wait.until(EC.presence_of_all_elements_located((USER))))
            if len_users >= 2:
                print(f'USERS >=1, OK, there are: {len_users} users')
            else:
                print(f'USERS !>=1, NOT OK, there are: {len_users} users')

            total_users_admins_before_delete = len_admins + len_users
            print(f'Total admins and users before delete: {total_users_admins_before_delete}')

    def take_usr_t_dlt(self):
        # 8. Choose any username with Admin or User role except yours.
        # Click on the "Settings" (three vertical dots) from the rightmost side of the user.
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(THREE_DOTS)).click()

    def dlt_drp_dwn_mn(self):
        # 9. Select "Delete" from the dropdown menu.
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located(DELETE_BTN)).click()

    def cnfrm_dlt(self):
        # 10. The pop-up dialog window "Delete user" appears after clicking on the "Delete" button.
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(DELETE_OK_BTN)).click()

    def vrf_usr_dltd(self):
        # 11. The "Users" page has opened and user is not in the list of users.
        wait = WebDriverWait(self.driver, 15)
        len_admins = len(wait.until(EC.presence_of_all_elements_located((ADMIN))))
        len_users = len(wait.until(EC.presence_of_all_elements_located((USER))))
        total_users_admins_before_delete = len_admins + len_users
        self.driver.refresh()
        len_admins = len(wait.until(EC.presence_of_all_elements_located((ADMIN))))
        len_users = len(wait.until(EC.presence_of_all_elements_located((USER))))
        total_admins_users_after_delete = len_admins + len_users
        if total_users_admins_before_delete - total_admins_users_after_delete == 1:
            print(
                f'Delete is OK: {total_users_admins_before_delete} - {total_admins_users_after_delete} = {total_users_admins_before_delete - total_admins_users_after_delete}')
        else:
            print(f'Delete is not OK')
        print(f'Total admins and users after delete: {total_admins_users_after_delete}')

        # End of the above code

    def entr_vld_wrng_eml(self, email):
        # 1. Enter valid, but the incorrect email address in the line "Email address"
        wait = WebDriverWait(self.driver, 15)
        # Send Login e-mail
        wait.until(EC.presence_of_element_located(LOGIN_EMAIL)).clear()
        wait.until(EC.presence_of_element_located(LOGIN_EMAIL)).send_keys(email)

    def entr_vld_crct_pswd(self, pswd):
        # 2. Send Correct Password
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located(LOGIN_PASSWORD)).clear()
        wait.until(EC.presence_of_element_located(LOGIN_PASSWORD)).send_keys(pswd)
        # Click on Login button
        wait.until(EC.element_to_be_clickable(LOGIN_BTN)).click()

    def vrf_invld_lgn_r_pswd_hr(self, expected_text):
        # 3. Verify Invalid Login or Password is here
        wait = WebDriverWait(self.driver, 15)
        actual_text = wait.until(EC.presence_of_element_located((INVLD_LGN_PSWRD_HR))).text
        print(actual_text)
        assert expected_text in actual_text
        print(f'Expected {expected_text}, and got: "{actual_text}" ')

        # End of the above code

    def clck_usr_nm(self):
        # 6. Click on triangle to enter the user
        wait = WebDriverWait(self.driver, 15)
        target = wait.until(EC.element_to_be_clickable(CLCK_TRNGL))
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        sleep(2)
        actions.click(target)
        actions.perform()

        # 7. Click on the User name in the Sidebar menu
        wait.until(EC.element_to_be_clickable(USR_NM)).click()

    def clck_lgt_btn(self):
        # 8. Hover over the "Logout" button in the dropdown menu and click on the button "Logout"
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(LGT_BTN)).click()
        self.driver.refresh()

    def vrf_lgn_pg_opn(self, url):
        # 9. Verify https://devcloud.connectedio.com is open
        expected_text = url
        actual_text = self.driver.current_url
        assert expected_text in actual_text
        if expected_text == actual_text:
            print(f'Expected "{expected_text}", and got: "{actual_text}" ')
        else:
            print(f'Expected "{expected_text}", and got: "{actual_text}" ')

        # End of the above code

    def clck_hdr_lgt_btn(self):
        # Hover over the "Logout" button at the right corner of the Header and click on the button "Logout"
        wait = WebDriverWait(self.driver, 15)
        target = wait.until(EC.element_to_be_clickable(CLCK_LGT))
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        actions.click(target)
        actions.perform()

    def lgn_opnd_aftr_lgout(self, lgn_opnd_aftr_lgout):
        # https://devcloud.connectedio.com/login is open after logout
        sleep(2)
        expected_text = lgn_opnd_aftr_lgout
        actual_text = self.driver.current_url
        assert expected_text in actual_text
        if expected_text == actual_text:
            print(f'Expected "{expected_text}", and got: "{actual_text}" ')
        else:
            print(f'Expected "{expected_text}", but got: "{actual_text}" ')

        # End of the above code

    def go_to_chng_pswrd_pg(self):
        # Click on triangle to enter the user
        wait = WebDriverWait(self.driver, 15)
        target = wait.until(EC.element_to_be_clickable(CLCK_TRNGL))
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        sleep(2)
        actions.click(target)
        actions.perform()

        # Click on the User name in the Sidebar menu
        wait.until(EC.element_to_be_clickable(USR_NM)).click()

        # Click on the Change Password button
        wait.until(EC.element_to_be_clickable(CHNG_PSWD)).click()

    def cng_pswd_url_opn(self, cng_pswd_url_opn):
        # https://devcloud.connectedio.com/profile/change-password is open
        expected_text = cng_pswd_url_opn
        actual_text = self.driver.current_url
        assert expected_text in actual_text
        if expected_text == actual_text:
            print(f'Expected "{expected_text}", and got: "{actual_text}" ')
        else:
            print(f'Expected "{expected_text}", but got: "{actual_text}" ')

    def ntr_old_pswd(self, old_pswd):
        # Enter the old password in the field "New Password" MyUSA2016!@
        wait = WebDriverWait(self.driver, 15)
        sleep(2)
        wait.until(EC.presence_of_element_located(NW_VLD_PSWD)).clear()
        wait.until(EC.presence_of_element_located(NW_VLD_PSWD)).send_keys(old_pswd)

    def cfrm_old_pswd(self, old_pswd):
        # Enter the same old password in the field "Confirm New Password"
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located(CNFRM_NW_VLD_PSWD)).clear()
        wait.until(EC.visibility_of_element_located(CNFRM_NW_VLD_PSWD)).send_keys(old_pswd)

    def clck_on_btn_save(self):
        # Click on the button "Save"
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(SV_BTN)).click()

    def old_new_r_nt_same(self, old_nw_r_nt_same):
        # Verify the words Old and new password cannot be same. is on the page
        wait = WebDriverWait(self.driver, 15)
        expected_text = old_nw_r_nt_same
        actual_text = wait.until(EC.element_to_be_clickable(SCSS_TXT_HR)).text
        assert expected_text in actual_text
        if expected_text == actual_text:
            print(f'Expected "{expected_text}", and got: "{actual_text}" ')
        else:
            print(f'Expected "{expected_text}", but got: "{actual_text}" ')

        # End of the above code

    def ll_lmnts_r_prsnt(self):
        # 6. Check if all elements are present.
        # 6.1. Cards: "DEVICE ONLINE", 6.2. "DEVICE OFFLINE",
        # 6.3. "INVENTORY", 6.4. "ALERT/NOTIFICATION", 6.5. "DATA USAGE"
        wait = WebDriverWait(self.driver, 15)
        # 1
        expected_text = 'DEVICE ONLINE'
        actual_text = wait.until(EC.presence_of_element_located((DVC_ONLN_TXT))).text
        assert expected_text in actual_text
        print(f'Expected {expected_text}, and got: "{actual_text}" ')
        # 2
        expected_text = 'DEVICE OFFLINE'
        actual_text = wait.until(EC.presence_of_element_located((DVC_OFFLN_TAB))).text
        assert expected_text in actual_text
        print(f'Expected {expected_text}, and got: "{actual_text}" ')
        # 3
        expected_text = 'INVENTORY'
        actual_text = wait.until(EC.presence_of_element_located((INVNTR))).text
        assert expected_text in actual_text
        print(f'Expected {expected_text}, and got: "{actual_text}" ')
        # 4
        expected_text = 'ALERT/NOTIFICATION'
        actual_text = wait.until(EC.presence_of_element_located((ALRT_NTFCTN))).text
        assert expected_text in actual_text
        print(f'Expected {expected_text}, and got: "{actual_text}" ')
        # 5
        expected_text = 'DATA USAGE'
        actual_text = wait.until(EC.presence_of_element_located((DT_USG))).text
        assert expected_text in actual_text
        print(f'Expected {expected_text}, and got: "{actual_text}" ')

    def ll_sctns_r_prsnt(self):
        # 7. Check if sections are present.
        # 7.1 "Data Usage Details", 7.2. "Notifications/Alerts",
        # 7.3. "Groups", 7.4. "Signal Strength", 7.5. "Device Location".
        # 1
        wait = WebDriverWait(self.driver, 15)
        expected_text = 'Data Usage Details'
        actual_text = wait.until(EC.presence_of_element_located((DT_USG_DTLS))).text
        assert expected_text in actual_text
        print(f'Expected {expected_text}, and got: "{actual_text}" ')
        # 2
        expected_text = 'Notifications / Alerts'
        actual_text = wait.until(EC.presence_of_element_located((NTFCTNS_ALRTS))).text
        assert expected_text in actual_text
        print(f'Expected {expected_text}, and got: "{actual_text}" ')
        # 3
        expected_text = 'Groups'
        actual_text = wait.until(EC.presence_of_element_located((GRPS))).text
        assert expected_text in actual_text
        print(f'Expected {expected_text}, and got: "{actual_text}" ')
        # 4
        expected_text = 'Signal Strength'
        actual_text = wait.until(EC.presence_of_element_located((SGNL_STRNTH))).text
        assert expected_text in actual_text
        print(f'Expected {expected_text}, and got: "{actual_text}" ')
        # 5
        expected_text = 'Device   Locations'
        actual_text = wait.until(EC.presence_of_element_located((DVC_LCTN))).text
        assert expected_text in actual_text
        print(f'Expected {expected_text}, and got: "{actual_text}" ')

        # Pictures
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        options.binary_location = "/usr/bin/chromium"
        # driver = webdriver.Chrome(chrome_options=options)
        images = self.driver.find_elements_by_tag_name('img')
        pics_on_page = len(images)
        for image in images:
            print(image.get_attribute('src'))
        print(f'There are: {pics_on_page} images on the page')

        # End of the above code

    def clck_on_dvc_nln(self):
        # Click on DEVICE ONLINE card
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(DVC_ONLN_TXT)).click()

    def dvc_mngmnt_ptrl_hr(self, dvc_mngmnt_ptrl_hr):
        # Verify words Device Management Portal are here
        wait = WebDriverWait(self.driver, 15)
        expected_text = dvc_mngmnt_ptrl_hr
        actual_text = wait.until(EC.presence_of_element_located((DVC_MNGMNT_PRTL))).text
        assert expected_text in actual_text
        print(f'Expected {expected_text}, and got: "{actual_text}" ')

    def onln_hr(self, onln_hr):
        # Verify words Device Management Portal are here
        wait = WebDriverWait(self.driver, 15)
        expected_text = onln_hr
        actual_text = wait.until(EC.presence_of_element_located((ONLN_HERE))).text
        assert expected_text in actual_text
        print(f'Expected {expected_text}, and got: "{actual_text}" ')

        # End of the above code

    def vrf_qntty_is_the_same(self):
        # Pay attention to the number of devices on the "DEVICE ONLINE" card
        wait = WebDriverWait(self.driver, 15)
        sleep(2)
        txt_frm_dvc_onln = wait.until(EC.visibility_of_element_located(DVC_ONLN)).text

        # Click on DEVICE ONLINE card
        wait.until(EC.element_to_be_clickable(DVC_ONLN)).click()

        # And if there are no data in Device Management Portal verify text No Data Available is here
        no_data_available = wait.until(EC.element_to_be_clickable(NO_DATA)).text

        # If txt_frm_dvc_onln = 0 and no_data_available = 'No Data Available' stop and exit program
        if txt_frm_dvc_onln == '0' and no_data_available == 'No Data Available':
            print(
                f'Number of devices from DEVICE ONLINE element: {txt_frm_dvc_onln}, type: {type(txt_frm_dvc_onln)};\nNo data avalable is here: {no_data_available}, type {type(no_data_available)}.')
            # Driver quit
            self.driver.quit()
            # break
        else:

            # Count the number of devices with online status on the Devices page
            len_tbl = len(wait.until(EC.presence_of_all_elements_located(DVCS_TBL)))
            print(f'Quantity of the strings in the devices table: {len_tbl}')

            # Verify if the number of devices on the DEVICE ONLINE card should match the number of devices with online status on the Devices page
            assert txt_frm_dvc_onln in str(len_tbl)
            print(f'Expected {txt_frm_dvc_onln}, and got: "{str(len_tbl)}" ')

            # End of the above code

    def clk_dvcs_onlc(self):
        # Click on DEVICE OFFLINE card
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(DVCS_OFFLN)).click()

    def url_dvcs_hr(self, url_dvcs_hr):
        # https://devcloud.connectedio.com/devices is here
        expected_text = url_dvcs_hr
        actual_text = self.driver.current_url
        assert expected_text in actual_text
        if expected_text == actual_text:
            print(f'Expected {expected_text}, and got: "{actual_text}" ')
        else:
            print(f'Expected {expected_text}, but got: "{actual_text}" ')

    def offln_sts_hr(self):
        # Verify Offline status in FILTERS field is seen
        wait = WebDriverWait(self.driver, 15)
        expected_text = 'Offline'
        actual_text = wait.until(EC.presence_of_element_located((OFFLN_TXT))).text
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')

        # End of the above code

    def vrf_qntty_ofldvcs_is_the_same(self):
        # 6. Pay attention to the number of devices on the "DEVICE OFFLINE" card
        wait = WebDriverWait(self.driver, 15)
        txt_frm_dvc_offln = (wait.until(EC.visibility_of_all_elements_located(DVC_OFFLN)))[1].text
        print(f'Devices offline: {txt_frm_dvc_offln}')

        # 7.1 Click on DEVICE OFFLINE card
        (wait.until(EC.visibility_of_all_elements_located(DVC_OFFLN)))[1].click()

        # # 7.2 And if there are no data in Device Management Portal verify text No Data Available is here
        no_data_available = wait.until(EC.element_to_be_clickable(NO_DATA)).text

        # 7.3 If txt_frm_dvc_offln = 0 and no_data_available = 'No Data Available' stop and exit program
        if txt_frm_dvc_offln == '0' and no_data_available == 'No Data Available':
            print(
                f'Number of devices from DEVICE OFFLINE element: {txt_frm_dvc_offln}, type: {type(txt_frm_dvc_offln)};\nNo data avalable is here: {no_data_available}, type {type(no_data_available)}.')
            # Driver quit
            self.driver.quit()
            # break
        else:

            # 8. Count the number of devices with offline status on the Devices page
            len_tbl = len(wait.until(EC.presence_of_all_elements_located(DVCS_TBL_EMPT)))
            print(f'Quantity of the strings in the devices table: {len_tbl}')

            # 9. Verify if the number of devices on the DEVICE ONLINE card should match the number of devices with online status on the Devices page
            assert txt_frm_dvc_offln in str(len_tbl)
            print(f'Expected {txt_frm_dvc_offln}, and got: "{str(len_tbl)}" ')

            # End of the above code

    def clck_on_invntr_elmnt(self):
        # Click on the INVENTORY card
        wait = WebDriverWait(self.driver, 15)
        invntr_elmnt = (wait.until(EC.presence_of_all_elements_located(INVNTR_ELMNT)))[2]
        invntr_elmnt.click()

    def invntr_sts_hr(self):
        # Inventory status in FILTERS field
        wait = WebDriverWait(self.driver, 15)
        expected_text = 'Inventory'
        actual_text = wait.until(EC.presence_of_element_located((INVNTR_TXT))).text
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')

        # End of the above code
