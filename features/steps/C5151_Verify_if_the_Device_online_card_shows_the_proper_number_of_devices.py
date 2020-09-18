from behave import *

# @then('Pay attention to the number of devices on the {txt_frm_dvc_onln} card')
# def dvc_onln_hr(context, txt_frm_dvc_onln):
#     """
#     Pay attention to the number of devices on the DEVICE ONLINE card
#     """
#     context.app.main_page.dvc_onln_hr(txt_frm_dvc_onln)
#
#
# @then("Count the number of devices with online status on the Devices page")
# def dvc_on_dvcs_pg(context):
#     """
#     Count the number of devices with online status on the Devices page
#     """
#     context.app.main_page.dvc_on_dvcs_pg()


@step("Verify if the number of devices on the DEVICE ONLINE card should match the number of devices with online status on the Devices page")
def vrf_qntty_is_the_same(context):
    """
    Verify if the number of devices on the DEVICE ONLINE card should match the number of devices with online status on the Devices page
    """
    context.app.main_page.vrf_qntty_is_the_same()