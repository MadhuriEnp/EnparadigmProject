from textwrap import fill
import sys
import os

# Add the project root directory to the sys.path
# import sys
# sys.path.append(r'/behaveProject/FUDTGameType')
from behave import given, then, when


from pages.UDT_Gametype_page import UDTGametypePage


@when(u'user searches for already created universal DT module')
def step_impl(context):
    context.UDTgametype = UDTGametypePage(context.page, context.browser_context)
    context.UDTgametype.searchesForAlreadyCreatedUDTmodDel()

@then(u'user should able to see the search outcome')
def step_impl(context):
    context.UDTgametype.ableToSeeSearchedModuleOutcome()


@when(u'user clicks on play button')
def step_impl(context):
    context.UDTgametype.clicksOnPlayButton()


@when(u'user clicks on play button and plays it from the user profile')
def step_impl(context):
    context.UDTgametype.clicksOnPlayBtnAndPlayUdtFromUserPro()

@when(u'user fill the module details in the step one and clicks on save and next in the Universal DT Gametype')
def step_impl(context):
    context.UDTgametype = UDTGametypePage(context.page, context.browser_context)
    context.UDTgametype.entersModuleStepOneUdt()

@when(u'user fills parameter settings in module steup in udt module')
def step_impl(context):
    context.UDTgametype.fillingParameterSettings1()



@when(u'user fill the details in step three and verify step3 and step2 parameters UDT')
def step_impl(context):
    context.UDTgametype.verifyParametersinStep2AndStep3ModuleContent()
@when(u'user fill the details in step three clicks on pubhish it for testing for creating UDT Gametype')
def step_impl(context):
    context.UDTgametype.fillingStepThreeUdtGametypedel()

@when(u'user clicks on modules and searchs for the just created udt module and published it  and plays it in simstudio user profile')
def step_impl(context):
    context.UDTgametype.searchesNewlyCreatedModAndPlaysit()

@when(u'user opts the different options and see the report')
def step_impl(context):
    context.UDTgametype.optsDifOptions()

@when(u'user starts the play the game')
def step_impl(context):
    context.UDTgametype.startsPlayGame()

@then(u'user should able to see enabled all three lifeline options')
def step_impl(context):
    context.UDTgametype.ableToSeeEnabledAllThreeLifelineOptions()

@then(u'user should able to see the text when hovering on the lifelines')
def step_impl(context):
    context.UDTgametype.hoveringTextonOptions()

@when(u'user clicks on preditcion button')
def step_impl(context):
    context.UDTgametype.clicksOnPredictionBtn()
# kkkkkkkkkkkkkkk

@then(u'user should able to see a prediction message appearing')
def step_impl(context):
    context.UDTgametype.predictionMesgAppearing()


@when(u'user clicks on any option of the choices')
def step_impl(context):
    context.UDTgametype.clicksAnyOptionOfChoices()

@then(u'user should able to prediction text on the option which we clicked')
def step_impl(context):
    context.UDTgametype.predictionTextOverOption()

@then(u'user should able to see disabled all three lifeline option')
def step_impl(context):
    context.UDTgametype.allThreeOptionsDisabled()

@when(u'user clicks on submit button')
def step_impl(context):
    context.UDTgametype.clicksSubmitBtn()

@then(u'user should able to see disabled prediction button and enabled clarity and popularity button in step 2')
def step_impl(context):
    context.UDTgametype.disabledPredEnabledClaPopStep2()

@then(u'user should be to see prediction text over the option')
def step_impl(context):
    context.UDTgametype.predictionTextOverOption()


@when(u'user clicks on clarity button')
def step_impl(context):
    context.UDTgametype.clicksClarityBtn()


@then(u'user should able to see a clarity message appearing')
def step_impl(context):
    context.UDTgametype.clarityMsgAppearing()

@then(u'user should able to see enabled clarity button and disabled prediction and popularity button')
def step_impl(context):
    context.UDTgametype.enabledClarityDisabledPredPop()

@when(u'user clicks on any option and clicks on submit button')
def step_impl(context):
    context.UDTgametype.clickOptSubmitBtn()

@then(u'user should able to see enabled popularity button and disabled prediction and clarity button in step 3')
def step_impl(context):
    context.UDTgametype.enabledPopDisPredClar()

@when(u'user clicks on popularity button')
def step_impl(context):
    context.UDTgametype.clicksOnPopBtn()

@then(u'user should able to be popularity icon over the options')
def step_impl(context):
    context.UDTgametype.popIconsOverOptAppearing()

@when(u'user clicks on any option in step 3 and submit button')
def step_impl(context):
    context.UDTgametype.clicksOptSubmitBtnStep3()

