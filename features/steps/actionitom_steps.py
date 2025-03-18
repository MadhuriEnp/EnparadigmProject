from behave import given, then, when
from pages.actionItem_page import ActionItemPage


@when(u'user clicks on Progress button')
def step_impl(context):
    context.ActionItemPage = ActionItemPage(context.page, context.browser_context)
    context.ActionItemPage.clickOnProgressBtn()


@then(u'user should able to see warning popup')
def step_impl(context):
    context.ActionItemPage.validateProgresstxt()


@when(u'user clicks on Social button')
def step_impl(context):
    context.ActionItemPage.clickOnSocialBtn()


@then(u'user should able to see Active Members Heading')
def step_impl(context):
    context.ActionItemPage.validaactiveMemberstxt()


@when(u'user clicks on Resources button')
def step_impl(context):
    context.ActionItemPage.clickOnResourcesBtn()


@then(u'user should able to see Assessment Reports Heading')
def step_impl(context):
    context.ActionItemPage.validateAssessmentReportstxt()


@when(u'user clicks on Achievements button')
def step_impl(context):
    context.ActionItemPage.clickOnAchievementsBtn()


@then(u'user should able to see Certificates Heading')
def step_impl(context):
    context.ActionItemPage.validateCertificatetxt()


@when(u'user clicks on notification button')
def step_impl(context):
    context.ActionItemPage.clickOnNotificationsBtn()


@then(u'user should able to see your pending items page')
def step_impl(context):
    context.ActionItemPage.validatePenidngItemstxt()


@when(u'user clicks on profile dropdown')
def step_impl(context):
    context.ActionItemPage.clickOnProfileDrpDwn()


@then(u'user should able to see logout button')
def step_impl(context):
    context.ActionItemPage.validateLogoutbtn()


@when(u'user clicks on logout button')
def step_impl(context):
    context.ActionItemPage.clickOnLogoutBtn()


@then(u'user should able to see login page')
def step_impl(context):
    context.ActionItemPage.clickWelcomeTxt()
