from behave import *

@then('Click on DEVICE OFFLINE card')
def clk_dvcs_onlc(context):
    """
    Click on DEVICE OFFLINE card
    """
    context.app.main_page.clk_dvcs_onlc()


@step("{url_dvcs_hr} is here")
def url_dvcs_hr(context, url_dvcs_hr):
    """
    Click on DEVICE OFFLINE card
    """
    context.app.main_page.url_dvcs_hr(url_dvcs_hr)


@then("Verify Offline status in FILTERS field is seen")
def offln_sts_hr(context):
    """
    Verify Offline status in FILTERS field is seen
    """
    context.app.main_page.offln_sts_hr()