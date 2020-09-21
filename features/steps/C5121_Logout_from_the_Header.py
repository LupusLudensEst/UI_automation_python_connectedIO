from behave import *

@then("Hover over the Logout button at the right corner of the Header and click on the button Logout")
def clck_hdr_lgt_btn(context):
    """
    Hover over the Logout button at the right corner of the Header and click on the button Logout
    """
    context.app.main_page.clck_hdr_lgt_btn()


@step("{lgn_opnd_aftr_lgout} is open after logout")
def lgn_opnd_aftr_lgout(context, lgn_opnd_aftr_lgout):
    """
    https://devcloud.connectedio.com/login is open after logout
    """
    context.app.main_page.lgn_opnd_aftr_lgout(lgn_opnd_aftr_lgout)