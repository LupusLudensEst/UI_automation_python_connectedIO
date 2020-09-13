from behave import *

@then("Click on the User name in the Sidebar menu")
def clck_usr_nm(context):
    """
    Click on the User name in the Sidebar menu
    """
    context.app.main_page.clck_usr_nm()


@then("Hover over the Logout button in the dropdown menu and click on the button Logout")
def clck_lgt_btn(context):
    """
    Hover over the Logout button in the dropdown menu and click on the button Logout
    """
    context.app.main_page.clck_lgt_btn()


@step("Verify {url} is open")
def vrf_lgn_pg_opn(context, url):
    """
    Verify https://devcloud.connectedio.com is open
    """
    context.app.main_page.vrf_lgn_pg_opn(url)