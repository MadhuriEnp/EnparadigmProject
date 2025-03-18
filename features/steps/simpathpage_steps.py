from behave import given, then, when
from pages.simpath_page import SimPage



@when(u'user clicks on sim1 resume button')
def step_impl(context):
    context.SimPage = SimPage(context.page, context.browser_context)
    context.SimPage.clickOnSim1ResumeBtn()


@then(u'user should able to see the sim1 heading')
def step_impl(context):
    context.SimPage.validateSim1Heading()


@when(u'user clicks on resume button in simulation1 page')
def step_impl(context):
    context.SimPage.clickOnResumeBtn()


@then(u'user should able to see the A Missed Promotion')
def step_impl(context):
    context.SimPage.validateMissedPromotionText()


@when(u'user clicks on sim2 resume button')
def step_impl(context):
    context.SimPage.clickOnSim2StartBtn()


@then(u'user should able to see the sim2 heading')
def step_impl(context):
    context.SimPage.validateSim2Heading()


@when(u'user selects cohort and company for creating learner user')
def step_impl(context):
    context.SimPage = SimPage(context.page, context.browser_context)
    context.SimPage.selectsCompanyCohortTestMadhuri()

@when(u'user enters valid details for the learning profile')
def step_impl(context):
    context.SimPage = SimPage(context.page, context.browser_context)
    context.SimPage.enterUserDetails()


@when(u'user verifies the details of user name and email')
def step_impl(context):
    context.SimPage.verifiesUserDetails()


@when(u'user clicks on talenthub button and verifies the values in different pages like performance, Action Item, Progress, Social,Resources, Achievements')
def step_impl(context):
    context.SimPage.verifiesAllValuesBeforeCourseCompletion()


@when(u'user clicks on learningPath and selcts the course and started the course')
def step_impl(context):
    context.SimPage.clciksLearningPathStartedCourse()

@then(u'user should able to see home page of learner profile')
def step_impl(context):
    context.SimPage.clicksOnaccept()
    context.array_of_strings = [context.config_data.get('testdata', 'String1'),
                                context.config_data.get('testdata', 'String2'),
                                context.config_data.get('testdata', 'String3'),
                                context.config_data.get('testdata', 'String4'),
                                context.config_data.get('testdata', 'String5'),
                                context.config_data.get('testdata', 'String6'),
                                context.config_data.get('testdata', 'String7'),
                                context.config_data.get('testdata', 'String8')]
    context.dynamic_usernames = context.SimPage.en_getDynamicUsername()
    print("DynamicUsername is : ", context.dynamic_usernames)
    expected_messages = [pattern.replace("{username}", context.dynamic_usernames) for pattern in
                         context.array_of_strings]
    actual_message = context.SimPage.en_homepagevalidation()
    print("Expected messages:", expected_messages)
    print("Actual message:", actual_message)
    assert actual_message in expected_messages, f"Expected message to be one of {expected_messages} but got '{actual_message}'"
    context.elements_count = context.SimPage.validateclass()
    print(f"Number of elements: {context.elements_count}")

@when(u'user did whatever he likes')
def step_impl(context):
    context.SimPage = SimPage(context.page, context.browser_context)
    context.SimPage.userdoeswhatever()

@then(u'user goes to another url')
def step_impl(context):
    context.SimPage = SimPage(context.page, context.browser_context)
    context.SimPage.goingToPage2()








