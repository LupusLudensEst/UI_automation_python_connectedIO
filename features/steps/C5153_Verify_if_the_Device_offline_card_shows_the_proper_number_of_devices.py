from behave import *

@step("Verify if the number of devices on the DEVICE OFFLINE card should match the number of devices with online status on the Devices page")
def vrf_qntty_ofldvcs_is_the_same(context):
    """
    Verify if the number of devices on the DEVICE OFFLINE card should match the number of devices with online status on the Devices page
    """
    context.app.main_page.vrf_qntty_ofldvcs_is_the_same()