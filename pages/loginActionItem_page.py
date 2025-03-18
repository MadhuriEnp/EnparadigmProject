from pages.base_page import BasePage
from playwright.sync_api import Page

import configparser

from pages.WebActions import WebActions

config = configparser.ConfigParser()
config.read('config.ini')


class LoginPage:
    def __init__(self, page, browser_context):
        self.actions = WebActions(page, browser_context)

        self.username_input = "#username"
        self.password_input = "#password"
        self.login_button = "#loginBtn"
        self.accpet_button = "//button[@id='acceptBtn']"
        self.en_username_input = "//input[@placeholder='Please enter your email ID']"
        self.en_signinWithPassword_button = "//button[@id='signin_with_password_button']"
        self.en_password_input = "//input[@placeholder='Enter Password']"
        self.en_login_button = "//button[@class='submit_password btn w-full mt-2 bg-pallet-color-1 hover:bg-pallet-color-1-hover text-white rounded-lg p-1 max-sm:mt-0 max-sm:p-3 text-fc-700 uppercase max-sm:text-m-pa-700']"
        self.en_talenthub_button = "//span[text()='Talent Hub']"
        self.en_homepage = "//span[text()='Talent Hub']"
        self.en_username = "//div[@class='w-fit ml-4 text-pa-400 max-sm:hidden cursor-pointer']"
        self.en_homepagetext = "//div[@class='text-m-ht-700 sm:text-ht-700']"
        self.en_actionItem_button = "//span[text()='Action Item']"
        self.en_actionPage_txt = "(//div[text()='Simulations Played'])[1]"
        self.filter_btn = "(//img[@class='w-8 cursor-pointer'])[1]"
        self.all_btn = "(//label[@class='flex items-center space-x-2 p-1.5 hover:bg-pallet-color-4'])[1]"
        self.pending_btn = "(//label[@class='flex items-center space-x-2 p-1.5 hover:bg-pallet-color-4'])[2]"
        self.completed_btn = "(//label[@class='flex items-center space-x-2 p-1.5 hover:bg-pallet-color-4'])[3]"
        self.sort_btn = "(//img[@class='w-8 cursor-pointer'])[2]"
        self.username_errorMsg = "//span[text()='Please enter a valid email ID']"
        self.password_errorMsg = "//span[@id='Please enter a valid password']"
        self.latestFirst_btn = "(//label[@class='flex items-center space-x-2 p-1.5 hover:bg-pallet-color-4 cursor-pointer'])[1]"
        self.oldestFirst_btn = "(//label[@class='flex items-center space-x-2 p-1.5 hover:bg-pallet-color-4 cursor-pointer'])[2]"
        self.clstxt = "//div[@class='col-span-1 animate-slide-in-bottom w-17']"

    def go_to_enurl(self, en_url):
        self.actions.goto(en_url)

    def validateclass(self) -> int:
        self.actions.wait_for_timeout(3000)
        self.actions.elements_count(self.clstxt)


    def enter_username(self, username: str):
        self.actions.fill(self.username_input, username)

    def enter_password(self, password: str):
        self.actions.fill(self.password_input, password)

    def click_login(self):
        self.actions.click(self.login_button)

    def en_enter_username(self, en_username: str):
        self.actions.click(self.accpet_button)
        self.actions.fill(self.en_username_input, en_username)
        self.actions.click(self.en_signinWithPassword_button)

    def en_enter_password(self, en_password: str):
        self.actions.click(self.en_password_input)
        self.actions.fill(self.en_password_input, en_password)
        self.actions.click(self.en_login_button)

    def getDynamicUsername(self):
        user_elements = self.actions.text_content(self.en_username)
        return user_elements

    def homepagevalidation(self):
        message_elements = self.actions.text_content(self.en_homepagetext)
        if "the expert in anything was once a beginner" or "your dedication and hard work have paid off." in message_elements:
            message_elements.strip()
        return message_elements

    def clickTalentHub(self):
        self.actions.click(self.en_talenthub_button)
        self.actions.click(self.en_actionItem_button)

    def actionItemHomepage(self):
        self.actions.is_visible(self.en_actionPage_txt, "Action Page")

    def clickFilterBtn(self):
        self.actions.click(self.filter_btn)

    def validateAllOptions(self):
        self.actions.is_visible(self.all_btn, "All")
        self.actions.is_visible(self.pending_btn, "Pending")
        self.actions.is_visible(self.completed_btn, "Completed")

    def clickSortBtn(self):
        self.actions.click(self.sort_btn)

    def validatesortOptions(self):
        self.actions.is_visible(self.latestFirst_btn, "Latest")
        self.actions.is_visible(self.oldestFirst_btn, "Oldest")

    def invalidusername(self, username: str):
        self.actions.click(self.accpet_button)
        self.actions.fill(self.en_username_input, username)
        self.actions.click(self.en_signinWithPassword_button)

    def validateinvalidusernamemsg(self):
        return self.actions.is_visible(self.username_errorMsg, "Username Error Message")

    def invalidpassword(self, password: str):
        self.actions.fill(self.en_password_input, password)
        self.actions.click(self.en_login_button)

    def validateinvalidpasswordmsg(self):
        self.actions.is_visible(self.password_errorMsg, "Password Error Message")

    def clicksOnaccept(self):
        self.actions.get_by_role("button", "Accept")
