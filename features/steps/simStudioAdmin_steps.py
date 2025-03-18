from behave import given, then, when
from pages.simStudioAdmin_pages import simStudioAdminPage

from pages.AIDiagnosticGametype_page import AIDiagnosticGametypePage


@given(u'user is in simstudio admin login page')
def step_impl(context):
    context.simStudioAdmin = simStudioAdminPage(context.page, context.browser_context)
    context.simStudioAdmin.navigate_to_url(context.config_data.get('Admin', 'simStudio_admin'))


@when(u'user clicks on sign in with google button and enters valid credentials')
def step_impl(context):
    context.simStudioAdmin.sign_in_with_google(context.config_data.get('Admin', "admin_username"),context.config_data.get('Admin', "admin_password"))


@then(u'user should able to see simstudio dashboard page')
def step_impl(context):
    context.simStudioAdmin.validateSimstudioAdminDashboard()


@when(u'user clicks on search button and enters details')
def step_impl(context):
    context.simStudioAdmin.clicksOnSearch()


@when(u'user clicks on selected AI coach play button')
def step_impl(context):
    context.AICoachName = context.simStudioAdmin.clickOnPlaybutton()


@then(u'user should able to see selected aicoach heading page')
def step_impl(context):
    context.simStudioAdmin.validateAiCoachPage()


@when(u'user clicks on next button and play\'s the simulation1,simulation2 and verifies all button in scenarios page')
def step_impl(context):
    context.simStudioAdmin = simStudioAdminPage(context.page, context.browser_context)
    context.simStudioAdmin.clicksOnNext()


@then(u'user should able to see completed round1 heading')
def step_impl(context):
    context.simStudioAdmin.validateRoundCompleted()



@when(u'user clicks on next button and play\'s the simulation1,simulation2 and does not enters the scenario1 reposnse')
def step_impl(context):
    context.simStudioAdmin.entersEmptyScenario1Response()


@when(u'user clicks on next button and play\'s the simulation1,simulation2 and does not enters the scenario2 response')
def step_impl(context):
    context.simStudioAdmin.entersEmptyScenario2Response()


@then(u'user should able to see submit button is still disabled')
def step_impl(context):
    context.simStudioAdmin.submitButtonDisabled()


@when(u'user clicks on next button and play\'s the simulation1,simulation2 and enters random "{response1}" in scenario1 response')
def step_impl(context,response1):
    context.simStudioAdmin.entersRandomScenario1Response(response1)


@when(u'user clicks on next button and play\'s the simulation1,simulation2 and enters random "{response2}" in scenario2 response')
def step_impl(context,response2):
    context.simStudioAdmin.entersRandomScenario2Response(response2)



@then(u'user should able to validate the score')
def step_impl(context):
    context.simStudioAdmin.validateScore()


@when(u'user fetches the username')
def step_impl(context):
    context.simStudioAdmin.fetchingUsername()

@when(u'user clicks on create module')
def step_impl(context):
    context.simStudioAdmin.clicksOnCreateModule()


@then(u'user should able to see create module page')
def step_impl(context):
    context.simStudioAdmin.createModulePage()


@when(u'user fill the module details in the step one and clicks on save and next')
def step_impl(context):
    context.simStudioAdmin.fillingStepOneDetails()

@then(u'user should able to see module setup step two')
def step_impl(context):
    context.simStudioAdmin.stepTwoPage()


@when(u'user fill the module details in the step two and click on save and next')
def step_impl(context):
    context.simStudioAdmin.fillingStepTwoDetails()

@then(u'user should able to see module content')
def step_impl(context):
    context.simStudioAdmin.moduleContentPage()


@when(u'user fill the details in step three clicks on pubhish it for testing')
def step_impl(context):
    context.simStudioAdmin.fillingDetailsStepThreecreatecatalyx(context.config_data.get('Admin', "moduleDescription"),
                                                   context.config_data.get('Admin', "gameTypeHeading"),
                                                   context.config_data.get('Admin', "gameTypeDesc"),
                                                   context.config_data.get('Admin', "gameTypeSceQues"),
                                                   context.config_data.get('Admin', "gameTypeSceHint"),
                                                   context.config_data.get('Admin', "gameTypeIdealResponse"))


@then(u'user should able to see fourth step report')
def step_impl(context):
    context.simStudioAdmin.fourthStepPage()

@when(u'fill details in step four and clicks on save button')
def step_impl(context):
    context.simStudioAdmin.fillingStepFourDetails()


@then(u'user should able to see the text data saved successfully')
def step_impl(context):
    context.simStudioAdmin.dataSaveSuccessfullyText()

@when(u'user clicks on modules and searchs for the just created module and published it')
def step_impl(context):
    context.simStudioAdmin.clickOnModulePublished()


@then(u'user should able to see published succesfully')
def step_impl(context):
    context.AIDiagnosticGametypePage = AIDiagnosticGametypePage(context.page, context.browser_context)
    context.simStudioAdmin.publishedSucfully()

@when(u'user clicks on sign in with google button and enters valid user credentials in the already signedin account')
def step_impl(context):
    context.simStudioAdmin.signInWithGoogleAlreadySignedIn(context.config_data.get('Admin', 'admin_username'),
                                                 context.config_data.get('Admin', 'admin_password'))

