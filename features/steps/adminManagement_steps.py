from behave import given, then, when
from pages.adminManagement_page import AdminManagementPage


@given(u'User navigates to admin login page')
def step_impl(context):
    context.AdminManagementPage = AdminManagementPage(context.page, context.browser_context)
    context.AdminManagementPage.navigateAdminUrl(context.config_data.get('Admin', 'admin_en_url'))


@when(u'user clicks on signin with google button and enters valid user credentials')
def step_impl(context):
    context.AdminManagementPage.clickOnSignInWithGoogle(context.config_data.get('Admin', 'admin_username'),
                                                 context.config_data.get('Admin', 'admin_password'))


@then(u'user should able to see the catalyx admin homepage')
def step_impl(context):
    context.AdminManagementPage.validateAdminHome()


@when(u'user clicks on admin management')
def step_impl(context):
    context.AdminManagementPage.clickOnAdminManagement()


@when(u'user clicks on create admin')
def step_impl(context):
    context.AdminManagementPage.clickOnCreateAdmin()


@then(u'user should able to see the create admin')
def step_impl(context):
    context.AdminManagementPage.validateCreateAdminPage()


@when(u'user enters all the user details and clicks on create user button')
def step_impl(context):
    context.AdminManagementPage.enterAllAdminDetails()

@then(u'User should able to see the successfull message of creating user')
def step_impl(context):
    context.AdminManagementPage.validateSuccessMsgCreateAccount()


@when(u'user clicks on create client admin')
def step_impl(context):
    context.AdminManagementPage.clickOnCreateClientAdmin()


@then(u'user should able to see the create client admin')
def step_impl(context):
    context.AdminManagementPage.validateCreateClientAdminPage()


@when(u'user enters all the client admin user details and clicks on create button')
def step_impl(context):
    context.AdminManagementPage.enterAllClientAdminDetails()


@then(u'User should able to see the successfull message of creating client admin user')
def step_impl(context):
    context.AdminManagementPage.validateCreateClientAdminPage()


@when(u'user enters the user details like "{name}", "{username}", "{password}"  empty one at a time')
def step_impl(context, name, username, password):
    context.AdminManagementPage.emptyValuesCreatingAdmin(name, username, password)


@when(u'user enters the user details without selecting role')
def step_impl(context):
    context.AdminManagementPage.withoutSelectingRole()



@when(u'user enters the creating user details with "{invalidUsername}" invalid username')
def step_impl(context, invalidUsername):
    context.AdminManagementPage.entersInvalidUsername(invalidUsername)


@then(u'user able to see the respective error messages')
def step_impl(context):
    context.AdminManagementPage.respectiveErrorMessages()


# @when(u'user clicks on update admin')
# def step_impl(context):
#     context.AdminManagementPage.clicksUpdateAdmin()
#
#
# @then(u'user should able to see the update admin page')
# def step_impl(context):
#     context.AdminManagementPage.updateAdminPage()
#
#
# @when(u'user enters all the update admin user details and clicks on update admin button')
# def step_impl(context):
#
#
#
#
# @then(u'User should able to see the successfull message of updating admin user')
# def step_impl(context):



