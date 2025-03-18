import os
from gc import isenabled
from time import sleep


from pages.base_page import BasePage
import configparser

from utils import randomUtils

from utils.shared_data import write_to_file
import pyperclip

from pages.WebActions import WebActions

config = configparser.ConfigParser()
config.read('config.ini')


class UDTGametypePage:
    def __init__(self, page, browser_context):
        self.actions = WebActions(page, browser_context)
        self.serchModule = "//input[@data-testid='search-modules']"
        #self.moduleTypeRow2 = "//table[@class='svelte-15iwbfd']/tbody/tr/td[2]"
        self.moduleTypeRow2 ="//td[@data-testid='dashboard-module-type-0']"
        self.moduleNameInput = "#module_name"
        self.moduleHeadInput = "#module_heading"
        self.moduleDescInput = "#module_description"
        self.moduleTimeDrpDwn = "#module_time_needed"
        self.gameTypeDrpdwn = "#select_game_type"
        self.colorPalatteDrpdwn = "#select_theme_type"
        self.saveNextModDetails="//button[@id='saveStep1_btn']"
        self.addSection ="//button[@data-testid='step3-add-section']"
        self.content = "//div[@data-testid='page-type-content']"
        self.contentPage1 = "//div[@data-testid='page-layout-0']"
        self.reference = "#reference_name"
        self.modRef = "//input[@data-testid='udt-reference-name']"
        self.modScenarioName = "//input[@data-testid='udt-scenario-name']"
        self.heading = "#heading"
        self.subheading = "#subheading"
        self.contenttt = "#tinymce"
        self.imageUrl = "#image_url"
        self.image = "//img[@data-testid='image-modal-0']"
        self.endpage = "//div[@data-testid='page-layout-6']"
        self.publishButton = "#publish_for_testing_btn"
        self.okbeforePublish="//button[@class='swal2-confirm swal2-styled swal2-default-outline']"
        self.okayBtn = "//button[normalize-space()='Ok']"
        self.fourthreportBtn = "//div[text()='Step 4: Report']"
        self.reportTxt = "//div[@id='create_module_step_4']/div[1]"
        self.proceedBtn = "//button[text()='Proceed']"
        self.sucTxt = "#swal2-html-container"
        self.saveNextBtn = "//button[@id='saveStep1_btn']"
        self.togVersionVariant="(//label[@class='slide-toggle-label unstyled flex items-center'])[1]"
        self.radioBtnVersion="(//input[@name='version_variant'])[1]"
        self.parentModulevv="//input[@id='parent-module']"
        self.versionNumber="//input[@id='version_number']"
        self.versionDesc="//textarea[@id='version_description']"
        self.toglDisableRewatch="(//label[@class='slide-toggle-label unstyled flex items-center'])[2]"
        self.toglDisableReports="(//label[@class='slide-toggle-label unstyled flex items-center'])[3]"
        self.toglSimulation="(//label[@class='slide-toggle-label unstyled flex items-center'])[4]"
        self.toglVoiceOver="(//label[@class='slide-toggle-label unstyled flex items-center'])[5]"
        self.saveNext = "//button[@id='content_layout_editor_save_btn']"
        self.saveNextEndPage = "//button[@data-testid='endp-page-save']"
        self.savenextModsetup   = "//button[@id='sib_gametype_save_btn']"
        self.inputPrameterName = "//input[@data-testid='parametere-name-0']"
        self.inputParameterDef = "//input[@data-testid='parameter-definition-0']"
        self.outputPrameterName = "//input[@data-testid='parametere-name-4']"
        self.outputPrameterName2="//input[@data-testid='parametere-name-5']"
        self.outputPrameterDef2="//input[@data-testid='parameter-definition-5']"
        self.outputPrameterDef = "//input[@data-testid='parameter-definition-4']"
        self.inputParaShowResTogBtn = "(//div[@data-testid='slide-toggle'])[2]"
        self.outputParaShowResTogBtn = "(//div[@data-testid='slide-toggle'])[11]"
        self.disableBackBtnTogBtn="(//label[@class='slide-toggle-label unstyled flex items-center'])[1]"
        self.gameType = "//div[@data-testid='page-type-gametype']"
        self.udtRefName = "//input[@data-testid='udt-reference-name']"
        self.UdtSceName = "//input[@data-testid='udt-scenario-name']"
        self.filePathElement = "//input[@class='input w-2/5 ml-4']"
        self.sliderQuestionInput1 = "//input[@placeholder='Slider Question']"
        self.sliderQuestionInput2 = "(//input[@placeholder='Slider Question'])[2]"
        self.enableCheckboxUdtTogBtn = "(// div[@ data-testid='slide-toggle'])[1]"
        self.checkBoxQuest = "//input[@placeholder='Checkbox Question']"
        self.opt1 = "(//input[@placeholder='Option 1'])[2]"
        self.opt2 = "(//input[@placeholder='Option 2'])[2]"
        self.opt3optional="(//input[@placeholder='Option 3'])[2]"
        self.modulesBtn = "//span[text()='Modules']"
        self.serchModule = "//input[@data-testid='search-modules']"
        self.moduleNameInModules = "//td[@data-testid='dashboard-module-name-0']"
        self.moduleTypeInModules = "//td[@data-testid='dashboard-module-type-0']"
        self.moduleStatusInMpdules = "//td[@data-testid='dashboard-module-status-0']"
        self.publishIcon = "#publish_module_to_catalyx"
        self.yesBtn = "//button[normalize-space()='Yes']"
        self.OkBtn = "//button[text()='OK']"
        self.searchInput = "//input[@data-testid='search-modules']"
        self.playSimula = "//img[@data-testid='dashboard-play-0']"
        self.NextBtn = "//button[text()='Next']"
        self.NextarrowDeepdive="//div[@class='flex max-sm:hidden w-full items-center gap-32']//button[2]"
        self.NextBtncanvas="//div[@class='flex px-6 max-sm:px-5 py-2 max-sm:py-3 rounded-full w-28 items-center ml-auto mr-10']//button"
        self.rightarrow="//img[@alt='right']"
        self.NextBtn2 = "#next"
        self.NextBtn3= "//div[text()='Next']"
        self.closeBtn = "//button[text()='Close']"
        self.narratoroption1="(//div[@class='rounded-2xl !z-[100]  '])[1]"
        self.narratoroption2 = "(//div[@class='rounded-2xl !z-[100]  '])[1]"
        self.firstOpt = "(//div[contains(@class,'cursor-pointer')])[1]"
        self.submitBtn = "//div[@data-testid='lifeline-submit']//div"
        self.submitBtnNarrator="//div[text()='Submit']"
        self.submitBtn1 = "//button[text()='Submit']"
        self.chekBoxOpt1 = "(//input[@type='checkbox'])[1]"
        self.radioVeryHighBtn = "(//input[@name='slider-radio'])[5]"
        self.endingText="//div[text()='Thank you for playing with us. ']"
        self.predicBtn = "(//div[@class='text-white font-normal leading-tight text-st-h15-400 max-sm:hidden'])[1]"
        self.LifeLineHoverTxt = "//div[@data-popup='popupHover']/p"
        self.clarityBtn = "//img[@alt='clarity']"
        self.popularityBtn = "//div[text()='Popularity']"
        self.predictionTxtOverOpt = "//img[@alt='prediction_icon']/parent::div/following-sibling::div"
        self.clarityTxtOver = "//img[contains(@src,'clarity_icon')]/parent::div/following-sibling::div"
        self.clarityTxt = "//div[@class='text-base']//div[contains(@class,'text-center')]"
        self.wrongBtn = "//button[@aria-label='Dismiss toast']"
        self.popularityIconOverOpt1 = "(//img[@alt='popularity']/parent::div)[1]"
        self.popularityIconOverOpt2 = "(//img[@alt='popularity']/parent::div)[2]"
        self.popularityIconOverOpt3 = "(//img[@alt='popularity']/parent::div)[3]"
        self.enableDebriefVideoToggleBtn = "(//div[contains(@class,'slide-toggle-thumb')])[2]"
        self.videoTitle = "//input[@placeholder='Video Heading']"
        self.videoSubTitle = "//input[@placeholder='Video Subtitle']"
        self.videoFrame = "//iframe[@title='Video Player Form']"
        self.videoRefNameInput = "//input[@placeholder='Name']"
        self.videoThumbnailInput = "// input[@accept='image/*']"
        self.videoInput = "//input[@accept='video/*']"
        self.uploadVideoBtn = "//button[text()='Upload Video']"
        self.iBtn = "//img[@alt='i_button']"
        self.secName = "//div[@class='modal contents ']//div[contains(@class,'text-center')]"
        self.senDescrip = "(//div[@class='modal contents ']//div[contains(@class,'text-white')])[2]/p"
        self.iBtnClose = "//img[@alt='close']"
        self.udtDrpDwn = "//option[text()='Universal DT Gametype']"
        self.company_drpdwn = "(//span[@title='All'])[2]"
        self.cominput = "//input[@class='select2-search__field']"
        self.cohort_drpdwn = "(//span[@role='combobox'])[11]"
        self.madhuri_cmpny = "//li[text()='testmadhuri']"
        self.magicLink_btn = "(//button[text()='Magic Link'])[1]"
        self.copyMagicLink_txt = "//button[text()='Copy Magic Link']"
        self.name_input = "(//input[@placeholder='Name'])[2]"
        self.username_input = "(//input[@placeholder='Username'])[2]"
        self.role_input = "//input[@placeholder='Designation']"
        self.manager_input = "(//input[@placeholder='Manager Name'])[2]"
        self.simulation_chkbx = "//input[@class='checkedSimulationModules']"
        self.createUser_btn = "//input[@class='btn btn-info createUser']"
        self.success_createuser_txt = "//span[text()='Success']"
        self.Close_btn = "(//button[text()='Close'])[1]"
        self.search_magic_link_page = "//input[@placeholder='Search']"
        self.serach_btn_magic_page = "//button[text()='Search']"
        self.name_magic_page = "//td[@class='nameTd']"
        self.username_magic_page = "//td[@class='usernameTd']"
        self.startBtn = "(//span[text()='Start'])[6]"
        self.startBtn2 = "//span[text()='Start']"
        self.pathManagement = "//p[text()='Path Management']"
        self.createPath = "//div[text()='Create Path']"
        self.static = "//div[text()='Static']"
        self.selectModulesCatAdm = "(//div[text()='Select Modules'])[1]"
        self.checkBox = "(//input[@type='checkbox'])[1]"
        self.saveNxtCatAdm = "//button[normalize-space()='SAVE & NEXT']"
        self.pathHeading = "//div[@class='flex justify-start px-3 py-1 text-lg']"
        self.pathName = "#path_name_static"
        self.pathImage = "#path_image_static"
        self.pathDesc = "#path_description_static"
        self.editModuleDetailsBtn = "//div[@data-testid='accordion-item']"
        self.googleSignInFrame = "iframe[title=\"Sign in with Google Button\"]"
        self.searchInputUDT = "//input[@placeholder='Search...']"
        self.firstRowSce = "((//table[@class='svelte-15iwbfd']//tr)[2]/td)[1]"
        self.playSimula = "//img[@data-testid='dashboard-play-0']"
        self.moduleNameTxt = "//div[contains(@class,'header-simulation-name')]"
        self.headingTxt = "(//div[@class='contentContainer']/div)[1]"
        self.moduleNameTxt2="//div[@class='header-simulation-name padding-left-45 padding-top-10 padding-bottom-10 theme-font2']"
        self.sideHeadingTxt = "//div[contains(@class,'sub_heading')]"
        self.contentPageRef = "//div[@class='heading theme-font16']"
        self.nextBtnUDT="//button[@data-testid='page-next-btn']"
        self.playYtVideoBtn="(//span[@class='vjs-control-text'])[2]"
        self.pauseYtVideoBtn="//img[@alt='video_btn_icon']"
        self.NextBtnAfterNarratorOptions="//div[text()='Next']"
        self.chkboxOptions="(//input[@name='single-select'])[1]"
        self.chkboxNextBtn = "//button[text()='Next']"
        self.sliderNextBtn = "//button[text()='Next']"
        self.sliderNextBtn2 = "//button[text()='Next']"
        self.ytsubmitBtn="//div[text()='Submit']"
        self.sliderRadioBtn="(//input[@name='slider-radio'])[4]"
        self.slidersubmitBtn="//button[text()='Submit']"
        self.secDescpTxt = "#text_player_content"
        self.secHeadingTxt = "//div[@class='text-white']/div[3]/span"
        self.secQuestTxt = "//div[contains(@class,'question_content')]"
        self.createNewBtn = "//button[text()='Create New']"
        self.modHeadPathMag = "//div[contains(@id,'static')]"
        self.editIconModules="(//img[@class='inline cursor-pointer'])[1]"
        self.deleteIconModuleContentPage1="(//span[@class='ml-2'])[2]"
        self.deleteIconModuleContentPage2="(//span[@class='ml-2'])[4]"
        self.yesDeleteModuleContentPage="//button[text()='Yes, delete it!']"
        self.contentpageVisible="(//div[@class='flex items-center cursor-move pl-10'])[1]"
        self.contentpageVisible2="(//div[@class='flex items-center cursor-move pl-10'])[2]"
        self.noEntriesFound="//aside[text()='No entries to found']"
        self.editIconModuleContentPage="(//span[text()='Edit'])[1]"
        self.editModulespage="//img[@data-testid='dashboard-edit-module-0']"
        self.editHeadingModuleContent="//input[@id='heading']"
        self.editSubHeadingModuleContent = "//input[@id='subheading']"
        self.editContentModuleContent="iframe[title='Rich Text Area. Press ALT-0 for help.']"
        self.headingTheme="//div[@class='contentContainer']//div[1]"
        self.subHeadingTheme="//div[@class='contentContainer']//div[2]"
        self.contentTheme="//div[@class='content theme-font18']"
        self.moduleSetupTab="//div[text()='Step 2: Module Setup']"
        self.inputParam2togBtn="(//div[@data-testid='slide-toggle'])[3]"
        self.inputParamName="//input[@data-testid='parametere-name-1']"
        self.inputParamDef="//input[@data-testid='parameter-definition-1']"
        self.inputPara2ShowResTogBtn ="(//div[@data-testid='slide-toggle'])[4]"
        self.outputParaShowResTogBtn = "(//div[@data-testid='slide-toggle'])[11]"
        self.outputparam2togBtn="(//div[contains(@class,'slide-toggle-thumb')])[13]"
        self.outputPara2ShowResTogBtn="(//div[@data-testid='slide-toggle'])[15]"
        self.inputparam1togBtn="(//label[@class='slide-toggle-label unstyled flex items-center'])[1]"
        self.outputparam1togBtn="(//div[@data-testid='slide-toggle'])[9]"
        self.clickNextBtnBeforeYT="//button[@data-testid='page-next-btn']"
        self.editgamtyperefOnModContent="(//img[@alt='edit_icon'])[3]"
        self.questionforoutparams1="//div[@class='text-xl font-bold mt-2']"
        self.questionforoutparams2="(//div[@class='text-xl font-bold mt-2'])[2]"
        self.textCheckboxEnabledQstnnOnReflectPage="//div[@class='text-st-h19-700 text-white mt-4']"
        self.checkboxqstn="//input[@placeholder='Checkbox Question']"
        self.checkboxqstnoptions1="(//input[@placeholder='Option 1'])[2]"
        self.checkboxqstnoptions2="(//input[@placeholder='Option 2'])[2]"
        self.textCheckboxOption1OnReflectPage="(//input[@type='checkbox'])[1]"
        self.textCheckboxOption2OnReflectPage="(//p[@class='text-st-h13-400'])[2]"
        self.modulesTab="(//div[@class='app-rail-label font-bold text-xs font-medium text-sm'])[1]"
        self.saveNextModuleSetUp="//button[@id='sib_gametype_save_btn']"
        self.saveNexContentPagetModContent="//button[@id='content_layout_editor_save_btn']"
        self.saveNextEndPageModContent="//button[@id='end_page_editor_save_btn']"
        self.qstnTextOnReflectPage="//div[@class='text-st-h19-700 text-white mt-4']"
        self.option1chkboxOnReflectPage="(//p[@class='text-st-h13-400'])[1]"
        self.option2chkboxOnReflectPage="(//p[@class='text-st-h13-400'])[2]"
        self.option3chkboxOnReflectPage ="(//p[@class='text-st-h13-400'])[3]"
        self.sliderQstnOnEffectPage="//div[@class='text-st-h19-700 text-white mt-4']"
        self.slderSubmitOnEffectPage="//button[@class='btn  bg-tw-pallet-color-6 text-white px-7 py-3 mt-7 outline-none w-34 text-st-h15-400']"
        self.debriefVideoTitleOnSimProfile="//div[@class='text-st-h20-700 text-white mt-6']"
        self.debriefVideoSubTitleOnSimProfile ="//div[@class='text-st-h14-400 text-white']"
        self.debriefVideoDescOnSimProfile="//div[@class='px-12 py-1 text-st-h14-400 text-white pb-10']"
        self.transcriptDebriefDesc="//p[text()='Transcript']"
        self.AddOptionalOption="//button[@class='mt-4 text-blue-500']"
        self.NarratorDeepdive="//div[@class='text-st-h13-400 max-sm:text-m-h8-400']"
    def searchesForAlreadyCreatedUDTmod(self):
        # self.actions.fill(self.serchModule, "modddd")
        # self.actions.keyboard_press("Enter")
        self.actions.click(self.modulesBtn)
        searchvalue = config['Admin']['ModuleNameUDT1']
        self.actions.fill(self.serchModule, searchvalue)
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(3000)

    def searchesForAlreadyCreatedUDTmodDel(self):
        # self.actions.fill(self.serchModule, "modddd")
        # self.actions.keyboard_press("Enter")
        self.actions.click(self.modulesBtn)
        searchvalue = config['Admin']['ModuleNameUDT']
        self.actions.fill(self.serchModule, searchvalue)
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(3000)


    def ableToSeeSearchedModuleOutcome(self):
        expectValue = "Universal DT"
        ModuleName = self.actions.text_content(self.moduleTypeRow2)
        self.actions.assertValues(ModuleName, expectValue)

    def clicksOnPlayButton(self):
        self.actions.newTabAfterClickingAnElement(self.playSimula)
        self.actions.newTab1WaitForTimeout(15000)


    def clicksOnPlayBtnAndPlayUdtFromUserPro(self):
        # self.actions.click(self.modulesBtn)
        # searchvalue=config['Admin']['ModuleNameUDT']
        # self.actions.fill(self.serchModule, searchvalue)
        # self.actions.keyboard_press("Enter")
        self.actions.newTabAfterClickingAnElement(self.playSimula)
        self.actions.newTab1WaitForTimeout(10000)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1WaitForTimeout(2000)
        self.actions.newTab1Click(self.closeBtn)
        self.actions.newTab1WaitForTimeout(4000)
        self.actions.newTab1GetByTextFirstClick("Narrator: Jane asks you to")
        #self.actions.click(self.narratoroption1)
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Narrator: Joe further elaborates on")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Narrator: Joe doesn't look happy with")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Joe: I need to go to another meeting")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Narrator: Joe says he does not have")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1Click(self.NextBtn3)
        self.actions.newTab1Click(self.chekBoxOpt1)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.radioVeryHighBtn)
        self.actions.newTab1WaitForTimeout(2000)
        self.actions.newTab1Click(self.submitBtn1)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.NextBtn)
        # self.actions.click("//button[@class='btn bg-tw-pallet-color-88 text-white px-7 outline-none w-34']")
        print(self.actions.newTab1TextContent(self.endingText))
        #print(self.actions.newTab1TextContent(self.endingText))

    def entersModuleStepOneUdt(self):
        self.modName = randomUtils.generate_random_string_with_prefix(length=10, prefix="test")
        self.actions.fill(self.moduleNameInput, self.modName)
        self.actions.wait_for_timeout(2000)
        self.actions.fill(self.moduleHeadInput, "moduleHeading")
        self.actions.wait_for_timeout(2000)
        self.actions.fill(self.moduleDescInput, "moduleDescription")
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.moduleTimeDrpDwn)
        self.actions.wait_for_timeout(2000)
        self.actions.keyboard_press("ArrowDown")
        self.actions.keyboard_press("ArrowDown")
        self.actions.wait_for_timeout(2000)
        self.actions.keyboard_press("Enter")
        self.actions.select_option_visible_text(self.gameTypeDrpdwn, "Universal DT Gametype")
        self.actions.wait_for_timeout(2000)
        self.actions.wait_for_timeout(4000)
        # self.actions.click(self.gameTypeDrpdwn)
        # self.actions.click(self.udtDrpDwn)
        self.actions.click(self.colorPalatteDrpdwn)
        self.actions.wait_for_timeout(2000)

        self.actions.keyboard_press("ArrowDown")
        self.actions.wait_for_timeout(2000)

        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.saveNextModDetails)
        self.actions.wait_for_timeout(2000)
        return self.modName

    def entersModuleStepOneToggleUdt(self):
        self.modName = randomUtils.generate_random_string_with_prefix(length=10, prefix="test")
        self.actions.fill(self.moduleNameInput, self.modName)
        self.actions.fill(self.moduleHeadInput, "moduleHeading")
        self.actions.fill(self.moduleDescInput, "moduleDescription")
        self.actions.click(self.moduleTimeDrpDwn)
        self.actions.keyboard_press("ArrowDown")
        self.actions.keyboard_press("ArrowDown")
        self.actions.keyboard_press("Enter")
        self.actions.select_option_visible_text(self.gameTypeDrpdwn, "Universal DT Gametype")
        self.actions.click(self.colorPalatteDrpdwn)
        self.actions.keyboard_press("ArrowDown")
        self.actions.keyboard_press("Enter")

    def enableDisableReportsSimulationTogglesUdt(self):
        self.actions.click(self.toglDisableRewatch)
        self.actions.click(self.toglDisableReports)
        #self.actions.click(self.toglSimulation)
        #self.actions.click(self.toglVoiceOver)


    def entersModuleStepOneClickSaveNextUdt(self):
            self.actions.click(self.saveNextModDetails)
            return self.modName


    def clicksOnmodulesPubhishedUdt(self, adminUsername:str, adminPassword:str,  ):
        self.actions.click(self.modulesBtn)
        self.actions.fill(self.serchModule, self.modName)
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(3000)
        expectValue = self.modName
        ModuleName = self.actions.text_content(self.moduleNameInModules)
        self.actions.assertValues(ModuleName, expectValue)
        ModuleType = self.actions.text_content(self.moduleTypeInModules)
        expectType = "Universal DT"
        self.actions.assertValues(ModuleType, expectType)
        moduleStatusBefore = self.actions.text_content(self.moduleStatusInMpdules)
        print("Module Status Before", moduleStatusBefore)
        self.actions.click(self.publishIcon)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.yesBtn)
        self.actions.wait_for_timeout(4000)
        actualMessage = self.actions.text_content(self.sucTxt)
        expected_message = "Module published successfully"
        self.actions.assertValues(actualMessage, expected_message)
        self.actions.click(self.okayBtn)
        self.actions.wait_for_timeout(1000)
        self.actions.reload()
        self.actions.wait_for_timeout(10000)
        self.actions.fill(self.searchInput, self.modName)
        self.actions.wait_for_timeout(3000)
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(2000)
        moduleStatusAfter = self.actions.text_content(self.moduleStatusInMpdules)
        self.actions.wait_for_timeout(3000)
        print("Module Status After", moduleStatusAfter)
        print(self.modName)
        self.actions.goto("https://simulation-test.catalyx.live/catalyx/adminlogin.php")
        self.actions.newTab1_after_clicking_frame_get_by_role("iframe[title=\"Sign in with Google Button\"]", "button",
                                                              "Madhuri's profile image Sign")
        self.actions.newTab1_get_by_role_dbclick("link", "Madhuri Budha (vendor)")
        try:
            if self.actions.newTab1_get_by_role_is_visible("link", "Madhuri Budha (vendor)"):
                self.actions.newTab1_get_by_role_dbclick("link", "Madhuri Budha (vendor)")
            else:
                print("Already clicked")

        except Exception as e:
            print("clicked")

        self.actions.wait_for_timeout(30000)
        self.actions.wait_for_timeout(3000)
        self.actions.click(self.pathManagement)
        # self.page.get_by_role("link", name=" Path Management").click()
        self.actions.wait_for_timeout(4000)
        self.actions.click(self.createPath)
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.static)
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.selectModulesCatAdm)
        self.actions.fill(self.serchModule, self.modName)
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(3000)
        self.actions.wait_for_timeout(3000)
        expectValue = self.modName
        # ModuleName = self.actions.text_content(self.moduleNameInModules)
        # ModuleName1 = ModuleName.strip() if ModuleName else None
        # assert expectValue == ModuleName1, f"Expected message '{expectValue}' but got '{ModuleName1}'"
        self.actions.click(self.checkBox)
        self.actions.click(self.saveNxtCatAdm)
        self.actions.wait_for_timeout(3000)

    def fillingParameterSettings(self):
        #self.actions.click(self.inputparam1togBtn)
        self.actions.fill(self.inputPrameterName, "Ip1")
        self.actions.fill(self.inputParameterDef, "Id1")
        self.actions.wait_for_timeout(3000)
        self.actions.click(self.inputParaShowResTogBtn)
        self.actions.fill(self.outputPrameterName, "Op1")
        self.actions.fill(self.outputPrameterDef, "Od1")
        self.actions.wait_for_timeout(3000)
        self.actions.click(self.outputParaShowResTogBtn)
        self.actions.click(self.disableBackBtnTogBtn)
        self.actions.click(self.saveNext)


    def fillingStepThreeUdtGametype(self):
        self.actions.click(self.addSection)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.content)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.contentPage1)
        self.actions.fill(self.reference, "Reference1")
        self.actions.fill(self.heading, "Heading")
        self.actions.fill(self.subheading, "Sub Heading")
        self.actions.wait_for_timeout(4000)
        self.actions.frame_locator_fill("iframe[title=\"Rich Text Area\\. Press ALT-0 for help\\.\"]","#tinymce", "moduleDescription")
        self.actions.click(self.imageUrl)
        self.actions.click(self.image)
        self.actions.click(self.saveNext)
        self.actions.click(self.addSection)
        self.actions.click(self.content)
        self.actions.click(self.endpage)
        self.actions.fill(self.reference, "Reference1")
        self.actions.click(self.saveNextEndPage)
        self.actions.wait_for_timeout(4000)
        self.actions.click(self.addSection)
        self.actions.wait_for_timeout(1500)
        self.actions.click(self.gameType)
        # actual = self.page.text_content(self.AIDiagnoGameType)
        # expected = "AI Diagnostic Gametype"
        # assert expected == actual, f"Expected message '{expected}' but got '{actual}'"
        self.actions.get_by_text_click("Universal DT Gametype")
        self.actions.fill(self.udtRefName, "UDT Reference Name")
        self.actions.fill(self.UdtSceName, "UDT Scenario Name")
        self.actions.wait_for_timeout(3000)
        self.actions.frame_locator_fill("iframe[title=\"Rich Text Area\\. Press ALT-0 for help\\.\"]", "#tinymce",
                                        "UDT moduleDescription")
        self.actions.wait_for_timeout(3000)

        self.actions.click(self.filePathElement)
        self.actions.wait_for_timeout(3000)
        self.actions.set_input_files(self.filePathElement, r"C:\NewEnp\Enparadigm\Enparadigm\Enparadigm\behaveProject\Upload\Thumnail\UDTSample.xlsx")
        self.actions.wait_for_timeout(3000)
        self.actions.fill(self.sliderQuestionInput1, "How are you feeling")
        self.actions.click(self.enableCheckboxUdtTogBtn)
        self.actions.fill(self.checkBoxQuest, "What is an Apple?")
        self.actions.fill(self.opt1, "Fruit")
        self.actions.fill(self.opt2, "Vegetable")
        self.actions.wait_for_timeout(3000)
        self.actions.click(self.saveNext)
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.publishButton)
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.okayBtn)

    def fillingStepThreeUdtGametypedel(self):
        self.actions.click(self.addSection)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.content)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.contentPage1)
        self.actions.fill(self.reference, "Reference1")
        self.actions.fill(self.heading, "Heading")
        self.actions.fill(self.subheading, "Sub Heading")
        self.actions.wait_for_timeout(4000)
        self.actions.frame_locator_fill("iframe[title=\"Rich Text Area\\. Press ALT-0 for help\\.\"]","#tinymce", "moduleDescription")
        self.actions.click(self.imageUrl)
        self.actions.click(self.image)
        self.actions.click(self.saveNext)
        # self.actions.click(self.addSection)
        # self.actions.click(self.content)
        # self.actions.click(self.endpage)
        # self.actions.fill(self.reference, "Reference1")
        # self.actions.click(self.saveNextEndPage)
        self.actions.wait_for_timeout(4000)
        self.actions.click(self.addSection)
        self.actions.wait_for_timeout(1500)
        self.actions.click(self.gameType)
        # actual = self.page.text_content(self.AIDiagnoGameType)
        # expected = "AI Diagnostic Gametype"
        # assert expected == actual, f"Expected message '{expected}' but got '{actual}'"
        self.actions.get_by_text_click("Universal DT Gametype")
        self.actions.fill(self.udtRefName, "UDT Reference Name")
        self.actions.fill(self.UdtSceName, "UDT Scenario Name")
        self.actions.wait_for_timeout(3000)
        self.actions.frame_locator_fill("iframe[title=\"Rich Text Area\\. Press ALT-0 for help\\.\"]", "#tinymce",
                                        "UDT moduleDescription")
        self.actions.wait_for_timeout(3000)

        #self.actions.click(self.filePathElement)
        self.actions.wait_for_timeout(3000)
        self.actions.set_input_files(self.filePathElement, r"C:\NewEnp\Enparadigm\Enparadigm\Enparadigm\behaveProject\Upload\Thumnail\UDTSample.xlsx")
        self.actions.wait_for_timeout(8000)
        self.actions.fill(self.sliderQuestionInput1, "How are you feeling")
        self.actions.wait_for_timeout(8000)
        self.actions.click(self.enableCheckboxUdtTogBtn)
        self.actions.fill(self.checkBoxQuest, "What is an Apple?")
        self.actions.fill(self.opt1, "Fruit")
        self.actions.fill(self.opt2, "Vegetable")
        self.actions.wait_for_timeout(3000)
        self.actions.wait_for_timeout(3000)
        self.actions.click(self.saveNext)
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.publishButton)
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.okayBtn)
        self.actions.is_visible(self.contentpageVisible,"visible contentpage1")
        self.actions.is_visible(self.contentpageVisible2,"visible contentpage1")

    def verifyParametersinStep2AndStep3ModuleContent(self):
        self.actions.click(self.addSection)
        self.actions.wait_for_timeout(1500)
        self.actions.click(self.gameType)
        # actual = self.page.text_content(self.AIDiagnoGameType)
        # expected = "AI Diagnostic Gametype"
        # assert expected == actual, f"Expected message '{expected}' but got '{actual}'"
        self.actions.get_by_text_click("Universal DT Gametype")
        self.actions.fill(self.udtRefName, "UDT Reference Name")
        self.actions.fill(self.UdtSceName, "UDT Scenario Name")
        self.actions.wait_for_timeout(3000)
        self.actions.frame_locator_fill("iframe[title=\"Rich Text Area\\. Press ALT-0 for help\\.\"]", "#tinymce",
                                        "UDT moduleDescription")
        self.actions.wait_for_timeout(3000)

        # self.actions.click(self.filePathElement)
        self.actions.wait_for_timeout(3000)
        self.actions.set_input_files(self.filePathElement,
                                     r"C:\NewEnp\Enparadigm\Enparadigm\Enparadigm\behaveProject\Upload\Thumnail\UDTSample.xlsx")
        self.actions.wait_for_timeout(8000)
        ####
        textOfOutputParams1InModuleContentPage = self.actions.text_content(self.questionforoutparams1)
        extractedOutputParamsInModuleContentPagetext = \
        textOfOutputParams1InModuleContentPage.split("Questions for ", 1)[1]
        print("extractedOutputParamsInModuleContentPagetext",extractedOutputParamsInModuleContentPagetext)

        expected = config['Admin']['outputParamNameValue1']
        print("expected",expected)
        actual = extractedOutputParamsInModuleContentPagetext
        assert actual == expected, f"Expected message '{expected}' but got '{actual}'"

        # textOfOutputParams2InModuleContentPage = self.actions.text_content(self.questionforoutparams2)
        # extractedOutputParams2InModuleContentPagetext = \
        # textOfOutputParams2InModuleContentPage.split("Questions for ", 1)[
        #     1]
        # expected = config['Admin']['outputParamNameValue2']
        # actual = extractedOutputParams2InModuleContentPagetext
        # assert actual == expected, f"Expected message '{expected}' but got '{actual}'"

        ##################
        self.actions.fill(self.sliderQuestionInput1, "How are you feeling")
        self.actions.wait_for_timeout(8000)
        self.actions.click(self.enableCheckboxUdtTogBtn)
        self.actions.fill(self.checkBoxQuest, "What is an Apple?")
        self.actions.fill(self.opt1, "Fruit")
        self.actions.fill(self.opt2, "Vegetable")
        self.actions.wait_for_timeout(3000)

        self.expectedChkboxQstn = self.actions.input_value(self.checkboxqstn)
        print("expectedChkboxQstn:-", self.expectedChkboxQstn)

        self.expectedChkboxOptns1 = self.actions.input_value(self.checkboxqstnoptions1)
        print("expectedChkboxOptns1:-", self.expectedChkboxOptns1)

        self.expectedChkboxOptns2 = self.actions.input_value(self.checkboxqstnoptions2)
        print("expectedChkboxOptns2:-", self.expectedChkboxOptns2)

        self.actions.wait_for_timeout(3000)
        self.actions.click(self.saveNext)
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.publishButton)
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.okayBtn)
        return self.expectedChkboxQstn,self.expectedChkboxOptns1,self.expectedChkboxOptns2



    def searchesNewlyCreatedModAndPlaysit(self):
        self.actions.click(self.modulesBtn)
        self.actions.fill(self.serchModule, self.modName)
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(3000)
        expectValue = self.modName
        ModuleName = self.actions.text_content(self.moduleNameInModules)
        self.actions.assertValues(ModuleName, expectValue)
        ModuleType = self.actions.text_content(self.moduleTypeInModules)
        expectType = "Universal DT"
        self.actions.assertValues(ModuleType, expectType)
        moduleStatusBefore = self.actions.text_content(self.moduleStatusInMpdules)
        print("Module Status Before", moduleStatusBefore)
        self.actions.click(self.publishIcon)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.yesBtn)
        self.actions.wait_for_timeout(4000)
        actualMessage = self.actions.text_content(self.sucTxt)
        expected_message = "Module published successfully"
        self.actions.assertValues(actualMessage, expected_message)
        self.actions.click(self.okayBtn)
        self.actions.wait_for_timeout(1000)
        self.actions.reload()
        self.actions.wait_for_timeout(10000)
        self.actions.fill(self.searchInput, self.modName)
        self.actions.wait_for_timeout(3000)
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(2000)
        moduleStatusAfter = self.actions.text_content(self.moduleStatusInMpdules)
        self.actions.wait_for_timeout(3000)
        print("Module Status After", moduleStatusAfter)
        print(self.modName)
        self.actions.newTabAfterClickingAnElement(self.playSimula)
        self.actions.newTab1WaitForTimeout(10000)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1WaitForTimeout(2000)
        #self.actions.newTab1Click(self.closeBtn)
        #self.actions.newTab1WaitForTimeout(5000)
        self.actions.newTab1GetByTextFirstClick("Narrator_03: Jane says the clients want")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Narrator_07: Before diving into the discussion, ")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Joe_09: My concerns are more future facing")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Joe_13: I need to think long-term before onboarding")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Narrator_16: Joe and you set up a meeting for next week")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1Click(self.NextBtn3)
        self.actions.newTab1WaitForTimeout(2000)
        self.actions.newTab1Click(self.textCheckboxOption1OnReflectPage)
        self.actions.newTab1WaitForTimeout(2000)
        # self.actions.newTab1Click(self.chekBoxOpt1)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.radioVeryHighBtn)
        self.actions.newTab1WaitForTimeout(2000)
        self.actions.newTab1Click(self.submitBtn1)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.NextBtn)
        #self.actions.click("//button[@class='btn bg-tw-pallet-color-88 text-white px-7 outline-none w-34']")
        print(self.actions.newTab1TextContent(self.endingText))


    def optsDifOptions(self):
        self.actions.newTabAfterClickingAnElement(self.playSimula)
        self.actions.newTab1WaitForTimeout(15000)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1WaitForTimeout(2000)
        self.actions.newTab1Click(self.closeBtn)
        self.actions.newTab1WaitForTimeout(5000)
        self.actions.newTab1GetByTextFirstClick("Narrator: Jane says the clients want")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Narrator: Before diving into the discussion, ")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Joe: My concerns are more future facing")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Joe: I need to think long-term before onboarding")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Narrator: Joe and you set up a meeting for next week")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1Click(self.NextBtn3)
        self.actions.newTab1Click(self.chekBoxOpt1)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.radioVeryHighBtn)
        self.actions.newTab1WaitForTimeout(2000)
        self.actions.newTab1Click(self.submitBtn1)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.NextBtn)
        print(self.actions.newTab1TextContent(self.endingText))

    def startsPlayGame(self):
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1WaitForTimeout(2000)
        self.actions.newTab1Click(self.closeBtn)
        self.actions.newTab1WaitForTimeout(5000)

    def ableToSeeEnabledAllThreeLifelineOptions(self):
        # step 1
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1isEnabled(self.predicBtn, "Prediction Button")
        self.actions.newTab1WaitForTimeout(5000)

        self.actions.newTab1isEnabled(self.clarityBtn, "Clarity Button")
        self.actions.newTab1isEnabled(self.popularityBtn, "Popularity Button")

    def hoveringTextonOptions(self):
        self.actions.newTab1_mouse_hover_get_text(self.predicBtn, self.LifeLineHoverTxt, "Prediction Button")
        self.actions.newTab1_mouse_hover_get_text(self.clarityBtn, self.LifeLineHoverTxt, "Clarity Button")
        self.actions.newTab1_mouse_hover_get_text(self.popularityBtn, self.LifeLineHoverTxt, "Popularity Button")
    def clicksOnPredictionBtn(self):
        # clicking Prediction btn
        self.actions.newTab1Click(self.predicBtn)

    def predictionMesgAppearing(self):
        print()
    #     need to implement

    def clicksAnyOptionOfChoices(self):
        self.actions.newTab1GetByTextFirstClick("Narrator: Jane asks you to")

    def predictionTextOverOption(self):
        expectPredTxt = self.actions.get_data_by_excel_file(
            r"C:\Users\hp\PycharmProjects\Enparadigm\Enparadigm\behaveProject\Upload\Thumnail\UDTSample.xlsx",
            "Sheet1", 3, 21)
        print(expectPredTxt)
        precTxtOverOption = self.actions.newTab1TextContent(self.predictionTxtOverOpt)
        print(precTxtOverOption)
        self.actions.assertValues(precTxtOverOption, expectPredTxt)

    def allThreeOptionsDisabled(self):
        self.actions.newTab1isDisabled(self.predicBtn, "Prediction Button")
        self.actions.newTab1isDisabled(self.clarityBtn, "Clarity Button")
        self.actions.newTab1isDisabled(self.popularityBtn, "Popularity Button")

    def clicksSubmitBtn(self):
        self.actions.newTab1Click(self.submitBtn)

    def disabledPredEnabledClaPopStep2(self):
        # step2
        self.actions.newTab1isDisabled(self.predicBtn, "Prediction Button")
        self.actions.newTab1isEnabled(self.clarityBtn, "Clarity Button")
        self.actions.newTab1isEnabled(self.popularityBtn, "Popularity Button")

    def predictionTextOverOption(self):
        precTxtOverOption = self.actions.newTab1TextContent(self.predictionTxtOverOpt)
        print(precTxtOverOption)

    def clicksClarityBtn(self):
        # clicking clarity button
        self.actions.newTab1Click(self.clarityBtn)

    def clarityMsgAppearing(self):
        expectclaTxt = self.actions.get_data_by_excel_file(
            r"C:\Users\hp\PycharmProjects\Enparadigm\Enparadigm\behaveProject\Upload\Thumnail\UDTSample.xlsx",
            "Sheet1", 1, 21)
        print(expectclaTxt)
        clarityTxtOverOption = self.actions.newTab1TextContent(self.clarityTxt).strip()
        print(clarityTxtOverOption)
        self.actions.assertValues(clarityTxtOverOption, expectclaTxt)


    def enabledClarityDisabledPredPop(self):
        self.actions.newTab1isDisabled(self.predicBtn, "Prediction Button")
        self.actions.newTab1isEnabled(self.clarityBtn, "Clarity Button")
        self.actions.newTab1isDisabled(self.popularityBtn, "Popularity Button")

    def clickOptSubmitBtn(self):
        self.actions.newTab1GetByTextLastClick("Narrator: Joe further elaborates on")
        self.actions.newTab1Click(self.submitBtn)

    def enabledPopDisPredClar(self):
        # step 3
        self.actions.newTab1isDisabled(self.predicBtn, "Prediction Button")
        self.actions.newTab1isDisabled(self.clarityBtn, "Clarity Button")
        self.actions.newTab1isEnabled(self.popularityBtn, "Popularity Button")

    def clicksOnPopBtn(self):
        # clicking popularity button
        self.actions.newTab1Click(self.popularityBtn)

    def popIconsOverOptAppearing(self):
        self.actions.newTab1_is_visible(self.popularityIconOverOpt1, "Prediction Button")
        self.actions.newTab1_is_visible(self.popularityIconOverOpt2, "Clarity Button")
        self.actions.newTab1_is_visible(self.popularityIconOverOpt3, "Popularity Button")

    def clicksOptSubmitBtnStep3(self):
        self.actions.newTab1GetByTextLastClick("Narrator: Joe doesn't look happy with")
        self.actions.newTab1Click(self.submitBtn)

    def diabledThreeLifelinesStep4(self):
        # step 4
        self.actions.newTab1isDisabled(self.predicBtn, "Prediction Button")
        self.actions.newTab1isDisabled(self.clarityBtn, "Clarity Button")
        self.actions.newTab1isDisabled(self.popularityBtn, "Popularity Button")

    def clicksInfoIconRightTopCorner(self):
        self.actions.newTab1Click(self.iBtn)

    def udtSceNameAndDesc(self):
        expectedSceName = "sffsf"
        actualSceName = self.actions.newTab1TextContent(self.secName)
        self.actions.assertValues(actualSceName, expectedSceName)
        expectedSceDesc = "ssfsfasf"
        actualSceDescrp = self.actions.newTab1TextContent(self.senDescrip)
        self.actions.assertValues(actualSceDescrp, expectedSceDesc)

    def closesPopupClicksAnyOptStep4(self):
        self.actions.newTab1Click(self.iBtnClose)
        self.actions.newTab1GetByTextFirstClick("Joe: I need to go to another meeting")

    def diabledThreeLifelinesStep4(self):
        self.actions.newTab1isDisabled(self.predicBtn, "Prediction Button")
        self.actions.newTab1isDisabled(self.clarityBtn, "Clarity Button")
        self.actions.newTab1isDisabled(self.popularityBtn, "Popularity Button")

    def clicksAnyOptSubBtn(self):
        self.actions.newTab1GetByTextLastClick("Narrator: Joe says he does not have")
        self.actions.newTab1Click(self.submitBtn)

    def clicksNextBtnAbleToSeeEndTxt(self):
        self.actions.newTab1Click(self.NextBtn3)
        self.actions.newTab1Click(self.chekBoxOpt1)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.radioVeryHighBtn)
        self.actions.newTab1WaitForTimeout(2000)
        self.actions.newTab1Click(self.submitBtn1)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.NextBtn)
        print(self.actions.newTab1TextContent(self.endingText))

    def verifiesLifelineFunctionality(self):

        # step 4

        self.actions.newTab1GetByTextFirstClick("Joe: I need to go to another meeting")
        self.actions.newTab1Click(self.submitBtn)
        # step 5
        self.actions.newTab1isDisabled(self.predicBtn, "Prediction Button")
        self.actions.newTab1isDisabled(self.clarityBtn, "Clarity Button")
        self.actions.newTab1isDisabled(self.popularityBtn, "Popularity Button")
        self.actions.newTab1GetByTextLastClick("Narrator: Joe says he does not have")
        self.actions.newTab1Click(self.submitBtn)
        self.actions.newTab1Click(self.NextBtn3)
        self.actions.newTab1Click(self.chekBoxOpt1)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.radioVeryHighBtn)
        self.actions.newTab1WaitForTimeout(2000)
        self.actions.newTab1Click(self.submitBtn1)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.NextBtn)
        print(self.actions.newTab1TextContent(self.endingText))

    def entersModuleStepThreeUdtDebriefVideo(self):
        self.actions.wait_for_timeout(3000)
        self.actions.click(self.addSection)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.content)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.contentPage1)
        self.actions.fill(self.reference, "Reference1")
        self.actions.fill(self.heading, "Heading")
        self.actions.fill(self.subheading, "Sub Heading")
        self.actions.wait_for_timeout(4000)
        self.actions.frame_locator_fill("iframe[title=\"Rich Text Area\\. Press ALT-0 for help\\.\"]", "#tinymce",
                                        "moduleDescription")
        self.actions.click(self.imageUrl)
        self.actions.click(self.image)
        self.actions.click(self.saveNexContentPagetModContent)
        self.actions.click(self.addSection)
        self.actions.click(self.content)
        self.actions.click(self.endpage)
        self.actions.fill(self.reference, "Reference1")
        self.actions.click(self.saveNextEndPageModContent)
        self.actions.wait_for_timeout(4000)
        self.actions.click(self.addSection)
        self.actions.wait_for_timeout(1500)
        self.actions.click(self.gameType)
        # actual = self.page.text_content(self.AIDiagnoGameType)
        # expected = "AI Diagnostic Gametype"
        # assert expected == actual, f"Expected message '{expected}' but got '{actual}'"
        self.actions.get_by_text_click("Universal DT Gametype")
        self.actions.fill(self.modRef, "UDT Reference")
        self.actions.fill(self.modScenarioName, "UDT Scenario Name")
        self.actions.frame_locator_fill("iframe[title=\"Rich Text Area\\. Press ALT-0 for help\\.\"]", "#tinymce",
                                        "UDT moduleDescription")
        self.actions.set_input_files(self.filePathElement,
                                     r"C:\NewEnp\Enparadigm\Enparadigm\Enparadigm\behaveProject\Upload\Thumnail\UDTSample.xlsx")
        self.actions.fill(self.sliderQuestionInput1, "How are you feeling")
        self.actions.click(self.enableCheckboxUdtTogBtn)
        self.actions.fill(self.checkBoxQuest, "What is an Apple?")
        self.actions.fill(self.opt1, "Fruit")
        self.actions.fill(self.opt2, "Vegetable")
        self.actions.click(self.enableDebriefVideoToggleBtn)
        self.actions.wait_for_timeout(5000)
        self.actions.fill(self.videoTitle, "UDT Video Title")
        self.actions.fill(self.videoSubTitle, "UDT Video Subtitle")
        self.actions.frame_locator_fill(self.videoFrame, self.videoRefNameInput, "Video Reference Name")
        # 1.Image
        self.actions.set_input_files_in_frame(self.videoFrame, self.videoThumbnailInput,
         r"C:\NewEnp\Enparadigm\Enparadigm\Enparadigm\behaveProject\Upload\Thumnail\LandscapeImage.jpg")
        #self.actions.wait_for_timeout(5000)
        # 2.Video
        #self.actions.set_input_files_in_frame(self.videoFrame, self.videoInput,
         #r"C:\NewEnp\Enparadigm\Enparadigm\Enparadigm\behaveProject\Upload\Video\LandscapeVideo.mp4")
        self.actions.wait_for_timeout(15000)
        self.actions.set_input_files_in_frame(self.videoFrame, self.videoInput,
            r"C:\NewEnp\Enparadigm\Enparadigm\Enparadigm\behaveProject\Upload\Video\LandscapeVideo.webm")
        self.actions.wait_for_timeout(10000)

        self.actions.frame_inside_frame_type(self.videoFrame,"iframe[title='Rich Text Area. Press ALT-0 for help.']",
                                             "#tinymce", "Udt Video Description")
        self.actions.wait_for_timeout(10000)
        self.actions.frame_locator_click(self.videoFrame,self.uploadVideoBtn )
        self.actions.wait_for_timeout(15000)
        self.actions.click(self.saveNext)
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.publishButton)
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.okayBtn)

    def searchesAndPlaysNewlyCreatedUdtDebriefVideo(self):
        self.actions.click(self.modulesBtn)
        self.actions.fill(self.serchModule, self.modName)
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(3000)
        expectValue = self.modName
        ModuleName = self.actions.text_content(self.moduleNameInModules)
        self.actions.assertValues(ModuleName, expectValue)
        ModuleType = self.actions.text_content(self.moduleTypeInModules)
        expectType = "Universal DT"
        self.actions.assertValues(ModuleType, expectType)
        moduleStatusBefore = self.actions.text_content(self.moduleStatusInMpdules)
        print("Module Status Before", moduleStatusBefore)
        self.actions.click(self.publishIcon)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.yesBtn)
        self.actions.wait_for_timeout(4000)
        actualMessage = self.actions.text_content(self.sucTxt)
        expected_message = "Module published successfully"
        self.actions.assertValues(actualMessage, expected_message)
        self.actions.click(self.okayBtn)
        self.actions.wait_for_timeout(1000)
        self.actions.reload()
        self.actions.wait_for_timeout(10000)
        self.actions.fill(self.searchInput, self.modName)
        self.actions.wait_for_timeout(3000)
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(2000)
        moduleStatusAfter = self.actions.text_content(self.moduleStatusInMpdules)
        self.actions.wait_for_timeout(3000)
        print("Module Status After", moduleStatusAfter)
        print(self.modName)
        self.actions.newTabAfterClickingAnElement(self.playSimula)
        self.actions.newTab1WaitForTimeout(15000)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1WaitForTimeout(2000)
        #self.actions.newTab1Click(self.closeBtn)
        #self.actions.newTab1WaitForTimeout(5000)
        self.actions.newTab1GetByTextFirstClick("Narrator_03: Jane says the clients want")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Narrator_07: Before diving into the discussion, ")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Joe_09: My concerns are more future facing")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Joe_13: I need to think long-term before onboarding")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Narrator_16: Joe and you set up a meeting for next week")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1Click(self.NextBtn3)
        self.actions.newTab1WaitForTimeout(2000)
        self.actions.newTab1Click(self.textCheckboxOption1OnReflectPage)
        self.actions.newTab1WaitForTimeout(2000)
        #self.actions.newTab1Click(self.chekBoxOpt1)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.radioVeryHighBtn)
        self.actions.newTab1WaitForTimeout(2000)
        self.actions.newTab1Click(self.submitBtn1)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.NextBtn)
        #self.actions.newTab1Click(self.NextBtncanvas)

        #print(self.actions.newTab1TextContent(self.endingText))
    def searchesAndPlaysNewlyCreatedUdtDebriefVideo14(self):
        self.actions.click(self.modulesBtn)
        self.actions.fill(self.serchModule, self.modName)
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(3000)
        expectValue = self.modName
        ModuleName = self.actions.text_content(self.moduleNameInModules)
        self.actions.assertValues(ModuleName, expectValue)
        self.actions.fill(self.searchInput, self.modName)
        self.actions.wait_for_timeout(3000)
        self.actions.newTabAfterClickingAnElement(self.playSimula)
        self.actions.newTab1WaitForTimeout(15000)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1WaitForTimeout(2000)
        #self.actions.newTab1Click(self.closeBtn)
        #self.actions.newTab1WaitForTimeout(5000)
        self.option1=self.actions.newTab1GetByTextFirstClick("Narrator_03: Jane says the clients want")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.option2=self.actions.newTab1GetByTextFirstClick("Narrator_07: Before diving into the discussion, ")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.option3=self.actions.newTab1GetByTextFirstClick("Joe_09: My concerns are more future facing")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.option4=self.actions.newTab1GetByTextFirstClick("Joe_13: I need to think long-term before onboarding")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.option5=self.actions.newTab1GetByTextFirstClick("Narrator_16: Joe and you set up a meeting for next week")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1Click(self.NextBtn3)
        self.actions.newTab1WaitForTimeout(2000)
        self.actions.newTab1Click(self.textCheckboxOption1OnReflectPage)
        self.actions.newTab1WaitForTimeout(2000)
        #self.actions.newTab1Click(self.chekBoxOpt1)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.radioVeryHighBtn)
        self.actions.newTab1WaitForTimeout(2000)
        self.actions.newTab1Click(self.submitBtn1)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.NextBtn)
        # self.actions.newTab1Click(self.NextBtn)
        return self.option1,self.option2,self.option3,self.option4,self.option5

    def selectsUDTCohrtComp(self):
        try:
            self.actions.click(self.company_drpdwn)
            self.actions.wait_for_timeout(3000)
            self.actions.click(self.company_drpdwn)
            self.actions.fill(self.cominput, "testmadhuri")
            self.actions.click(self.madhuri_cmpny)
            self.actions.wait_for_timeout(4000)
            self.actions.click(self.cohort_drpdwn)
            self.actions.fill(self.cominput, "udt-cohort")
            self.actions.keyboard_press("ArrowDown")
            self.actions.keyboard_press("Enter")
            self.actions.wait_for_timeout(4000)
        except Exception as e:
            self.actions.click(self.company_drpdwn)
            self.actions.wait_for_timeout(3000)
            self.actions.click(self.company_drpdwn)
            self.actions.fill(self.cominput, "testmadhuri")
            self.actions.click(self.madhuri_cmpny)
            self.actions.wait_for_timeout(4000)
            self.actions.click(self.cohort_drpdwn)
            self.actions.fill(self.cominput, "udt-cohort")
            self.actions.keyboard_press("ArrowDown")
            self.actions.keyboard_press("Enter")
            self.actions.wait_for_timeout(4000)

    def userDetailsUdt(self):
        self.user = randomUtils.generate_random_string_with_prefix(length=10, prefix="test")
        self.actions.fill(self.name_input, self.user)
        self.emailrandom = randomUtils.generate_random_email()
        self.actions.fill(self.username_input, self.emailrandom)
        self.actions.fill(self.role_input, "teamlead")
        self.actions.fill(self.manager_input, "madhuri")
        # self.page.check(self.simulation_chkbx)
        self.actions.click(self.createUser_btn)
        self.actions.wait_for_timeout(3000)
        if self.actions.is_visible(self.Close_btn, "Close Button"):
            print("visible")
            self.actions.get_by_role("button", "Close").click()
        self.actions.wait_for_timeout(3000)
        return self.user, self.emailrandom

    def verifiesUser(self):
        self.actions.fill(self.search_magic_link_page, self.user)
        self.actions.click(self.serach_btn_magic_page)
        actualMessage = self.actions.text_content(self.name_magic_page)
        expected_message = self.user
        assert expected_message == actualMessage, f"Expected message '{expected_message}' but got '{actualMessage}'"
        print("actualMessage", actualMessage)
        print("expected message", expected_message)
        actualMessage1 = self.actions.text_content(self.username_magic_page)
        expected_message1 = self.emailrandom
        assert expected_message == actualMessage, f"Expected message '{expected_message1}' but got '{actualMessage1}'"
        print("actualMessage", actualMessage1)
        print("expected message", expected_message1)

    def clicksMagicLinkCopiesPlaysUdtGame(self):
        self.actions.click(self.magicLink_btn)
        self.actions.click(self.copyMagicLink_txt)
        copied_link = pyperclip.paste()
        self.actions.openNewTab1()
        self.actions.open_url_in_newTab1(copied_link)
        self.actions.newTab1_get_by_role("button", "Accept")
        self.actions.newTab1Click(self.startBtn)
        self.actions.newTab1Click(self.startBtn2)