@then(u'user should able to see disabled all three lifeline option in step 4')
def step_impl(context):
    context.UDTgametype.diabledThreeLifelinesStep4()

@when(u'user clicks on info icon on the right top corner')
def step_impl(context):
    context.UDTgametype.clicksInfoIconRightTopCorner()

@then(u'user should able to be see udt scenario name and udt scenario description')
def step_impl(context):
    context.UDTgametype.udtSceNameAndDesc()

@when(u'user closes that popup and clicks on any option in the step 4')
def step_impl(context):
    context.UDTgametype.closesPopupClicksAnyOptStep4()

@then(u'user should able to see disabled all three lifeline option in step 5')
def step_impl(context):
    context.UDTgametype.diabledThreeLifelinesStep4()

@when(u'user clicks on any option and submit button in step 5')
def step_impl(context):
    context.UDTgametype.clicksAnyOptSubBtn()

@then(u'user clicks on next buttons and able to end text')
def step_impl(context):
    context.UDTgametype.clicksNextBtnAbleToSeeEndTxt()

# ffff

@then(u'user verifies the lifeline functionality with all features')
def step_impl(context):
    context.UDTgametype.verifiesLifelineFunctionality()

@when(u'user fill the details in step three clicks on pubhish it for testing for creating UDT Gametype with enabling debrief video')
def step_impl(context):
    context.UDTgametype.entersModuleStepThreeUdtDebriefVideo()

@when(u'user clicks on modules and searchs for the just created udt module with debrief video and published it  and plays it in simstudio user profile')
def step_impl(context):
    context.UDTgametype.searchesAndPlaysNewlyCreatedUdtDebriefVideo14()

@when(u'user selects cohort and company for udt')
def step_impl(context):
    context.UDTgametype.selectsUDTCohrtComp()


@when(u'user enters valid details for udt')
def step_impl(context):
    context.UDTgametype.userDetailsUdt()


@when(u'user verifies the details of user name and email for udt')
def step_impl(context):
    context.UDTgametype.verifiesUser()


@then(u'user clicks on MagicLink and clicks on copy magic Link and plays the udt game')
def step_impl(context):
    context.UDTgametype.clicksMagicLinkCopiesPlaysUdtGame()

@when(u'user clicks on modules and searchs for the just created udt module and published it for udt')
def step_impl(context):
    context.UDTgametype.clicksOnmodulesPubhishedUdt(context.config_data.get('Admin', 'admin_username'),context.config_data.get('Admin', 'admin_password'))


@when(u'user clicks on path management, create path and clicks on static and selects Path for udt module')
def step_impl(context):
    context.UDTgametype.clicksOnPathManagementAndfillDetailsUDTModule()


@when(u'user fills the module details on step one')
def step_impl(context):
    context.UDTgametype = UDTGametypePage(context.page, context.browser_context)
    context.UDTgametype.entersModuleStepOneToggleUdt()

@when(u'user enables toggles for Disable Reports,Simulation,Disable Rewatch video')
def step_impl(context):
        context.UDTgametype.enableDisableReportsSimulationTogglesUdt()

@when(u'clicks on save and next in the Universal DT Gametype')
def step_impl(context):
        context.UDTgametype.entersModuleStepOneClickSaveNextUdt()

@when(u'user clicks on modules and searchs for the just created udt module and published it and plays it in simstudio user profile')
def step_impl(context):
        context.UDTgametype.searchesAndPlaysNewlyCreatedUdtDebriefVideo()

@then(u'user should be able to see the Reports and Rewatch video disabled while playing')
def step_impl(context):
    context.UDTgametype.validateTogglesDisabledReportsUDT()

    #UDT text fields matching display

@when(u'user clicks on Modules search bar and enters UDT module name')
def step_impl(context):
    context.UDTgametype = UDTGametypePage(context.page, context.browser_context)

    context.UDTgametype.searchModuleUDT()


@then(u'user should able to see the searched UDT module in Modules section')
def step_impl(context):
    context.UDTgametype.ableToSeeOutcomeUDT()


@when(u'user clicks on play and verifies if all the fileds are accurately displayed in the simstudio user profile')
def step_impl(context):
    context.UDTgametype.verifiesUDTModuleFieldsPropelyDisplayedInUserProperly()

@when(u'user clicks on path management, create path and clicks on static and selects Path for UDT\'s-1@ UDT\'s-2 module')
def step_impl(context):
        context.UDTgametype.clicksOnPathManagementAndSearchModuleUDT()

#@then(u'user should able to see the searched UDT module in Modules section')
#def step_impl(context):
  #      context.UDTgametype.fillingPathDetailsUDT()


