from behave import *
from behave.reporter.junit import JUnitReporter

@step('I am on test page')
def test_page(context):
    pass

@step('I see test fail')
def test_fail(context):
    assert False
    
@step('I see test pass')
def test_pass(context):
    pass
    