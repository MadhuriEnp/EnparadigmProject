from behave import given, then, when

from pages.AIDiagnosticGametype_page import AIDiagnosticGametypePage


@when(u'user fills the atom setup details in atom set up step1b')
def step_impl(context):
    context.AIDiagnosticGametypePage.enter_Details_In_AtomSetUp()

@when(u'user fill the module details in the step one and clicks on save and next in the AI Diagnostic Gametype')
def step_impl(context):
    context.AIDiagnosticGametypePage = AIDiagnosticGametypePage(context.page, context.browser_context)
    context.AIDiagnosticGametypePage.filling_details_in_step1()

@when(u'user fill the details in step three clicks on pubhish it for testing for creating AI Diagnostic Gametype')
def step_impl(context):
    context.AIDiagnosticGametypePage.enter_details_in_third_step(context.config_data.get('Admin', "moduleDescription"))

@when(u'user enters the Ai diagnostics in the search bar and clicks on play button')
def step_impl(context):
    context.AIDiagnosticGametypePage = AIDiagnosticGametypePage(context.page, context.browser_context)
    context.AIDiagnosticGametypePage.enters_search_clicks_playbutton()

@when(u'user plays the AI diagnostic sim')
def step_impl(context):
    context.AIDiagnosticGametypePage.playsAIDiagnosticsssSimulation()

@when(u'user selects cohort and company for Ai diagnosticsss')
def step_impl(context):
    context.AIDiagnosticGametypePage = AIDiagnosticGametypePage(context.page, context.browser_context)
    context.AIDiagnosticGametypePage.selectsCohortandComForAIDia()


@when(u'user enters valid details for Ai diagnosticsss')
def step_impl(context):
    context.AIDiagnosticGametypePage.enterValidUserDetailsAIDia()

@when(u'user verifies the details of user name and email for aid')
def step_impl(context):
    context.AIDiagnosticGametypePage.verifiesNameAndEmailUser()


@then(u'user clicks on MagicLink and clicks on copy magic Link and plays the game')
def step_impl(context):
    context.AIDiagnosticGametypePage = AIDiagnosticGametypePage(context.page, context.browser_context)
    context.AIDiagnosticGametypePage.clickOnmagicLink2()

@when(u'user clicks on scenario bank and clicks on create scenario')
def step_impl(context):
    context.AIDiagnosticGametypePage = AIDiagnosticGametypePage(context.page, context.browser_context)
    context.AIDiagnosticGametypePage.clicksScenarioBankCreateScenario()


@when(u'user fills all the details in the text scenario for the creation')
def step_impl(context):
    context.AIDiagnosticGametypePage = AIDiagnosticGametypePage(context.page, context.browser_context)

    context.AIDiagnosticGametypePage.fillsTextScenarioBankCreate(
                                                   context.config_data.get('Admin', "gameTypeDesc"),
                                                   context.config_data.get('Admin', "gameTypeSceQues"),
                                                   context.config_data.get('Admin', "gameTypeSceHint"),
                                                   context.config_data.get('Admin', "gameTypeIdealResponse"))

@when(u'user fills all the details in the video scenario for the creation')
def step_impl(context):
    file_path1 = r"C:\NewEnp\Enparadigm\Enparadigm\Enparadigm\behaveProject\Upload\Thumnail\Thumbnail.png"
    file_path2 = r"C:\NewEnp\Enparadigm\Enparadigm\Enparadigm\behaveProject\Upload\Video\VideoRefName.mp4"
    context.AIDiagnosticGametypePage.fillsVideoScenarioBankCreate(file_path1, file_path2, context.config_data.get('Admin', "moduleDescription"),
                                                   context.config_data.get('Admin', "gameTypeHeading"),
                                                   context.config_data.get('Admin', "gameTypeDesc"),
                                                   context.config_data.get('Admin', "gameTypeSceQues"),
                                                   context.config_data.get('Admin', "gameTypeSceHint"),
                                                   context.config_data.get('Admin', "gameTypeIdealResponse"))

@when(u'user clicks on modules and searchs for the just created module and published it in AIDiagnostic and plays it')
def step_impl(context):
    context.AIDiagnosticGametypePage.searchesPubhished()

@when(u'user clicks on modules and searchs for the just created module and published it in Video AIDiagnostic and plays it in simstudio user profile')
def step_impl(context):
    context.AIDiagnosticGametypePage.serachesPlayVideoAISimUser()

@when(u'user enters module name in the search and clicks on publish')
def step_impl(context):
    context.AIDiagnosticGametypePage.moduleNameSearchesPublish()

@when(u'user clicks on path management, create path and clicks on static and selects Path1')
def step_impl(context):
    context.AIDiagnosticGametypePage.clicksOnPathManagementAndfillDetails1()

@then(u'user clicks on MagicLink and clicks on copy magic Link2 and plays the game')
def step_impl(context):
    context.AIDiagnosticGametypePage.clickOnmagicLink3()