#         starts
        self.actions.newTab1WaitForTimeout(10000)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1WaitForTimeout(2000)
        self.actions.newTab1Click(self.closeBtn)
        self.actions.newTab1WaitForTimeout(5000)
        self.actions.newTab1GetByTextFirstClick("Narrator: Jane asks you to")
        self.actions.newTab1Click(self.submitBtn)
        self.actions.newTab1GetByTextFirstClick("Narrator: Joe further elaborates on")
        self.actions.newTab1Click(self.submitBtn)
        self.actions.newTab1GetByTextFirstClick("Narrator: Joe doesn't look happy with")
        self.actions.newTab1Click(self.submitBtn)
        self.actions.newTab1GetByTextFirstClick("Joe: I need to go to another meeting")
        self.actions.newTab1Click(self.submitBtn)
        self.actions.newTab1GetByTextFirstClick("Narrator: Joe says he does not have")
        self.actions.newTab1Click(self.submitBtn)
        self.actions.newTab1Click(self.NextBtn3)
        self.actions.newTab1Click(self.chekBoxOpt1)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.radioVeryHighBtn)
        self.actions.newTab1WaitForTimeout(2000)
        self.actions.newTab1Click(self.submitBtn1)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.NextBtn)
        # self.actions.click("//button[@class='btn bg-tw-pallet-color-88 text-white px-7 outline-none w-34']")
        print(self.actions.newTab1TextContent(self.endingText))

