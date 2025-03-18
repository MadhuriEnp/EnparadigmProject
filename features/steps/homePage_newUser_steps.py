from behave import given, then, when
from pages.homePage_newUser_page import HomePage


@when(u'user clicks on filter button in homepage')
def step_impl(context):
    context.home_page = HomePage(context.page, context.browser_context)
    context.home_page.click_homeFilter()


@then(u'user should able to see different filter options')
def step_impl(context):
    context.home_page.validate_homeFilterOptions()


@when(u'user clicks on sort button in homepage')
def step_impl(context):
    context.home_page = HomePage(context.page)
    context.home_page.click_homeSort()


@then(u'user should able to see different sort options')
def step_impl(context):
    context.home_page.validate_homeFilterOptions()


@when(u'clicks on NotStarted button')
def step_impl(context):
    context.home_page.click_Notstarted()


@then(u'user should able to see Start button')
def step_impl(context):
    context.home_page.validate_start()


@when(u'clicks on Inprogress button')
def step_impl(context):
    context.home_page.click_Inprogress()


@then(u'user should able to see Resume button')
def step_impl(context):
    context.home_page.validate_resume()


@when(u'clicks on Completed button')
def step_impl(context):
    context.home_page.click_Completed()


@then(u'user should able to see Enter Path button')
def step_impl(context):
    context.home_page.validate_enterpath()


@when(u'clicks on Recently Started button')
def step_impl(context):
    context.home_page.click_recentlyAccessed()


@when(u'user clicks on A-Z button in homepage')
def step_impl(context):
    context.home_page.click_AZtext()


@when(u'clicks on Z-A button')
def step_impl(context):
    context.home_page.click_ZAtext()