@when(u'user clicks on cohort management and create user1')
def step_impl(context):
    context.AIDiagnosticGametypePage.clickOnCohortCreateUser()


@when('user fills empty values like "{SceHeading}", "{SceDescrip}", "{SceQuestion}", "{SceHint}", "{SceIdealResp}", "{MetaTags}", and "{Atoms}" in the text scenario for the creation')
def step_impl(context, SceHeading, SceDescrip, SceQuestion, SceHint, SceIdealResp, MetaTags, Atoms ):
    context.AIDiagnosticGametypePage.fillingEmptyValuesCreatingTextScenario(SceHeading, SceDescrip, SceQuestion, SceHint, SceIdealResp, MetaTags, Atoms)




@then(u'user should able to see the respective error messages for scenario creation')
def step_impl(context):
    context.AIDiagnosticGametypePage.validatingTextScenarioErrorMessages()

@when(u'user fills empty values like "{SceHeading}", "{SceDescrip}", "{VideoRefName}", "{Thumbnail}", "{Video}", "{SceQuestion}", "{SceHint}", "{SceIdealResp}", "{MetaTags}", and "{Atoms}" in the video scenario for the creation')
def step_impl(context, SceHeading, SceDescrip, VideoRefName, Thumbnail, Video, SceQuestion, SceHint, SceIdealResp, MetaTags, Atoms ):
    context.AIDiagnosticGametypePage.fillingEmptyValuesCreatingVideoScenario(SceHeading, SceDescrip, VideoRefName, Thumbnail, Video, SceQuestion, SceHint, SceIdealResp, MetaTags, Atoms )


@when(u'user clicks on scenario bank and clicks on search scenario text box')
def step_impl(context):
    context.AIDiagnosticGametypePage = AIDiagnosticGametypePage(context.page, context.browser_context)
    context.AIDiagnosticGametypePage.clicksOnSceClicksOnSearch()


@when(u'user enters {PossibleSearch} search input')
def step_impl(context, PossibleSearch):
    context.AIDiagnosticGametypePage.entersValidSearchInput(PossibleSearch)



@then(u'user should able to be see the search outcome')
def step_impl(context):
    context.AIDiagnosticGametypePage.ableToSeeSearchOutcome()

@when(u'user clicks on scenario bank and clicks on edit button')
def step_impl(context):
    context.AIDiagnosticGametypePage = AIDiagnosticGametypePage(context.page, context.browser_context)
    context.AIDiagnosticGametypePage.clicksSceBankEditBtn()


@when(u'user edit some for the scenario details')
def step_impl(context):
    context.AIDiagnosticGametypePage.editScenarioDetails()

@when(u'user enters non existing scenario')
def step_impl(context):
    context.AIDiagnosticGametypePage.entersNonExistingScenario()


@then(u'user should not able to be see the search outcome')
def step_impl(context):
    context.AIDiagnosticGametypePage.NotAbleToBeSeeSearch()


@when(u'user clears and fills empty values like "{SceHeading}", "{SceDescrip}", "{SceQuestion}", "{SceHint}", "{SceIdealResp}", "{MetaTags}", and "{Atoms}" in the text scenario for the creation')
def step_impl(context, SceHeading, SceDescrip, SceQuestion, SceHint, SceIdealResp, MetaTags, Atoms ):
    context.AIDiagnosticGametypePage.fillingEmptyValuesEditingTextScenario(SceHeading, SceDescrip, SceQuestion, SceHint, SceIdealResp, MetaTags, Atoms)

@when(u'user clicks on scenario bank and clicks on edit button1')
def step_impl(context):
    context.AIDiagnosticGametypePage = AIDiagnosticGametypePage(context.page, context.browser_context)
    context.AIDiagnosticGametypePage.clicksSceBnkEditBtn1()

@when(u'user searches for the newly created scenario and delete the scenario')
def step_impl(context):
    context.AIDiagnosticGametypePage.searchesSceDeleteSce()

@when(u'user clicks on search bar and enters module name')
def step_impl(context):
    context.AIDiagnosticGametypePage = AIDiagnosticGametypePage(context.page, context.browser_context)
    context.AIDiagnosticGametypePage.searchModule()

@then(u'user should able to see the searched module')
def step_impl(context):
    context.AIDiagnosticGametypePage.ableToSeeOutcome()

@when(u'user clicks on play and verifies all the fileds are sccureately displayed are not in the user profile')
def step_impl(context):
    context.AIDiagnosticGametypePage.verifiesModuleFieldsPropelyDisplayedInUserProperly()

@when(u'user clicks on path management, create path and clicks on static and selects Path for Sim\'s-1@ Sim\'s-2 module')
def step_impl(context):
    context.AIDiagnosticGametypePage = AIDiagnosticGametypePage(context.page, context.browser_context)
    context.AIDiagnosticGametypePage.clicksOnPathManagementAndSearchModule()

@then(u'user should able to see edit module details page and verifies whether module details are properly displayed are not')
def step_impl(context):
    context.AIDiagnosticGametypePage.verifiesModuleDetailsProperlyDisplayed()








