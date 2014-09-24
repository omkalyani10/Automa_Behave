from behave import *
import methods


@step('I see test fail again')
def test_fail_again(context):
    context.execute_steps('''and I see test fail''')
    
@step('I say {text}')
def test_text(context, text):
    print "*******************************"
    print context
    print text
    