@then(u'user should able to see edit module details page and verifies if UDT module details are properly displayed')
def step_impl(context):
    context.UDTgametype.verifiesModuleDetailsProperlyDisplayedUDT()

@when(u'user fills all the UDT path details and click on save and next button')
def step_impl(context):
    context.simStudioAdmin.fillingPathDetailsUDT()


@when(u'user clicks on edit icon in simstudio user profile')
def step_impl(context):
    context.UDTgametype.clickEditIconOnSelectedModule()


@then(u'user should be directed to Module Content Page')
def step_impl(context):
    context.simStudioAdmin.moduleContentPage()

@when(u'user clicks on delete icon on Module content Page and clicks on \'Yes delete it!\'')
def step_impl(context):
    context.UDTgametype.clickDelteIconOnModuleContentPage()

@then(u'user should not be able to see the content pages in ModuleContent page')
def step_impl(context):
    context.UDTgametype.verifyDeletedModuleNotFoundInModuleContent()

@then(u'user should not be able to see the searched UDT module in Modules section')
def step_impl(context):
    context.UDTgametype.verifyDeletedModuleNotFoundInModules()

@when(u'user enables toggle for Version/Variant')
def step_impl(context):
    context.UDTgametype.enterDetailsVersionVariantToggleInModuleCreation()

@then(u'user should see the Module Name same as selected parent module name along with version number')
def step_impl(context):
    context.UDTgametype.fillingParameterSettings1del()
    context.UDTgametype.verifyVersionVariantToggleInModuleCreation()

@when(u'user clicks on edit icon on Module content Page')
def step_impl(context):
    context.UDTgametype.clickEditIconOnModuleContentPage()


@when(u'user edits the Heading , Sub Heading , Content on Module Content Page and clicks on Save and Next')
def step_impl(context):
    context.UDTgametype = UDTGametypePage(context.page, context.browser_context)
    context.UDTgametype.editHeadingSubHeadingContentOnModuleContentPage()


@when(u'user clicks on Modules search bar and enters the same UDT module name and plays it')
def step_impl(context):
    context.UDTgametype = UDTGametypePage(context.page, context.browser_context)
    context.UDTgametype.searchModuleUDTdel()
    #context.UDTgametype.clicksOnPlayBtnAndPlayUdtEditsimstudio()


@then(u'user should be able to see the same edited fields on this page in SimStudio profile')
def step_impl(context):
    context.UDTgametype.verifyHeadingSubContentOnPlaySimStudioprofileUDT()

@when(u'user clicks on Step2 Module Setup and adds one more input and output parameter clicks on save&next')
def step_impl(context):
    context.UDTgametype.clickOnModuleSetup()
    context.UDTgametype.fillingParameterSettings12()
    context.UDTgametype.fillingParameterSettings2()

@when(u'user clicks on next buttons')
def step_impl(context):
    context.UDTgametype.clickNextButtonUDTBeforePlayYT()
@then(u'user should be able to see the input and output parameters on check your focus page same as those entered in Module Setup')
def step_impl(context):
    context.UDTgametype.verifyInputParamsOnCheckYourFocusPage()
@then(u'user clicks on step3 Module Content page and verify the given parameters in ModuleSetup Page')
def step_impl(context):
    #context.UDTgametype.verifyInputOutputParamsOnModuleContentPage()
    #context.UDTgametype.searchModuleUDTEdit()
    #context.UDTgametype.clicksOnPlayButton()
    context.UDTgametype.validateChkboxQstnOnReflectPage()

@when(u'user should be able to see the parameters in step3 ModuleContent same as entered in step2 ModuleSetup')
def step_impl(context):
    context.UDTgametype.verifyInputOutputParamsOnModuleContentPage()

@when(u'user fills the details in step3 validates output parameters of UDT Gametype with enabling debrief video from step2 and step3 and clicks on publish')
def step_impl(context):
    context.UDTgametype.entersModuleStepThreeUdtDebriefVideoConfigFileAndValidate()

@when(u'user clicks on Modules search bar and enters UDT module name with debrief video on')
def step_impl(context):
    context.UDTgametype.searchModuleUDTwithdebriefEnabled()


@then(u'user seacrhed the module in Modules tab and validates input parameters and debrief titles with debrief enabled on simstudio Play Page')
def step_impl(context):
     context.UDTgametype.verifyInputParamsChkboxQuestionsOnSimstudioPlayPage()
     context.UDTgametype.verifyInputParamsOnCheckYourFocusPage()
     context.UDTgametype.canvas()

@then(u'user should be able to see the selected narrator options in the simstudio complete deepdive page')
def step_impl(context):
     context.UDTgametype.verifyNarratorOptionsOnDeepdivePage()