@when(u'user clicks on path management, create path and clicks on static and selects Path')
def step_impl(context):
    context.simStudioAdmin.clicksOnPathManagementAndfillDetails()


@then(u'user should able to see edit path details page')
def step_impl(context):
    context.simStudioAdmin.editPathDetailsPage()

@when(u'user fills all the path details and click on save and next button')
def step_impl(context):
    context.simStudioAdmin.fillingPathDetails()

@then(u'user should able to see edit module details page')
def step_impl(context):
    context.simStudioAdmin.editModuleDetailsPage()

@when(u'user fills all the module details and click on save and next button')
def step_impl(context):
    context.simStudioAdmin.fillingModuleDetails(context.config_data.get('Admin',"moduleHeading"),
                                                 context.config_data.get('Admin',"moduleDescription"))

@then(u'user should able to see add feedback questions page')
def step_impl(context):
    context.simStudioAdmin.feedbackQuestionPage()

@when(u'user selects feedback questions and clicks on publish button')
def step_impl(context):
    context.simStudioAdmin.selectsFeedbackQuestion()

@then(u'user should able to see manage path sage and verifies the path')
def step_impl(context):
    context.simStudioAdmin.managingPath()

@when(u'user clicks on cohort management1')
def step_impl(context):
    context.simStudioAdmin.clicksOnCohortManagement()

@when(u'user enters the cohort details and selects the learning path')
def step_impl(context):
    context.simStudioAdmin.enterDetailsAndSelectPath()


@then(u'user should able to see of cohortsuccesspopup1')
def step_impl(context):
    context.simStudioAdmin.cohortsuccesspopup1()

@when(u'user clicks on content and gametype')
def step_impl(context):
    context.simStudioAdmin.clickOnGameType()


@then(u'user should able to verify all the fields and elements')
def step_impl(context):
    context.simStudioAdmin.verifyAllTheFieldsinTextGamePlay()


@then(u'user should able to verify all the fields and elements in the video')
def step_impl(context):
    context.simStudioAdmin.verifyAllTheFieldsinVideoGamePlay()


@when(u'user fill the details for video game type in step three clicks on pubhish it for testing')
def step_impl(context):
    # Hardcoded file path or obtained from a config
    file_path1 = r"C:\Users\hp\PycharmProjects\Enparadigm\Enparadigm\behaveProject\Upload\Thumnail\Thumbnail.png"
    file_path2 = r"C:\Users\hp\PycharmProjects\Enparadigm\Enparadigm\behaveProject\Upload\Video\VideoRefName.mp4"
    context.simStudioAdmin.GameTypeVideo(file_path1, file_path2, context.config_data.get('Admin', "moduleDescription"),
                                                   context.config_data.get('Admin', "gameTypeHeading"),
                                                   context.config_data.get('Admin', "gameTypeDesc"),
                                                   context.config_data.get('Admin', "gameTypeSceQues"),
                                                   context.config_data.get('Admin', "gameTypeSceHint"),
                                                   context.config_data.get('Admin', "gameTypeIdealResponse"))

@when(u'user fill the module details in the step one with empty details like "{ModName}", "{ModHeading}", "{Description}", "{NeededTime}", "{gameType}" and "{colorPalette}" and clicks on save and next')
def step_impl(context, ModName, ModHeading, Description, NeededTime, gameType, colorPalette ):
    context.simStudioAdmin.emptyparametersForStep1creatingmodule(ModName, ModHeading, Description, NeededTime, gameType, colorPalette)

@then(u'user should able to see respective error message in step3')
def step_impl(context):
    context.simStudioAdmin.verifyingErrorMessagesstep3()
@then(u'user should able to see respective error message for creating module')
def step_impl(context):
    context.simStudioAdmin.verifyingErrorMessagesCreatingMofdule()
@when(u'user clicks on create user')
def step_impl(context):
    context.simStudioAdmin.clicksOnCreateUser()

@then(u'user should able to see home page of learner profile1')
def step_impl(context):
    context.simStudioAdmin.clickOnAcceptButton()

@when(u'user clicks on start and starts plays the game')
def step_impl(context):
    context.simStudioAdmin.clicksOnStartandPlaysGame()

@when(u'user clicks on save and next button in creating module')
def step_impl(context):
    context.simStudioAdmin.clicksSaveNextBtn()


@when(u'user clicks on publish module for testing button in creating module')
def step_impl(context):
    context.simStudioAdmin.clicksOnPublishButton()

@when(u'user enters the empty values like "{RefeName}", "{Heading}", "{Context}" and "{ImageUrl}"')
def step_impl(context,RefeName, Heading, Context, ImageUrl):
    context.simStudioAdmin.emptyParametersStep3Content(RefeName, Heading, Context, ImageUrl)

@when(u'user selects cohort and company for creating learner user in gametype')
def step_impl(context):
    context.simStudioAdmin.selectingCompanyNewCreatedCohort()

@then(u'user clicks on MagicLink and clicks on copy magic Link1')
def step_impl(context):
    context.simStudioAdmin.clickOnmagicLink1()