#UDT Text display

    def searchModuleUDT(self):
        self.actions.click(self.modulesTab)
        search_value = config['Admin']['ModuleNameUDT1']
        self.actions.fill(self.serchModule, search_value)
        self.actions.keyboard_press("Enter")

    def searchModuleUDTEdit(self):
        self.actions.click(self.modulesTab)
        # search_value = config['Admin']['ModuleNameUDT']
        self.actions.fill(self.serchModule, self.modName)
        self.actions.keyboard_press("Enter")

    def searchModuleUDTdel(self):
        self.actions.click(self.modulesBtn)
        self.actions.fill(self.serchModule, self.modName)
        self.actions.keyboard_press("Enter")

    def ableToSeeOutcomeUDT(self):
        actualModuleName = self.actions.text_content(self.firstRowSce)
        #expectedModuleName = "UDT's-1@ UDT's-2"
        expectedModuleName = config['Admin']['ModuleNameUDT1']
        assert expectedModuleName == actualModuleName, f"Expected message '{expectedModuleName}' but got '{actualModuleName}'"
        print("actualMessage", actualModuleName)
        print("expected message", expectedModuleName)

    def ableToSeeOutcomeUDTEdit(self):
        actualModuleName = self.actions.text_content(self.firstRowSce)
        #expectedModuleName = "UDT's-1@ UDT's-2"
        expectedModuleName = config['Admin']['ModuleNameUDT']
        assert expectedModuleName == actualModuleName, f"Expected message '{expectedModuleName}' but got '{actualModuleName}'"
        print("actualMessage", actualModuleName)
        print("expected message", expectedModuleName)


    def ableToSeeOutcomeUDTdel(self):
        actualModuleName = self.actions.text_content(self.firstRowSce)
        # expectedModuleName = "UDT's-1@ UDT's-2"
        expectedModuleName = config['Admin']['ModuleNameUDT']
        assert expectedModuleName == actualModuleName, f"Expected message '{expectedModuleName}' but got '{actualModuleName}'"
        print("actualMessage", actualModuleName)
        print("expected message", expectedModuleName)

    def verifiesUDTModuleFieldsPropelyDisplayedInUserProperly(self):
        self.actions.newTabAfterClickingAnElement(self.playSimula)
        self.actions.newTab1WaitForTimeout(3000)
        actualModuleName = self.actions.newTab1TextContent(self.moduleNameTxt)
        expectedModuleName = config['Admin']['ModuleNameUDT1']
        #expectedModuleName = "UDT's-1@ UDT's-2"
        assert expectedModuleName == actualModuleName, f"Expected message '{expectedModuleName}' but got '{actualModuleName}'"
        print("actualMessage", actualModuleName)
        print("expected message", expectedModuleName)


        actualheadingName = self.actions.newTab1TextContent(self.headingTxt)
        #expectedheadinName = "heading-8989"
        expectedheadinName=config['Admin']['Module Headingmod']
        assert expectedheadinName == actualheadingName, f"Expected message '{expectedheadinName}' but got '{actualheadingName}'"
        print("actualMessage", actualheadingName)
        print("expected message", expectedheadinName)


        actualsubheadingName = self.actions.newTab1TextContent(self.sideHeadingTxt)
        #expectedsubheadingName = "subheading-5665"
        expectedsubheadingName=config['Admin']['ReferenceNameContentSubHeadingmod']
        assert expectedsubheadingName == actualsubheadingName, f"Expected message '{expectedsubheadingName}' but got '{actualsubheadingName}'"
        print("actualMessage", actualsubheadingName)
        print("expected message", expectedsubheadingName)

        actualReferenceNameContentPageContent = self.actions.newTab1TextContent(self.contentPageRef)
        expectedactualReferenceNameContentPageContent =config['Admin']['ReferenceNameContentPageContentmod']
        assert expectedactualReferenceNameContentPageContent == actualReferenceNameContentPageContent, f"Expected message '{expectedactualReferenceNameContentPageContent}' but got '{actualReferenceNameContentPageContent}'"
        print("actualMessage", actualReferenceNameContentPageContent)
        print("expected message", expectedactualReferenceNameContentPageContent)

        actualModuleName = self.actions.newTab1TextContent(self.moduleNameTxt2)
        expectedModuleName = config['Admin']['ModuleNameUDT1']
        # expectedModuleName = "UDT's-1@ UDT's-2"
        assert expectedModuleName == actualModuleName, f"Expected message '{expectedModuleName}' but got '{actualModuleName}'"
        print("actualMessage", actualModuleName)
        print("expected message", expectedModuleName)
        self.actions.newTab1Click(self.nextBtnUDT)
        self.actions.newTab1WaitForTimeout(15000)
        # self.actions.newTab1Click(self.closeBtn)
        # self.actions.newTab1WaitForTimeout(5000)
        self.actions.newTab1GetByTextFirstClick("Narrator_03: Jane says the clients want")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Narrator_07: Before diving into the discussion, ")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Joe_09: My concerns are more future facing")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Joe_13: I need to think long-term before onboarding")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Narrator_16: Joe and you set up a meeting for next week")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1Click(self.NextBtn3)
        #self.actions.click(self.NextBtnAfterNarratorOptions)
        self.actions.newTab1Click(self.textCheckboxOption1OnReflectPage)
        self.actions.newTab1WaitForTimeout(2000)
        # self.actions.newTab1Click(self.chekBoxOpt1)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.radioVeryHighBtn)
        self.actions.newTab1WaitForTimeout(2000)
        self.actions.newTab1Click(self.submitBtn1)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.NextBtn)
        #self.actions.click("//button[@class='btn bg-tw-pallet-color-88 text-white px-7 outline-none w-34']")
        print(self.actions.newTab1TextContent(self.endingText))


    def clicksOnPathManagementAndSearchModuleUDT(self):
        self.actions.wait_for_timeout(3000)
        self.actions.click(self.pathManagement)
        # self.page.get_by_role("link", name=" Path Management").click()
        self.actions.wait_for_timeout(4000)
        self.actions.click(self.createPath)
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.static)
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.selectModulesCatAdm)

        search_value = config['Admin']['ModuleNameUDT']
        self.actions.fill(self.serchModule, search_value)
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(3000)
        self.actions.wait_for_timeout(3000)
        expectValue = config['Admin']['ModuleNameUDT']
        ModuleName = self.actions.text_content(self.moduleNameInModules)
        ModuleName1 = ModuleName.strip() if ModuleName else None
        assert expectValue == ModuleName1, f"Expected message '{expectValue}' but got '{ModuleName1}'"
        self.actions.click(self.checkBox)
        self.actions.click(self.saveNxtCatAdm)
        self.actions.click(self.createNewBtn)
        self.actions.wait_for_timeout(3000)

    def verifiesModuleDetailsProperlyDisplayedUDT(self):
        self.actions.click(self.OkayBtnCatAdm)
        self.actions.click(self.editModuleDetailsBtn)
        self.actions.wait_for_timeout(2000)
        actual = self.actions.text_context(self.modHeadPathMag)
        expectValue2 = config['Admin']['ModuleNameUDT']
        assert expectValue2 == actual, f"Expected message '{expectValue2}' but got '{actual}'"
        self.actions.wait_for_timeout(2000)
        actual = self.actions.input_value(self.headingPathEdit)
        expectValue = config['Admin']['ReferenceNameContentHeading']
        assert expectValue == actual, f"Expected message '{expectValue}' but got '{actual}'"
        self.actions.wait_for_timeout(2000)
        actual1 = self.actions.input_value(self.descPathEdit)
        expectvalue2 = "description is describing description's - description"
        assert expectvalue2 == actual1, f"Expected message '{expectvalue2}' but got '{actual1}'"
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.saveNxtCatAdm)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.OkayBtnCatAdm)

    def fillingPathDetailsUDT(self):
        self.actions.wait_for_timeout(2000)
        self.pathNameTxt = randomUtils.generate_random_string_with_prefix(length=10, prefix="test")
        self.actions.fill(self.pathName, self.pathNameTxt)
        self.actions.click(self.pathImage)
        self.actions.wait_for_timeout(10000)
        self.actions.locator_first_click(self.image)
        self.actions.wait_for_timeout(2000)
        #self.actions.fill(self.pathDesc, "UDT's-1@ UDT's-2")
        UDTpathDesc=config['admin']['UDTPathDesc']
        self.actions.fill(self.pathDesc,UDTpathDesc)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.pathName)
        self.actions.click(self.saveNxtCatAdm)
        self.actions.wait_for_timeout(2000)
        return self.pathNameTxt
    def clickEditIconOnSelectedModule(self):
        self.actions.click(self.editIconModules)
    def clickDelteIconOnModuleContentPage(self):
        self.actions.click(self.modulesBtn)
        self.actions.fill(self.serchModule, self.modName)
        self.actions.keyboard_press("Enter")
        self.actions.click(self.editModulespage)
        self.actions.click(self.deleteIconModuleContentPage1)
        self.actions.wait_for_timeout(3000)
        self.actions.click(self.yesDeleteModuleContentPage)
        self.actions.wait_for_timeout(3000)
        self.actions.click(self.deleteIconModuleContentPage1)
        self.actions.wait_for_timeout(3000)
        self.actions.click(self.yesDeleteModuleContentPage)
        self.actions.wait_for_timeout(3000)


    def verifyDeletedModuleNotFoundInModuleContent(self):

        if not self.actions.is_visible(self.contentpageVisible, "deleteModuleContentPage"):
               print("Not visible")

    def enterDetailsVersionVariantToggleInModuleCreation(self):
        self.actions.click(self.togVersionVariant)
        self.actions.wait_for_timeout(3000)
        self.actions.click(self.radioBtnVersion)
        self.actions.wait_for_timeout(3000)
        self.actions.click(self.parentModulevv)
        self.actions.wait_for_timeout(3000)
        self.actions.keyboard_press("ArrowDown")
        self.actions.wait_for_timeout(3000)
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(5000)
        actual = self.actions.input_value(self.moduleNameInput)
        self.ParentModulevv = self.actions.text_content(self.parentModulevv)
        print("parentModule captured:", self.ParentModulevv)
        self.actions.wait_for_timeout(8000)
        VersionDescription = config['Admin']['TogVersionDescription']
        self.actions.fill(self.versionDesc, VersionDescription)
        self.actions.wait_for_timeout(8000)
        self.actions.click(self.saveNextModDetails)
        return self.ParentModulevv

    def verifyVersionVariantToggleInModuleCreation(self):
        self.actions.wait_for_timeout(4000)
        self.actions.click(self.publishButton)
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(2000)
        # self.actions.click(self.publishButton)
        self.actions.click(self.modulesBtn)
        self.actions.fill(self.serchModule, self.ParentModulevv)
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(3000)
        self.actions.is_visible(self.moduleNameInModules, "version Module visible")

    def validateTogglesDisabledReportsUDT(self):
        print("Validation for Disabled Toggles need to be done")

    def clickEditIconOnModuleContentPage(self):
        self.actions.click(self.editIconModuleContentPage)


    def editHeadingSubHeadingContentOnModuleContentPage(self):
       # self.actions.click(self.editHeadingModuleContent)
        #self.actions.clear_text_field(self.editHeadingModuleContent)
        #self.actions.fill(self.editHeadingModuleContent,"")
        self.actions.clear_text_with_backspace(self.editHeadingModuleContent,10)
        editHeadingValue = config['Admin']['ReferenceNameContentHeadingEdit']
        self.actions.fill(self.editHeadingModuleContent, editHeadingValue)

        self.actions.click(self.editSubHeadingModuleContent)
        self.actions.clear_text_field(self.editSubHeadingModuleContent)
        editSubHeadingValue = config['Admin']['ReferenceNameContentSubHeadingEdit']
        self.actions.fill(self.editSubHeadingModuleContent, editSubHeadingValue)

        # self.actions.click(self.editContentModuleContent)
        # self.actions.clear_text_field(self.editContentModuleContent)
        # editContentValue = config['Admin']['ReferenceNameContentPageContentEdit']
        # self.actions.fill(self.editContentModuleContent, editContentValue)
        self.actions.click(self.saveNext)


    def clicksOnPlayBtnAndPlayUdtEditsimstudio(self):
        self.actions.newTabAfterClickingAnElement(self.playSimula)
        self.actions.newTab1WaitForTimeout(10000)

    def verifyHeadingSubContentOnPlaySimStudioprofileUDT(self):
        self.actions.newTabAfterClickingAnElement(self.playSimula)
        self.actions.newTab1WaitForTimeout(20000)
        expected = config['Admin']['ReferenceNameContentHeadingEdit']
        self.actions.newTab1WaitForTimeout(15000)
        actual=self.actions.newTab1TextContent(self.headingTheme)
        assert actual == expected, f"Expected message '{expected}' but got '{actual}'"

        expected = config['Admin']['ReferenceNameContentSubHeadingEdit']
        actual=self.actions.newTab1TextContent(self.subHeadingTheme)
        assert actual == expected, f"Expected message '{expected}' but got '{actual}'"

        # expected = config['Admin']['ReferenceNameContentPageContentEdit']
        # actual = self.actions.newTab1TextContent(self.contentTheme)
        # assert actual == expected, f"Expected message '{expected}' but got '{actual}'"

    def clickOnModuleSetup(self):
        self.actions.click(self.moduleSetupTab)

    def fillingParameterSettings2(self):
         self.actions.click(self.inputParam2togBtn)
         #self.actions.click(self.inputParamName)
         inputParamNameValue = config['Admin']['inputParamNameValue2']
         self.actions.fill(self.inputParamName, inputParamNameValue)
         inputParamDefValue2 = config['Admin']['inputParamDefValue2']
         self.actions.fill(self.inputParamDef, inputParamDefValue2)
         self.actions.click(self.inputPara2ShowResTogBtn)
         self.actions.click(self.savenextModsetup)

         self.actions.click(self.outputparam2togBtn)
         outputParamNameValue2 = config['Admin']['outputParamNameValue2']
         self.actions.fill(self.outputPrameterName2, outputParamNameValue2)
         outputParamDefValue2 = config['Admin']['outputParamDefValue2']
         self.actions.fill(self.outputPrameterDef2, outputParamDefValue2)
         self.actions.wait_for_timeout(10000)
         #self.actions.click(self.outputPara2ShowResTogBtn)
         self.actions.wait_for_timeout(5000)

    def fillingParameterSettings1(self):
        #self.actions.click(self.inputparam1togBtn)
        self.actions.wait_for_timeout(2000)

        inputParamNameValue1 = config['Admin']['inputParamNameValue1']
        self.actions.fill(self.inputPrameterName, inputParamNameValue1)
        inputParamDefValue1 = config['Admin']['inputParamDefValue1']
        self.actions.fill(self.inputParameterDef, inputParamDefValue1)
        self.actions.click(self.inputParaShowResTogBtn)
        self.actions.wait_for_timeout(2000)
        #self.actions.click(self.outputparam1togBtn)
        self.actions.wait_for_timeout(4000)
        outputParamNameValue1 = config['Admin']['outputParamNameValue1']
        self.actions.fill(self.outputPrameterName, outputParamNameValue1)
        outputParamDefValue1 = config['Admin']['outputParamDefValue1']
        self.actions.fill(self.outputPrameterDef, outputParamDefValue1)
        self.actions.click(self.outputParaShowResTogBtn)
        self.actions.wait_for_timeout(4000)
        self.actions.click(self.savenextModsetup)

    def fillingParameterSettings12(self):
        # self.actions.click(self.inputparam1togBtn)
        inputParamNameValue1 = config['Admin']['inputParamNameValue1']
        self.actions.fill(self.inputPrameterName, inputParamNameValue1)
        inputParamDefValue1 = config['Admin']['inputParamDefValue1']
        self.actions.fill(self.inputParameterDef, inputParamDefValue1)
        self.actions.click(self.inputParaShowResTogBtn)
        # self.actions.click(self.outputparam1togBtn)
        outputParamNameValue1 = config['Admin']['outputParamNameValue1']
        self.actions.fill(self.outputPrameterName, outputParamNameValue1)
        outputParamDefValue1 = config['Admin']['outputParamDefValue1']
        self.actions.fill(self.outputPrameterDef, outputParamDefValue1)
        self.actions.click(self.outputParaShowResTogBtn)
        #self.actions.click(self.savenextModsetup)



    def fillingParameterSettings1del(self):
        inputParamNameValue1 = config['Admin']['inputParamNameValue1']
        self.actions.fill(self.inputPrameterName, inputParamNameValue1)
        inputParamDefValue1 = config['Admin']['inputParamDefValue1']
        self.actions.fill(self.inputParameterDef, inputParamDefValue1)
        self.actions.click(self.inputParaShowResTogBtn)
        self.actions.wait_for_timeout(2000)
        #self.actions.click(self.outputparam1togBtn)
        self.actions.wait_for_timeout(4000)
        outputParamNameValue1 = config['Admin']['outputParamNameValue1']
        self.actions.fill(self.outputPrameterName, outputParamNameValue1)
        outputParamDefValue1 = config['Admin']['outputParamDefValue1']
        self.actions.fill(self.outputPrameterDef, outputParamDefValue1)
        self.actions.click(self.outputParaShowResTogBtn)
        self.actions.wait_for_timeout(4000)
        self.actions.click(self.savenextModsetup)


    def fillParametersBasedOnExisting(self):
        if isenabled(self.inputparam1togBtn):
            self.fillingParameterSettings2()
        else:
            self.fillingParameterSettings1()
            self.fillingParameterSettings2()


        self.actions.click(self.saveNext)

    def clickNextButtonUDTBeforePlayYT(self):
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1WaitForTimeout(2000)
        # self.actions.newTab1Click(self.closeBtn)
        # self.actions.newTab1WaitForTimeout(5000)
        self.actions.newTab1GetByTextFirstClick("Narrator_03: Jane says the clients want")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Narrator_07: Before diving into the discussion, ")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Joe_09: My concerns are more future facing")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Joe_13: I need to think long-term before onboarding")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Narrator_16: Joe and you set up a meeting for next week")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1Click(self.NextBtn3)
        self.actions.newTab1WaitForTimeout(2000)
        self.actions.newTab1Click(self.textCheckboxOption1OnReflectPage)
        self.actions.newTab1WaitForTimeout(2000)
        # self.actions.newTab1Click(self.chekBoxOpt1)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.radioVeryHighBtn)
        self.actions.newTab1WaitForTimeout(2000)
        self.actions.newTab1Click(self.submitBtn1)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1Click(self.NextBtn)

    def verifyInputParamsOnCheckYourFocusPage(self):
        print("validation to be done in canvas")

    def editModuleContentGameTypePage(self):
        self.actions.click(self.editgamtyperefOnModContent)

        textOfOutputParams1InModuleContentPage = self.actions.text_content(self.questionforoutparams1)
        extractedOutputParamsInModuleContentPagetext = textOfOutputParams1InModuleContentPage.split("Questions for ", 1)[1]
        expected=config['Admin']['outputParamNameValue1']
        actual=extractedOutputParamsInModuleContentPagetext
        assert actual == expected, f"Expected message '{expected}' but got '{actual}'"

        textOfOutputParams2InModuleContentPage = self.actions.text_content(self.questionforoutparams2)
        extractedOutputParams2InModuleContentPagetext = textOfOutputParams2InModuleContentPage.split("Questions for ", 1)[
            1]
        expected = config['Admin']['outputParamNameValue2']
        actual = extractedOutputParams2InModuleContentPagetext
        assert actual == expected, f"Expected message '{expected}' but got '{actual}'"

        self.expectedChkboxQstn=self.actions.input_value(self.checkboxqstn)

        self.expectedChkboxOptns1=self.actions.input_value(self.checkboxqstnoptions1)
        self.expectedChkboxOptns2=self.actions.input_value(self.checkboxqstnoptions2)

        return self.expectedChkboxQstn,self.expectedChkboxOptns1,self.expectedChkboxOptns2

    def saveNextModuleSetup(self):
        self.actions.click(self.saveNext)

    def  validateChkboxQstnOnReflectPage(self):
        self.actions.click(self.modulesTab)
        # search_value = config['Admin']['ModuleNameUDT']
        self.actions.fill(self.serchModule, self.modName)
        self.actions.keyboard_press("Enter")
        self.actions.newTabAfterClickingAnElement(self.playSimula)
        self.actions.newTab1WaitForTimeout(8000)
        #self.actions.newTab1Click(self.clickNextBtnBeforeYT)
        #self.actions.newTab1WaitForTimeout(8000)
        # self.actions.newTab1Click(self.closeBtn)
        # self.actions.newTab1WaitForTimeout(5000)
        self.actions.newTab1GetByTextFirstClick("Narrator_03: Jane says the clients want")
        self.actions.newTab1WaitForTimeout(4000)
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Narrator_07: Before diving into the discussion, ")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Joe_09: My concerns are more future facing")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Joe_13: I need to think long-term before onboarding")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Narrator_16: Joe and you set up a meeting for next week")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1Click(self.NextBtn3)
        #return self.expectedChkboxQstn,self.expectedChkboxOptns1,self.expectedChkboxOptns2

        #expectedChkboxQstnrv,expectedChkboxOptns1rv,expectedChkboxOptns2rv=self.verifyParametersinStep2AndStep3ModuleContent()
        self.actions.newTab1WaitForTimeout(8000)

        actualchkqstn=self.actions.text_content(self.textCheckboxEnabledQstnnOnReflectPage)
        expectedchkqstn= self.expectedChkboxQstn
        print("actualchkqstn",actualchkqstn)
        print("expectedchkqstn",expectedchkqstn)
        self.actions.newTab1WaitForTimeout(8000)

        assert actualchkqstn == expectedchkqstn, f"Expected message '{expectedchkqstn}' but got '{actualchkqstn}'"

        actual = self.actions.text_content(self.textCheckboxOption1OnReflectPage)
        expected = self.expectedChkboxOptns1
        print("actualChkboxOptns1", actual)
        print("expectedChkboxOptns1", expected)
        assert actual == expected, f"Expected message '{expected}' but got '{actual}'"
        self.actions.newTab1WaitForTimeout(8000)

        actual = self.actions.text_content(self.textCheckboxOption2OnReflectPage)
        expected = self.expectedChkboxOptns2
        print("actualChkboxOptns2", actual)
        print("expectedChkboxOptns2", expected)
        assert actual == expected, f"Expected message '{expected}' but got '{actual}'"



    def entersModuleStepThreeUdtDebriefVideoConfigFileAndValidate(self):
        self.actions.wait_for_timeout(3000)
        self.actions.click(self.addSection)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.content)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.contentPage1)
        self.actions.fill(self.reference, "Reference1")
        self.actions.fill(self.heading, "Heading")
        self.actions.fill(self.subheading, "Sub Heading")
        self.actions.wait_for_timeout(4000)
        self.actions.frame_locator_fill("iframe[title=\"Rich Text Area\\. Press ALT-0 for help\\.\"]", "#tinymce",
                                        "moduleDescription")
        self.actions.click(self.imageUrl)
        self.actions.click(self.image)

        self.actions.click(self.saveNexContentPagetModContent)
        self.actions.click(self.addSection)
        self.actions.click(self.content)
        self.actions.click(self.endpage)
        self.actions.fill(self.reference, "Reference1")
        self.actions.click(self.saveNextEndPageModContent)
        self.actions.wait_for_timeout(4000)
        self.actions.click(self.addSection)
        self.actions.wait_for_timeout(1500)
        self.actions.click(self.gameType)
        # actual = self.page.text_content(self.AIDiagnoGameType)
        # expected = "AI Diagnostic Gametype"
        # assert expected == actual, f"Expected message '{expected}' but got '{actual}'"
        self.actions.get_by_text_click("Universal DT Gametype")
        self.actions.fill(self.modRef, "UDT Reference")
        self.actions.fill(self.modScenarioName, "UDT Scenario Name")
        self.actions.frame_locator_fill("iframe[title=\"Rich Text Area\\. Press ALT-0 for help\\.\"]", "#tinymce",
                                        "UDT moduleDescription")
        self.actions.click(self.filePathElement)
        self.actions.wait_for_timeout(4000)
        self.actions.set_input_files(self.filePathElement,
                                     r"C:\NewEnp\Enparadigm\Enparadigm\Enparadigm\behaveProject\Upload\Thumnail\UDTSample.xlsx")

        self.actions.wait_for_timeout(12000)

        textOfOutputParams1InModuleContentPage = self.actions.text_content(self.questionforoutparams1)
        extractedOutputParamsInModuleContentPagetext = \
        textOfOutputParams1InModuleContentPage.split("Questions for ", 1)[1]
        expected = config['Admin']['outputParamNameValue1']
        actual = extractedOutputParamsInModuleContentPagetext
        assert actual == expected, f"Expected message '{expected}' but got '{actual}'"

        # textOfOutputParams2InModuleContentPage = self.actions.text_content(self.questionforoutparams2)
        # extractedOutputParams2InModuleContentPagetext = \
        # textOfOutputParams2InModuleContentPage.split("Questions for ", 1)[
        #     1]
        # expected = config['Admin']['outputParamNameValue2']
        # actual = extractedOutputParams2InModuleContentPagetext
        # assert actual == expected, f"Expected message '{expected}' but got '{actual}'"

        SliderQuestion1createC=config['Admin']['SliderQuestion1create']
        self.actions.fill(self.sliderQuestionInput1, SliderQuestion1createC)
        self.actions.click(self.enableCheckboxUdtTogBtn)

        # SliderQuestion2create = config['Admin']['SliderQuestion2create']
        # self.actions.fill(self.sliderQuestionInput2, SliderQuestion2create)
        # #self.actions.click(self.enableCheckboxUdtTogBtn)

        CheckboxEnableQuestion1create = config['Admin']['CheckboxEnableQuestion1create']
        self.actions.fill(self.checkBoxQuest, CheckboxEnableQuestion1create)
        Option1ChkboxEnabledAns=config['Admin']['Option1ChkboxEnabledAns']
        self.actions.fill(self.opt1, Option1ChkboxEnabledAns)
        Option2ChkboxEnabledAns = config['Admin']['Option2ChkboxEnabledAns']
        self.actions.fill(self.opt2, Option2ChkboxEnabledAns)

        self.actions.click(self.AddOptionalOption)
        Option3ChkboxEnabledAns = config['Admin']['Option3ChkboxEnabledAns']
        self.actions.fill(self.opt3optional,Option3ChkboxEnabledAns)

        self.actions.wait_for_timeout(5000)

        self.actions.click(self.enableDebriefVideoToggleBtn)
        self.actions.wait_for_timeout(5000)

        DebriefUDTVideoTitle=config['Admin']['DebriefUDTVideoTitle']
        self.actions.fill(self.videoTitle, DebriefUDTVideoTitle)

        DebriefUDTVideoSubTitle = config['Admin']['DebriefUDTVideoSubTitle']
        self.actions.fill(self.videoSubTitle, DebriefUDTVideoSubTitle)

        DebriefUDTVideoRefName = config['Admin']['DebriefUDTVideoRefName']
        self.actions.frame_locator_fill(self.videoFrame, self.videoRefNameInput, DebriefUDTVideoRefName)
        # 1.Image
        self.actions.set_input_files_in_frame(self.videoFrame, self.videoThumbnailInput,
                                              r"C:\NewEnp\Enparadigm\Enparadigm\Enparadigm\behaveProject\Upload\Thumnail\LandscapeImage.jpg")
        self.actions.wait_for_timeout(5000)
        # 2.Video
        self.actions.set_input_files_in_frame(self.videoFrame, self.videoInput,
                                              r"C:\NewEnp\Enparadigm\Enparadigm\Enparadigm\behaveProject\Upload\Video\Dear.mp4")
        self.actions.wait_for_timeout(15000)
        self.actions.set_input_files_in_frame(self.videoFrame, self.videoInput,
                                              r"C:\NewEnp\Enparadigm\Enparadigm\Enparadigm\behaveProject\Upload\Video\LandscapeVideo.webm")

        DebriefUDTVideoDesc = config['Admin']['DebriefUDTVideoDescription']
        self.actions.frame_inside_frame_type(self.videoFrame, "iframe[title='Rich Text Area. Press ALT-0 for help.']",
                                             "#tinymce", DebriefUDTVideoDesc)
        self.actions.wait_for_timeout(10000)
        self.actions.frame_locator_click(self.videoFrame, self.uploadVideoBtn)
        self.actions.wait_for_timeout(15000)

        self.actions.wait_for_timeout(3000)
        self.actions.click(self.saveNext)
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.publishButton)
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.okayBtn)

    def searchModuleUDTwithdebriefEnabled(self):
        self.actions.click(self.modulesBtn)
        self.actions.fill(self.serchModule, self.modName)
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(3000)
        expectValue = self.modName
        ActualModuleName = self.actions.text_content(self.moduleNameInModules)
        self.actions.assertValues(ActualModuleName, expectValue)
        self.actions.newTabAfterClickingAnElement(self.playSimula)
        self.actions.newTab1WaitForTimeout(15000)

    def verifyInputParamsChkboxQuestionsOnSimstudioPlayPage(self):
        self.actions.click(self.modulesBtn)
        self.actions.fill(self.serchModule, self.modName)
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(3000)
        expectValue = self.modName
        ActualModuleName = self.actions.text_content(self.moduleNameInModules)
        self.actions.assertValues(ActualModuleName, expectValue)
        self.actions.newTabAfterClickingAnElement(self.playSimula)
        self.actions.newTab1WaitForTimeout(15000)
        self.actions.newTab1Click(self.clickNextBtnBeforeYT)
        #self.actions.click(self.playYtVideoBtn)
        #self.actions.click(self.pauseYtVideoBtn)
        self.actions.newTab1GetByTextFirstClick("Narrator_03: Jane says the clients want")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Narrator_07: Before diving into the discussion, ")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Joe_09: My concerns are more future facing")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Joe_13: I need to think long-term before onboarding")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1GetByTextFirstClick("Narrator_16: Joe and you set up a meeting for next week")
        self.actions.newTab1Click(self.submitBtnNarrator)
        self.actions.newTab1Click(self.NextBtn3)
        ActualQstnOnReflect=self.actions.text_content(self.qstnTextOnReflectPage)
        ExpectedQstnOnModuleContent = config['Admin']['CheckboxEnableQuestion1create']
        assert ActualQstnOnReflect == ExpectedQstnOnModuleContent, f"Expected message '{ExpectedQstnOnModuleContent}' but got '{ActualQstnOnReflect}'"

        Actualoption1chkboxOnReflectPage = self.actions.text_content(self.option1chkboxOnReflectPage)
        Expectedoption1chkboxOnReflectPage = config['Admin']['Option1ChkboxEnabledAns']
        assert Actualoption1chkboxOnReflectPage == Expectedoption1chkboxOnReflectPage, f"Expected message '{Expectedoption1chkboxOnReflectPage}' but got '{Actualoption1chkboxOnReflectPage}'"

        Actualoption2chkboxOnReflectPage = self.actions.text_content(self.option2chkboxOnReflectPage)
        Expectedoption2chkboxOnReflectPage = config['Admin']['Option2ChkboxEnabledAns']
        assert Actualoption2chkboxOnReflectPage == Expectedoption2chkboxOnReflectPage, f"Expected message '{Expectedoption2chkboxOnReflectPage}' but got '{Actualoption2chkboxOnReflectPage}'"

        Actualoption3chkboxOnReflectPage = self.actions.text_content(self.option3chkboxOnReflectPage)
        Expectedoption3chkboxOnReflectPage = config['Admin']['Option3ChkboxEnabledAns']
        assert Actualoption3chkboxOnReflectPage == Expectedoption3chkboxOnReflectPage, f"Expected message '{Expectedoption3chkboxOnReflectPage}' but got '{Actualoption3chkboxOnReflectPage}'"

        #self.actions.click(self.chkboxNextBtn)

        self.actions.newTab1Click(self.textCheckboxOption1OnReflectPage)
        self.actions.newTab1WaitForTimeout(2000)

        self.actions.newTab1Click(self.textCheckboxOption1OnReflectPage)

        self.actions.newTab1WaitForTimeout(2000)
        # self.actions.newTab1Click(self.chekBoxOpt1)
        self.actions.click(self.NextBtn)


        ActualsliderQstnOnEffectPage=self.actions.text_content(self.sliderQstnOnEffectPage)
        ExpectedsliderQstnOnEffectPage=config['Admin']['SliderQuestion1create']
        assert ActualsliderQstnOnEffectPage == ExpectedsliderQstnOnEffectPage, f"Expected message '{ExpectedsliderQstnOnEffectPage}' but got '{ActualsliderQstnOnEffectPage}'"

        self.actions.newTab1Click(self.radioVeryHighBtn)
        self.actions.newTab1WaitForTimeout(2000)
        self.actions.newTab1Click(self.submitBtn1)
        #self.actions.click(self.radioVeryHighBtn)
        #self.actions.click(self.slderSubmitOnEffectPage)
        self.actions.click(self.sliderNextBtn)
        self.actions.click(self.sliderNextBtn2)

        ExpectedDebriefVideoTitle=config['Admin']['DebriefUDTVideoTitle']
        ActualDebriefVideoTitle=self.actions.text_content(self.debriefVideoTitleOnSimProfile)
        assert ActualDebriefVideoTitle == ExpectedDebriefVideoTitle, f"Expected message '{ExpectedDebriefVideoTitle}' but got '{ActualDebriefVideoTitle}'"

        ExpectedDebriefVideoSubTitle = config['Admin']['DebriefUDTVideoSubTitle']
        ActualDebriefVideoSubTitle = self.actions.text_content(self.debriefVideoSubTitleOnSimProfile)
        assert ActualDebriefVideoSubTitle == ExpectedDebriefVideoSubTitle, f"Expected message '{ExpectedDebriefVideoSubTitle}' but got '{ActualDebriefVideoSubTitle}'"

        self.actions.click(self.transcriptDebriefDesc)
        ExpectedDebriefUDTVideoDesc = config['Admin']['DebriefUDTVideoDescription']
        ActualDebriefUDTVideoDesc = self.actions.text_content(self.debriefVideoDescOnSimProfile)
        assert ActualDebriefUDTVideoDesc == ExpectedDebriefUDTVideoDesc, f"Expected message '{ExpectedDebriefUDTVideoDesc}' but got '{ActualDebriefUDTVideoDesc}'"


    def canvas(self):
        print(self.actions.captureTextFromCanvas())

    def verifyNarratorOptionsOnDeepdivePage(self):
     Actualoption1=self.actions.text_content(self.NarratorDeepdive)
     assert Actualoption1 == self.option1, f"Expected message '{self.option1}' but got '{Actualoption1}'"
     self.actions.click(self.NextarrowDeepdive)

     Actualoption2=self.actions.text_content(self.NarratorDeepdive)
     assert Actualoption2 == self.option2, f"Expected message '{self.option2}' but got '{Actualoption2}'"
     self.actions.click(self.NextarrowDeepdive)

     Actualoption3 = self.actions.text_content(self.NarratorDeepdive)
     assert Actualoption3 == self.option3, f"Expected message '{self.option3}' but got '{Actualoption3}'"
     self.actions.click(self.NextarrowDeepdive)

     Actualoption4 = self.actions.text_content(self.NarratorDeepdive)
     assert Actualoption4 == self.option4, f"Expected message '{self.option4}' but got '{Actualoption4}'"
     self.actions.click(self.NextarrowDeepdive)

     Actualoption5 = self.actions.text_content(self.NarratorDeepdive)
     assert Actualoption5 == self.option5, f"Expected message '{self.option5}' but got '{Actualoption5}'"
     self.actions.click(self.NextarrowDeepdive)
     self.actions.click(self.NextBtn)




