from behave import given, then, when
from pages.loginActionItem_page import LoginPage


@given(u'User opens login page')
def step_impl(context):
    context.login_page = LoginPage(context.page, context.browser_context)
    context.login_page.go_to_enurl(context.config_data.get('testdata', 'en_url'))


@when(u'user enters user name and clicks on continue button')
def step_impl(context):
    context.login_page.en_enter_username(context.config_data.get('testdata', 'en_username'))


@when(u'user enters password and clicks on login button')
def step_impl(context):
    context.login_page.en_enter_password(context.config_data.get('testdata', 'en_password'))


@then(u'user should able to see home page')
def step_impl(context):
    context.array_of_strings = [context.config_data.get('testdata', 'String1'),
                                context.config_data.get('testdata', 'String2'),
                                context.config_data.get('testdata', 'String3'),
                                context.config_data.get('testdata', 'String4'),
                                context.config_data.get('testdata', 'String5'),
                                context.config_data.get('testdata', 'String6'),
                                context.config_data.get('testdata', 'String7'),
                                context.config_data.get('testdata', 'String8'),
                                context.config_data.get('testdata', 'String9'),
                                context.config_data.get('testdata', 'String10'),
                                context.config_data.get('testdata', 'String11'),
                                context.config_data.get('testdata', 'String12')]
    context.dynamic_usernames = context.login_page.getDynamicUsername()
    print("DynamicUsername is : ", context.dynamic_usernames)
    expected_messages = [pattern.replace("{username}", context.dynamic_usernames) for pattern in
                         context.array_of_strings]
    actual_message = context.login_page.homepagevalidation()
    print("Expected messages:", expected_messages)
    print("Actual message:", actual_message)
    assert actual_message in expected_messages, f"Expected message to be one of {expected_messages} but got '{actual_message}'"
    context.elements_count = context.login_page.validateclass()
    print(f"Number of elements: {context.elements_count}")


@when(u'user clicks on talenthub button and clicks on Action itom button')
def step_impl(context):
    context.login_page.clickTalentHub()


@then(u'user should able to see action page button')
def step_impl(context):
    context.login_page.actionItemHomepage()


@when(u'user clicks on filter button')
def step_impl(context):
    context.login_page.clickFilterBtn()


@then(u'user should able to see all,pending,completed buttons')
def step_impl(context):
    context.login_page.validateAllOptions()


@when(u'user clicks on sort button')
def step_impl(context):
    context.login_page.clickSortBtn()


@then(u'user should able to see latest first and oldest first buttons')
def step_impl(context):
    context.login_page.validatesortOptions()


@then(u'user should able to see username error message')
def step_impl(context):
    assert context.login_page.validateinvalidusernamemsg()


@when(u'user enters "{username}" and clicks on continue button')
def step_impl(context, username):
    context.login_page.invalidusername(username)


@then(u'user should able to see password error message')
def step_impl(context):
    context.login_page.validateinvalidpasswordmsg()


@when(u'user enters "{password}" and clicks on login button')
def step_impl(context, password):
    context.login_page.invalidpassword(password)
