from behave import given, then, when
from pages.catalyxAdminLogin_page import CatalyxAdminPage

from pages.UDT_Gametype_page import UDTGametypePage


@given(u'User opens admin login page')
def step_impl(context):
    context.catalyxAdmin = CatalyxAdminPage(context.page, context.browser_context)
    context.UDTgametype = UDTGametypePage(context.page, context.browser_context)
    context.catalyxAdmin.navigateAdminUrl(context.config_data.get('Admin', 'admin_en_url'))


@when(u'user clicks on sign in with google button and enters valid user credentials')
def step_impl(context):
    context.catalyxAdmin.clickOnSignInWithGoogle(context.config_data.get('Admin', 'admin_username'),
                                                 context.config_data.get('Admin', 'admin_password'))


@then(u'user should able to see catalyx admin homepage')
def step_impl(context):
    context.catalyxAdmin.validateAdminHome()


@when(u'user enters company details and clicks on crete company')
def step_impl(context):
    context.catalyxAdmin.createcomapny(context.config_data.get('Admin', 'noOfLicences'))


@then(u'user should able to see successpopup')
def step_impl(context):
    context.catalyxAdmin.validatesuccessmsg()


@when(u'user clicks on cohort management')
def step_impl(context):
    context.catalyxAdmin.clickOnCohortManagement()


@when(u'user clicks on create catalyx cohort and enters valida details')
def step_impl(context):
    context.catalyxAdmin.clickOncreateCatalyx(context.config_data.get('Admin', 'hrname'),
                                              context.config_data.get('Admin', 'hremail'))


@then(u'user should able to see of cohortsuccesspopup')
def step_impl(context):
    context.catalyxAdmin.validatecreatecohortsuccessmsg()


@when(u'user clicks on cohort management and create user')
def step_impl(context):
    context.catalyxAdmin.clickOncreateuser()


@when(u'user selects cohort and company')
def step_impl(context):
    context.catalyxAdmin.selectCompany()


@when(u'user enters valid details')
def step_impl(context):
    context.catalyxAdmin.enterUserDetails(context.config_data.get('Admin', 'hrname'),
                                          context.config_data.get('Admin', 'hremail'),
                                          context.config_data.get('Admin', 'role'))


@then(u'user should able to see success popup of user creation')
def step_impl(context):
    context.catalyxAdmin.validatesuccessCreateUser()



@when(u'user enters the empty details for "{compName}" , "{domainName}" and "{selIndus}" for the creating the company')
def step_impl(context, compName, domainName, selIndus ):
    context.catalyxAdmin.emptyParametersCreatingCompany(compName, domainName, selIndus)


@then(u'user should able to see respective error messsages for creating company')
def step_impl(context):
    context.catalyxAdmin.respectiveErrorMessagesForCreativeComp()



@when(u'user clicks on create deal')
def step_impl(context):
    context.catalyxAdmin.clickOnCreateDeal()


@when(u'user needs to enter all the details in that particular page')
def step_impl(context):
    context.catalyxAdmin.enterDealDetails()


@when(u'user enters the empty details for "{dealName}", "{selComp}", "{selSalesOwner}", "{selDeliOwner}" for the creating the deal')
def step_impl(context, dealName, selComp, selSalesOwner, selDeliOwner):
    context.catalyxAdmin.emptyingDetailsOfCreatingDeal(dealName, selComp, selSalesOwner, selDeliOwner)


@then(u'user should able to see respective error messsages for creating deal')
def step_impl(context):
    context.catalyxAdmin.respectiveErrorMessagesForCreatingDeal()


@then(u'user should able to see success popup')
def step_impl(context):
    context.catalyxAdmin.validateSuccessCreateDeal()


@when(u'user clicks on Post Rollout')
def step_impl(context):
    context.catalyxAdmin.clickOnPOstRollOut()


@when(u'user clicks on Usermanagement')
def step_impl(context):
    context.catalyxAdmin.clickOnUserManagement()


@when(u'user enters compay and cohort name in respective fields')
def step_impl(context):
    context.catalyxAdmin.enterValidDetailsIncompanyAndCohortInusermanagement()


@then(u'user clicks on MagicLink and clicks on copy magic Link')
def step_impl(context):
    context.catalyxAdmin.clickOnmagicLink()


@then(u'user should be in the signin page')
def step_impl(context):
    context.catalyxAdmin.validateinvalidusernamemsg()


@when(u'user enters the invalid "{username}" and clicks on continue button')
def step_impl(context, username):
    context.catalyxAdmin.invalidusername(username)


@when(u'user enters the user name and clicks on continue button')
def step_impl(context):
    context.catalyxAdmin.en_enter_username(context.config_data.get('Admin', 'admin_username'))


@when(u'user enters valid username and invalid "{password}" and clicks on login button')
def step_impl(context, password):
    context.catalyxAdmin.invalidpassword(context.config_data.get('Admin', 'admin_username'),password)


@then(u'Then user should able to see login page')
def step_impl(context):
    context.catalyxAdmin.validateAdminHome()

@when(u'user clicks on create catalyx cohort and enters empty details for "{cohortName}", "{company}", "{deal}", "{hrname}", "{hremail}", "{startDate}", "{deadline}", "{deliveryOwner}", "{learningPath}"')
def step_impl(context, cohortName, company, deal, hrname, hremail, startDate, deadline, deliveryOwner, learningPath):
    context.catalyxAdmin.entersEmptyParametersCohort(cohortName, company, deal, hrname, hremail, startDate, deadline, deliveryOwner, learningPath)

@then(u'user should able to see respective error message for creating cohort')
def step_impl(context):
    context.catalyxAdmin.respectiveErrorMessagesForCreatingCohort()


@when(u'user clicks on create catalyx cohort and enters the invalid hr email "{InvalidEmail}"')
def step_impl(context, InvalidEmail):
    context.catalyxAdmin.entersInvalidEmailCreatCohort(InvalidEmail)


@when(u'user enters valid details with empty parameters for "{name}" and "{username}"')
def step_impl(context, name, username):
    context.catalyxAdmin.creatingUserEmptyParameters(name, username)


@then(u'user should able to see respective error message for creating user')
def step_impl(context):
    context.catalyxAdmin.respectiveErrorMessagesForCreatingUser()





