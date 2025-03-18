from time import sleep


from pages.base_page import BasePage
import configparser

from utils import randomUtils

from utils.shared_data import write_to_file
import pyperclip

from pages.WebActions import WebActions

config = configparser.ConfigParser()
config.read('config.ini')


class simStudioAdminPage:
    def __init__(self, page, browser_context):
        #xpaths
        self.actions = WebActions(page, browser_context)
        self.moduleNameInpathmanage="//td[normalize-space()='chkpath details']"
        self.sign_in_with_google_btn = "//div[@class='ssJRIf']"
        self.enter_username_input = "//input[@id='identifierId']"
        self.next_btn = "(//div[@class='VfPpkd-RLmnJb'])[2]"
        self.enter_password_input = "//input[@type='password']"
        self.simstudio_dashboard_txt = "(//div[text()='Dashboard'])[1]"
        self.SimAdminSearch_btn = "//input[@placeholder='Search...']"
        self.ethosSimAIcoacplay_btn = "//img[@data-module='1f3b0664-2fa4-4091-aa24-a6045e9426ea']"
        self.moduleHeading_txt = "//div[text()='Ethos (AI)']"
        self.ethosAIC_txt = "//td[text()='Ethos (AI)']"
        self.nxt_btn = "//div[@class='content_page1_container']/div/div/div[2]/button"
        self.beginRound1_btn = "//button[text()='Begin Round 1']"
        self.playvideo_btn = "//span[text()='Play Video']"
        self.mute_btn = "(//img[@alt='button'])[1]"
        self.fastmode_btn = "(//img[@alt='button'])[2]"
        self.videonxt_btn = "//div[@id='next']"
        self.textresponse_input = "//textarea[@id='user_input']"
        self.next_btn1 = "(//div[contains(@class,'flex bg-tw-pallet-color-36 hover:bg-tw-pallet-color-37 cursor-pointer p-1 rounded-full w-fit items-center ')])[3]/div"
        self.scenario_btn = "//div[@id='scenario']"
        self.yourresponse_btn = "//div[@id='your_response']"
        self.yourResponse_txt = "//div[text()='Thank you for your interest, Mrs. Ellis. While it offers excellent rewards, it also comes with higher annual fees than some of our other cards. Would that be a challenge for you, considering your fixed income? If so, I can recommend a few other cards based on your needs']"
        self.sampleResponse = "//div[@id='ideal_response']"
        self.afterscenarioNxt_btn = "//div[@id='submit']"
        self.consolodatedDebrief_txt = "//div[text()='Consolidated Debrief']"
        self.consolodatedDebrief_nxt_btn = "//div[text()='Next']"
        self.previous_btn = "//div[text()='Previous']"
        self.completedRound1_txt = "//div[@class='heading theme-font16']"
        self.scenarioEffectiveness = "//div[text()='Scenario Effectiveness']/following-sibling::div"
        self.avgModuleEffectiveness = "//div[text()='Avg Module Effectiveness*']/following-sibling::div"
        self.rank = "//div[text()='Your Rank*']/following-sibling::div"
        self.createModuleBtn = "//span[text()='Module']"
        self.createModuleTxt = "//div[text()='CREATE MODULE']"
        self.pageHeader = "(//div[@class='flex justify-between items-center']/div)[1]"
        self.saveNext = "//span[text()='Save & Next']"
        self.moduleNameInput = "#module_name"
        self.moduleHeadInput = "#module_heading"
        self.moduleDescInput = "#module_description"
        self.moduleTimeDrpDwn = "#module_time_needed"
        self.gameTypeDrpdwn  = "#select_game_type"
        self.colorPalatteDrpdwn = "#select_theme_type"
        self.addSection = "//span[text()='Add Section']"
        self.content = "//span[text()='Content']"
        self.contentPage1 = "//span[text()='content page 1']"
        self.reference = "#reference_name"
        self.heading = "#heading"
        self.subheading = "#subheading"
        self.contenttt = "#tinymce"
        self.imageUrl = "#image_url"
        self.image = "//img[1]"
        self.endpage= "//span[text()='end page 1']"
        self.publishButton = "//span[text()='Publish Module For Testing']"
        self.okayBtn = "//button[normalize-space()='Ok']"
        self.fourthreportBtn = "//div[text()='Step 4: Report']"
        self.reportTxt = "//div[@id='create_module_step_4']/div[1]"
        self.proceedBtn = "//button[text()='Proceed']"
        self.sucTxt = "#swal2-html-container"
        self.saveNextBtn = "//button[text()='Save & Next']"
        self.modulesBtn = "//span[text()='Modules']"
        self.serchModule = "//input[@placeholder='Search...']"
        self.moduleNameInModules = "//td[@data-testid='dashboard-module-name-0']"
        self.moduleTypeInModules = "//table[@class='svelte-15iwbfd']//td[2]"
        self.moduleStatusInMpdules = "//table[@class='svelte-15iwbfd']//td[3]"
        self.publishIcon = "#publish_module_to_catalyx"
        self.yesBtn = "//button[normalize-space()='Yes']"
        self.OkBtn = "//button[text()='OK']"
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
        self.editModuleDetailsBtn ="(//div[@data-testid='accordion-item'])[16]"
        self.headingPathEdit = "(//textarea[@placeholder='Enter some long form content.'])[1]"
        self.descPathEdit = "(//textarea[@placeholder='Enter some long form content.'])[2]"
        self.OkayBtnCatAdm = "//button[normalize-space()='OK']"
        self.checkBox2  = "(//input[@type='checkbox'])[2]"
        self.publishCatAdm = "//button[normalize-space()='PUBLISH']"
        self.managePath = "//span[text()='Manage Path']"
        self.cohortmngmnt_btn = "//div[text()='Cohort Management']"
        self.cohortmngmnt_btn1 = "//p[text()='Cohort Management ']"
        self.createcohortmngmnt_btn = "//div[text()='Create Catalyx Cohort']"
        self.cohortname_input = "//input[@placeholder='Cohort Name']"
        self.selectCompany_drpdwn = "(//span[@class='select2-selection__rendered' and @title='Select'])[8]"
        self.companyMadhuri = "//li[text()='testmadhuri']"
        self.hrname_input = "//input[@placeholder='HR Name']"
        self.hremail_input = "//input[@placeholder='HR Email']"
        self.inputdate = "//input[@id='datepicker-startdate']"
        self.date = "//a[text()='8']"
        self.deadlinedate = "//input[@id='datepicker-deadline']"
        self.enddateyr = "//select[@class='ui-datepicker-year']"
        self.selectyr = "//select[@class='ui-datepicker-year']"
        self.chooseyr_btn = "//option[text()='2026']"
        self.enddate_btn = "//a[text()='17']"
        self.owner_drpdwn = "(//span[@class='select2-selection__arrow' and @role='presentation'])[14]"
        self.pallavi_option = "//option[text()='Pallabi']"
        self.learningpath_drpdwn = "(//span[@class='select2-selection__arrow' and @role='presentation'])[17]"
        self.lucid_option = "//li[text()='Lucid - assertiveness at work']"
        self.noOfLicencesInCohort = "//input[@id='no_of_licenses']"
        self.createcohort_btn = "//input[@value='Create Cohort']"
        self.cominput = "//input[@class='select2-search__field']"
        self.pathDrpdowncohort = "(//span[text()='Select'])[11]"
        self.selectDeal_drpdwn = "//span[@id='select2-o5nq-container']"
        self.madhuriDeal_btn = "//li[text()='testm']"
        self.gameType = "//span[text()='Gametype']"
        self.AIcoachGameType = "//span[text()='AI Coach Gametype']"
        self.gamTypHead = "#heading"
        self.gamTypQues = "(//textarea[@id='hint'])[1]"
        self.gamTypHint = "(//textarea[@id='hint'])[2]"
        self.gamTypIdealResp = "//textarea[@id='response']"
        self.gamTypeHeadTxt = "//input[@id='heading']/preceding-sibling::span"
        self.gamTypeDescTxt = "//label[@for='description']/span"
        self.gamTypeQuesTxt = "(//textarea[@id='hint'])[1]/preceding-sibling::span"
        self.gameTypeHintTxt = "(//textarea[@id='hint'])[2]/preceding-sibling::span"
        self.gameTypeRespTxt = "(//textarea[@id='response'])[1]/preceding-sibling::span"
        self.gameTypeFileBtn = "//span[normalize-space()='File']"
        self.gameTypeEditBtn = "//span[normalize-space()='Edit']"
        self.gameTypeViewBtn = "//span[normalize-space()='View']"
        self.gameTypeInsertBtn = "//span[normalize-space()='Insert']"
        self.gameTypeFormatBtn = "//span[normalize-space()='Format']"
        self.gameTypeTableBtn = "//span[normalize-space()='Table']"
        self.gameTypeHelpBtn = "//span[normalize-space()='Help']"
        self.boldBtn = "//button[@title='Bold']"
        self.italic = "//button[@title='Italic']"
        self.backgrundClr = "//div[@title='Background color']"
        self.alignLeft = "//button[@title='Align left']"
        self.alignCenter = "//button[@title='Align center']"
        self.alignRight = "//button[@title='Align right']"
        self.justify = "//button[@title='Justify']"
        self.bulletPoint = "//div[@title='Bullet list']"
        self.numberedList = "//div[@title='Numbered list']"
        self.decreased = "//button[@title='Decrease indent']"
        self.clearFormatting = "//button[@title='Clear formatting']"
        self.tableIcon = "//button[@title='Table']"
        self.videoRadioBtn = "//label[@class='flex items-center space-x-2 my-2 mx-12']//input[@name='radio-direct-0']"
        self.videoRefName ="//span[text()='Video Reference Name']"
        self.videoThumbnail = "//span[normalize-space()='Thumbnail *']"
        self.video = "//span[normalize-space()='Video *']"
        self.videoTrans = "//span[contains(text(), 'Video Transcript')]"
        self.iframeVideo1 = "#videoPlayerFormCoach_0"
        self.iframeSecondSecenario = "#videoPlayerFormCoach_1"
        self.iframeVideo2 = "#transcript_ifr"
        self.videoRefNameInput = "//input[@placeholder='Name']"
        self.videoThumbnailInput = "(//input[@type='file'])[1]"
        self.videoInput = "(//input[@type='file'])[2]"
        self.createUserList_btn = "//li[@id='createUserListItem']"
        self.parWeight1 = "(//input[@inputmode='numeric'])[1]"
        self.parWeight2 = "(//input[@inputmode='numeric'])[2]"
        self.parWeight3 = "(//input[@inputmode='numeric'])[3]"
        self.parWeight4 = "(//input[@inputmode='numeric'])[4]"
        self.addScenarioBtn = "//span[normalize-space()='Add a Scenario']"
        self.clickToCollapse = "//div[normalize-space()='Click to collapse']"
        self.clickToCollapse2 = "(//div[normalize-space()='Click to collapse'])[5]"
        self.company_drpdwn = "(//span[@title='All'])[2]"
        self.cominput = "//input[@class='select2-search__field']"
        self.cohort_drpdwn = "(//span[@role='combobox'])[11]"
        # self.madhuri_cmpny = "//li[text()='testmadhuri']"
        self.madhuri_cmpny = "//li[text()='testmadhuri']"
        self.magicLink_btn = "(//button[text()='Magic Link'])[1]"
        self.copyMagicLink_txt = "//button[text()='Copy Magic Link']"
        self.googleSignInFrame = "iframe[title=\"Sign in with Google Button\"]"



    def navigate_to_url(self, url):
        self.actions.goto(url)
        sleep(9)

    def sign_in_with_google(self, adminUsername: str, adminPassword: str):
        self.actions.newTabAfterClickingAnElementWhichIsInFrame(self.googleSignInFrame,
                                                                "Sign in with Google")
        self.actions.new_tab1_get_by_label_fill("Email or phone", adminUsername)
        self.actions.newTab1_get_by_role("button", "Next")
        self.actions.new_tab1_get_by_label_fill("Enter your password", adminPassword)
        self.actions.newTab1_get_by_role("button", "Next")
        self.actions.wait_for_timeout(30000)


    def validateSimstudioAdminDashboard(self):
        self.actions.is_visible(self.simstudio_dashboard_txt, "Simstudio Dashboard")
        self.actions.text_content(self.simstudio_dashboard_txt)

    def clicksOnSearch(self):
        self.actions.fill("[placeholder='Search...']", "Ethos")
        self.actions.keyboard_press("Enter")

    def clickOnPlaybutton(self):
        self.actions.get_by_role_get_by_role_click("row","Ethos (AI) AI Coach Published 5 Jul 2024, 9:00 PM edit_icon copy_link "
                                   "feedback_icon hide_icon play_simulation",
            "img", "play_simulation")
        print("Ethos paly simulation button clicked")

    def validateAiCoachPage(self):
        self.actions.wait_for_timeout(3000)
        expected_message = config['Admin']['Ethos_Validation'].format(Ethos=self.moduleHeading_txt)
        success_message = self.actions.text_content(self.ethosAIC_txt)
        print("Actual_msg :", success_message)
        print("expected_message :", expected_message)
        assert expected_message == success_message, f"Expected message '{expected_message}' but got '{success_message}'"

    def clicksOnNext(self):
        self.actions.newTab1_after_get_by_role_get_by_role_click("row", "Ethos (AI) AI Coach Published 5 Jul 2024, 9:00 PM edit_icon copy_link "
                                       "feedback_icon hide_icon play_simulation", "img", "play_simulation")
        self.actions.newTab1_get_by_role("button", "Next")
        print("Begin Round 1 button clicked")
        print("Next button clicked")
        self.actions.newTab1_get_by_role("button", "Begin Round 1")
        self.actions.newTab1_get_by_role("button", "Close")
        print("closed the popup")
        self.actions.newTab1WaitForTimeout(10000)
        self.actions.newTab1GetByTextClick("Next")
        print("next after popup closed")
        self.actions.newTab1_get_by_role("img", "transcript_icon")
        print("transcript icon clicked")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        print("Speaker icon is clicked")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker","img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speed","img", "button")
        print("speed icon is clicked")
        self.actions.newTab1_get_by_placeholder_fill("Type your response",
            "Thank you for your interest, Mrs. Ellis. While it offers excellent rewards, it also comes with higher "
            "annual fees than some of our other cards. Would that be a challenge for you, considering your fixed "
            "income? If so, I can recommend a few other cards based on your needs")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speed", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1GetByTextClick("Get a hint")
        self.actions.newTab1_get_by_role_nth_click("img", "hint_icon", 1)
        print("Get a hint button is clicked")
        self.actions.newTab1GetByTextClick("Submit")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1GetByTextClick("Scenario")
        print("Scenario button is clicked")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1GetByTextClick("Your Response")
        print("Your Response button is clicked")
        self.actions.newTab1GetByTextClick("Sample Response")
        print("Sample Response button is clicked")
        self.actions.newTab1GetByTextClick("Next")
        self.actions.newTab1_get_by_role("button", "Close")
        self.actions.newTab1_get_by_role("img", "transcript_icon")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speed", "img", "button")
        self.actions.newTab1GetByTextClick("Next")
        print("Scenario debreif next button is clicked")
        self.actions.newTab1_get_by_placeholder_fill("Type your response",
            "I understand the urgency and appreciate our long-standing relationship. However, falsifying income is "
            "fraud and could have serious consequences for both of us. Can you help me understand what your current "
            "income level is? I can help you with a suitable solution accordingly.")

        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speed", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1GetByTextClick("Get a hint")
        self.actions.newTab1_get_by_role_nth_click("img", "hint_icon", 1)
        self.actions.newTab1GetByTextClick("Submit")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1GetByTextClick("Next")
        print("next1 clicked")
        self.actions.newTab1GetByTextClick("Next")
        print("next2 clicked")
        self.actions.newTab1WaitForTimeout(30000)


    def validateRoundCompleted(self):
        self.actions.is_visible(self.completedRound1_txt, "Complete Round")
        print("completed Round1 text is visible")


    def entersEmptyScenario1Response(self):
        self.actions.newTab1_after_get_by_role_get_by_role_click("row",
                                                                 "Ethos (AI) AI Coach Published 5 Jul 2024, 9:00 PM edit_icon copy_link "
                                                                 "feedback_icon hide_icon play_simulation", "img",
                                                                 "play_simulation")
        self.actions.newTab1_get_by_role("button", "Next")
        print("Begin Round 1 button clicked")
        print("Next button clicked")
        self.actions.newTab1_get_by_role("button", "Begin Round 1")
        self.actions.newTab1_get_by_role("button", "Close")
        print("close the popup")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_get_by_role("img", "transcript_icon")
        print("transcript icon clicked")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        print("Speaker icon is clicked")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speed", "img", "button")
        print("speed icon is clicked")
        # removed entering first scenario response
        self.actions.newTab1GetByTextClick("Next")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speed", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1GetByTextClick("Get a hint")
        self.actions.newTab1_get_by_role_nth_click("img", "hint_icon", 1)
        self.actions.newTab1GetByTextClick("Submit")
        print("check 1")




    def entersEmptyScenario2Response(self):
        self.actions.newTab1_after_get_by_role_get_by_role_click("row",
                                                                 "Ethos (AI) AI Coach Published 5 Jul 2024, 9:00 PM edit_icon copy_link "
                                                                 "feedback_icon hide_icon play_simulation", "img",
                                                                 "play_simulation")
        self.actions.newTab1_get_by_role("button", "Next")
        print("Begin Round 1 button clicked")
        print("Next button clicked")
        self.actions.newTab1_get_by_role("button", "Begin Round 1")
        self.actions.newTab1_get_by_role("button", "Close")
        print("close the popup")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_get_by_role("img", "transcript_icon")
        print("transcript icon clicked")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        print("Speaker icon is clicked")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speed", "img", "button")
        print("speed icon is clicked")
        self.actions.newTab1GetByTextClick("Next")
        self.actions.newTab1_get_by_placeholder_fill("Type your response",
                                                     "Thank you for your interest, Mrs. Ellis. While it offers excellent rewards, it also comes with higher "
                                                     "annual fees than some of our other cards. Would that be a challenge for you, considering your fixed "
                                                     "income? If so, I can recommend a few other cards based on your needs")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speed", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1GetByTextClick("Get a hint")
        self.actions.newTab1_get_by_role_nth_click("img", "hint_icon", 1)
        print("Get a hint button is clicked")
        self.actions.newTab1GetByTextClick("Submit")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1GetByTextClick("Scenario")
        print("Scenario button is clicked")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1GetByTextClick("Your Response")
        print("Your Response button is clicked")
        self.actions.newTab1GetByTextClick("Sample Response")
        print("Sample Response button is clicked")
        self.actions.newTab1GetByTextClick("Next")
        self.actions.newTab1_get_by_role("img", "transcript_icon")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speed", "img", "button")
        self.actions.newTab1GetByTextClick("Next")
        print("Scenario debreif next button is clicked")

        # enters empty scenario 2 response
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speed", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1GetByTextClick("Get a hint")
        self.actions.newTab1_get_by_role_nth_click("img", "hint_icon", 1)


    def submitButtonDisabled(self):
        if not self.actions.is_visible("//div[contains(@class,'text-white text-center text-xl w-32 max-sm:w-20 font-bold leading-tight')]","submit disable chk"):
            print("Submit Button is Disabled")



    def entersRandomScenario1Response(self, response1:str):
        self.actions.newTab1_after_get_by_role_get_by_role_click("row",
                                                                 "Ethos (AI) AI Coach Published 5 Jul 2024, 9:00 PM edit_icon copy_link "
                                                                 "feedback_icon hide_icon play_simulation", "img",
                                                                 "play_simulation")
        self.actions.newTab1_get_by_role("button", "Next")
        print("Begin Round 1 button clicked")
        print("Next button clicked")
        self.actions.newTab1_get_by_role("button", "Begin Round 1")
        self.actions.newTab1_get_by_role("button", "Close")
        print("close the popup")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_get_by_role("img", "transcript_icon")
        print("transcript icon clicked")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        print("Speaker icon is clicked")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speed", "img", "button")
        print("speed icon is clicked")
        self.actions.newTab1GetByTextClick("Next")
        self.actions.newTab1_get_by_placeholder_fill("Type your response",response1)
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speed", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1GetByTextClick("Get a hint")
        self.actions.newTab1_get_by_role_nth_click("img", "hint_icon", 1)
        print("Get a hint button is clicked")
        self.actions.newTab1GetByTextClick("Submit")

        self.actions.newTab1WaitForTimeout(5000)
        scenarioEffectivenesssTxt = self.actions.newTab1TextContent(self.scenarioEffectiveness)
        print(scenarioEffectivenesssTxt)
        avgModuleEffectivenessTxt = self.actions.newTab1TextContent(self.avgModuleEffectiveness)
        print(avgModuleEffectivenessTxt)
        rankTxt = self.actions.newTab1TextContent(self.rank)
        print(rankTxt)



    def validateScore(self):
        self.actions.newTab1_is_visible(self.completedRound1_txt,"validate score text")
        print("Score Details Noted")

    def entersRandomScenario2Response(self, response2:str):
        self.actions.newTab1_after_get_by_role_get_by_role_click("row",
                                                                 "Ethos (AI) AI Coach Published 5 Jul 2024, 9:00 PM edit_icon copy_link "
                                                                 "feedback_icon hide_icon play_simulation", "img",
                                                                 "play_simulation")
        self.actions.newTab1_get_by_role("button", "Next")
        print("Begin Round 1 button clicked")
        print("Next button clicked")
        self.actions.newTab1_get_by_role("button", "Begin Round 1")
        self.actions.newTab1_get_by_role("button", "Close")
        print("close the popup")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_get_by_role("img", "transcript_icon")
        print("transcript icon clicked")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        print("Speaker icon is clicked")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speed", "img", "button")
        print("speed icon is clicked")
        self.actions.newTab1GetByTextClick("Next")
        self.actions.newTab1_get_by_placeholder_fill("Type your response",
                                                     "Thank you for your interest, Mrs. Ellis. While it offers excellent rewards, it also comes with higher "
                                                     "annual fees than some of our other cards. Would that be a challenge for you, considering your fixed "
                                                     "income? If so, I can recommend a few other cards based on your needs")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speed", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1GetByTextClick("Get a hint")
        self.actions.newTab1_get_by_role_nth_click("img", "hint_icon", 1)
        print("Get a hint button is clicked")
        self.actions.newTab1GetByTextClick("Submit")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1GetByTextClick("Scenario")
        print("Scenario button is clicked")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1GetByTextClick("Your Response")
        print("Your Response button is clicked")
        self.actions.newTab1GetByTextClick("Sample Response")
        print("Sample Response button is clicked")
        #self.actions.newTab1_get_by_role("button", "Close")
        print("next button debrief is not clicked")

        self.actions.newTab1GetByTextClick("Next")
        print("next button debrief is clicked")
        self.actions.newTab1_get_by_role("button", "Close")

        # self.actions.newTab1_get_by_role("img", "transcript_icon")
        # self.actions.newTab1WaitForTimeout(3000)
        # self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        # self.actions.newTab1WaitForTimeout(3000)
        # self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        # self.actions.newTab1WaitForTimeout(3000)
        # self.actions.newTab1_locator_get_by_role("#speed", "img", "button")
        self.actions.newTab1GetByTextClick("Next")
        print("Scenario debreif next button is clicked")
        self.actions.newTab1_get_by_placeholder_fill("Type your response",response2)
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speaker", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_locator_get_by_role("#speed", "img", "button")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1GetByTextClick("Get a hint")
        self.actions.newTab1_get_by_role_nth_click("img", "hint_icon", 1)
        self.actions.newTab1GetByTextClick("Submit")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1WaitForTimeout(5000)
        scenarioEffectivenesssTxt = self.actions.newTab1TextContent(self.scenarioEffectiveness)
        print(scenarioEffectivenesssTxt)
        avgModuleEffectivenessTxt = self.actions.newTab1TextContent(self.avgModuleEffectiveness)
        print(avgModuleEffectivenessTxt)
        rankTxt = self.actions.newTab1TextContent(self.rank)
        print(rankTxt)


    def fetchingUsername(self):
        self.actions.wait_for_timeout(1000000)

    def clicksOnCreateModule(self):
        self.actions.click(self.createModuleBtn)

    def createModulePage(self):
        actualMessage = self.actions.text_content(self.createModuleTxt)
        expected_message = "CREATE MODULE"
        assert expected_message == actualMessage, f"Expected message '{expected_message}' but got '{actualMessage}'"
        print("actualMessage", actualMessage)
        print("expected message", expected_message)
        actualMessage1 = self.actions.text_content(self.pageHeader)
        expected_message1 = "Module Details"
        assert expected_message1 == actualMessage1, f"Expected message '{expected_message1}' but got '{actualMessage1}'"
        print("actualMessage", actualMessage1)
        print("expected message", expected_message1)

    def fillingStepOneDetails(self):
        self.modName = randomUtils.generate_random_string_with_prefix(length=10, prefix="test")
        self.actions.fill(self.moduleNameInput, self.modName)
        self.actions.fill(self.moduleHeadInput, "moduleHeading")
        self.actions.fill(self.moduleDescInput, "moduleDescription")
        self.actions.click(self.moduleTimeDrpDwn)
        self.actions.keyboard_press("ArrowDown")
        self.actions.keyboard_press("ArrowDown")
        self.actions.keyboard_press("Enter")
        self.actions.click(self.gameTypeDrpdwn)
        self.actions.keyboard_press("ArrowDown")
        self.actions.keyboard_press("ArrowDown")
        self.actions.keyboard_press("ArrowDown")
        self.actions.keyboard_press("Enter")
        self.actions.click(self.colorPalatteDrpdwn)
        self.actions.keyboard_press("ArrowDown")
        self.actions.keyboard_press("Enter")
        self.actions.click(self.saveNext)
        return self.modName


    def stepTwoPage(self):
        self.actions.wait_for_timeout(4000)
        actualMessage = self.actions.text_content(self.pageHeader)
        expected_message = "Module Setup"
        assert expected_message == actualMessage, f"Expected message '{expected_message}' but got '{actualMessage}'"
        print("actualMessage", actualMessage)
        print("expected message", expected_message)


    def fillingStepTwoDetails(self):
        for i in range(3,7):
            if (i > 2):
                self.actions.click("(//div[@role='switch'])[" + str(i) + "]")
                self.actions.wait_for_timeout(500)
        for i in range(1,6):
            self.parameter = "parameter"+str(i)
            self.actions.wait_for_timeout(500)
            self.actions.fill("(//input[@placeholder='Name'])["+str(i)+"]",self.parameter)
            self.actions.wait_for_timeout(500)
            self.definition = "definition"+str(i)
            self.actions.wait_for_timeout(500)
            self.actions.fill("(//input[@placeholder='Enter the definition for the parameter.'])["+str(i)+"]",self.definition)
        # self.page.click("(//input[@name='range'])[1]").fill("2.5")
        # Weight Settings
        self.actions.fill(self.parWeight1, "20")
        self.actions.fill(self.parWeight2, "30")
        self.actions.fill(self.parWeight3, "20")
        self.actions.fill(self.parWeight4, "30")
        self.actions.get_by_role("button", "Add Atoms")
        self.actions.click(".indicators")
        self.actions.get_by_text_click("Sets clear goals at a team and individual level")
        self.actions.get_by_role("button", "Save & Next")




    def moduleContentPage(self):
        self.actions.wait_for_timeout(4000)
        actualMessage = self.actions.text_content(self.pageHeader)
        expected_message = "Module Content"
        assert expected_message == actualMessage, f"Expected message '{expected_message}' but got '{actualMessage}'"
        print("actualMessage", actualMessage)
        print("expected message", expected_message)

    def fillingDetailsStepThreecreate(self, moduleDescription:str, gameTypeHeading:str, gameTypeDesc:str, gameTypeSceQues:str, gameTypeSceHint:str, gameTypeIdealResponse:str):
        self.actions.click(self.addSection)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.content)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.contentPage1)
        self.actions.fill(self.reference, "Reference1")
        self.actions.fill(self.heading, "Heading")
        self.actions.fill(self.subheading, "Sub Heading")
        self.actions.wait_for_timeout(4000)
        self.actions.frame_locator_fill("iframe[title=\"Rich Text Area\\. Press ALT-0 for help\\.\"]", "#tinymce", moduleDescription)
        self.actions.click(self.imageUrl)
        self.actions.click(self.image)
        self.actions.click(self.saveNext)
        self.actions.click(self.addSection)
        self.actions.click(self.content)
        self.actions.click(self.endpage)
        self.actions.fill(self.reference, "Reference1")
        self.actions.click(self.saveNext)
        self.actions.wait_for_timeout(4000)
        self.actions.click(self.addSection)
        self.actions.wait_for_timeout(1500)
        self.actions.click(self.gameType)
        actual = self.actions.text_content(self.AIcoachGameType)
        expected = "AI Coach Gametype"
        assert expected == actual, f"Expected message '{expected}' but got '{actual}'"
        self.actions.click(self.AIcoachGameType)
        self.actions.wait_for_timeout(1000)

        self.actions.click("#bank_undefined")
        self.actions.wait_for_timeout(1000)
        for i in range(3):
            self.actions.keyboard_press("ArrowDown")
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(1000)


        # self.actions.fill(self.gamTypHead, gameTypeHeading)
        # self.actions.frame_locator_fill("iframe[title=\"Rich Text Area\\. Press ALT-0 for help\\.\"]", "#tinymce", gameTypeDesc)
        # self.actions.fill(self.gamTypQues, gameTypeSceQues)
        # self.actions.fill(self.gamTypHint, gameTypeSceHint)
        # self.actions.fill(self.gamTypIdealResp, gameTypeIdealResponse)
        # self.actions.click(self.clickToCollapse)
        # self.actions.wait_for_timeout(1000)
        # self.actions.click(self.addScenarioBtn)
        # self.actions.fill(self.gamTypHead, gameTypeHeading)
        # self.actions.frame_locator_fill("iframe[title=\"Rich Text Area\\. Press ALT-0 for help\\.\"]","#tinymce",
        #     gameTypeDesc)
        # self.actions.fill(self.gamTypQues, gameTypeSceQues)
        # self.actions.fill(self.gamTypHint, gameTypeSceHint)
        # self.actions.fill(self.gamTypIdealResp, gameTypeIdealResponse)
        # self.actions.click(self.clickToCollapse2)
        # self.actions.wait_for_timeout(1000)
        # self.actions.click(self.addScenarioBtn)
        # self.actions.fill(self.gamTypHead, gameTypeHeading)
        # self.actions.frame_locator_fill("iframe[title=\"Rich Text Area\\. Press ALT-0 for help\\.\"]", "#tinymce",
        #     gameTypeDesc)
        # self.actions.fill(self.gamTypQues, gameTypeSceQues)
        # self.actions.fill(self.gamTypHint, gameTypeSceHint)
        # self.actions.fill(self.gamTypIdealResp, gameTypeIdealResponse)
        # self.actions.click(self.saveNext)
        # self.actions.wait_for_timeout(1000)
        # self.actions.click(self.publishButton)
        # self.actions.wait_for_timeout(1000)
        # self.actions.click(self.okayBtn)

    def fillingDetailsStepThreecreatecatalyx(self, moduleDescription: str, gameTypeHeading: str, gameTypeDesc: str,
                                      gameTypeSceQues: str, gameTypeSceHint: str, gameTypeIdealResponse: str):
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
                                        moduleDescription)
        self.actions.click(self.imageUrl)
        self.actions.click(self.image)
        self.actions.click(self.saveNext)
        self.actions.click(self.addSection)
        self.actions.click(self.content)
        self.actions.click(self.endpage)
        self.actions.fill(self.reference, "Reference1")
        self.actions.click(self.saveNext)
        self.actions.wait_for_timeout(4000)
        self.actions.click(self.addSection)
        self.actions.wait_for_timeout(1500)
        self.actions.click(self.gameType)
        actual = self.actions.text_content(self.AIcoachGameType)
        expected = "AI Coach Gametype"
        assert expected == actual, f"Expected message '{expected}' but got '{actual}'"
        self.actions.click(self.AIcoachGameType)
        self.actions.wait_for_timeout(1000)

        self.actions.click("#bank_undefined")
        self.actions.wait_for_timeout(1000)
        for i in range(3):
            self.actions.keyboard_press("ArrowDown")
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(1000)

        # self.actions.fill(self.gamTypHead, gameTypeHeading)
        # self.actions.frame_locator_fill("iframe[title=\"Rich Text Area\\. Press ALT-0 for help\\.\"]", "#tinymce", gameTypeDesc)
        # self.actions.fill(self.gamTypQues, gameTypeSceQues)
        # self.actions.fill(self.gamTypHint, gameTypeSceHint)
        # self.actions.fill(self.gamTypIdealResp, gameTypeIdealResponse)
        # self.actions.click(self.clickToCollapse)
        # self.actions.wait_for_timeout(1000)
        # self.actions.click(self.addScenarioBtn)
        # self.actions.fill(self.gamTypHead, gameTypeHeading)
        # self.actions.frame_locator_fill("iframe[title=\"Rich Text Area\\. Press ALT-0 for help\\.\"]","#tinymce",
        #     gameTypeDesc)
        # self.actions.fill(self.gamTypQues, gameTypeSceQues)
        # self.actions.fill(self.gamTypHint, gameTypeSceHint)
        # self.actions.fill(self.gamTypIdealResp, gameTypeIdealResponse)
        # self.actions.click(self.clickToCollapse2)
        # self.actions.wait_for_timeout(1000)
        # self.actions.click(self.addScenarioBtn)
        # self.actions.fill(self.gamTypHead, gameTypeHeading)
        # self.actions.frame_locator_fill("iframe[title=\"Rich Text Area\\. Press ALT-0 for help\\.\"]", "#tinymce",
        #     gameTypeDesc)
        # self.actions.fill(self.gamTypQues, gameTypeSceQues)
        # self.actions.fill(self.gamTypHint, gameTypeSceHint)
        # self.actions.fill(self.gamTypIdealResp, gameTypeIdealResponse)
        self.actions.click(self.saveNext)
        self.actions.wait_for_timeout(1000)
        self.actions.click("//button[@data-testid='atom-popup-save']")
        self.actions.click(self.publishButton)
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.okayBtn)

    def fillingDetailsStepThree(self, moduleDescription:str, gameTypeHeading:str, gameTypeDesc:str, gameTypeSceQues:str, gameTypeSceHint:str, gameTypeIdealResponse:str):
        self.actions.click(self.addSection)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.content)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.contentPage1)
        self.actions.fill(self.reference, "Reference1")
        self.actions.fill(self.heading, "Heading")
        self.actions.fill(self.subheading, "Sub Heading")
        self.actions.wait_for_timeout(4000)
        self.actions.frame_locator_fill("iframe[title=\"Rich Text Area\\. Press ALT-0 for help\\.\"]", "#tinymce", moduleDescription)
        self.actions.click(self.imageUrl)
        self.actions.click(self.image)
        self.actions.click(self.saveNext)
        self.actions.click(self.addSection)
        self.actions.click(self.content)
        self.actions.click(self.endpage)
        self.actions.fill(self.reference, "Reference1")
        self.actions.click(self.saveNext)
        self.actions.wait_for_timeout(4000)
        self.actions.click(self.addSection)
        self.actions.wait_for_timeout(1500)
        self.actions.click(self.gameType)
        actual = self.actions.text_content(self.AIcoachGameType)
        expected = "AI Coach Gametype"
        assert expected == actual, f"Expected message '{expected}' but got '{actual}'"
        self.actions.click(self.AIcoachGameType)
        self.actions.wait_for_timeout(1000)
        self.actions.fill(self.gamTypHead, gameTypeHeading)
        self.actions.frame_locator_fill("iframe[title=\"Rich Text Area\\. Press ALT-0 for help\\.\"]", "#tinymce", gameTypeDesc)
        self.actions.fill(self.gamTypQues, gameTypeSceQues)
        self.actions.fill(self.gamTypHint, gameTypeSceHint)
        self.actions.fill(self.gamTypIdealResp, gameTypeIdealResponse)
        self.actions.click(self.clickToCollapse)
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.addScenarioBtn)
        self.actions.fill(self.gamTypHead, gameTypeHeading)
        self.actions.frame_locator_fill("iframe[title=\"Rich Text Area\\. Press ALT-0 for help\\.\"]","#tinymce",
            gameTypeDesc)
        self.actions.fill(self.gamTypQues, gameTypeSceQues)
        self.actions.fill(self.gamTypHint, gameTypeSceHint)
        self.actions.fill(self.gamTypIdealResp, gameTypeIdealResponse)
        self.actions.click(self.clickToCollapse2)
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.addScenarioBtn)
        self.actions.fill(self.gamTypHead, gameTypeHeading)
        self.actions.frame_locator_fill("iframe[title=\"Rich Text Area\\. Press ALT-0 for help\\.\"]", "#tinymce",
            gameTypeDesc)
        self.actions.fill(self.gamTypQues, gameTypeSceQues)
        self.actions.fill(self.gamTypHint, gameTypeSceHint)
        self.actions.fill(self.gamTypIdealResp, gameTypeIdealResponse)
        self.actions.click(self.saveNext)
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.publishButton)
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.okayBtn)

    def fourthStepPage(self):
        self.actions.click(self.fourthreportBtn)
        self.actions.is_visible(self.reportTxt, "Report")
    def fillingStepFourDetails(self):
        # self.actions.fill("//input[@placeholder='Image Page 1']",r"C:\NewEnp\Enparadigm\Enparadigm\Enparadigm\behaveProject\Upload\Thumnail\Thumbnail.png")
        self.actions.click(self.saveNextBtn)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.proceedBtn)

    def dataSaveSuccessfullyText(self):
        # actualMessage = self.page.locator(self.sucTxt).text_content()
        # expected_message = "Data saved successfully"
        # assert expected_message == actualMessage, f"Expected message '{expected_message}' but got '{actualMessage}'"
        # print("actualMessage", actualMessage)
        # print("expected message", expected_message)
        self.actions.wait_for_timeout(3000)
        self.actions.click(self.okayBtn)

    def clickOnModulePublished(self):
        self.actions.click(self.modulesBtn)
        self.actions.fill(self.serchModule, self.modName)
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(3000)
        expectValue = self.modName
        ModuleName = self.actions.text_content(self.moduleNameInModules)
        assert expectValue == ModuleName, f"Expected message '{expectValue}' but got '{ModuleName}'"
        ModuleType = self.actions.text_content(self.moduleTypeInModules)
        expectType = "AI Coach"
        assert expectType == ModuleType, f"Expected message '{expectType}' but got '{ModuleType}'"
        self.actions.click("//img[@id='publish_module_to_catalyx']")
        self.actions.click("(//button[@type='button'])[5]")

    def clickPublishBtn(self):
         #self.actions.click("//img[@id='publish_module_to_catalyx']")
         print("module published simstudio profile")

    def publishedSucfully(self):
        # actualMessage = self.actions.text_content(self.sucTxt)
        # expected_message = "Module published successfully"
        # assert expected_message == actualMessage, f"Expected message '{expected_message}' but got '{actualMessage}'"
        # self.actions.click(self.okayBtn)
        # self.actions.wait_for_timeout(1000)
        # self.actions.reload()
        # self.actions.wait_for_timeout(4000)
        # moduleStatusAfter = self.actions.text_content(self.moduleStatusInMpdules)
        # self.actions.wait_for_timeout(3000)
        actualModName = self.actions.text_content(self.moduleNameInModules)
        expectedModName = self.modName
        assert expectedModName == actualModName, f"Expected message '{expectedModName}' but got '{actualModName}'"
        print("Module successfully created")
        moduleStatusAfter = self.actions.text_content(self.moduleStatusInMpdules)
        print("Module Status After", moduleStatusAfter)



    def signInWithGoogleAlreadySignedIn(self, admin_username:str, admin_password:str):
        self.actions.newTab1_after_clicking_frame_get_by_role("iframe[title=\"Sign in with Google Button\"]", "button", "Madhuri's profile image Sign")
        self.actions.newTab1_get_by_role_dbclick("link", "Madhuri Budha (vendor)")
        # self.actions.keyboard_press("Enter")
        self.actions.newTab1Click("//div[@data-email='vendor.qobox.madhuri@enparadigm.com']")
        self.actions.wait_for_timeout(3000)


        # try :
        #     if  self.actions.newTab1_get_by_role_is_visible("link", "Madhuri Budha (vendor)"):
        #         self.actions.newTab1_get_by_role_dbclick("link", "Madhuri Budha (vendor)")
        #     else :
        #         print("Already clicked")
        #
        # except Exception as e:
        #     print("clicked")

        self.actions.wait_for_timeout(30000)

    def clicksOnPathManagementAndfillDetails(self):
        self.actions.wait_for_timeout(3000)
        print("pathmanagement before")

        self.actions.click(self.pathManagement)
        print("pathmanagement after")

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
        ModuleName = self.actions.text_content("//td[@class='!text-base !align-middle']")
        ModuleName1 = ModuleName.strip() if ModuleName else None
        assert expectValue == ModuleName1, f"Expected message '{expectValue}' but got '{ModuleName1}'"
        print("pathmanagemnt module srch dispalyed")
        self.actions.click(self.checkBox)
        self.actions.click(self.saveNxtCatAdm)
        self.actions.wait_for_timeout(3000)

    def editPathDetailsPage(self):
        self.actions.click(self.OkayBtnCatAdm)
        self.actions.wait_for_timeout(3000)
        actual = self.actions.text_content(self.pathHeading)
        expected = "Path Details"
        assert expected == actual, f"Expected message '{expected}' but got '{actual}'"

    def fillingPathDetails(self):
        self.actions.wait_for_timeout(2000)
        self.pathNameTxt = randomUtils.generate_random_string_with_prefix(length=10, prefix="test")
        self.actions.fill(self.pathName, self.pathNameTxt)
        self.actions.click(self.pathImage)
        self.actions.wait_for_timeout(10000)
        self.actions.locator_first_click(self.image)
        self.actions.wait_for_timeout(2000)
        self.actions.fill(self.pathDesc, "Description will describe the description")
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.pathName)
        self.actions.click(self.saveNxtCatAdm)
        self.actions.wait_for_timeout(2000)
        return self.pathNameTxt

    def editModuleDetailsPage(self):
        self.actions.click(self.OkayBtnCatAdm)
        self.actions.wait_for_timeout(2000)
        actual = self.actions.text_content(self.pathHeading)
        expected = "Edit Module Details (Optional)"
        assert expected == actual, f"Expected message '{expected}' but got '{actual}'"

    def fillingModuleDetails(self, moduleHeading:str, moduleDescription:str):
        self.actions.click(self.editModuleDetailsBtn)
        self.actions.wait_for_timeout(2000)
        actual = self.actions.input_value(self.headingPathEdit)
        assert "moduleHeading" == actual, f"Expected message '{moduleHeading}' but got '{actual}'"
        self.actions.wait_for_timeout(2000)
        actual1 = self.actions.input_value(self.descPathEdit)
        assert "moduleDescription" == actual1, f"Expected message '{moduleDescription}' but got '{actual1}'"
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.saveNxtCatAdm)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.OkayBtnCatAdm)



    def feedbackQuestionPage(self):
        actual = self.actions.text_content(self.pathHeading)
        actual1 = actual.strip() if actual else None
        expected = "Feedback Questions (Optional)"
        assert expected == actual1, f"Expected message '{expected}' but got '{actual1}'"


    def selectsFeedbackQuestion(self):
        self.actions.click(self.checkBox)
        self.actions.click(self.checkBox2)
        self.actions.click(self.publishCatAdm)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.OkayBtnCatAdm)
        self.actions.wait_for_timeout(3000)


    def managingPath(self):
        print(self.actions.text_content(self.managePath))
        print(self.pathNameTxt)
        self.actions.fill(self.serchModule, self.pathNameTxt)
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(3000)
        # expectValue = self.pathNameTxt
        # pathName = self.actions.text_content(self.moduleNameInpathmanage)
        # assert expectValue == pathName, f"Expected message '{expectValue}' but got '{pathName}'"

    def clicksOnCohortManagement(self):
        self.actions.click(self.cohortmngmnt_btn)
        self.actions.click(self.createcohortmngmnt_btn)



    def enterDetailsAndSelectPath(self):
        self.actions.wait_for_timeout(5000)
        self.cohort_name = randomUtils.generate_random_string_with_prefix(length=10, prefix="test")
        self.actions.fill(self.cohortname_input, self.cohort_name)
        print(self.cohort_name)
        write_to_file(self.cohort_name)
        # try:
        #     self.actions.click(self.selectCompany_drpdwn)
        #     self.actions.wait_for_timeout(3000)
        #     self.actions.fill(self.cominput, "testmadhuri")
        #     self.actions.click(self.companyMadhuri)
        # except Exception as e:
        self.actions.click(self.selectCompany_drpdwn)
        self.actions.wait_for_timeout(3000)
        self.actions.fill(self.cominput, "testmadhuri")
        self.actions.click(self.companyMadhuri)
        self.actions.dealbtnclick()

        print("deal worked)")


        # self.actions.click(self.selectDeal_drpdwn)
        # self.actions.wait_for_timeout(1000)
        # self.actions.click(self.selectDeal_drpdwn)
        # self.actions.wait_for_timeout(1000)
        #self.actions.click(self.madhuriDeal_btn)
        # self.actions.keypress("ArrowDown")
        # self.actions.keypress("Enter")
        self.actions.fill(self.hrname_input, "Madhuri")
        self.actions.fill(self.hremail_input, "madhuriii@gmail.com")
        self.actions.click(self.inputdate)
        self.actions.click(self.date)
        self.actions.click(self.deadlinedate)
        self.actions.click(self.enddateyr)
        # self.page.click(self.selectyr)
        # self.page.get_by_role("combobox").nth(4).select_option("2032")

        # self.page.click(self.chooseyr_btn)
        self.actions.get_by_role_nth_select_option("#ui-datepicker-div", "combobox", 1, "2031")
        self.actions.get_by_role("link", "14")
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.hremail_input)
        self.actions.click(self.hremail_input)
        self.actions.select_option_value(
            "//select[@class='cs_adminidSelectBox selectBox form-control select2 select2-hidden-accessible']",
            'Pallabi')
        self.actions.select_option_value(
            "//select[@class='packageSelectBox form-control selectBox select2 select2-hidden-accessible']",
        self.pathNameTxt)
        self.actions.click(self.createcohort_btn)
        return self.cohort_name


    def cohortsuccesspopup1(self):
        self.actions.wait_for_timeout(3000)
        self.actions.click(self.OkayBtnCatAdm)
        self.actions.wait_for_timeout(3000)
        self.actions.click(self.cohortmngmnt_btn)

    def clickOnGameType(self):
        self.actions.click(self.addSection)
        self.actions.wait_for_timeout(1500)
        self.actions.click(self.gameType)
        actual = self.actions.text_content(self.AIcoachGameType)
        expected = "AI Coach Gametype"
        assert expected == actual, f"Expected message '{expected}' but got '{actual}'"
        self.actions.click(self.AIcoachGameType)
        self.actions.wait_for_timeout(1000)

    def clicksOnCreateUser(self):
        self.actions.click(self.createUserList_btn)

    def verifyAllTheFieldsinTextGamePlay(self):
        self.actions.is_visible(self.gamTypeHeadTxt, "Heading")
        self.actions.is_visible(self.gamTypeDescTxt, "Description")
        self.actions.is_visible(self.gamTypeQuesTxt, "Question")
        self.actions.is_visible(self.gameTypeHintTxt, "Hint")
        self.actions.is_visible(self.gameTypeRespTxt, "Response")
        self.actions.is_visible(self.gameTypeFileBtn, "File")
        self.actions.is_visible(self.gameTypeEditBtn, "Edit")
        self.actions.is_visible(self.gameTypeViewBtn, "View")
        self.actions.is_visible(self.gameTypeInsertBtn, "Insert")
        self.actions.is_visible(self.gameTypeFormatBtn, "Format")
        self.actions.is_visible(self.gameTypeTableBtn, "Table")
        self.actions.is_visible(self.gameTypeHelpBtn, "Help")
        self.actions.is_visible(self.boldBtn, "Bold")
        self.actions.is_visible(self.italic, "Italic")
        self.actions.is_visible(self.backgrundClr, "BackGround Color")
        self.actions.is_visible(self.alignLeft, "Align Left")
        self.actions.is_visible(self.alignCenter, "Align Center")
        self.actions.is_visible(self.alignRight, "Align Right")
        self.actions.is_visible(self.justify, "Justify")
        self.actions.is_visible(self.bulletPoint, "Bullet Point")
        self.actions.is_visible(self.numberedList, "Numbered List")
        self.actions.is_visible(self.decreased, "Decreased")
        self.actions.is_visible(self.clearFormatting, "Clear Formatting")
        self.actions.is_visible(self.tableIcon, "Table")

    def verifyAllTheFieldsinVideoGamePlay(self):
        self.actions.click("#bank_undefined")
        for i in range(12):
            self.actions.keyboard_press("ArrowDown")
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(2000)
        #self.actions.select_option_visible_text("#bank_undefined", "Aligning A Client and Your Team")
        self.actions.wait_for_timeout(2000)
        # self.actions.fill(self.gamTypeHeadTxt, "Heading")
        # self.actions.fill(self.gamTypeQuesTxt, "Question")
        # self.actions.frame_locator_loc_is_visible(self.iframeVideo1, self.videoRefName, "Reference")
        # self.actions.frame_locator_loc_is_visible(self.iframeVideo1, self.videoThumbnail, "Thumbnail")
        # self.actions.frame_locator_loc_is_visible(self.iframeVideo1, self.video, "Video")
        # self.actions.frame_inside_frame_loc_is_visible(self.iframeVideo1, self.iframeVideo2, self.videoTrans, "Trans")
        self.actions.is_visible(self.gameTypeHintTxt, "Hint")
        self.actions.is_visible(self.gameTypeRespTxt, "Response")
        self.actions.is_visible(self.gameTypeFileBtn, "File")
        self.actions.is_visible(self.gameTypeEditBtn, "Edit")
        self.actions.is_visible(self.gameTypeViewBtn, "View")
        self.actions.is_visible(self.gameTypeInsertBtn, "Insert")
        self.actions.is_visible(self.gameTypeFormatBtn, "Format")
        self.actions.is_visible(self.gameTypeTableBtn, "Table")
        self.actions.is_visible(self.gameTypeHelpBtn, "Help")
        self.actions.is_visible(self.boldBtn, "Bold")
        self.actions.is_visible(self.italic, "Italic")
        self.actions.is_visible(self.backgrundClr, "BackGround Color")
        self.actions.is_visible(self.alignLeft, "Align Left")
        self.actions.is_visible(self.alignCenter, "Align Center")
        self.actions.is_visible(self.alignRight, "Align Right")
        self.actions.is_visible(self.justify, "Justify")
        self.actions.is_visible(self.bulletPoint, "Bullet Point")
        self.actions.is_visible(self.numberedList, "Numbered List")
        self.actions.is_visible(self.decreased, "Decreased")
        self.actions.is_visible(self.clearFormatting, "Clear Formatting")
        self.actions.is_visible(self.tableIcon, "Table")
        self.actions.click("//span[normalize-space()='Save & Next']")


    def GameTypeVideo(self, file_path1:str, file_path2:str,  moduleDescription:str, gameTypeHeading:str, gameTypeDesc:str, gameTypeSceQues:str, gameTypeSceHint:str, gameTypeIdealResponse:str):
        self.actions.click(self.addSection)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.content)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.contentPage1)
        self.actions.fill(self.reference, "Reference1")
        self.actions.fill(self.heading, "Heading")
        self.actions.fill(self.subheading, "Sub Heading")
        self.actions.wait_for_timeout(10000)
        self.actions.frame_locator_fill("//iframe[@title='Rich Text Area. Press ALT-0 for help.']", "#tinymce",
            moduleDescription)
        self.actions.click(self.imageUrl)
        self.actions.click(self.image)
        self.actions.click(self.saveNext)
        self.actions.click(self.addSection)
        self.actions.click(self.content)
        self.actions.click(self.endpage)
        self.actions.fill(self.reference, "Reference1")
        self.actions.click(self.saveNext)
        self.actions.wait_for_timeout(4000)
        # self.actions.click(self.addSection)
        # self.actions.wait_for_timeout(1500)
        # self.actions.click(self.gameType)

        self.actions.click(self.addSection)
        self.actions.click(self.gameType)
        actual = self.actions.text_content(self.AIcoachGameType)
        expected = "AI Coach Gametype"
        assert expected == actual, f"Expected message '{expected}' but got '{actual}'"
        self.actions.click(self.AIcoachGameType)
        self.actions.wait_for_timeout(1000)

        self.actions.click("#bank_undefined")
        for i in range(12):
            self.actions.keyboard_press("ArrowDown")
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(2000)
        # self.actions.wait_for_timeout(1000)
        # self.actions.click(self.videoRadioBtn)
        # self.actions.wait_for_timeout(1000)
        # self.actions.fill(self.gamTypHead, gameTypeHeading)
        # self.actions.fill(self.gamTypQues, gameTypeSceQues)
        # self.actions.frame_locator_fill(self.iframeVideo1, self.videoRefNameInput, "Video Reference Name1")
        # self.actions.set_input_files_in_frame(self.iframeVideo1, self.videoThumbnailInput, file_path1)
        # self.actions.set_input_files_in_frame(self.iframeVideo1, self.videoInput, file_path2)
        # self.actions.wait_for_timeout(3000)
        # # self.page.frame_locator(self.iframeVideo1).frame_locator(self.iframeVideo2).locator("#tinycme").fill(moduleDescription)
        # self.actions.frame_inside_frame_type("iframe[title='Video Player Form']",
        #     "iframe[title='Rich Text Area. Press ALT-0 for help.']","#tinymce",
        #     moduleDescription)
        # self.actions.frame_locator_click(self.iframeVideo1, "//button[text()='Upload Video']")
        # self.actions.wait_for_timeout(10000)
        # self.actions.fill(self.gamTypHint, gameTypeSceHint)
        # self.actions.fill(self.gamTypIdealResp, gameTypeIdealResponse)
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.saveNext)
        self.actions.wait_for_timeout(1000)
        self.actions.click("//button[@data-testid='atom-popup-save']")
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.publishButton)
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.okayBtn)


    def emptyparametersForStep1creatingmodule(self, ModName:str, ModHeading:str, Description:str, NeededTime:str, gameType:str, colorPalette:str):
        if ModName == '""':  # Handle empty string from Gherkin
            ModName = ""
        self.actions.fill(self.moduleNameInput, ModName)
        if ModHeading == '""':  # Handle empty string from Gherkin
            ModHeading = ""
        self.actions.fill(self.moduleHeadInput, ModHeading)
        if Description == '""':  # Handle empty string from Gherkin
            Description = ""
        self.actions.fill(self.moduleDescInput, Description)
        if NeededTime == "selNeedTime":
            self.actions.click(self.moduleTimeDrpDwn)
            self.actions.keyboard_press("ArrowDown")
            self.actions.keyboard_press("ArrowDown")
            self.actions.keyboard_press("Enter")
        else:
            print("..")
        if gameType == "selgameType":
            self.actions.click(self.gameTypeDrpdwn)
            self.actions.keyboard_press("ArrowDown")
            self.actions.keyboard_press("ArrowDown")
            self.actions.keyboard_press("ArrowDown")
            self.actions.keyboard_press("Enter")

        else:
            print("..")
        if colorPalette == "selcolPal":
            self.actions.click(self.colorPalatteDrpdwn)
            self.actions.keyboard_press("ArrowDown")
            self.actions.keyboard_press("Enter")
        else:
            print("..")
        self.actions.click(self.saveNext)
    def verifyingErrorMessagesstep3(self):
        actualerrormsgstep3=self.actions.text_content("//div[@id='swal2-html-container']")
        expectederrormsgstep3="Please add the end page layout before publishing"
        assert expectederrormsgstep3 == actualerrormsgstep3, f"Expected message '{expectederrormsgstep3}' but got '{actualerrormsgstep3}'"
        print("Actual error msg:",actualerrormsgstep3)
        print("Expected error msg:",expectederrormsgstep3)

    def verifyingErrorMessagesCreatingMofdule(self):
        actualMessage = self.actions.text_content(self.sucTxt)
        if actualMessage == "Please enter module name":
            expected_message = "Please enter module name"
            assert expected_message == actualMessage, f"Expected message '{expected_message}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message)
        elif actualMessage == "Please enter module heading":
            expected_message1 = "Please enter module heading"
            assert expected_message1 == actualMessage, f"Expected message '{expected_message1}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message1)
        elif actualMessage == "Please enter module description":
            expected_message3 = "Please enter module description"
            assert expected_message3 == actualMessage, f"Expected message '{expected_message3}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message3)
        elif actualMessage == "Please select module time needed":
            expected_message4 = "Please select module time needed"
            assert expected_message4 == actualMessage, f"Expected message '{expected_message4}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message4)
        elif actualMessage == "Please select game type":
            expected_message5 = "Please select game type"
            assert expected_message5 == actualMessage, f"Expected message '{expected_message5}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message5)
        elif actualMessage == "Please fill all the parameter names":
            expected_message6 = "Please fill all the parameter names"
            assert expected_message6 == actualMessage, f"Expected message '{expected_message6}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message6)
        elif actualMessage == "Please enter reference name":
            expected_message7 = "Please enter reference name"
            assert expected_message7 == actualMessage, f"Expected message '{expected_message7}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message7)
        elif actualMessage == "Please enter heading":
            expected_message8 = "Please enter heading"
            assert expected_message8 == actualMessage, f"Expected message '{expected_message8}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message8)
        elif actualMessage == "Please enter content text":
            expected_message9 = "Please enter content text"
            assert expected_message9 == actualMessage, f"Expected message '{expected_message9}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message9)
        elif actualMessage == "Please select image":
            expected_message10 = "Please select image"
            assert expected_message10 == actualMessage, f"Expected message '{expected_message10}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message10)
        else:
            expected_message2 = "Please select color palette"
            assert expected_message2 == actualMessage, f"Expected message '{expected_message2}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message2)


    def clickOnAcceptButton(self):
        self.actions.newTab1_get_by_role("button", "Accept")

    def clicksOnStartandPlaysGame(self):
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_get_by_role("button", "Start button hover icon")
        self.actions.newTab1WaitForTimeout(2000)
        self.actions.newTab1_get_by_role("button", "Start button hover icon")
        self.actions.newTab1WaitForTimeout(2000)
        self.actions.newTab1_get_by_role("button", "Next")
        self.actions.newTab1WaitForTimeout(1000)
        self.actions.newTab1GetByTextClick("Scenario")
        self.actions.newTab1WaitForTimeout(5000)
        self.actions.newTab1Click("//div[text()='Next']")
        try:
            self.actions.newTab1Click("//div[text()='Next']")
        except Exception as e :
            print("")
        self.actions.newTab1_get_by_placeholder_click("Type your response")
        self.actions.newTab1_get_by_placeholder_fill("Type your response", "fdfdsfdsdffds")
        self.actions.newTab1WaitForTimeout(1000)
        self.actions.newTab1GetByTextClick("Submit")
        self.actions.newTab1WaitForTimeout(5000)
        self.actions.newTab1GetByTextClick("Next")
        self.actions.newTab1GetByTextClick("Scenario")
        self.actions.newTab1WaitForTimeout(5000)
        self.actions.newTab1Click("//div[text()='Next']")
        try:
            self.actions.newTab1Click("//div[text()='Next']")
        except Exception as e :
            print("")
        self.actions.newTab1_get_by_placeholder_fill("Type your response", "fdfdfsdf")
        self.actions.newTab1WaitForTimeout(1000)
        self.actions.newTab1GetByTextClick("Submit")
        self.actions.newTab1WaitForTimeout(5000)
        self.actions.newTab1GetByTextClick("Next")
        self.actions.newTab1GetByTextClick("Scenario")
        self.actions.newTab1WaitForTimeout(5000)
        self.actions.newTab1Click("//div[text()='Next']")
        try:
            self.actions.newTab1Click("//div[text()='Next']")
        except Exception as e :
            print("")
        self.actions.newTab1_get_by_placeholder_fill("Type your response","dfdsffd")
        self.actions.newTab1GetByTextClick("Submit")
        self.actions.newTab1WaitForTimeout(5000)
        self.actions.newTab1GetByTextClick("Next")
        self.actions.newTab1WaitForTimeout(2000)
        self.actions.newTab1GetByTextClick("Next")
        self.actions.newTab1WaitForTimeout(1000)
        self.actions.newTab1GetByTextClick("Next")
        self.actions.newTab1_locator_filter_has_text_first_click("#feedbackData1 span", "10")
        self.actions.newTab1_get_by_role("button", "Submit")
        self.actions.newTab1_locator_filter_has_text_first_click("#feedbackData2 span", "10")
        self.actions.newTab1_get_by_role("button", "Submit")
        self.actions.newTab1GetByTextClick("Talent Hub")
        self.actions.newTab1GetByTextClick("Learning Path")
        self.actions.newTab1_get_by_role("button", "Give Feedback button hover")

    def clicksSaveNextBtn(self):
        self.actions.click(self.saveNext)

    def clicksOnPublishButton(self):
        self.actions.click(self.publishButton)

    def emptyParametersStep3Content(self, RefeName:str, Heading:str, Context:str, ImageUrl:str):
        self.actions.click(self.addSection)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.content)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.contentPage1)
        if RefeName == '""':  # Handle empty string from Gherkin
            RefeName = ""
        self.actions.fill(self.reference, RefeName)
        if Heading == '""':  # Handle empty string from Gherkin
            Heading = ""
        self.actions.fill(self.heading, Heading)
        self.actions.wait_for_timeout(4000)
        if Context == '""':  # Handle empty string from Gherkin
            Context = ""
        self.actions.frame_locator_fill("iframe[title=\"Rich Text Area\\. Press ALT-0 for help\\.\"]", "#tinymce", Context)
        if ImageUrl == "selImage":
            self.actions.click(self.imageUrl)
            self.actions.click(self.image)
        else:
            print("..")
        self.actions.click(self.saveNext)

    def selectingCompanyNewCreatedCohort(self):
            try:
                self.actions.click(self.company_drpdwn)
                self.actions.wait_for_timeout(3000)
                # self.page.click(self.company_drpdwn)
                self.actions.fill(self.cominput, "testmadhuri")
                self.actions.click(self.madhuri_cmpny)
                self.actions.wait_for_timeout(1000)
                self.actions.click(self.cohort_drpdwn)
                self.actions.wait_for_timeout(3000)
                self.actions.fill(self.cominput, self.cohort_name)
                self.actions.keyboard_press("ArrowDown")
                self.actions.keyboard_press("Enter")

            except Exception as e:
                self.actions.click(self.company_drpdwn)
                self.actions.wait_for_timeout(3000)
                # self.page.click(self.company_drpdwn)
                self.actions.fill(self.cominput, "testmadhuri")
                self.actions.click(self.madhuri_cmpny)
                self.actions.wait_for_timeout(10000)
                self.actions.click(self.cohort_drpdwn)
                self.actions.wait_for_timeout(3000)
                self.actions.fill(self.cominput, self.cohort_name)
                self.actions.keyboard_press("ArrowDown")
                self.actions.keyboard_press("Enter")

    def clickOnmagicLink1(self):
        # username = self.page.get_by_text(self.nameTable_txt)
        # LoginMail = self.page.get_by_text(self.emailTable_txt)
        self.actions.click(self.magicLink_btn)
        self.actions.click_link_open_new_tab_coping(self.copyMagicLink_txt)

















































