from behave import *
from automa.api import *

@given('I click notepad')
def step_impl(context):
    start("notepad")
    pass

@when('I click image')
def step_impl(context):
    click(Image("C:\Automation\Tutorial\max.png"))
    pass

@then('I see result')
def step_impl(context):
    click("File")
    click("Open")
    click("Cancel")
    pass