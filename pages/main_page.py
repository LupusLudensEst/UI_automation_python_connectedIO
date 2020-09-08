from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from random import randint
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

# Locators
CONTACT_BTN = (By.XPATH, "//a[contains(text(), 'Contact')]")
NAME_FLD = (By.NAME, "name")
EMAIL_FLD = (By.NAME, "email")
PHONE_FLD = (By.NAME, "contact_no")
COMPANY_FLD = (By.NAME, "company")
WEBSITE_FLD = (By.NAME, "website")
INQUARY_FLD = (By.ID, "inputinquiry")
TEXT_FLD = (By.NAME, "enquiry")
SUBMIT = (By.NAME, "submit")
CAPTCHA_REQ = (By.XPATH, "//span[@class='alert alert-danger']")
TOP_BUTTONS = (By.XPATH, "//a[@class='nav-link']")
ABOUT_US_BTN_SUBMENU = (By.CSS_SELECTOR, "a.nav-link.dropdown-toggle")
ALL_SUBMENU_BTNS = (By.CSS_SELECTOR, "a.dropdown-item")
NEWS_BTN = (By.XPATH, "//a[@class='dropdown-item  ']")
NEWS_BTN_TXT = (By.XPATH, "//div[@class='col-md-12 text-center']")
TESTIMONIALS_BTN = (By.XPATH, "(//a[@class='dropdown-item  '])[2]")
TESTIMONIALS_BTN_TXT = (By.XPATH, "//div[@class='col-md-12 text-center']")
OUR_TEAM_BTN = (By.XPATH, "(//a[@class='dropdown-item  '])[3]")
OUR_TEAM_BTN_TXT = (By.XPATH, "//div[@class='col-md-12 text-center']")
CAREERS_BTN = (By.XPATH, "(//a[@class='dropdown-item  '])[4]")
CAREERS_BTN_TXT = (By.XPATH, "//div[@class='col-md-12 text-center']")
BACKGROUND_BTN = (By.XPATH, "(//a[@class='dropdown-item  '])[5]")
BACKGROUND_BTN_TXT = (By.XPATH, "//div[@class='col-md-12 text-center']")
PRTNR_PROGS_BTN = (By.XPATH, "(//a[@class='dropdown-item  '])[6]")
PRTNR_PROGS_BTN_TXT = (By.XPATH, "//div[@class='col-md-12 text-center']")
SEND_MSG_BTN = (By.CSS_SELECTOR, "span#short-message")
NAME_FLD_SEND_FORM = (By.CSS_SELECTOR, "input#offline0Field.textinput")
EMAIL_FLD_SEND_FORM  = (By.ID, "offline1Field")
MSG_FLD = (By. ID, "offline2Field")
DROP_OUT_SBMN = (By.ID, "offline3Field")
SBMT_BTN = (By.ID, "formSubmit")
AWAY = (By.ID, "tawkchat-status-text-container")
PRESALES = (By.XPATH, "//label[text()='Pre-Sales']")
PRODUCT_SUPPORT =  (By.XPATH, "//label[text()='Product Support']")
NAME_CHAT = (By.ID, "prechat1Field")
PHONE_CHAT = (By. ID, "prechat2Field")
EMAIL_CHAT = (By.ID, "prechat3Field")
SUPPORT_MERAKY = (By.XPATH, "//label[@for='prechat4check0']")
START_CHAT = (By.ID, "formSubmit")
TEXT_HEREIN = (By.ID, "shortMessage")

