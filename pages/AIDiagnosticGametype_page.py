import os
from time import sleep


from pages.base_page import BasePage
import configparser

from utils import randomUtils

from utils.shared_data import write_to_file
import pyperclip

from pages.WebActions import WebActions

config = configparser.ConfigParser()
config.read('config.ini')


class AIDiagnosticGametypePage:
    def __init__(self, page, browser_context):

        self.actions = WebActions(page, browser_context)

        self.saveNext = "//span[text()='Save & Next']"
        self.moduleNameInput = "#module_name"
        self.moduleHeadInput = "#module_heading"
        self.moduleDescInput = "#module_description"
        self.moduleTimeDrpDwn = "#module_time_needed"
        self.gameTypeDrpdwn = "#select_game_type"
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
        self.endpage = "//span[text()='end page 1']"
        self.publishButton = "//span[text()='Publish Module For Testing']"
        self.okayBtn = "//button[normalize-space()='Ok']"
        self.fourthreportBtn = "//div[text()='Step 4: Report']"
        self.reportTxt = "//div[@id='create_module_step_4']/div[1]"
        self.proceedBtn = "//button[text()='Proceed']"
        self.sucTxt = "#swal2-html-container"
        self.saveNextBtn = "//button[text()='Save & Next']"
        self.modulesBtn = "//span[text()='Modules']"
        self.serchModule = "//input[@placeholder='Search...']"
        self.moduleNameInModules = "//table[@class='svelte-15iwbfd']//td[1]"
        self.moduleTypeInModules = "//table[@class='svelte-15iwbfd']//td[2]"
        self.moduleStatusInMpdules = "//table[@class='svelte-15iwbfd']//td[3]"
        self.publishIcon = "#publish_module_to_catalyx"
        self.yesBtn = "//button[normalize-space()='Yes']"
        self.OkBtn = "//button[text()='OK']"
        self.gameType = "//span[text()='Gametype']"
        self.AIDiagnoGameType = "//span[text()='AI Diagnostic Gametype']/preceding-sibling::img"
        self.gamTypHead = "#heading"
        self.videoTitleScBank="(//input[@class='input'])[1]"
        self.thumbnailTextscBank="//input[@accept='image/*']"
        self.videoscbank="((//label[@class='label mt-4'])//div[@class='flex flex-col']//input)[2]"
        self.videoscbank2="(//input[@accept='video/*'])[2]"
        self.uplaodVideosscbank="//button[text()='Upload All Videos']"
        self.gamTypQues = "(//textarea[@id='hint'])[1]"
        self.framevideosc="iframe[title=\"Video Player Form\"]"
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
        self.videoRadioBtn = "//p[text()='Video']/preceding-sibling::input"
        self.videoRefName = "//span[text()='Video Reference Name']"
        self.videoThumbnail = "//span[normalize-space()='Thumbnail *']"
        self.video = "//span[normalize-space()='Video *']"
        self.videoTrans = "//span[contains(text(), 'Video Transcript')]"
        self.iframeVideo1 = "#videoPlayerFormCoach_0"
        self.iframeSecondSecenario = "#videoPlayerFormCoach_1"
        self.iframeVideo2 = "#transcript_ifr"
        self.videoRefNameInput = "//input[@placeholder='Name']"
        self.videoThumbnailInput = "(//input[@type='file'])[1]"
        self.videoInput = "//input[@accept='video/*']"
        self.createUserList_btn = "//li[@id='createUserListItem']"
        self.createUserBtn = "//div[text()='Create User']"
        self.parWeight1 = "(//input[@inputmode='numeric'])[1]"
        self.parWeight2 = "(//input[@inputmode='numeric'])[2]"
        self.parWeight3 = "(//input[@inputmode='numeric'])[3]"
        self.parWeight4 = "(//input[@inputmode='numeric'])[4]"
        self.addScenarioBtn = "//span[normalize-space()='Add a Scenario']"
        self.clickToCollapse = "//div[normalize-space()='Click to collapse']"
        self.clickToCollapse2 = "(//div[normalize-space()='Click to collapse'])[5]"
        self.company_drpdwn = "(//span[@class='select2-selection__rendered'])[9]"
        self.cominput = "//input[@class='select2-search__field']"
        self.cohort_drpdwn = "(//span[@role='combobox'])[11]"
        # self.madhuri_cmpny = "//li[text()='testmadhuri']"
        self.madhuri_cmpny = "//li[text()='Product Testing - AI Diagnostic']"
        self.magicLink_btn = "(//button[text()='Magic Link'])[1]"
        self.copyMagicLink_txt = "//button[@id='copy_magic_link_for_user']"
        self.searchInput = "//input[@placeholder='Search...']"
        self.playSimula = "(//img[@alt='play_simulation'])[1]"
        self.NextBtn = "//button[text()='Next']"
        self.NextBtnAID="//div[text()='Next']"
        self.NextBtn2 = "#next"
        self.closeBtn = "//button[text()='Close']"
        self.typeResponseInput = "#user_input"
        self.submitBtn = "#submit"
        self.fiveStar = "//div[@class='rating cursor-pointer']/div[5]"
        self.fiveCheckBox = "(//input[@type='checkbox'])[5]"
        self.viewReport = "//div[text()='View Report']"
        self.reportText1 = "//div[@class='text-xl font-extrabold leading-7 text-white text-center px-4']"
        self.reportText2 = "//div[@class='text-xl font-extrabold leading-7 text-white mt-2 text-center px-4']"
        self.reportHeading = "(//h1)[2]"
        self.reportAIDHead="(//h1[@class='svelte-7i26t6'])[1]"
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
        self.name_magic_page = "(//td[@class='nameTd'])[1]"
        self.username_magic_page = "//td[@class='usernameTd']"
        self.startBtn = "(//span[@class='transition duration-700 ease-in-out translate-x-0'])[2]"
        self.startBtn2 = "(//span[@class='transition duration-700 ease-in-out -translate-x-1'])[1]"
        self.saveBtn = "//button[text()='Save']"
        self.searchedOutcome = "((//tr[@class='theme-font6'])[1]/td)[1]"
        self.pathManagement = "(//div[@class='accordion-summary flex-1'])[3]"
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
        self.headingPathEdit = "(//textarea[@placeholder='Enter some long form content.'])[1]"
        self.descPathEdit = "(//textarea[@placeholder='Enter some long form content.'])[2]"
        self.OkayBtnCatAdm = "//button[normalize-space()='OK']"
        self.checkBox2 = "(//input[@type='checkbox'])[2]"
        self.publishCatAdm = "//button[normalize-space()='PUBLISH']"
        self.managePath = "//span[text()='Manage Path']"
        self.cohortmngmnt_btn = "//div[text()='Cohort Management']"
        self.outcomeSearch = "//section[@id='tutor-content']//td[text()='A Sudden Presentation']"
        self.editBtn = "(//span[text()='Edit'])[3]"
        self.nonExistingScenarioOutcome = "(//table[@class='svelte-15iwbfd']//tr)[2]"
        self.deleteIcon = "//img[@alt='delete']"
        self.editBtn1 = "(//span[text()='Edit'])[1]"
        self.metatagsWrngButton = "//img[contains(@class, 'cursor-pointer')]"
        self.deleteButton = "(//span[text()='Delete'])[1]"
        self.cancelButton = "//button[text()='Cancel']"
        self.firstRowSce = "((//table[@class='svelte-15iwbfd']//tr)[2]/td)[1]"
        self.moduleNameTxt = "//div[contains(@class,'header-simulation-name')]"
        self.headingTxt = "(//div[@class='contentContainer']/div)[1]"
        self.sideHeadingTxt = "//div[contains(@class,'sub_heading')]"
        self.contentPageRef = "#content_page1_content"
        self.secDescpTxt = "#text_player_content"
        self.secHeadingTxt = "//div[@class='text-white']/div[3]/span"
        self.secQuestTxt= "//div[contains(@class,'question_content')]"
        self.createNewBtn = "//button[text()='Create New']"
        self.modHeadPathMag = "//div[contains(@id,'static')]"


    def filling_details_in_step1(self):
        self.modName = randomUtils.generate_random_string_with_prefix(length=10, prefix="test")
        self.actions.fill(self.moduleNameInput, self.modName)
        self.actions.fill(self.moduleHeadInput, "moduleHeading")
        self.actions.fill(self.moduleDescInput, "moduleDescription")
        self.actions.click(self.moduleTimeDrpDwn)
        self.actions.keyboard_press("ArrowDown")
        self.actions.keyboard_press("ArrowDown")
        self.actions.keyboard_press("Enter")
        self.actions.click(self.gameTypeDrpdwn)
        self.actions.keyboard_presss("ArrowDown")
        self.actions.keyboard_press("ArrowDown")
        self.actions.keyboard_press("ArrowDown")
        self.actions.keyboard_press("ArrowDown")
        self.actions.keyboard_press("ArrowDown")
        self.actions.keyboard_press("Enter")
        self.actions.click(self.colorPalatteDrpdwn)
        self.actions.keyboard_press("ArrowDown")
        self.actions.keyboard_press("Enter")
        self.actions.click(self.saveNext)
        return self.modName

    def enter_Details_In_AtomSetUp(self):
        self.actions.get_by_role("button", "Add Atoms")
        self.actions.click(".indicators")
        self.actions.get_by_text_click("Sets clear goals at a team and individual level")
        self.actions.get_by_placeholder_dbclick("Ideal Score(1-5)")
        self.actions.get_by_placeholder_fill("Ideal Score(1-5)", "2")
        self.actions.get_by_role("button", "Add Molecules")
        self.actions.get_by_placeholder_click("Molecule Name")
        self.actions.get_by_placeholder_fill("Molecule Name", "Molecule1")
        self.actions.get_by_placeholder_click("Molecule Description")
        self.actions.get_by_placeholder_fill("Molecule Description", "description is molecule")
        self.actions.get_by_role_select_option("combobox", "0")
        self.actions.get_by_role("button", "Save & Next")
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.saveNext)




    def enters_search_clicks_playbutton(self):
        self.actions.fill(self.searchInput, "Ai diagnosticsss")
        self.actions.wait_for_timeout(3000)
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(2000)


    def playsAIDiagnosticsssSimulation(self):
        self.actions.newTabAfterClickingAnElement(self.playSimula)
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1WaitForTimeout(8000)
        # scenario1
        self.actions.newTab1Click(self.closeBtn)
        self.actions.newTab1Click(self.NextBtn2)
        self.actions.newTab1Fill(self.typeResponseInput, "I understand the urgency and appreciate our long-standing relationship.")
        self.actions.newTab1Click(self.submitBtn)
        self.actions.newTab1WaitForTimeout(3000)
        #scenario2
        self.actions.newTab1WaitForTimeout(3000)

        self.actions.newTab1Click(self.NextBtn2)
        self.actions.newTab1WaitForTimeout(2000)
        # try:
        #     self.actions.click(self.NextBtnAID)
        # except TimeoutError:
        #     print("Timeout: Element was not found or clickable within the specified time.")
        self.actions.newTab1Fill(self.typeResponseInput,
                        "I understand the urgency and appreciate our long-standing relationship.")
        self.actions.newTab1Click(self.submitBtn)
        self.actions.newTab1WaitForTimeout(3000)
        # scenario3
        self.actions.newTab1Click(self.NextBtn2)
        self.actions.newTab1WaitForTimeout(2000)
        # try:
        #     self.actions.newTab1Click(self.NextBtn2)
        # except TimeoutError:
        #     print("Timeout: Element was not found or clickable within the specified time.")
        self.actions.newTab1Fill(self.typeResponseInput,
                        "I understand the urgency and appreciate our long-standing relationship.")
        self.actions.newTab1Click(self.submitBtn)
        self.actions.newTab1WaitForTimeout(3000)
        # scenario4
        self.actions.newTab1Click(self.NextBtn2)
        self.actions.newTab1WaitForTimeout(2000)
        # try:
        #     self.actions.newTab1Click(self.NextBtn2)
        # except TimeoutError:
        #     print("Timeout: Element was not found or clickable within the specified time.")
        self.actions.newTab1Fill(self.typeResponseInput,
                        "I understand the urgency and appreciate our long-standing relationship.")
        self.actions.newTab1Click(self.submitBtn)
        self.actions.newTab1WaitForTimeout(3000)
        # scenario5
        self.actions.newTab1Click(self.NextBtn2)
        self.actions.newTab1WaitForTimeout(2000)
        # try:
        #     self.actions.newTab1Click(self.NextBtn2)
        # except TimeoutError:
        #     print("Timeout: Element was not found or clickable within the specified time.")
        self.actions.newTab1Fill(self.typeResponseInput,
                        "I understand the urgency and appreciate our long-standing relationship.")
        self.actions.newTab1Click(self.submitBtn)
        self.actions.newTab1WaitForTimeout(3000)
        #self.actions.newTab1Click(self.fiveStar)
        #self.actions.newTab1Click(self.fiveCheckBox)
        #self.actions.newTab1Click(self.NextBtn)
        #print(self.actions.newTab1TextContent(self.reportText1))
        #print(self.actions.newTab1TextContent(self.reportText2))
        self.actions.wait_for_timeout(30000)

        self.actions.goto_newtab2_by_clicking_element(self.viewReport)
        self.actions.new_tab2_wait_for_timeout(3000)
        print(self.actions.new_tab2_text_content(self.reportAIDHead))


    def selectsCohortandComForAIDia(self):
        self.actions.wait_for_timeout(10000)

        self.actions.click(self.company_drpdwn)
        self.actions.wait_for_timeout(10000)

        self.actions.fill(self.cominput, "testmadhuri")
        self.actions.wait_for_timeout(10000)

        self.actions.keyboard_press("Enter")


        # try:
        #     self.actions.click(self.company_drpdwn)
        #     self.actions.wait_for_timeout(3000)
        #     self.actions.click(self.company_drpdwn)
        #     self.actions.fill(self.cominput, "Product Testing - AI Diagnostic")
        #     self.actions.click(self.madhuri_cmpny)
        # except Exception as e:
        #     self.actions.click(self.company_drpdwn)
        #     self.actions.wait_for_timeout(3000)
        #     self.actions.click(self.company_drpdwn)
        #     self.actions.fill(self.cominput, "Product Testing - AI Diagnostic")
        #     self.actions.click(self.madhuri_cmpny)
    def enterValidUserDetailsAIDia(self):
        self.user = randomUtils.generate_random_string_with_prefix(length=10, prefix="test")
        self.actions.fill(self.name_input, self.user)
        self.emailrandom = randomUtils.generate_random_email()
        self.actions.fill(self.username_input, self.emailrandom)
        self.actions.fill(self.role_input, "QA Analyst role")
        self.actions.fill(self.manager_input, "madhuri")
        # self.page.check(self.simulation_chkbx)
        self.actions.click(self.createUser_btn)
        self.actions.wait_for_timeout(3000)
        if self.actions.is_visible(self.Close_btn, "Close Button"):
            print("visible")
            self.actions.get_by_role("button", "Close")
            self.actions.wait_for_timeout(3000)
            self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(3000)
        return self.user, self.emailrandom

    def verifiesNameAndEmailUser(self):
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

    def clickOnmagicLink2(self):
        # username = self.page.get_by_text(self.nameTable_txt)
        # LoginMail = self.page.get_by_text(self.emailTable_txt)
        self.actions.click(self.magicLink_btn)
        self.actions.click_link_open_new_tab_coping(self.copyMagicLink_txt)
        #self.actions.newTab1_get_by_role("button", "Accept").click()
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(10000)
        self.actions.newTab1Click(self.startBtn)
        self.actions.newTab1Click(self.startBtn2)
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1WaitForTimeout(8000)
        # scenario1
        self.actions.newTab1Click(self.closeBtn)
        self.actions.newTab1Click(self.NextBtn2)
        self.actions.newTab1Fill(self.typeResponseInput,
                        "I understand the urgency and appreciate our long-standing relationship.")
        self.actions.newTab1Click(self.submitBtn)
        self.actions.newTab1WaitForTimeout(3000)
        # scenario2
        self.actions.newTab1Click(self.NextBtn2)
        self.actions.newTab1WaitForTimeout(2000)
        try:
            self.actions.newTab1Click(self.NextBtn2)
        except TimeoutError:
            print("Timeout: Element was not found or clickable within the specified time.")
        self.actions.newTab1Fill(self.typeResponseInput,
                        "I understand the urgency and appreciate our long-standing relationship.")
        self.actions.newTab1Click(self.submitBtn)
        self.actions.newTab1WaitForTimeout(3000)
        # scenario3
        self.actions.newTab1Click(self.NextBtn2)
        self.actions.newTab1WaitForTimeout(2000)
        try:
            self.actions.newTab1Click(self.NextBtn2)
        except TimeoutError:
            print("Timeout: Element was not found or clickable within the specified time.")
        self.actions.newTab1Fill(self.typeResponseInput,
                        "I understand the urgency and appreciate our long-standing relationship.")
        self.actions.newTab1Click(self.submitBtn)
        self.actions.newTab1WaitForTimeout(3000)
        # scenario4
        self.actions.newTab1Click(self.NextBtn2)
        self.actions.newTab1WaitForTimeout(2000)
        try:
            self.actions.newTab1Click(self.NextBtn2)
        except TimeoutError:
            print("Timeout: Element was not found or clickable within the specified time.")
        self.actions.newTab1Fill(self.typeResponseInput,
                        "I understand the urgency and appreciate our long-standing relationship.")
        self.actions.newTab1Click(self.submitBtn)
        self.actions.newTab1WaitForTimeout(3000)
        # scenario5
        self.actions.newTab1Click(self.NextBtn2)
        self.actions.newTab1WaitForTimeout(2000)
        try:
            self.actions.newTab1Click(self.NextBtn2)
        except TimeoutError:
            print("Timeout: Element was not found or clickable within the specified time.")
        self.actions.newTab1Fill(self.typeResponseInput,
                        "I understand the urgency and appreciate our long-standing relationship.")
        self.actions.newTab1Click(self.submitBtn)
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1Click(self.fiveStar)
        self.actions.newTab1Click(self.fiveCheckBox)
        self.actions.newTab1Click(self.NextBtn)
        print(self.actions.newTab1TextContent(self.reportText1))
        print(self.actions.newTab1TextContent(self.reportText2))
        self.actions.goto_newtab2_by_clicking_element(self.viewReport)
        self.actions.new_tab3_wait_for_timeout(3000)
        print(self.actions.new_tab3_text_content())


    def clicksScenarioBankCreateScenario(self):
        self.actions.get_by_text_click("ScenarioBank")
        self.actions.wait_for_timeout(1000)
        self.actions.get_by_role("button", "Create Scenario")


    def fillsTextScenarioBankCreate(self, gameTypeDesc:str, gameTypeSceQues:str, gameTypeSceHint:str, gameTypeIdealResponse:str):
        self.gameTypeHeadinggg = randomUtils.generate_random_string_with_prefix(length=10, prefix="test")
        self.actions.fill(self.gamTypHead, self.gameTypeHeadinggg)
        self.actions.frame_locator_fill("iframe[title=\"Rich Text Area\\. Press ALT-0 for help\\.\"]", "#tinymce", gameTypeDesc)
        self.actions.fill(self.gamTypQues, gameTypeSceQues)
        self.actions.fill(self.gamTypHint, gameTypeSceHint)
        self.actions.fill(self.gamTypIdealResp, gameTypeIdealResponse)
        self.actions.get_by_role("button", "Add Meta Tags")
        self.actions.click("#difficulty_level_tags")
        self.actions.get_by_text_click("Beginner")
        self.actions.get_by_test_id_by_role_click("modal-component","button", "Add Meta Tags")
        self.actions.get_by_role("button", "Add Atoms")
        self.actions.get_by_placeholder_click("Please select")
        self.actions.get_by_text_click("Sets clear goals at a team and individual level")

        self.actions.frame_locator_fill("iframe[title=\"Video Player Form\"]", "(//input[@class='input'])[1]", "SC Video Title")

        self.actions.wait_for_timeout(10000)

        #self.actions.set_input_files("(//input[@type='file'])[1]", r"C:\NewEnp\Enparadigm\Enparadigm\Enparadigm\behaveProject\Upload\Thumnail\LandscapeImage.jpg")

        self.actions.set_input_files_in_frame(self.framevideosc, self.thumbnailTextscBank, r"C:\NewEnp\Enparadigm\Enparadigm\Enparadigm\behaveProject\Upload\Thumnail\LandscapeImage.jpg")


        self.actions.wait_for_timeout(10000)

        #self.actions.set_input_files(self.videoscbank,
            #                                  r"C:\NewEnp\Enparadigm\Enparadigm\Enparadigm\behaveProject\Upload\Video\LandscapeVideo.webm")

        self.actions.set_input_files_in_frame(self.framevideosc, self.videoscbank,r"C:\NewEnp\Enparadigm\Enparadigm\Enparadigm\behaveProject\Upload\Video\LandscapeVideo.webm")
        self.actions.wait_for_timeout(10000)

        #self.actions.frame_locator_fill("iframe[title=\"Video Player Form\"]", "#tinymce", "Sc transcript1")
        self.actions.wait_for_timeout(10000)

        self.actions.set_input_files_in_frame(self.framevideosc,self.videoscbank2,
                                     r"C:\NewEnp\Enparadigm\Enparadigm\Enparadigm\behaveProject\Upload\Video\LandscapeVideo.webm")

        self.actions.wait_for_timeout(10000)
        self.actions.click("//button[@type='submit']")
        self.actions.wait_for_timeout(30000)
        self.actions.click(self.saveBtn)
        self.actions.wait_for_timeout(1500)
        self.actions.fill(self.serchModule, self.gameTypeHeadinggg)
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(1000)
        actualMessage = self.actions.text_content(self.searchedOutcome)
        expected_message = self.gameTypeHeadinggg
        assert expected_message == actualMessage, f"Expected message '{expected_message}' but got '{actualMessage}'"
        print("actualMessage", actualMessage)
        print("expected message", expected_message)
        return self.gameTypeHeadinggg

    def fillsVideoScenarioBankCreate(self, file_path1:str, moduleDescription:str, file_path2:str, gameTypeHeading:str, gameTypeDesc:str, gameTypeSceQues:str, gameTypeSceHint:str, gameTypeIdealResponse:str):
        self.actions.click(self.videoRadioBtn)
        self.actions.wait_for_timeout(5000)
        self.gameTypeVideoHeadinggg = randomUtils.generate_random_string_with_prefix(length=10, prefix="test")
        self.actions.fill(self.gamTypHead, self.gameTypeVideoHeadinggg)
        self.actions.fill(self.gamTypQues, gameTypeSceQues)
        self.actions.frame_locator_fill(self.iframeVideo1, self.videoRefNameInput, "Video Reference Name1")
        # 1.Image
        self.actions.set_input_files_in_frame(self.iframeVideo1, self.videoThumbnailInput, file_path1)
        #self.actions.set_input_files_in_frame(self.framevideosc, self.thumbnailTextscBank, r"C:\NewEnp\Enparadigm\Enparadigm\Enparadigm\behaveProject\Upload\Thumnail\LandscapeImage.jpg")

        self.actions.wait_for_timeout(5000)
        self.actions.click(self.gamTypHead)
        # 2.Video
        self.actions.set_input_files_in_frame(self.iframeVideo1, self.videoInput,
                                              r"C:\NewEnp\Enparadigm\Enparadigm\Enparadigm\behaveProject\Upload\Video\Dear.mp4")
        self.actions.wait_for_timeout(15000)
        self.actions.set_input_files_in_frame(self.iframeVideo1, self.videoInput,
                                              r"C:\NewEnp\Enparadigm\Enparadigm\Enparadigm\behaveProject\Upload\Video\VideoRefName.mp4")
        # self.actions.frame_inside_frame_type("iframe[title='Video Player Form']",
        #                                      "iframe[title='Rich Text Area. Press ALT-0 for help.']",
        #                                      "#tinymce",
        #                                      moduleDescription)
        self.actions.wait_for_timeout(15000)

        self.actions.frame_inside_frame_type_content("[data-testid=\"video-scenario-iframe\"]","iframe[title=\"Rich Text Area\\. Press ALT-0 for help\\.\"]", "#tinymce", "Video Transcript1 Transcript1 Transcript1")

        self.actions.wait_for_timeout(15000)
        #self.actions.frame_locator_click(self.iframeVideo1, "//div[@class='flex justify-end gap-4 mt-8']//button[@class='btn variant-filled']")
        #self.actions.click("//div[@class='flex justify-end gap-4 mt-8']//button[@class='btn variant-filled']")
        #self.actions.click_button_in_iframe("[data-testid=\"video-scenario-iframe\"]", "button", "Upload Video")
        #self.actions.click_button_in_iframe()
        self.actions.wait_for_timeout(60000)
        self.actions.fill(self.gamTypHint, gameTypeSceHint)
        self.actions.fill(self.gamTypIdealResp, gameTypeIdealResponse)
        self.actions.wait_for_timeout(1000)
        self.actions.get_by_role("button", "Add Meta Tags")
        self.actions.click("#difficulty_level_tags")
        self.actions.get_by_text_click("Beginner")
        self.actions.get_by_test_id_by_role_click("modal-component","button", "Add Meta Tags")
        self.actions.get_by_role("button", "Add Atoms")
        self.actions.get_by_placeholder_click("Please select")
        self.actions.get_by_text_click("Sets clear goals at a team and individual level")
        self.actions.frame_locator_fill("#iFrameResizer0", "(//label[@class='label'])//input", "Video title above video1")

        self.actions.wait_for_timeout(5000)
        self.actions.set_input_files_in_frame("iframe[title=\"Video Player Form\"]", self.videoThumbnailInput, file_path1)

        self.actions.video1upload("iframe[title='Video Player Form']", "form div", "VideoRefName.mp4")
        self.actions.wait_for_timeout(5000)

        self.actions.wait_for_timeout(5000)
        #self.actions.video1upload()
        self.actions.video1upload("iframe[title='Video Player Form']", "form div", "VideoRefName.mp4")
        self.actions.wait_for_timeout(5000)


        #self.actions.set_input_files_in_frame("iFrameResizer0", self.videoscbank,file_path2)
        self.actions.video2upload("iframe[title='Video Player Form']", "form div", "VideoRefName.mp4")

        self.actions.wait_for_timeout(5000)

        #self.actions.set_input_files_in_frame("iFrameResizer0", self.videoscbank2,file_path2)
        self.actions.wait_for_timeout(5000)

        self.actions.frame_inside_frame_type_content("#iFrameResizer0","#editor_1_ifr","#tinymce","TRANSOOO2")


        self.actions.wait_for_timeout(5000)

        self.actions.click(self.saveBtn)
        self.actions.wait_for_timeout(1500)
        self.actions.fill(self.serchModule, self.gameTypeVideoHeadinggg)
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(1000)
        actualMessage = self.actions.text_content(self.searchedOutcome)
        expected_message = self.gameTypeVideoHeadinggg
        assert expected_message == actualMessage, f"Expected message '{expected_message}' but got '{actualMessage}'"
        print("actualMessage", actualMessage)
        print("expected message", expected_message)
        return self.gameTypeVideoHeadinggg

    def enter_details_in_third_step(self, moduleDescription: str):
        self.actions.click(self.addSection)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.content)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.contentPage1)
        self.actions.fill(self.reference, "Reference1")
        self.actions.fill(self.heading, "Heading")
        self.actions.fill(self.subheading, "Sub Heading")
        self.actions.wait_for_timeout(4000)
        self.actions.frame_locator_fill("iframe[title=\"Rich Text Area\\. Press ALT-0 for help\\.\"]",
                                        "#tinymce",
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
        # actual = self.page.text_content(self.AIDiagnoGameType)
        # expected = "AI Diagnostic Gametype"
        # assert expected == actual, f"Expected message '{expected}' but got '{actual}'"
        self.actions.get_by_text_click("AI Diagnostic Gametype")
        self.actions.wait_for_timeout(3000)
        self.actions.click("//select[@class='select']")
        count = self.actions.elements_count("//select[@class='select']/option")
        elements = self.actions.locator("//select[@class='select']/option")
        for i in range(count):
             self.actions.keyboard_press("ArrowDown")
        self.actions.keyboard_press("Enter")
        # self.page.locator("//select[@class='select']").select_option(label={self.gameTypeHeadinggg})
        # dynamicXpath= f"//option[contains(text(), '{self.gameTypeVideoHeadinggg}')]"
        # self.page.click(dynamicXpath)
        self.actions.wait_for_timeout(4000)
        self.actions.click(self.saveNext)
        self.actions.wait_for_timeout(2000)
        self.actions.click("//button[text()='Save']")
        self.actions.get_by_role("button", "Add Section")
        self.actions.click(".mt-4 > div:nth-child(3)")
        self.actions.locator_gettext_click("#layout_container", "Quiz")
        self.actions.get_by_placeholder_click("Quiz Reference Name")
        self.actions.get_by_placeholder_fill("Quiz Reference Name", "quizzz")
        self.actions.locator_first_click(".slide-toggle-track")
        self.actions.locator_first_click("div:nth-child(4) > .slide-toggle > .slide-toggle-label > .slide-toggle-track")
        self.actions.click("div:nth-child(5) > .slide-toggle > .slide-toggle-label > .slide-toggle-track")
        self.actions.click("div:nth-child(6) > .slide-toggle > .slide-toggle-label > .slide-toggle-track")
        self.actions.click("div:nth-child(7) > .slide-toggle > .slide-toggle-label > .slide-toggle-track")
        self.actions.fill("#question_text1","what is an apple")
        self.actions.fill("#option_text11", "Fruit")
        self.actions.fill("#option_text12","Vegetable")
        self.actions.click(
            "#question_content1 > div:nth-child(2) > div:nth-child(3) > .slide-toggle > .slide-toggle-label > .slide-toggle-track")
        self.actions.fill("#explanation1", "apple is a fruit")
        self.actions.get_by_role("button", "Save & Next")
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.publishButton)
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.okayBtn)

    def searchesPubhished(self):
        self.actions.click(self.modulesBtn)
        self.actions.fill(self.serchModule, self.modName)
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(3000)
        expectValue = self.modName
        ModuleName = self.actions.text_content(self.moduleNameInModules)
        assert expectValue == ModuleName, f"Expected message '{expectValue}' but got '{ModuleName}'"
        ModuleType = self.actions.text_content(self.moduleTypeInModules)
        expectType = "AI Diagnostics"
        assert expectType == ModuleType, f"Expected message '{expectType}' but got '{ModuleType}'"
        moduleStatusBefore = self.actions.text_content(self.moduleStatusInMpdules)
        print("Module Status Before", moduleStatusBefore)
        self.actions.click(self.publishIcon)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.yesBtn)
        self.actions.wait_for_timeout(4000)
        actualMessage = self.actions.text_content(self.sucTxt)
        expected_message = "Module published successfully"
        assert expected_message == actualMessage, f"Expected message '{expected_message}' but got '{actualMessage}'"
        self.actions.click(self.okayBtn)
        self.actions.wait_for_timeout(1000)
        self.actions.reload()
        self.actions.wait_for_timeout(4000)
        moduleStatusAfter = self.actions.text_content(self.moduleStatusInMpdules)
        self.actions.wait_for_timeout(3000)
        print("Module Status After", moduleStatusAfter)
        print(self.modName)
        self.actions.fill(self.searchInput, self.modName)
        self.actions.wait_for_timeout(3000)
        self.actions.keyboard_press("Enter")
        self.actions.newTabAfterClickingAnElement(self.playSimula)
        self.actions.newTab1WaitForTimeout(2000)
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_get_by_role("button", "Next")
        # self.page2.get_by_role("button", name="Close").click()
        self.actions.newTab1GetByTextClick("Next")
        self.actions.newTab1WaitForTimeout(2000)
        try:
            self.actions.newTab1GetByTextClick("Next")
        except TimeoutError:
            print("Timeout: Element was not found or clickable within the specified time.")
        self.actions.get_by_placeholder_fill("Type your response", "respinse1")
        self.actions.click("#submit")
        self.actions.newTab1GetByTextClick("Let's Begin")
        self.actions.newTab1GetByTextClick(2000)
        try:
            self.actions.newTab1GetByTextClick("Let's Begin")
        except TimeoutError:
            print("Timeout: Element was not found or clickable within the specified time.")
        self.actions.newTab1GetByTextClick("Fruit", exact=True)
        self.actions.newTab1GetByTextClick("Submit")
        self.actions.newTab1GetByTextClick("Next Question")
        self.actions.goto_newtab2_by_clicking_element("div:nth-child(3) > div > .flex")
        self.actions.new_tab2_wait_for_timeout(3000)
        actualModuleName = self.actions.new_tab2_text_content(self.reportHeading)
        expectedModuleName = self.modName
        assert expectedModuleName == actualModuleName, f"Expected message '{expectedModuleName}' but got '{actualModuleName}'"
        print("actualMessage", actualModuleName)
        print("expected message", expectedModuleName)


    def serachesPlayVideoAISimUser(self):
        self.actions.click(self.modulesBtn)
        self.actions.fill(self.serchModule, self.modName)
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(3000)
        expectValue = self.modName
        ModuleName = self.actions.text_content(self.moduleNameInModules)
        assert expectValue == ModuleName, f"Expected message '{expectValue}' but got '{ModuleName}'"
        ModuleType = self.actions.text_content(self.moduleTypeInModules)
        expectType = "AI Diagnostics"
        assert expectType == ModuleType, f"Expected message '{expectType}' but got '{ModuleType}'"
        moduleStatusBefore = self.actions.text_content(self.moduleStatusInMpdules)
        print("Module Status Before", moduleStatusBefore)
        self.actions.click(self.publishIcon)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.yesBtn)
        self.actions.wait_for_timeout(4000)
        actualMessage = self.actions.text_context(self.sucTxt)
        expected_message = "Module published successfully"
        assert expected_message == actualMessage, f"Expected message '{expected_message}' but got '{actualMessage}'"
        self.actions.click(self.okayBtn)
        self.actions.wait_for_timeout(1000)
        self.actions.reload()
        self.actions.wait_for_timeout(4000)
        moduleStatusAfter = self.actions.text_content(self.moduleStatusInMpdules)
        self.actions.wait_for_timeout(3000)
        print("Module Status After", moduleStatusAfter)
        print(self.modName)
        self.actions.fill(self.searchInput, self.modName)
        self.actions.wait_for_timeout(3000)
        self.actions.keyboard.press("Enter")
        self.actions.wait_for_timeout(2000)
        self.actions.newTabAfterClickingAnElement(self.playSimula)
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1_get_by_role("button", "Next")
        try:
            self.actions.newTab1_get_by_role("button", "Close")
        except TimeoutError:
            print("Timeout: Element was not found or clickable within the specified time.")
        self.actions.newTab1GetByTextClick("Next")
        self.actions.newTab1WaitForTimeout(2000)
        try:
            self.actions.newTab1GetByTextClick("Next")
        except TimeoutError:
            print("Timeout: Element was not found or clickable within the specified time.")
        self.actions.newTab1_get_by_placeholder_fill("Type your response", "respinse1")
        self.actions.click("#submit")
        self.actions.newTab1GetByTextClick("Let's Begin")
        self.actions.newTab1WaitForTimeout(2000)
        try:
            self.actions.newTab1GetByTextClick("Let's Begin")
        except TimeoutError:
            print("Timeout: Element was not found or clickable within the specified time.")
        self.actions.newTab1GetByTextClick("Fruit", exact=True)
        self.actions.newTab1GetByTextClick("Submit")
        self.actions.newTab1GetByTextClick("Next Question")
        self.actions.goto_newtab2_by_clicking_element("div:nth-child(3) > div > .flex")
        self.actions.new_tab2_wait_for_timeout(3000)
        actualModuleName = self.actions.new_tab2_text_content(self.reportHeading)
        expectedModuleName = self.modName
        assert expectedModuleName == actualModuleName, f"Expected message '{expectedModuleName}' but got '{actualModuleName}'"
        print("actualMessage", actualModuleName)
        print("expected message", expectedModuleName)

    def moduleNameSearchesPublish(self):
        self.actions.click(self.modulesBtn)
        self.actions.fill(self.serchModule, self.modName)
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(3000)
        expectValue = self.modName
        ModuleName = self.actions.text_content(self.moduleNameInModules)
        assert expectValue == ModuleName, f"Expected message '{expectValue}' but got '{ModuleName}'"
        ModuleType = self.actions.text_content(self.moduleTypeInModules)
        expectType = "AI Diagnostics"
        assert expectType == ModuleType, f"Expected message '{expectType}' but got '{ModuleType}'"
        moduleStatusBefore = self.actions.text_content(self.moduleStatusInMpdules)
        print("Module Status Before", moduleStatusBefore)
        self.actions.click(self.publishIcon)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.yesBtn)
        self.actions.wait_for_timeout(4000)
        actualMessage = self.actions.text_content(self.sucTxt)
        expected_message = "Module published successfully"
        assert expected_message == actualMessage, f"Expected message '{expected_message}' but got '{actualMessage}'"
        self.actions.click(self.okayBtn)
        self.actions.wait_for_timeout(1000)
        self.actions.reload()
        self.actions.wait_for_timeout(4000)
        moduleStatusAfter = self.actions.text_content(self.moduleStatusInMpdules)
        self.actions.wait_for_timeout(3000)
        print("Module Status After", moduleStatusAfter)
        print(self.modName)
        self.actions.fill(self.searchInput, self.modName)
        self.actions.wait_for_timeout(3000)
        self.actions.keyboard.press("Enter")
        self.actions.wait_for_timeout(2000)

    def clicksOnPathManagementAndfillDetails1(self):
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
        ModuleName = self.actions.text_content(self.moduleNameInModules)
        ModuleName1 = ModuleName.strip() if ModuleName else None
        assert expectValue == ModuleName1, f"Expected message '{expectValue}' but got '{ModuleName1}'"
        self.actions.click(self.checkBox)
        self.actions.click(self.saveNxtCatAdm)
        self.actions.wait_for_timeout(3000)


    def clickOnmagicLink3(self):
        # username = self.page.get_by_text(self.nameTable_txt)
        # LoginMail = self.page.get_by_text(self.emailTable_txt)
        self.actions.click(self.magicLink_btn)
        self.actions.click_link_open_new_tab_coping(self.copyMagicLink_txt)
        try:
            self.actions.newTab1_get_by_role("button", "Accept")
        except Exception as e:
            print(f"An error occurred while trying to click the button: {e}")
        self.actions.newTab1Click(self.startBtn)
        self.actions.newTab1Click(self.startBtn2)
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1Click(self.NextBtn)
        self.actions.newTab1WaitForTimeout(8000)

        try:
            self.actions.newTab1Click(self.closeBtn)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        self.actions.newTab1GetByTextClick("Next")
        self.actions.newTab1WaitForTimeout(2000)
        try:
            self.actions.newTab1GetByTextClick("Next")
        except TimeoutError:
            print("Timeout: Element was not found or clickable within the specified time.")
        self.actions.newTab1_get_by_placeholder_fill("Type your response", "respinse1")
        self.actions.click("#submit")
        self.actions.newTab1GetByTextClick("Let's Begin")
        self.actions.newTab1WaitForTimeout(2000)
        try:
            self.actions.newTab1GetByTextClick("Let's Begin")
        except TimeoutError:
            print("Timeout: Element was not found or clickable within the specified time.")
        self.actions.newTab1GetByTextClick("Fruit")
        self.actions.newTab1GetByTextClick("Submit")
        self.actions.newTab1GetByTextClick("Next Question")
        self.actions.goto_newtab2_by_clicking_element("div:nth-child(3) > div > .flex")
        self.actions.new_tab2_wait_for_timeout(3000)
        actualModuleName = self.actions.new_tab2_text_content(self.reportHeading)
        expectedModuleName = self.modName
        assert expectedModuleName == actualModuleName, f"Expected message '{expectedModuleName}' but got '{actualModuleName}'"
        print("actualMessage", actualModuleName)
        print("expected message", expectedModuleName)

    def clickOnCohortCreateUser(self):
        self.actions.click(self.createUserBtn)
        self.actions.wait_for_timeout(10000)

    def fillingEmptyValuesCreatingTextScenario(self, SceHeading:str, SceDescrip:str, SceQuestion:str, SceHint:str, SceIdealResp:str, MetaTags:str, Atoms:str):
        if SceHeading == '""':  # Handle empty string from Gherkin
            SceHeading = ""
        self.actions.fill(self.gamTypHead, SceHeading)
        if SceDescrip == '""':  # Handle empty string from Gherkin
            SceDescrip = ""
        self.actions.frame_locator_fill("iframe[title=\"Rich Text Area\\. Press ALT-0 for help\\.\"]", "#tinymce",
            SceDescrip)
        if SceQuestion == '""':  # Handle empty string from Gherkin
            SceQuestion = ""
        self.actions.fill(self.gamTypQues, SceQuestion)
        if SceHint == '""':  # Handle empty string from Gherkin
            SceHint = ""
        self.actions.fill(self.gamTypHint, SceHint)
        if SceIdealResp == '""':  # Handle empty string from Gherkin
            SceIdealResp = ""
        self.actions.fill(self.gamTypIdealResp, SceIdealResp)
        if MetaTags == "selMetTag":
            self.actions.get_by_role("button", "Add Meta Tags")
            self.actions.click("#difficulty_level_tags")
            self.actions.get_by_text_click("Beginner")
            self.actions.get_by_test_id_by_role_click("modal-component", "button", "Add Meta Tags")
        else:
            print("..")
        if Atoms == "selAtom":
            self.actions.get_by_role("button", "Add Atoms")
            self.actions.get_by_placeholder_click("Please select")
            self.actions.get_by_text_click("Sets clear goals at a team and individual level")
        else:
            print("..")
        self.actions.click(self.saveBtn)

    def validatingTextScenarioErrorMessages(self):
        actualMessage = self.actions.text_content(self.sucTxt)
        if actualMessage == "Please select atleast one tag":
            expected_message = "Please select atleast one tag"
            assert expected_message == actualMessage, f"Expected message '{expected_message}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message)
        elif actualMessage == "Please select atleast one atom":
            expected_message1 = "Please select atleast one atom"
            assert expected_message1 == actualMessage, f"Expected message '{expected_message1}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
        elif actualMessage == "Please select/upload a video":
            expected_message3 = "Please select/upload a video"
            assert expected_message3 == actualMessage, f"Expected message '{expected_message3}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
        else:
            expected_message2 = "Please fill all the fields in the scenario"
            assert expected_message2 == actualMessage, f"Expected message '{expected_message2}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message2)

    def fillingEmptyValuesCreatingVideoScenario(self, SceHeading:str, SceDescrip:str, VideoRefName:str, Thumbnail:str, Video:str, SceQuestion:str, SceHint:str, SceIdealResp:str, MetaTags:str, Atoms:str ):
        self.actions.click(self.videoRadioBtn)
        self.actions.wait_for_timeout(5000)
        if SceHeading == '""':  # Handle empty string from Gherkin
            SceHeading = ""
        self.actions.fill(self.gamTypHead, SceHeading)
        if SceQuestion == '""':  # Handle empty string from Gherkin
            SceQuestion = ""
        self.actions.fill(self.gamTypQues, SceQuestion)
        if VideoRefName == '""':  # Handle empty string from Gherkin
            VideoRefName = ""
        self.actions.frame_locator_fill(self.iframeVideo1, self.videoRefNameInput, VideoRefName)
        # 1.Image
        if Thumbnail == "selthumnl":
            self.actions.set_input_files_in_frame(self.iframeVideo1, self.videoThumbnailInput,
                r"C:\Users\hp\PycharmProjects\Enparadigm\Enparadigm\behaveProject\Upload\Thumnail\Thumbnail.png"
            )
            self.actions.wait_for_timeout(5000)
            self.actions.click(self.gamTypHead)
        else:
            print("..")
        # 2.Video
        if Video == "selvd":  # Handle empty string from Gherkin
            self.actions.set_input_files_in_frame(self.iframeVideo1, self.videoInput,
                r"C:\Users\hp\PycharmProjects\Enparadigm\Enparadigm\behaveProject\Upload\Video\Dear.mp4")
            self.actions.wait_for_timeout(15000)
            self.actions.set_input_files_in_frame(self.iframeVideo1, self.videoInput,
                r"C:\Users\hp\PycharmProjects\Enparadigm\Enparadigm\behaveProject\Upload\Video\VideoRefName.mp4")
        else:
            print("..")
        if SceDescrip == '""':  # Handle empty string from Gherkin
            SceDescrip = ""
        self.actions.frame_inside_frame_type("iframe[title='Video Player Form']",
            "iframe[title='Rich Text Area. Press ALT-0 for help.']", "#tinymce",
            SceDescrip)
        self.actions.wait_for_timeout(10000)
        if Thumbnail == "selthumnl" or Video == "selvd" or VideoRefName != "":
            self.actions.frame_locator_click(self.iframeVideo1, "//button[text()='Upload Video']")
        else:
            print("")
        self.actions.wait_for_timeout(15000)
        if SceHint == '""':  # Handle empty string from Gherkin
            SceHint = ""
        self.actions.fill(self.gamTypHint, SceHint)
        if SceIdealResp == '""':  # Handle empty string from Gherkin
            SceIdealResp = ""
        self.actions.fill(self.gamTypIdealResp, SceIdealResp)
        if MetaTags == "selMetTag":
            self.actions.get_by_role("button", "Add Meta Tags")
            self.actions.locator("#difficulty_level_tags").click()
            self.actions.get_by_text_click("Beginner")
            self.actions.get_by_test_id_by_role_click("modal-component", "button", "Add Meta Tags")
        else:
            print("..")
        if Atoms == "selAtom":
            self.actions.get_by_role("button", "Add Atoms")
            self.actions.get_by_placeholder_click("Please select")
            self.actions.get_by_text_click("Sets clear goals at a team and individual level")
        else:
            print("..")
        self.actions.click(self.saveBtn)


    def clicksOnSceClicksOnSearch(self):
        self.actions.get_by_text_click("ScenarioBank")
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.serchModule)


    def entersValidSearchInput(self, PossibleSearch):
        self.actions.fill(self.serchModule, PossibleSearch)
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(2000)


    def ableToSeeSearchOutcome(self):
        actualModuleName = self.actions.text_content(self.firstRowSce)
        expectedModuleName = "A Sudden Presentation"
        assert expectedModuleName == actualModuleName, f"Expected message '{expectedModuleName}' but got '{actualModuleName}'"
        print("actualMessage", actualModuleName)
        print("expected message", expectedModuleName)

    def clicksSceBankEditBtn(self):
        self.actions.get_by_text_click("ScenarioBank")
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.editBtn)

    def editScenarioDetails(self):
        self.actions.fill(self.gamTypQues, "editooq")
        self.actions.fill(self.gamTypHint, "editoooh")
        self.actions.fill(self.gamTypIdealResp, "editooir")
        self.actions.click(self.saveBtn)
        self.actions.wait_for_timeout(1500)

    def entersNonExistingScenario(self):
        self.actions.fill(self.serchModule, "...............")
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(2000)


    def NotAbleToBeSeeSearch(self):
        if self.actions.is_visible(self.nonExistingScenarioOutcome, "nonExistingScenarioOutcome"):
            print("Scenario is existed")
        else:
            print("Scenario is not existed")

    def clicksSceBnkEditBtn1(self):
        self.actions.get_by_text_click("ScenarioBank")
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.editBtn1)

    def fillingEmptyValuesEditingTextScenario(self, SceHeading, SceDescrip, SceQuestion, SceHint, SceIdealResp, MetaTags, Atoms):
        if SceHeading == '""':  # Handle empty string from Gherkin
            SceHeading = ""
        self.actions.fill(self.gamTypHead, SceHeading)
        if SceDescrip == '""':  # Handle empty string from Gherkin
            SceDescrip = ""
        self.actions.frame_locator_fill("iframe[title=\"Rich Text Area\\. Press ALT-0 for help\\.\"]", "#tinymce",
            SceDescrip)
        if SceQuestion == '""':  # Handle empty string from Gherkin
            SceQuestion = ""
        self.actions.fill(self.gamTypQues, SceQuestion)
        if SceHint == '""':  # Handle empty string from Gherkin
            SceHint = ""
        self.actions.fill(self.gamTypHint, SceHint)
        if SceIdealResp == '""':  # Handle empty string from Gherkin
            SceIdealResp = ""
        self.actions.fill(self.gamTypIdealResp, SceIdealResp)
        if MetaTags == "selMetTag":
            print("..")
        else:
            self.actions.click(self.metatagsWrngButton)
            self.actions.click(self.metatagsWrngButton)
            self.actions.click(self.metatagsWrngButton)
            self.actions.click(self.metatagsWrngButton)
            self.actions.click(self.metatagsWrngButton)
            self.actions.click(self.metatagsWrngButton)
            self.actions.click(self.metatagsWrngButton)
        if Atoms == "selAtom":
            print("...")
        else:
            self.actions.click(self.deleteIcon)
        self.actions.click(self.saveBtn)

    def searchesSceDeleteSce(self):
        self.actions.fill(self.serchModule, self.gameTypeHeadinggg)
        self.actions.keyboard_press("Enter")
        actualModuleName = self.actions.text_context(self.firstRowSce)
        expectedModuleName = self.gameTypeHeadinggg
        assert expectedModuleName == actualModuleName, f"Expected message '{expectedModuleName}' but got '{actualModuleName}'"
        print("actualMessage", actualModuleName)
        print("expected message", expectedModuleName)
        self.actions.click(self.deleteButton)
        self.actions.click(self.cancelButton)
        self.actions.fill(self.serchModule, self.gameTypeHeadinggg)
        if self.actions.is_visible(self.nonExistingScenarioOutcome, "nonExistingScenarioOutcome"):
            print("Scenario is not deleted")
        else:
            print("Scenario is not existed")


    def searchModule(self):
        self.actions.fill(self.searchInput, "Sim's-1@ Sim's-2")
        self.actions.keyboard_press("Enter")

    def ableToSeeOutcome(self):
        actualModuleName = self.actions.text_content(self.firstRowSce)
        expectedModuleName = "Sim's-1@ Sim's-2"
        assert expectedModuleName == actualModuleName, f"Expected message '{expectedModuleName}' but got '{actualModuleName}'"
        print("actualMessage", actualModuleName)
        print("expected message", expectedModuleName)

    def verifiesModuleFieldsPropelyDisplayedInUserProperly(self):
        self.actions.newTabAfterClickingAnElement(self.playSimula)
        self.actions.newTab1WaitForTimeout(3000)
        actualModuleName = self.actions.newTab1TextContent(self.moduleNameTxt)
        expectedModuleName = "Sim's-1@ Sim's-2"
        assert expectedModuleName == actualModuleName, f"Expected message '{expectedModuleName}' but got '{actualModuleName}'"
        print("actualMessage", actualModuleName)
        print("expected message", expectedModuleName)
        actualheadingName = self.actions.newTab1TextContent(self.headingTxt)
        expectedheadinName = "heading-8989"
        assert expectedheadinName == actualheadingName, f"Expected message '{expectedheadinName}' but got '{actualheadingName}'"
        print("actualMessage", actualheadingName)
        print("expected message", expectedheadinName)
        actualsubheadingName = self.actions.newTab1TextContent(self.sideHeadingTxt)
        expectedsubheadingName = "subheading-5665"
        assert expectedsubheadingName == actualsubheadingName, f"Expected message '{expectedsubheadingName}' but got '{actualsubheadingName}'"
        print("actualMessage", actualsubheadingName)
        print("expected message", expectedsubheadingName)
        actualcontentPageRefName = self.actions.newTab1TextContent(self.contentPageRef)
        expectedcontentPageRefName = "fsaaaaaaaaaa, jkjk"
        assert expectedcontentPageRefName == actualcontentPageRefName, f"Expected message '{expectedcontentPageRefName}' but got '{actualcontentPageRefName}'"
        print("actualMessage", actualcontentPageRefName)
        print("expected message", expectedcontentPageRefName)
        self.actions.newTab1_get_by_role("button", "Next")
        actualsecDescpTxtName = self.actions.newTab1TextContent(self.secDescpTxt)
        expectedsecDescpTxtName = "description's progessive & format"
        assert expectedsecDescpTxtName == actualsecDescpTxtName, f"Expected message '{expectedsecDescpTxtName}' but got '{actualsecDescpTxtName}'"
        print("actualMessage", actualsecDescpTxtName)
        print("expected message", expectedsecDescpTxtName)
        actualsecHeadingTxtName = self.actions.newTab1TextContent(self.secHeadingTxt)
        expectedsecHeadingTxtName = "heading-100"
        assert expectedsecHeadingTxtName == actualsecHeadingTxtName, f"Expected message '{expectedsecHeadingTxtName}' but got '{actualsecHeadingTxtName}'"
        print("actualMessage", actualsecHeadingTxtName)
        print("expected message", expectedsecHeadingTxtName)
        self.actions.newTab1Click("#next")
        actualsecQuestTxt = self.actions.newTab1TextContent(self.secQuestTxt)
        #self.actions.newTab1Click("#next")
        expectedsecQuestTxt = "what is an apple & mango @ forest"
        assert expectedsecQuestTxt == actualsecQuestTxt, f"Expected message '{expectedsecQuestTxt}' but got '{actualsecQuestTxt}'"
        print("actualMessage", actualsecQuestTxt)
        print("expected message", expectedsecQuestTxt)

    def clicksOnPathManagementAndSearchModule(self):
        self.actions.wait_for_timeout(30000)
        self.actions.click(self.pathManagement)
        self.actions.click(self.pathManagement)

        #self.page.get_by_role("link", name=" Path Management").click()
        self.actions.wait_for_timeout(4000)
        self.actions.click(self.createPath)
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.static)
        self.actions.wait_for_timeout(1000)
        self.actions.click(self.selectModulesCatAdm)
        self.actions.fill(self.serchModule, "Sim's-1@ Sim's-2")
        self.actions.keyboard_press("Enter")
        self.actions.wait_for_timeout(3000)
        self.actions.wait_for_timeout(3000)
        expectValue = "Sim's-1@ Sim's-2"
        ModuleName = self.actions.text_content(self.moduleNameInModules)
        ModuleName1 = ModuleName.strip() if ModuleName else None
        assert expectValue == ModuleName1, f"Expected message '{expectValue}' but got '{ModuleName1}'"
        self.actions.click(self.checkBox)
        self.actions.click(self.saveNxtCatAdm)
        self.actions.click(self.createNewBtn)
        self.actions.wait_for_timeout(3000)


    def verifiesModuleDetailsProperlyDisplayed(self):
        self.actions.click(self.OkayBtnCatAdm)
        self.actions.click(self.editModuleDetailsBtn)
        self.actions.wait_for_timeout(2000)
        actual = self.actions.text_context(self.modHeadPathMag)
        expectValue2 = "Sim's-1@ Sim's-2"
        assert expectValue2 == actual, f"Expected message '{expectValue2}' but got '{actual}'"
        self.actions.wait_for_timeout(2000)
        actual = self.actions.input_value(self.headingPathEdit)
        expectValue = "Sim & heading"
        assert expectValue == actual, f"Expected message '{expectValue}' but got '{actual}'"
        self.actions.wait_for_timeout(2000)
        actual1 = self.actions.input_value(self.descPathEdit)
        expectvalue2 = "description is describing description's - description"
        assert expectvalue2 == actual1, f"Expected message '{expectvalue2}' but got '{actual1}'"
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.saveNxtCatAdm)
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.OkayBtnCatAdm)


















