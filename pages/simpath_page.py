import configparser

from pages.base_page import BasePage
from playwright.sync_api import Page

from utils import randomUtils


from features.environment import browser_context

from pages.WebActions import WebActions

config = configparser.ConfigParser()
config.read('config.ini')


class SimPage:

    def __init__(self, page, browser_context):

        self.actions = WebActions(page, browser_context)


        self.sim1Resume_btn = "(//span[text()='Resume'])[2]"
        self.sim1Header_txt = "//div[text()='Lucid - assertiveness at work']"
        self.sim2Start_btn = "//div[2]//div[1]//section[1]//div[2]//button[2]"
        self.sim2Resume_btn = "(//span[text()='Resume'])[4]"
        self.sim2Header_txt = "(//div[text()='Test path 1308'])[1]"
        self.resume_btn = "(//span[text()='Resume'])"
        self.missedPromotion_text = "//div[@class='padding-right-20 theme-font4 scenario-title']"
        self.company_drpdwn = "(//span[@title='All'])[2]"
        self.cominput = "//input[@class='select2-search__field']"
        self.cohort_drpdwn = "(//span[@role='combobox'])[11]"
        # self.madhuri_cmpny = "//li[text()='testmadhuri']"
        self.madhuri_cmpny = "//li[text()='testmadhuri']"
        self.name_input = "(//input[@placeholder='Name'])[2]"
        self.username_input = "(//input[@placeholder='Username'])[2]"
        self.role_input = "//input[@placeholder='Designation']"
        self.manager_input = "(//input[@placeholder='Manager Name'])[2]"
        self.createUser_btn = "//input[@class='btn btn-info createUser']"
        self.success_createuser_txt = "//span[text()='Success']"
        self.search_magic_link_page = "//input[@placeholder='Search']"
        self.serach_btn_magic_page = "//button[text()='Search']"
        self.name_magic_page = "//td[@class='nameTd']"
        self.username_magic_page = "//td[@class='usernameTd']"
        self.en_talenthub_button = "//span[text()='Talent Hub']"
        self.en_actionItem_button = "//span[text()='Action Item']"
        self.progress_btn = "//span[text()='Progress']"
        self.resources_btn = "//span[text()='Resources']"
        self.social_btn = "//span[text()='Social']"
        self.achievements = "//span[text()='Achievements']"
        self.roletxt = "//span[text()='Your Role']/ancestor::div[@class='flex']/following-sibling::div/span"
        self.managertxt = "//span[text()='Manager']/ancestor::div[@class='flex']/following-sibling::div/span"
        self.completiontxt = "//div[@class='flex ']//figure"
        self.fitscore = "//div[@class='flex']//figure"
        self.timeSpent = "(//div[text()='Time Spent'])[1]/following-sibling::div"
        self.modulesCom = "(//div[text()='Modules Completed'])[1]/following-sibling::div"
        self.lastAccAct = "(//div[text()='Last Account Activity'])[1]/following-sibling::div"
        self.activeMem = "(//div[text()='Active Members'])[1]/following-sibling::div"
        self.recPaths = "(//div[text()='Recommended Paths'])[1]/following-sibling::div"
        self.yourActivityScore = "(//div[text()='Your Activity Score'])[1]/following-sibling::div"
        self.diagReports = "(//div[text()='Diagnostic Reports'])[1]/following-sibling::div"
        self.simReports = "(//div[text()='Simulation Reports'])[1]/following-sibling::div"
        self.conceptVideos = "(//div[text()='Concept Videos'])[1]/following-sibling::div"
        self.progressNum= "(//div[@class='items-top pl-2 pb-5 text-es-400 text-pallet-color-23'])[2]"
        self.learningPathBtn = "//span[text()='Learning Path']"
        self.startBtn = "(//span[text()='Start'])[4]"
        self.insideStartBtn = "//span[text()='Start']"
        self.firstOptionInReadMail = "(//div[@class='optionInnerContainer theme-font5']/div)[1]"
        self.ContBtnInCourse = "//input[@value='Continue']"
        self.opinatedOption = "(//div[@value='5'])[1]"
        self.opinatedOption1 = "(//div[@value='5'])[2]"
        self.checkbox1 = "(//div[@class='checkmarkbox'])[6]"
        self.beginBtn = "//button[normalize-space()='Begin']"
        self.nxtQuest = "(//div[@class='nextButtonContainer']/button)"
        self.conBtn = "//button[@value='Continue']"
        self.nextBtn = "//button[@value='Next']"
        self.rating = "//span[@rating='5']"
        self.en_username = "//div[@class='w-fit ml-4 text-pa-400 max-sm:hidden cursor-pointer']"
        self.en_homepagetext = "//div[@class='text-m-ht-700 sm:text-ht-700']"
        self.clstxt = "//div[@class='col-span-1 animate-slide-in-bottom w-17']"
        self.Close_btn = "(//button[text()='Close'])[1]"
        self.nexxtBtn1 = "(//input[@value='Next'])[1]"
        self.nexxtBtn2 = "(//input[@value='Next'])[2]"
        self.resourceViewIcon = "(//span[text()='View']/preceding-sibling::img)[1]"
        self.viewReportTxt = "//span[text()='View Report']"
        self.downloadReportResources = "//span[text()='Download Report']/ancestor::button"
        self.resourcereportCloseBtn = "(//div[@class='flex items-center']/following-sibling::button)[2]"
        self.certificateAchie = "(//img[@alt='certificate'])[2]"
        self.badgeAchive = "//div[@id='badge-undefined']"
        self.viewBtn1Achie = "(//span[text()='View'])[1]"
        self.viewBtn2Achie = "(//span[text()='View'])[2]"
        self.certiCourseName = "//img[@alt='certificate']/ancestor::span/following-sibling::span"
        self.closeBtnAchiev = "//img[@alt='close']"
        self.download1Achie = "(//span[text()='Download'])[1]"
        self.download2Achie = "(//span[text()='Download'])[2]"
        self.badgetxtAchi = "//span[text()='Congratulations!']"



    def clickOnSim1ResumeBtn(self):
        self.actions.click(self.sim1Resume_btn)

    def validateSim1Heading(self):
        self.actions.is_visible(self.sim1Header_txt, "Sim1 Header")

    def clickOnResumeBtn(self):
        self.actions.click(self.resume_btn)

    def validateMissedPromotionText(self):
        self.actions.is_visible(self.missedPromotion_text, "Missed Promotion")

    def clickOnSim2StartBtn(self):
        print(self.actions.url)
        self.actions.go_back()
        self.actions.go_back()
        print(self.actions.url)
        self.actions.click(self.sim2Resume_btn)

    def validateSim2Heading(self):
        self.actions.is_visible(self.sim2Header_txt, "Sim2 Header")


    def selectsCompanyCohortTestMadhuri(self):
        try:
            self.actions.click(self.company_drpdwn)
            self.actions.wait_for_timeout(3000)
            self.actions.click(self.company_drpdwn)
            self.actions.fill(self.cominput, "testmadhuri")
            self.actions.click(self.madhuri_cmpny)
        except Exception as e:
            self.actions.click(self.company_drpdwn)
            self.actions.wait_for_timeout(3000)
            self.actions.click(self.company_drpdwn)
            self.actions.fill(self.cominput, "testmadhuri")
            self.actions.click(self.madhuri_cmpny)

    def enterUserDetails(self):
        self.co_name = randomUtils.generate_random_string_with_prefix(length=10, prefix="test")
        self.actions.fill(self.name_input, self.co_name)
        self.user_username= randomUtils.generate_random_email()
        self.actions.fill(self.username_input, self.user_username)
        self.actions.fill(self.role_input, "team lead")
        self.actions.fill(self.manager_input, "Madhuri")
        # self.page.check(self.simulation_chkbx)
        self.actions.click(self.createUser_btn)
        self.actions.wait_for_timeout(4000)
        if self.actions.is_visible(self.Close_btn, "Close Button"):
            print("visible")
            self.actions.get_by_role("button", "Close")
        return self.co_name, self.user_username

    def verifiesUserDetails(self):
        self.actions.fill(self.search_magic_link_page, self.co_name)
        self.actions.click(self.serach_btn_magic_page)
        actualMessage = self.actions.text_content(self.name_magic_page)
        expected_message = self.co_name
        assert expected_message == actualMessage, f"Expected message '{expected_message}' but got '{actualMessage}'"
        print("actualMessage", actualMessage)
        print("expected message", expected_message)
        actualMessage1 = self.actions.text_content(self.username_magic_page)
        expected_message1 = self.user_username
        assert expected_message == actualMessage, f"Expected message '{expected_message1}' but got '{actualMessage1}'"
        print("actualMessage", actualMessage1)
        print("expected message", expected_message1)


    def verifiesAllValuesBeforeCourseCompletion(self):
        self.actions.opening_browse_context_newTab1()
        self.actions.newTab1Click(self.en_talenthub_button)
        # Menu
        print("Menu")
        self.youreRoleTxt = self.actions.newTab1TextContent(self.roletxt)
        print("Your Role ", self.youreRoleTxt)
        self.managerTxt = self.actions.newTab1TextContent(self.managertxt)
        print("Your Manager ", self.managerTxt)
        try:
            self.compTxt = self.actions.newTab1_get_attribute(self.completiontxt, "aria-valuenow")
            print("Completion ", self.compTxt, "%")
        except Exception as e:
            print("No Completion")
        try:
            self.fitScoreTxt = self.actions.newTab1_get_attribute(self.fitscore, "aria-valuenow")
            print("Fit Score ", self.fitScoreTxt, "%")
        except Exception as e:
            print("No Fit Score")

        # Performance
        print("Performance")

        self.total_skills =  self.actions.newTab1_get_by_role_nth_text_content("cell", "Total Skills","div", 1)
        print("Total Skills ", self.total_skills)
        self.proficent_skills = self.actions.newTab1_get_by_role_nth_text_content("cell", "Proficient Skills", "div", 1)
        print("Proficent Skills ", self.proficent_skills)
        self.developing_skills = self.actions.newTab1_get_by_role_nth_text_content("cell", "Developing Skills", "div", 1)
        print("Developing Skills ", self.developing_skills)
        # Action Item
        print("Action Item ")
        self.actions.newTab1Click(self.en_actionItem_button)
        self.simul_played = self.actions.newTab1_get_by_role_nth_text_content("cell", "Simulations Played","div", 1)
        print("Simulation Played ", self.simul_played)
        self.actionitems_selected = self.actions.newTab1_get_by_role_nth_text_content("cell", "Action Items Selected","div", 1)
        print("Action Item Selected ", self.actionitems_selected )
        self.actionitems_completed = self.actions.newTab1_get_by_role_nth_text_content("cell", "Action Items Completed", "div", 1)
        print("Action Item Completed ", self.actionitems_completed)