class MainPage(Page):

    # Click on contact button, fill the fields and verify "The captcha is required." is here
    def click_cntct_btn(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(CONTACT_BTN)).click()
        # Generators of password, name and email
        password = str(randint(999, 9999))
        name = 'name' + password
        email = (name + '@sample.com')
        print(f'\nName: {name}, password: {password} and email: {email}')
        # Fill the name field
        self.driver.find_element(*NAME_FLD).clear()
        self.driver.find_element(*NAME_FLD).send_keys(name)
        # Fill the email field
        self.driver.find_element(*EMAIL_FLD).clear()
        self.driver.find_element(*EMAIL_FLD).send_keys(email)
        # Fill the phone field
        self.driver.find_element(*PHONE_FLD).clear()
        self.driver.find_element(*PHONE_FLD).send_keys('4074354433')
        # Fill the company name field
        self.driver.find_element(*COMPANY_FLD).clear()
        self.driver.find_element(*COMPANY_FLD).send_keys('Red Cucumber LLC')
        # Fill the website field
        self.driver.find_element(*WEBSITE_FLD).clear()
        self.driver.find_element(*WEBSITE_FLD).send_keys('https://github.com/LupusLudensEst?tab=repositories')
        # Choose inquary type
        self.driver.find_element(*INQUARY_FLD).click()
        drop_menu = wait.until(EC.presence_of_all_elements_located((By.ID, "inputinquiry")))[0]
        # If item has a select option
        element = wait.until(EC.visibility_of_element_located((By.ID, "inputinquiry")))
        select = Select(element)
        select.select_by_value("sales_email")
        # Fill the inquary field
        self.driver.find_element(*TEXT_FLD).clear()
        self.driver.find_element(*TEXT_FLD).send_keys('Test text')
        # Click submit
        self.driver.find_element(*SUBMIT).click()
        # Verify "The captcha is required." is here
        actual_text = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='alert alert-danger']"))).text
        assert text in actual_text
        print(f'Text is here: "{actual_text}" ')
        sleep(2)

        # Driver quit
        self.driver.quit()

    def click_top_buttons(self):
        len_array = len(self.driver.find_elements(*TOP_BUTTONS))
        counter = 0
        print(f'Length of array: {len_array}')
        for i in range(counter, len_array - 2):
            while counter <= len_array - 2:
                counter += 1
                self.driver.find_elements(*TOP_BUTTONS)[counter].click()
                sleep(1)
            # Step back in the browser hystory
            self.driver.back()

        # Driver quit
        self.driver.quit()

    def privacy_here(self, privacy_text):
        wait = WebDriverWait(self.driver, 10)
        # Click on privacy button
        # wait.until(EC.element_to_be_clickable((PRIVACY_ICN))).click()
        # driver.find_element(*PRIVACY_ICN).click()
        target = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Privacy Policy')]")
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        sleep(2)
        actions.click(target)
        actions.perform()

        # Verify page has "PRIVACY POLICY"
        actual_text = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Privacy Policy')]"))).text
        assert privacy_text in actual_text
        print(f'Text is here: "{actual_text}" ')
        sleep(2)
        # Step back in the browser hystory
        self.driver.back()

        # Driver quit
        self.driver.quit()

    # Click on About Us button
    def clck_on_abt_us_btn(self):
        old_window = self.driver.current_window_handle
        print(f'Old window: {old_window}')
        wait = WebDriverWait(self.driver, 10)
        # Click on About Us button
        wait.until(EC.element_to_be_clickable(ABOUT_US_BTN_SUBMENU)).click()
        # To see how many there are submenu buttons
        len_array = len(wait.until(EC.presence_of_all_elements_located(ALL_SUBMENU_BTNS)))
        print(f'There are {len_array} drop-out menu buttons')

    # Click on the News btn
    def clck_on_news_btn(self, news):
        old_window = self.driver.current_window_handle
        print(f'Old window: {old_window}')
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(NEWS_BTN)).click()
        original_window = self.driver.window_handles
        print(f'New window: {original_window}')
        wait.until(EC.new_window_is_opened)
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        text_is_here = wait.until(EC.visibility_of_element_located(NEWS_BTN_TXT)).text
        print(f'Text is here: \n{text_is_here}')
        assert news in text_is_here
        self.driver.close()
        self.driver.switch_to.window(old_window)

        # Driver quit
        self.driver.quit()

    # Click on the Testimonials btn
    def clck_on_tsmnls_btn(self, tsmnls):
        old_window = self.driver.current_window_handle
        print(f'Old window: {old_window}')
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(TESTIMONIALS_BTN)).click()
        original_window = self.driver.window_handles
        print(f'New window: {original_window}')
        wait.until(EC.new_window_is_opened)
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        text_is_here = wait.until(EC.visibility_of_element_located(TESTIMONIALS_BTN_TXT)).text
        print(f'Text is here: \n{text_is_here}')
        assert tsmnls in text_is_here
        self.driver.close()
        self.driver.switch_to.window(old_window)

        # Driver quit
        self.driver.quit()

    # Click on the OurTeam btn
    def clck_on_our_team_btn(self, our_team):
        old_window = self.driver.current_window_handle
        print(f'Old window: {old_window}')
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(OUR_TEAM_BTN)).click()
        original_window = self.driver.window_handles
        print(f'New window: {original_window}')
        wait.until(EC.new_window_is_opened)
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        text_is_here = wait.until(EC.visibility_of_element_located(OUR_TEAM_BTN_TXT)).text
        print(f'Text is here: \n{text_is_here}')
        assert our_team in text_is_here
        self.driver.close()
        self.driver.switch_to.window(old_window)

        # Driver quit
        self.driver.quit()

    # Click on the Careers btn
    def clck_on_crrs_btn(self, crrs):
        old_window = self.driver.current_window_handle
        print(f'Old window: {old_window}')
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(CAREERS_BTN)).click()
        original_window = self.driver.window_handles
        print(f'New window: {original_window}')
        wait.until(EC.new_window_is_opened)
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        text_is_here = wait.until(EC.visibility_of_element_located(CAREERS_BTN_TXT)).text
        print(f'Text is here: \n{text_is_here}')
        assert crrs in text_is_here
        self.driver.close()
        self.driver.switch_to.window(old_window)

        # Driver quit
        self.driver.quit()

    # Click on the Background btn
    def clck_on_bckgrd_btn(self, bckgrd):
        old_window = self.driver.current_window_handle
        print(f'Old window: {old_window}')
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(BACKGROUND_BTN)).click()
        original_window = self.driver.window_handles
        print(f'New window: {original_window}')
        wait.until(EC.new_window_is_opened)
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        text_is_here = wait.until(EC.visibility_of_element_located(BACKGROUND_BTN_TXT)).text
        print(f'Text is here: \n{text_is_here}')
        assert bckgrd in text_is_here
        self.driver.close()
        self.driver.switch_to.window(old_window)

        # Driver quit
        self.driver.quit()

    # Click on the Partners Program btn
    def clck_on_prtnrs_prgrm_btn(self, prtnrs_prgrm):
        old_window = self.driver.current_window_handle
        print(f'Old window: {old_window}')
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(PRTNR_PROGS_BTN)).click()
        original_window = self.driver.window_handles
        print(f'New window: {original_window}')
        wait.until(EC.new_window_is_opened)
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        text_is_here = wait.until(EC.visibility_of_element_located(PRTNR_PROGS_BTN_TXT)).text
        print(f'Text is here: \n{text_is_here}')
        assert prtnrs_prgrm in text_is_here
        self.driver.close()
        self.driver.switch_to.window(old_window)

        # Driver quit
        self.driver.quit()

    # Click on Send message button
    def click_on_send_message_btn(self):
        # Switch to iFrame #1
        iframe_list = self.driver.find_elements(By.TAG_NAME, "iframe")
        length = len(iframe_list)
        print(length)
        iframe = self.driver.find_elements(By.TAG_NAME, "iframe")[1]
        self.driver.switch_to.frame(iframe)

        self.driver.find_element(*SEND_MSG_BTN).click()
        self.driver.switch_to.default_content()

    # Fill the name field by random test name
    def fill_name_fld(self):
        # Switch to iFrame #2
        iframe_list = self.driver.find_elements(By.TAG_NAME, "iframe")
        length = len(iframe_list)
        print(length)
        iframe = self.driver.find_elements(By.TAG_NAME, "iframe")[0]
        self.driver.switch_to.frame(iframe)

        # Generators of password, name and email
        password = str(randint(999, 9999))
        name = 'name' + password
        email = (name + '@sample.com')
        print(f'\nName: {name}, password: {password} and email: {email}')

        self.driver.find_element(*NAME_FLD_SEND_FORM).clear()
        self.driver.find_element(*NAME_FLD_SEND_FORM).send_keys(name)
        self.driver.switch_to.default_content()

    # Fill the email field by random email
    def fill_email_fld(self):
        # Switch to iFrame #2
        iframe_list = self.driver.find_elements(By.TAG_NAME, "iframe")
        length = len(iframe_list)
        print(length)
        iframe = self.driver.find_elements(By.TAG_NAME, "iframe")[0]
        self.driver.switch_to.frame(iframe)
        # Generators of password, name and email
        password = str(randint(999, 9999))
        name = 'name' + password
        email = (name + '@sample.com')
        print(f'\nName: {name}, password: {password} and email: {email}')

        self.driver.find_element(*EMAIL_FLD_SEND_FORM).clear()
        self.driver.find_element(*EMAIL_FLD_SEND_FORM).send_keys(email)
        self.driver.switch_to.default_content()

    # Fill the message field by Test text
    def fill_message_fld(self, message_fld):
        # Switch to iFrame #2
        iframe_list = self.driver.find_elements(By.TAG_NAME, "iframe")
        length = len(iframe_list)
        print(length)
        iframe = self.driver.find_elements(By.TAG_NAME, "iframe")[0]
        self.driver.switch_to.frame(iframe)

        self.driver.find_element(*MSG_FLD).clear()
        self.driver.find_element(*MSG_FLD).send_keys(message_fld)
        self.driver.switch_to.default_content()

    # Choose option from the drop-out menu Technical Support (Offline)
    def choose_option(self, option):
        wait = WebDriverWait(self.driver, 15)
        # Switch to iFrame #2
        iframe_list = self.driver.find_elements(By.TAG_NAME, "iframe")
        length = len(iframe_list)
        print(length)
        iframe = self.driver.find_elements(By.TAG_NAME, "iframe")[0]
        self.driver.switch_to.frame(iframe)

        self.driver.find_element(*DROP_OUT_SBMN).click()
        drop_menu = wait.until(EC.presence_of_all_elements_located((By.ID, "offline3Field")))[0]
        # If item has a select option
        element = wait.until(EC.visibility_of_element_located((By.ID, "offline3Field")))
        select = Select(element)
        select.select_by_value("1b40b600-e398-11e8-ab1a-a1df207e6aef")
        self.driver.switch_to.default_content()

    # Click Submit button
    def click_submit(self):
        wait = WebDriverWait(self.driver, 15)
        # Switch to iFrame #2
        iframe_list = self.driver.find_elements(By.TAG_NAME, "iframe")
        length = len(iframe_list)
        print(length)
        iframe = self.driver.find_elements(By.TAG_NAME, "iframe")[0]
        self.driver.switch_to.frame(iframe)

        wait.until(EC.element_to_be_clickable(SBMT_BTN)).click()
        self.driver.switch_to.default_content()

    # Assert text is here Your message was sent successfully!
    def assert_text_here(self, assert_here):
        wait = WebDriverWait(self.driver, 15)
        # Switch to iFrame #2
        iframe_list = self.driver.find_elements(By.TAG_NAME, "iframe")
        length = len(iframe_list)
        print(length)
        iframe = self.driver.find_elements(By.TAG_NAME, "iframe")[0]
        self.driver.switch_to.frame(iframe)

        text_here = assert_here
        actual_text = wait.until(EC.visibility_of_element_located((By.ID, "overlayOfflineForm"))).text
        assert text_here in actual_text
        print(f'Text is here: "{actual_text}" ')

        # Sleep to see what we have
        sleep(2)

        # Driver quit
        self.driver.quit()

    # Click on Away button
    def click_away(self):
        # Switch to iFrame #1
        iframe_list = self.driver.find_elements(By.TAG_NAME, "iframe")
        length = len(iframe_list)
        print(length)
        iframe = self.driver.find_elements(By.TAG_NAME, "iframe")[1]
        self.driver.switch_to.frame(iframe)
        self.driver.find_element(*AWAY).click()
        self.driver.switch_to.default_content()

    # Click on Pre-Sales check box
    def click_on_presales(self):
        # Switch to iFrame #2
        iframe_list = self.driver.find_elements(By.TAG_NAME, "iframe")
        length = len(iframe_list)
        print(length)
        iframe = self.driver.find_elements(By.TAG_NAME, "iframe")[0]
        self.driver.switch_to.frame(iframe)
        self.driver.find_element(*PRESALES).click()

    # Click on Product Support check-box
    def click_on_prod_supp(self):
        self.driver.find_element(*PRODUCT_SUPPORT).click()

    # Fill the name field in Away by random test name
    def name_in_away(self):
        # Generators of password, name and email
        password = str(randint(999, 9999))
        name = 'name' + password
        email = (name + '@sample.com')
        print(f'\nName: {name}, password: {password} and email: {email}')
        self.driver.find_element(*NAME_CHAT).clear()
        self.driver.find_element(*NAME_CHAT).send_keys(name)

    # Fill the phone field 7045343344
    def pfn_fld(self, phn_fld):
        self.driver.find_element(*PHONE_CHAT).clear()
        self.driver.find_element(*PHONE_CHAT).send_keys(phn_fld)

    # Fill the Email field in Away by random email
    def email_in_away(self):
        # Generators of password, name and email
        password = str(randint(999, 9999))
        name = 'name' + password
        email = (name + '@sample.com')
        print(f'\nName: {name}, password: {password} and email: {email}')
        self.driver.find_element(*EMAIL_CHAT).clear()
        self.driver.find_element(*EMAIL_CHAT).send_keys(email)

    # Click on Modem Support with Meraki check-box
    def meraki_chk_bx(self):
        self.driver.find_element(*SUPPORT_MERAKY).click()

    # Click Start Chat button
    def cht_btn(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(START_CHAT)).click()

    # Assert text is in Away Away
    def assert_text_away(self, text_away):
        wait = WebDriverWait(self.driver, 15)
        # # Switch to iFrame #2
        # iframe_list = self.driver.find_elements(By.TAG_NAME, "iframe")
        # length = len(iframe_list)
        # print(length)
        # iframe = self.driver.find_elements(By.TAG_NAME, "iframe")[0]
        # self.driver.switch_to.frame(iframe)

        text_here = text_away
        actual_text = wait.until(EC.visibility_of_element_located((By.ID, "shortMessage"))).text
        assert text_here in actual_text
        print(f'Text is here: "{actual_text}" ')

        # Sleep to see what we have
        sleep(2)

        # Driver quit
        self.driver.quit()




















