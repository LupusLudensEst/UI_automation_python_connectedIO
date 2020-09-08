from behave import *

@then("Click on the Background button and verify there is a text {bckgrd} on the newly open page")
def clck_on_bckgrd_btn(context, bckgrd):
    """
    Click on the Background button and verify there is a text Background on the newly open page
    """
    context.app.main_page.clck_on_bckgrd_btn(bckgrd)