#         Progress
        print("Progess")
        self.actions.newTab1Click(self.progress_btn)
        self.time_spentt = self.actions.newTab1TextContent(self.timeSpent)
        print("Time Spent ", self.time_spentt)
        self.modules_completedd = self.actions.newTab1TextContent(self.modulesCom)
        print("Modules Completed ", self.modules_completedd)
        self.last_account_activityy = self.actions.newTab1TextContent(self.lastAccAct)
        print("Last Account Activity ", self.last_account_activityy)
        self_progessNumTxt = self.actions.newTab1TextContent(self.progressNum)
        print("Progess ", self_progessNumTxt)

#         Social
        print("Social")
        self.actions.newTab1Click(self.social_btn)
        self.activeMemmm = self.actions.newTab1TextContent(self.activeMem)
        print("Active Members ", self.activeMemmm)
        self.recPathsss = self.actions.newTab1TextContent(self.recPaths)
        print("Recording Paths ", self.recPathsss)
        self.yourActivityScoreee = self.actions.newTab1TextContent(self.yourActivityScore)
        print("Your Activity Score ", self.yourActivityScoreee)

#         Resources
        print("Resources")
        self.actions.newTab1Click(self.resources_btn)
        self.diagReportstxt = self.actions.newTab1TextContent(self.diagReports)
        print("Diagnostics Reports ", self.diagReportstxt)
        self.simReportstxt = self.actions.newTab1TextContent(self.simReports)
        print("Simulation Reports ", self.simReportstxt)
        self.conceptVideostxt = self.actions.newTab1TextContent(self.conceptVideos)
        print("Concept Videos ", self.conceptVideostxt)
        try:
            if self.actions.newTab1_is_visible(self.resourceViewIcon):
                self.actions.newTab1Click(self.resourceViewIcon)
                print(self.actions.newTab1TextContent(self.viewReportTxt))
                self.actions.newTab1Click(self.downloadReportResources)
                self.actions.newTab1WaitForTimeout(5000)
                self.actions.newTab1Click(self.resourcereportCloseBtn)
            else :
                print("Before Doing Course")
        except Exception as e:
            print("Before Doing Course")

        # Achievements
        print("Achievements")
        self.actions.newTab1WaitForTimeout(3000)
        self.actions.newTab1Click(self.achievements)
        self.actions.newTab1WaitForTimeout(3000)
        try:
            # certificate
            if self.actions.newTab1_is_visible(self.certificateAchie):
                self.actions.newTab1Click(self.viewBtn1Achie)
                print(self.actions.newTab1TextContent(self.certiCourseName))
                self.actions.newTab1Click(self.closeBtnAchiev)
                self.actions.newTab1Click(self.download1Achie)
                self.actions.newTab1WaitForTimeout(5000)
                # badge
                self.actions.newTab1Click(self.viewBtn2Achie)
                print(self.actions.newTab1TextContent(self.badgetxtAchi))
                self.actions.newTab1Click(self.closeBtnAchiev)
                self.actions.newTab1Click(self.download2Achie)
                self.actions.newTab1WaitForTimeout(5000)
            else :
                print("No certificate and badge")

        except Exception as e:
            print("Before Doing Course")

    def clciksLearningPathStartedCourse(self):
        self.actions.newTab1Click(self.learningPathBtn)
        self.actions.newTab1Click(self.startBtn)
        self.actions.newTab1Click(self.insideStartBtn)
        self.actions.newTab1_get_by_role("button", "Read Mail")
        self.actions.newTab1_get_by_role("button", "Next")
        # firsttime
        self.actions.newTab1_get_by_role("button", "Start Playing")
        for i in range(1,6):
            self.actions.newTab1WaitForTimeout(5000)
            self.actions.newTab1_dbclick(self.firstOptionInReadMail)
            self.actions.newTab1WaitForTimeout(5000)
            if i <= 5:
                self.actions.newTab1Click(self.ContBtnInCourse)
        self.actions.newTab1_get_by_role("button", "NEXT")
        self.actions.newTab1Click(self.opinatedOption)
        self.actions.newTab1_get_by_role("button", "Next")
        self.actions.newTab1_locator_first_click(".checkmarkbox")
        self.actions.newTab1_get_by_role("button", "Next")
        self.actions.newTab1Click(self.opinatedOption1)
        self.actions.newTab1_get_by_role("button", "Next")
        self.actions.newTab1Click(self.checkbox1)
        self.actions.newTab1_get_by_role("button", "Next")
        for i in range(1,5):
            self.actions.newTab1Click("(//button[text()='Next'])["+str(i)+"]")
        self.actions.newTab1_get_by_role("button", "Next")
        self.actions.newTab1WaitForTimeout(5000)
        try:
            self.actions.newTab1_get_by_role("button", "Close")
        except Exception as e:
            print("")
        self.actions.newTab1_get_by_role("button", "Next")
        # second time
        self.actions.newTab1_get_by_role("button", "Start Playing")
        for i in range(1,6):
            self.actions.newTab1WaitForTimeout(5000)
            self.actions.newTab1_dbclick(self.firstOptionInReadMail)
            self.actions.newTab1WaitForTimeout(5000)
            if i <= 5:
                self.actions.newTab1Click(self.ContBtnInCourse)
        self.actions.newTab1_get_by_role("button", "NEXT")
        self.actions.newTab1Click(self.opinatedOption)
        self.actions.newTab1_get_by_role("button", "Next")
        self.actions.newTab1_locator_first_click(".checkmarkbox")
        self.actions.newTab1_get_by_role("button", "Next")
        self.actions.newTab1Click(self.opinatedOption1)
        self.actions.newTab1_get_by_role("button", "Next")
        self.actions.newTab1Click(self.checkbox1)
        self.actions.newTab1_get_by_role("button", "Next")
        for i in range(1,5):
            self.actions.newTab1Click("(//button[text()='Next'])["+str(i)+"]")
        self.actions.newTab1_get_by_role("button", "Next")
        self.actions.newTab1WaitForTimeout(5000)
        try:
            self.actions.newTab1_get_by_role("button", "Close")
        except Exception as e:
            print("")
        self.actions.newTab1_get_by_role("button", "Next")
        self.actions.newTab1_get_by_role("button", "Next")
