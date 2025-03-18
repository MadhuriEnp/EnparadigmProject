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


class AdminManagementPage:
    def __init__(self, page, browser_context):
        self.actions = WebActions(page, browser_context)

        self.signInWithGoogle_btn = "//span[@class='nsm7Bb-HzV7m-LgbsSe-BPrWId']"
        self.enterUsername_input = "//input[@id='identifierId']"
        self.next_btn = "(//div[@class='VfPpkd-RLmnJb'])[2]"
        self.enterPassword_input = "//input[@type='password']"
        self.en_password_input = "//input[@placeholder='Enter Password']"
        self.en_login_button = "//button[@class='submit_password btn w-full mt-2 bg-pallet-color-1 hover:bg-pallet-color-1-hover text-white rounded-lg p-1 max-sm:mt-0 max-sm:p-3 text-fc-700 uppercase max-sm:text-m-pa-700']"
        self.catalyxTip_txt = "//ul[@id='tabsList']"
        self.adminManagement_drpdwn = "//p[normalize-space()='Admin Management']"
        self.createAdmin = "(//*[@id='createAdminListItem']/a/p)[1]"
        self.name_input = "//input[contains(@class,'form-control nameOfUser textBox')]"
        self.username_input = "//input[@class='form-control username textBox']"
        self.password_input = "//input[@placeholder='Password']"
        self.role_input = "//span[@id='select2-dw4e-container']"
        self.createAdmin_btn = "//input[@value='Create Admin']"
        self.createAdmin_val = "//h3[@class='card-title']"
        self.successMsgCreateAccount_val = "//h2[normalize-space()='Succesfully created account']"
        self.createClientAdmin_btn = "//*[@id='createClientAdminListItem']/a/p"
        self.createClientAdmin_val = "//span[@class='text-2xl pl-6 text-[#37446B] font-semibold']"
        self.create_btn = "//button[@type='button']"
        self.clientAdminName_input = "//input[@placeholder='Name']"
        self.clientAdminUsername_input = "//input[@placeholder='User Name']"
        self.clientAdminPassword_input = "//input[@placeholder='Password']"
        self.successMsgCreateClientAccount_val = "//*[@id='swal2-html-container']"
        self.oK_btn = "//button[text()='Ok']"
        self.roleDrpdwn = "//select[@class='form-control roleOfAdmin select2 select2-hidden-accessible']"
        self.comDrpDwn = "//div[@class='row companyFieldContainer ']//span[@class='selection']"
        self.googleSignInFrame = "iframe[title=\"Sign in with Google Button\"]"
        self.erroMsg = "//h2"
        self.comName = "//li[text()='Internal Demo']"

    def navigateAdminUrl(self, admin_en_url: str):
        self.actions.goto(admin_en_url)

    def clickOnSignInWithGoogle(self, adminUsername: str, adminPassword: str):
        self.actions.newTabAfterClickingAnElementWhichIsInFrame(self.googleSignInFrame,
                                                                "Sign in with Google")
        self.actions.new_tab1_get_by_label_fill("Email or phone", adminUsername)
        self.actions.newTab1_get_by_role("button", "Next")
        self.actions.new_tab1_get_by_label_fill("Enter your password", adminPassword)
        self.actions.newTab1_get_by_role("button", "Next")
        self.actions.wait_for_timeout(30000)

    def validateAdminHome(self):
        self.actions.is_visible(self.catalyxTip_txt, "Sign In Text")

    def clickOnAdminManagement(self):
        self.actions.click(self.adminManagement_drpdwn)

    def clickOnCreateAdmin(self):
        self.actions.click(self.createAdmin)

    def enterAllAdminDetails(self):
        self.name = randomUtils.generate_random_string_with_prefix(length=10, prefix="test")
        self.actions.fill(self.name_input, self.name)
        self.username = randomUtils.generate_random_email()
        self.actions.fill(self.username_input, self.username)
        self.password = randomUtils.generate_random_string_with_prefix(length=6, prefix="test")
        self.actions.fill(self.password_input, self.password)
        print(self.actions.title())
        self.actions.query_selector_click(self.roleDrpdwn, "admin")
        self.actions.wait_for_timeout(3000)
        self.actions.click(self.createAdmin_btn)

    def validateCreateAdminPage(self):
        self.actions.is_visible(self.createAdmin_val, "Create Admin")

    def validateSuccessMsgCreateAccount(self):
        actualMessage = self.actions.text_content(self.erroMsg)
        expected_message = "Succesfully created account"
        assert expected_message == actualMessage, f"Expected message '{expected_message}' but got '{actualMessage}'"
        print("actualMessage", actualMessage)
        print("expected message", expected_message)

        # expected_message = config['Admin']['success_message_createAccount'].format(createadminUser=self.successMsgCreateAccount_val)
        # success_message = self.page.text_content(self.successMsgCreateAccount_val)
        # print("Actual_msg :", success_message)
        # print("expected_message :", expected_message)
        # self.page.click(self.oK_btn)
        # assert expected_message == success_message, f"Expected message '{expected_message}' but got '{success_message}'"

    def emptyValuesCreatingAdmin(self, name:str, username:str, password:str):
        if name == '""':  # Handle empty string from Gherkin
            name = ""
        self.actions.fill(self.name_input, name)
        if username == '""':  # Handle empty string from Gherkin
            username = ""
        self.actions.fill(self.username_input,username)
        if password == '""':  # Handle empty string from Gherkin
            password = ""
        self.actions.fill(self.password_input, password)
        print(self.actions.title())
        self.actions.query_selector_click(self.roleDrpdwn, "admin")
        self.actions.wait_for_timeout(3000)
        self.actions.click(self.createAdmin_btn)


    def withoutSelectingRole(self):
        self.actions.fill(self.name_input, "Madhu")
        self.actions.fill(self.username_input, "madhu@gmail.com")
        self.actions.fill(self.password_input, "madhu")
        print(self.actions.title())
        self.actions.wait_for_timeout(3000)
        self.actions.click(self.createAdmin_btn)

    def entersInvalidUsername(self, invalidUsername:str):
        self.actions.fill(self.name_input, "Madhu")
        self.actions.fill(self.username_input, invalidUsername)
        self.actions.fill(self.password_input, "madhu")
        print(self.actions.title())
        self.actions.query_selector_click(self.roleDrpdwn, "admin")
        self.actions.wait_for_timeout(3000)
        self.actions.click(self.createAdmin_btn)


    def respectiveErrorMessages(self):
        actualMessage = self.actions.text_content(self.erroMsg)
        if actualMessage == "Please enter name":
            expected_message = "Please enter name"
            assert expected_message == actualMessage, f"Expected message '{expected_message}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message)
        elif actualMessage == "The username(s) you entered are invalid. Please make sure the username is in the correct format (e.g. username@example.com) and try again.":
            expected_message1 = "The username(s) you entered are invalid. Please make sure the username is in the correct format (e.g. username@example.com) and try again."
            assert expected_message1 == actualMessage, f"Expected message '{expected_message1}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message1)
        elif actualMessage == "Please choose Role":
             expected_message3 = "Please choose Role"
             assert expected_message3 == actualMessage, f"Expected message '{expected_message3}' but got '{actualMessage}'"
             print("actualMessage", actualMessage)
             print("expected message", expected_message3)
        else :
            expected_message2 = "Please enter Password"
            assert expected_message2 == actualMessage, f"Expected message '{expected_message2}' but got '{actualMessage}'"
            print("actualMessage", actualMessage)
            print("expected message", expected_message2)


    def clickOnCreateClientAdmin(self):
        self.actions.click(self.createClientAdmin_btn)


    def enterAllClientAdminDetails(self):
        self.actions.wait_for_timeout(2000)
        self.name = randomUtils.generate_random_string_with_prefix(length=10, prefix="test")
        self.actions.fill(self.name_input, self.name)
        self.username = randomUtils.generate_random_email()
        self.actions.fill(self.username_input, self.username)
        self.password = randomUtils.generate_random_string_with_prefix(length=6, prefix="test")
        self.actions.fill(self.password_input, self.password)
        print(self.actions.title())
        self.actions.query_selector_click(self.roleDrpdwn, "Client")
        self.actions.click(self.comDrpDwn)
        self.actions.click(self.comName)
        self.actions.wait_for_timeout(3000)
        self.actions.click(self.createAdmin_btn)

    def validateCreateClientAdminPage(self):
        self.actions.is_visible(self.create_btn, "Create Button")
        self.actions.click(self.create_btn)



