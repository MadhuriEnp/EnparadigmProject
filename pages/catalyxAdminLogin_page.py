from loguru import logger
from pages.base_page import BasePage
from utils import randomUtils
from playwright.sync_api import Page, expect
import configparser
from utils.shared_data import write_to_file, read_from_file
import pyperclip

from pages.WebActions import WebActions

config = configparser.ConfigParser()
config.read('config.ini')


class CatalyxAdminPage():
    def __init__(self, page, browser_context):

        self.actions = WebActions(page, browser_context)

        self.signInWithGoogle_btn = "//span[@class='nsm7Bb-HzV7m-LgbsSe-BPrWId']"
        self.signin_txt = "//span[normalize-space()='Sign in']"
        self.enterUsername_input = "//input[@id='identifierId']"
        self.next_btn = "(//div[@class='VfPpkd-RLmnJb'])[2]"
        self.enterPassword_input = "//input[@type='password']"
        self.en_password_input = "//input[@placeholder='Enter Password']"
        self.en_login_button = "//button[@class='submit_password btn w-full mt-2 bg-pallet-color-1 hover:bg-pallet-color-1-hover text-white rounded-lg p-1 max-sm:mt-0 max-sm:p-3 text-fc-700 uppercase max-sm:text-m-pa-700']"
        self.username_errorMsg = "//*[@id='yDmH0d']/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[2]/div[2]/div/text()"
        self.catalyxTip_txt = "//ul[@id='tabsList']"
        self.companyname_input = "//input[@id='company_name']"
        self.domainname_input = "//input[@id='domain_name']"
        self.noOfLicenses_input = "//input[@id='no_of_licenses']"
        self.industry_drpdwn = "//span[@id='select2-industrySelectBox-container']"
        self.it_drpdwm = "//li[text()='IT-ITES-BPO']"
        self.createcompany_btn = "//input[@value='Create Company']"
        self.successmsgCreatecompany = "//h2"
        self.oK_btn = "//button[text()='OK']"
        self.cohortmngmnt_btn = "(//a[@class='nav-link'])//p[text()='Cohort Management ']"
        self.createcohortmngmnt_btn = "//li[@id='createDepartmentListItem']"
        self.cohortname_input = "//input[@placeholder='Cohort Name']"
        self.selectCompany_drpdwn = "(//span[@class='select2-selection__rendered' and @title='Select'])[8]"
        self.companyMadhuri = "//li[text()='testYUlvGu']"
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
        self.selectDeal_drpdwn = "(//span[@class='select2-selection__arrow'])[13]"
        self.madhuriDeal_btn = "//li[text()='madhuri_test_deal']"
        # --------------CreateUser--------------------------
        self.createUserList_btn = "//li[@id='createUserListItem']"
        self.company_drpdwn = "(//span[@title='All'])[2]"
        self.cominput = "//input[@class='select2-search__field']"
        self.madhuri_cmpny = "//li[text()='testYUlvGu']"
        self.cohort_drpdwn = "(//span[@class='select2-selection__arrow'])[11]"
        self.testCmpny = "//input[@type='search']"
        self.name_input = "(//input[@placeholder='Name'])[2]"
        self.username_input = "(//input[@placeholder='Username'])[2]"
        self.role_input = "//input[@placeholder='Designation']"
        self.manager_input = "(//input[@placeholder='Manager Name'])[2]"
        self.simulation_chkbx = "//input[@class='checkedSimulationModules']"
        self.createUser_btn = "//input[@class='btn btn-info createUser']"
        self.success_createuser_txt = "//span[text()='Success']"
        self.Close_btn = "(//button[text()='Close'])[1]"
        # --------------CreateDeal--------------------------
        self.createDeal_btn = "//p[normalize-space()='Create Deal']"
        self.dealname_txt = "//input[@placeholder='Deal Name']"
        self.selectCompanyIncreateDeal_drpdwn = "//input[@placeholder='Select Company']"
        self.companySelection_drpdwn = "//div[text()='testYUlvGu']"
        self.createdealNoOfLicences_txt = "//input[@placeholder='Number of Licenses']"
        self.createDealSelectOwner_drpdwn = "//input[@placeholder='Select Sales Owner']"
        self.apoorva_btn = "//div[text()='Apoorva Chauhan']"
        self.createDealDeliveryOwner_drpdwn = "//input[@placeholder='Select Delivery Owner']"
        self.createDealLicenceType_drpdwn = "//input[@placeholder='Select License Type']"
        self.pathLevel_btn = "//div[text()='Path Level']"
        self.saveDeal_btn = "//button[text()='SAVE']"
        self.success_createDeal_popup_txt = "//div[text()='Deal created successfully.']"
        self.okCreateDeal_btn = "//button[text()='Ok']"
        # --------------PostRollOut--------------------------
        self.posstRollOut_btn = "//p[text()='Post Rollout ']"
        self.userManagement_btn = "//p[text()='User Management']"
        self.nameTable_txt = "//td[@class='nameTd']"
        self.emailTable_txt = "//td[@class='usernameTd']"
        self.magicLink_btn = "(//button[text()='Magic Link'])[1]"
        self.copyMagicLink_txt = "//button[text()='Copy Magic Link']"
        self.errorMsg = "//h2"
        self.errorMsg2 = "(//h2/following-sibling::div)[1]"
        self.errorMsg3 = "//div[@class='modal-body createUserModal']"
        self.errorMsg4 = "//div[@class='modal-body createUserModal']/div"
        self.googleSignInFrame = "iframe[title=\"Sign in with Google Button\"]"

    def navigateAdminUrl(self, admin_en_url: str):
        self.actions.goto(admin_en_url)

    def clickOnSignInWithGoogle(self, adminUsername: str, adminPassword: str):
        self.actions.newTabAfterClickingAnElementWhichIsInFrame("iframe[title=\"Sign in with Google Button\"]", "Sign in with Google")
        self.actions.new_tab1_get_by_label_fill("Email or phone", adminUsername)
        self.actions.newTab1_get_by_role("button", "Next")
        self.actions.new_tab1_get_by_label_fill("Enter your password", adminPassword)
        self.actions.newTab1_get_by_role("button", "Next")
        self.actions.wait_for_timeout(30000)


    def validateAdminHome(self):
        self.actions.is_visible(self.signin_txt, "Sign In Text")

    def createcomapny(self, noOfLicences: str):
        self.company_name = randomUtils.generate_random_string_with_prefix(length=10, prefix="test")
        self.actions.fill(self.companyname_input, self.company_name)
        print(self.company_name)
        # self.page.fill(self.companyname_input,companyName)
        # self.page.fill(self.domainname_input,domainName)
        self.actions.fill(self.domainname_input, self.company_name)
        # self.page.fill(self.noOfLicenses_input,noOfLicences)
        self.actions.click(self.industry_drpdwn)
        self.actions.click(self.it_drpdwm)
        self.actions.click(self.createcompany_btn)
        return self.company_name

    def validatesuccessmsg(self):
        expected_message = config['Admin']['success_message_template'].format(company_name=self.company_name)
        success_message = self.actions.text_content(self.successmsgCreatecompany)
        print("Actual_msg :", success_message)
        print("expected_message :", expected_message)
        self.actions.click(self.oK_btn)
        assert expected_message == success_message, f"Expected message '{expected_message}' but got '{success_message}'"

    def emptyParametersCreatingCompany(self, compName:str, domainName:str, selIndus:str):
        if compName == '""':  # Handle empty string from Gherkin
            compName = ""
        self.actions.fill(self.companyname_input, compName)
        if domainName == '""':  # Handle empty string from Gherkin
            domainName = ""
        self.actions.fill(self.domainname_input, domainName)
        # self.page.fill(self.noOfLicenses_input,noOfLicences)
        if selIndus == "role" :
            self.actions.click(self.industry_drpdwn)
            self.actions.click(self.it_drpdwm)
        else:
            print("..")

        self.actions.click(self.createcompany_btn)

    def respectiveErrorMessagesForCreativeComp(self):
        actualMessage = self.actions.text_content(self.errorMsg)
        if actualMessage == "Company name cannot be empty":
            expected_message = "Company name cannot be empty"
            assert expected_message == actualMessage, f"Expected message '{expected_message}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message)
        elif actualMessage == "Domain name cannot be empty":
            expected_message1 = "Domain name cannot be empty"
            assert expected_message1 == actualMessage, f"Expected message '{expected_message1}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message1)
        else:
            expected_message2 = "Industry cannot be empty"
            assert expected_message2 == actualMessage, f"Expected message '{expected_message2}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message2)


    def clickOnCohortManagement(self):
        self.actions.click(self.cohortmngmnt_btn)
        self.actions.click(self.createcohortmngmnt_btn)

    def clickOncreateCatalyx(self, hrname: str, hremail: str):
        self.actions.click(self.createcohortmngmnt_btn)
        self.cohort_name = randomUtils.generate_random_string_with_prefix(length=10, prefix="test")
        self.actions.fill(self.cohortname_input, self.cohort_name)
        print(self.cohort_name)
        write_to_file(self.cohort_name)
        self.actions.click(self.selectCompany_drpdwn)
        self.actions.click(self.companyMadhuri)
        self.actions.click(self.selectDeal_drpdwn)
        self.actions.click(self.madhuriDeal_btn)
        self.actions.fill(self.hrname_input, hrname)
        self.actions.fill(self.hremail_input, hremail)
        self.actions.click(self.inputdate)
        self.actions.click(self.date)
        self.actions.click(self.deadlinedate)
        self.actions.click(self.enddateyr)
        # self.page.click(self.selectyr)
        # self.page.get_by_role("combobox").nth(4).select_option("2032")
        # self.page.click(self.chooseyr_btn)
        self.actions.get_by_role_nth_select_option("#ui-datepicker-div", "combobox", 1, "2031")
        self.actions.get_by_role("link", "14")
        self.actions.click(self.hremail_input)
        self.actions.select_option_value(
            "//select[@class='cs_adminidSelectBox selectBox form-control select2 select2-hidden-accessible']",
            'Pallabi')
        self.actions.select_option_value(
            "//select[@class='packageSelectBox form-control selectBox select2 select2-hidden-accessible']",
           '2008 path level')
        self.actions.click(self.createcohort_btn)
        return self.cohort_name

    def validatecreatecohortsuccessmsg(self):
        cohort_expected_message = config['Admin']['create_cohort_success_message_template'].format(
            cohort_name=self.cohort_name)
        cohort_success_message = self.actions.text_content(self.successmsgCreatecompany)
        print("Actual_cohort_msg :", cohort_success_message)
        print("expected_cohort_message :", cohort_expected_message)
        self.actions.click(self.oK_btn)
        assert cohort_expected_message == cohort_success_message, f"Expected message '{cohort_expected_message}' but got '{cohort_success_message}'"

    def clickOncreateuser(self):
        self.actions.click(self.cohortmngmnt_btn)
        self.actions.wait_for_timeout(3000)

        self.actions.click(self.createUserList_btn)
        self.actions.wait_for_timeout(3000)

    def selectCompany(self):
        try:
            self.actions.click(self.company_drpdwn)
            self.actions.wait_for_timeout(3000)
            self.actions.click(self.company_drpdwn)
            self.actions.fill(self.cominput, "testYUlvGu")
            self.actions.click(self.madhuri_cmpny)
        except Exception as e:
            self.actions.click(self.company_drpdwn)
            self.actions.wait_for_timeout(3000)
            self.actions.click(self.company_drpdwn)
            self.actions.fill(self.cominput, "testYUlvGu")
            self.actions.click(self.madhuri_cmpny)



    def enterUserDetails(self, hremail: str, hrname: str, role: str):
        # self.page.click(self.cohort_drpdwn)
        # self.cohort_name = read_from_file()
        # self.page.click(self.cohort_name)
        # self.page.keyboard.press('Enter')
        self.co_name = randomUtils.generate_random_string_with_prefix(length=10, prefix="test")
        self.actions.fill(self.name_input, self.co_name)
        self.actions.fill(self.username_input, "hremail@mail.com")
        self.actions.fill(self.role_input, role)
        self.actions.fill(self.manager_input, "hrname")
        # self.page.check(self.simulation_chkbx)
        self.actions.click(self.createUser_btn)

    def validatesuccessCreateUser(self):
        self.actions.is_visible(self.successmsgCreatecompany, "successmsgCreatecompany")
        if self.actions.is_visible(self.Close_btn, "Close Button"):
            print("visible")
            self.actions.get_by_role("button", "Close")




    def clickOnCreateDeal(self):
        self.actions.click(self.createDeal_btn)

    def enterDealDetails(self):
        self.deal_name = randomUtils.generate_random_string_with_prefix(length=10, prefix="test")
        self.actions.fill(self.dealname_txt, self.deal_name)
        self.actions.click(self.selectCompanyIncreateDeal_drpdwn)
        self.actions.click(self.companySelection_drpdwn)
        self.actions.fill(self.createdealNoOfLicences_txt, "2")
        self.actions.click(self.createDealSelectOwner_drpdwn)
        self.actions.click(self.apoorva_btn)
        self.actions.click(self.createDealDeliveryOwner_drpdwn)
        self.actions.keyboard_press("ArrowDown")
        self.actions.keyboard_press("Enter")
        # self.page.click(self.createDealLicenceType_drpdwn)
        # self.page.click(self.pathLevel_btn)

        self.actions.click(self.saveDeal_btn)


    def emptyingDetailsOfCreatingDeal(self, dealName:str, selComp:str, selSalesOwner:str, selDeliOwner:str):
        if dealName == '""':  # Handle empty string from Gherkin
            dealName = ""
        self.actions.fill(self.dealname_txt, dealName)
        if selComp == "selectComp" :
            self.actions.click(self.selectCompanyIncreateDeal_drpdwn)
            self.actions.click(self.companySelection_drpdwn)
        else:
            print("..")
        self.actions.fill(self.createdealNoOfLicences_txt, "2")
        if selSalesOwner == "selectSales":
            self.actions.click(self.createDealSelectOwner_drpdwn)
            self.actions.click(self.apoorva_btn)
        else:
            print('..')
        if selDeliOwner == "selectDelOwn":
            self.actions.click(self.createDealDeliveryOwner_drpdwn)
            self.actions.keyboard_press("ArrowDown")
            self.actions.keyboard_press("Enter")
        else:
            print("..")
        self.actions.click(self.saveDeal_btn)


    def validateSuccessCreateDeal(self):
        self.actions.is_visible(self.success_createDeal_popup_txt, "success_createDeal_popup_txt")
        self.actions.click(self.okCreateDeal_btn)

    def respectiveErrorMessagesForCreatingDeal(self):
        actualMessage = self.actions.text_content(self.errorMsg2)
        if actualMessage == "Please enter a valid deal name.":
            expected_message = "Please enter a valid deal name."
            assert expected_message == actualMessage, f"Expected message '{expected_message}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message)
        elif actualMessage == "Please select a company.":
            expected_message1 = "Please select a company."
            assert expected_message1 == actualMessage, f"Expected message '{expected_message1}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message1)
        elif actualMessage == "Please select a delivery owner.":
            expected_message1 = "Please select a delivery owner."
            assert expected_message1 == actualMessage, f"Expected message '{expected_message1}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message1)
        else:
            expected_message2 = "Please select a sales owner."
            assert expected_message2 == actualMessage, f"Expected message '{expected_message2}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message2)


    def clickOnPOstRollOut(self):
        self.actions.click(self.posstRollOut_btn)

    def clickOnUserManagement(self):
        self.actions.click(self.userManagement_btn)

    def enterValidDetailsIncompanyAndCohortInusermanagement(self):
        self.actions.click(self.company_drpdwn)
        self.actions.click(self.madhuri_cmpny)

    def clickOnmagicLink(self):
        # username = self.page.get_by_text(self.nameTable_txt)
        # LoginMail = self.page.get_by_text(self.emailTable_txt)
        self.actions.click(self.magicLink_btn)
        self.actions.click_link_open_new_tab_coping(self.copyMagicLink_txt)

    def validateloginpage(self):
        print("")
        # self.page2.is_visible()

    def invalidusername(self, username: str):
        self.actions.newTabAfterClickingAnElementWhichIsInFrame(self.googleSignInFrame,
                                                                "Sign in with Google")
        self.actions.new_tab1_get_by_label_fill("Email or phone", username)

        # page1.get_by_role("button", name="Next").click()
        # self.page.click(self.en_signinWithPassword_button)

    def validateinvalidusernamemsg(self):
        self.actions.is_visible(self.signin_txt, "SignIn Text")

    def en_enter_username(self, adminUsername: str):
        self.actions.newTabAfterClickingAnElementWhichIsInFrame(self.googleSignInFrame,
                                                                "Sign in with Google")
        self.actions.new_tab1_get_by_label_fill("Email or phone", adminUsername)
        self.actions.newTab1_get_by_role("button", "Next")
        self.actions.newTab1Click(self.enterPassword_input)

    def invalidpassword(self, adminUsername:str , password: str):
        self.actions.newTabAfterClickingAnElementWhichIsInFrame(self.googleSignInFrame,
                                                                "Sign in with Google")
        self.actions.new_tab1_get_by_label_fill("Email or phone", adminUsername)
        self.actions.newTab1_get_by_role("button", "Next")
        self.actions.new_tab1_get_by_label_fill("Enter your password", password)
        # page1.get_by_role("button", name="Next").click()


    def entersEmptyParametersCohort(self, cohortName:str, company:str, deal:str, hrname:str, hremail:str, startDate:str, deadline:str, deliveryOwner:str, learningPath:str):
        self.actions.click(self.createcohortmngmnt_btn)
        if cohortName == '""':
            if cohortName == '""':  # Handle empty string from Gherkin
                cohortName = ""

        elif cohortName == "TestMadhu":
            self.actions.fill(self.cohortname_input,cohortName)

        else :
            self.actions.fill(self.cohortname_input, randomUtils.generate_random_string_with_prefix(length=10, prefix="test"))

        if company == "selectComp":
            self.actions.click(self.selectCompany_drpdwn)
            self.actions.click(self.companyMadhuri)
        else:
            print("..")
        if deal == "selectDeal" and company == "selectComp":
            self.actions.click(self.selectDeal_drpdwn)
            self.actions.click(self.madhuriDeal_btn)
        else:
            print("..")
        if hrname == '""':  # Handle empty string from Gherkin
            hrname = ""
        self.actions.fill(self.hrname_input, hrname)
        if hremail == '""':  # Handle empty string from Gherkin
            hremail = ""
        self.actions.fill(self.hremail_input, hremail)
        if startDate == "selStartDate":
            self.actions.click(self.inputdate)
            self.actions.click(self.date)
        else:
            print("..")
        if deadline == "selDeadline":
            self.actions.click(self.deadlinedate)
            self.actions.click(self.enddateyr)
            self.actions.get_by_role_nth_select_option("#ui-datepicker-div", "combobox", 1, "2031")
            self.actions.get_by_role("link", "14")
        else:
            print("..")
        # self.page.click(self.selectyr)
        # self.page.get_by_role("combobox").nth(4).select_option("2032")
        # self.page.click(self.chooseyr_btn)
        if deliveryOwner == "selDelOwner":
            self.actions.select_option_value(
                "//select[@class='cs_adminidSelectBox selectBox form-control select2 select2-hidden-accessible']",
                'Pallabi')
        else:
            print("..")
        if learningPath == "selLearnPath" and company == "selectComp":
            self.actions.select_option_value(
                "//select[@class='packageSelectBox form-control selectBox select2 select2-hidden-accessible']",
                '2008 path level')
        else:
            print("..")


        self.actions.click(self.createcohort_btn)



    def respectiveErrorMessagesForCreatingCohort(self):
        actualMessage = self.actions.locator(self.errorMsg).text_content()
        if actualMessage == "Cohort name cannot be empty":
            expected_message = "Cohort name cannot be empty"
            assert expected_message == actualMessage, f"Expected message '{expected_message}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message)
        elif actualMessage == "Company need to be selected":
            expected_message1 = "Company need to be selected"
            assert expected_message1 == actualMessage, f"Expected message '{expected_message1}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message1)
        if actualMessage == "HR name cannot be empty":
            expected_message2 = "HR name cannot be empty"
            assert expected_message2 == actualMessage, f"Expected message '{expected_message2}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message2)
        elif actualMessage == "Please select Delivery Owner ":
            expected_message3 = "Please select Delivery Owner "
            assert expected_message3 == actualMessage, f"Expected message '{expected_message3}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message3)
        if actualMessage == "Start Date cannot be empty":
            expected_message4 = "Start Date cannot be empty"
            assert expected_message4 == actualMessage, f"Expected message '{expected_message4}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message4)
        elif actualMessage == "Deadline cannot be empty":
            expected_message5 = "Deadline cannot be empty"
            assert expected_message5 == actualMessage, f"Expected message '{expected_message5}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message5)
        if actualMessage == "Please select Deal ":
            expected_message6 = "Please select Deal "
            assert expected_message6 == actualMessage, f"Expected message '{expected_message6}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message6)
        elif actualMessage == "HR email cannot be empty":
            expected_message7 = "HR email cannot be empty"
            assert expected_message7 == actualMessage, f"Expected message '{expected_message7}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message7)
        elif actualMessage == "Please select learning path":
            expected_message8 = "Please select learning path"
            assert expected_message8 == actualMessage, f"Expected message '{expected_message8}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message8)
        elif actualMessage == "Cohort name exists. Try a different cohort name":
            expected_message9 = "Cohort name exists. Try a different cohort name"
            assert expected_message9 == actualMessage, f"Expected message '{expected_message9}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message9)
        elif actualMessage == "HR email is not valid":
            expected_message10 = "HR email is not valid"
            assert expected_message10 == actualMessage, f"Expected message '{expected_message10}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message10)


    def entersInvalidEmailCreatCohort(self, InvalidEmail:str) :
        self.actions.click(self.createcohortmngmnt_btn)
        self.cohort_name = randomUtils.generate_random_string_with_prefix(length=10, prefix="test")
        self.actions.fill(self.cohortname_input, self.cohort_name)
        print(self.cohort_name)
        write_to_file(self.cohort_name)
        self.actions.click(self.selectCompany_drpdwn)
        self.actions.click(self.companyMadhuri)
        self.actions.click(self.selectDeal_drpdwn)
        self.actions.click(self.madhuriDeal_btn)
        self.actions.fill(self.hrname_input, "safasd")
        self.actions.fill(self.hremail_input, InvalidEmail)
        self.actions.click(self.inputdate)
        self.actions.click(self.date)
        self.actions.click(self.deadlinedate)
        self.actions.click(self.enddateyr)
        # self.page.click(self.selectyr)
        # self.page.get_by_role("combobox").nth(4).select_option("2032")
        # self.page.click(self.chooseyr_btn)
        self.actions.get_by_role_nth_select_option("#ui-datepicker-div", "combobox", 1, "2031")
        self.actions.get_by_role("link", "14")
        self.actions.select_option_value(
            "//select[@class='cs_adminidSelectBox selectBox form-control select2 select2-hidden-accessible']",
            'Pallabi')
        self.actions.select_option_value(
            "//select[@class='packageSelectBox form-control selectBox select2 select2-hidden-accessible']",
            '2008 path level')
        self.actions.click(self.createcohort_btn)


    def creatingUserEmptyParameters(self, name:str, username:str):
        self.co_name = randomUtils.generate_random_string_with_prefix(length=10, prefix="test")
        if name == '""':  # Handle empty string from Gherkin
            name = ""
        self.actions.fill(self.name_input, name)
        if username == '""':  # Handle empty string from Gherkin
            username = ""
        self.actions.fill(self.username_input, username)
        self.actions.fill(self.role_input, "team lead")
        self.actions.fill(self.manager_input, "hrname")
        self.actions.click(self.createUser_btn)

    def respectiveErrorMessagesForCreatingUser(self):
        try:
            actualMessage = self.actions.text_content(self.errorMsg3)
            if actualMessage == "Name cannot be empty":
                expected_message = "Name cannot be empty"
                assert expected_message == actualMessage, f"Expected message '{expected_message}' but got '{actualMessage}'"
                print("actualMessage", actualMessage)
                print("expected message", expected_message)
            elif actualMessage == "Username cannot be empty":
                expected_message1 = "Username cannot be empty"
                assert expected_message1 == actualMessage, f"Expected message '{expected_message1}' but got '{actualMessage}'"
                print("actualMessage", actualMessage)
                print("expected message", expected_message1)
            elif actualMessage == "Select the correct Company and Cohort":
                expected_message2 = "Select the correct Company and Cohort"
                assert expected_message2 == actualMessage, f"Expected message '{expected_message2}' but got '{actualMessage}'"
                print("actualMessage", actualMessage)
                print("expected message", expected_message2)
        except Exception as e:
            print("Lower if else executed")

        try:
            actualMessage1 = self.actions.text_content(self.errorMsg4)
            if actualMessage1 == "Please make sure the username is in the correct format (e.g. username@example.com) and try again":
                expected_message3 = "Please make sure the username is in the correct format (e.g. username@example.com) and try again"
                assert expected_message3 == actualMessage1, f"Expected message '{expected_message3}' but got '{actualMessage1}'"
                print("actualMessage", actualMessage1)
                print("expected message", expected_message3)
        except Exception as e:
            print('Upper if else executed')
        if self.actions.is_visible(self.Close_btn, "close button"):
            print("visible")
            self.actions.get_by_role("button", "Close")