#         quiz
        self.actions.newTab1Click(self.beginBtn)
        for i in range(1,8):
            self.actions.newTab1Click("(//div[@optionId='1'])["+ str(i)+"]")
            self.actions.newTab1Click("//div[@class='submitButtonConatiner']/button")
            self.actions.newTab1Click("(//div[@class='nextButtonContainer']/button)["+str(i)+"]")
        self.actions.newTab1Click(self.conBtn)
        self.actions.newTab1Click(self.nextBtn)
        self.actions.newTab1Click(self.rating)
        self.actions.newTab1_locator_first_click(".checkmarkbox")
        self.actions.newTab1_get_by_role("button", "Submit")
        self.actions.newTab1_get_by_role("button", "Continue To Catalyx Home")
        self.actions.newTab1WaitForTimeout(10000)

    def clicksOnaccept(self):
        self.actions.newTab1_get_by_role("button", "Accept")

    def en_getDynamicUsername(self):
        user_elements = self.actions.newTab1TextContent(self.en_username)
        return user_elements

    def en_homepagevalidation(self):
        message_elements = self.actions.newTab1TextContent(self.en_homepagetext)
        if "the expert in anything was once a beginner" in message_elements:
            message_elements.trim()
        return message_elements

    def validateclass(self) -> int:
        self.actions.newTab1WaitForTimeout(self.clstxt)
        elements = self.actions.newTab1_elements_count(self.clstxt)
        return elements

    def userdoeswhatever(self):
        self.actions.goto("https://test.catalyx.live/catalyxapi/v1/user_magic_link_mapping/verify_magic_link?user_magic_link_token=aca33724-8ab6-4e33-967f-3ed1633ec397")
        self.actions.wait_for_timeout(3000)
        self.actions.click(self.en_talenthub_button)
        self.actions.wait_for_timeout(3000)
        self.actions.click(self.achievements)
        self.actions.wait_for_timeout(3000)
        # certificate
        if self.actions.is_visible(self.certificateAchie, "certificateAchie"):
            self.actions.click(self.viewBtn1Achie)
            print(self.actions.text_content(self.certiCourseName))
            self.actions.click(self.closeBtnAchiev)
            self.actions.click(self.download1Achie)
            self.actions.wait_for_timeout(5000)
            # badge
            self.actions.click(self.viewBtn2Achie)
            print(self.actions.text_content(self.badgetxtAchi))
            self.actions.click(self.closeBtnAchiev)
            self.actions.click(self.download2Achie)
            self.actions.wait_for_timeout(5000)
        else:
            print("No certificate and badge")


























