from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()

# Locators
LOGIN_EMAIL = (By.XPATH, "//input[@placeholder='Email address']")
LOGIN_PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
LOGIN_BTN = (By.CSS_SELECTOR, "button.btn.btn-primary.text-uppercase.w-100.font-weight-bold.gradient-btn.shadow-1.border-0")
POP_UP_WNDW_OK_BTN = (By.XPATH, "//div[@class='swal2-actions']//button[@class='swal2-confirm btn btn-outline-primary btn-sm btn-custom swal2-styled']")
DT_USG_CRD = (By.CSS_SELECTOR, "div.card.overflowhidden.number-chart.p-4")
CLLR = (By.XPATH, "(//strong[@class='ng-tns-c6-0'])[1]")
WAN = (By.XPATH, "(//strong[@class='ng-tns-c6-0'])[4]")
DSCH_BRD_ICN = (By.XPATH, "(//a[@class='ng-star-inserted'])[1]")
DSCH_BRD_TXT = (By.XPATH, "//h2[@class='mb-0']")
USG_DTLS_TXT = (By.XPATH, "(//h6[@class='tile-title text-uppercase'])[1]")
QSTN_CRCL_MRK = (By.XPATH, "//i[@class='fa fa-question-circle']")
TL_TIP_TXT = (By.XPATH, "//span[@tool-tip='WAN/Cellular data usage classified periodically.']")

# Explicit wait
wait = WebDriverWait(driver, 15)

# 1. Open the url
driver.get( 'https://devcloud.connectedio.com' )

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

# 6. Click Dashboard menu icon and make sure Dashboard page reloaded
wait.until(EC.element_to_be_clickable(DSCH_BRD_ICN)).click()
dsch_brd_txt = wait.until(EC.visibility_of_element_located(DSCH_BRD_TXT)).text
print(f'Text is here: "{dsch_brd_txt}"')

# 7. Make sure Data Usage Details block is present on the screen
usg_dtls_txt = wait.until(EC.visibility_of_element_located(USG_DTLS_TXT)).text
print(f'Text is here: "{usg_dtls_txt}"')

# 8. Hover over question mark in top right of the block and make sure tooltip appears
tl_tp_txt = wait.until(EC.visibility_of_element_located(TL_TIP_TXT)).text
print(f'Text is here: "{tl_tp_txt}"')
target = wait.until(EC.element_to_be_clickable(TL_TIP_TXT))
actions = ActionChains(driver)
actions.move_to_element(target)
actions.click_and_hold(target)
actions.perform()
# TL_TIP_TXT.getattr('')


# def test_chart_renders_from_url(self):
#     url = 'http://localhost:8000/analyse/'
#     self.browser.get(url)
#     org = driver.find_element_by_id('org')
#     # Find the value of org?
#     val = org.get_attribute("attribute name")

# Sleep to see what we have
sleep(2)

# # Driver quit
# driver.quit()