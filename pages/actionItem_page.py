from pages.base_page import BasePage
from playwright.sync_api import Page

from pages.WebActions import WebActions


class ActionItemPage:
    def __init__(self, page, browser_context):
        self.actions = WebActions(page, browser_context)
        self.progress_btn = "//span[text()='Progress']"
        self.progress_txt="//h2[@id='swal2-title']"
        self.close_btn="//button[@aria-label='Close this dialog']"
        self.social_btn="//span[text()='Social']"
        self.activemembers_txt="(//div[text()='Active Members'])[1]"
        self.resources_btn="//span[text()='Resources']"
        self.assessment_reports_txt="(//div[text()='Assessment Reports'])[1]"
        self.achievements_btn="//span[text()='Achievements']"
        self.certificate_txt="//span[text()='Certificate']"
        self.notification_btn="//div[@class='relative w-7 h-7 bg-pallet-color-29 rounded-full flex items-center justify-center cursor-pointer']"
        self.pendingItems_txt="//div[text()='Your Pending Items']"
        self.profile_drpdwn="//button[@id='dropdown-toggle']"
        self.logout_btn="(//button[text()='Logout'])[2]"
        self.welcome_txt="//div[text()='Welcome to Catalyx']"


    def clickOnProgressBtn(self):
        self.actions.click(self.progress_btn)

    def validateProgresstxt(self):
        # self.page.is_visible(self.progress_txt)
        try:
            popup = self.actions.wait_for_selector(self.close_btn, 5000)
            if popup:
                popup.click()
                print("Popup closed")
        except TimeoutError:
            print("No popup appeared")
        except Exception as e:
            print(f"An error occurred while handling the popup: {e}")

    def clickOnSocialBtn(self):
        self.actions.click(self.social_btn)

    def validaactiveMemberstxt(self):
        self.actions.is_visible(self.activemembers_txt, "Active Members")

    def clickOnResourcesBtn(self):
        self.actions.click(self.resources_btn)

    def validateAssessmentReportstxt(self):
        self.actions.is_visible(self.assessment_reports_txt, "Assessment Reports")

    def clickOnAchievementsBtn(self):
        self.actions.click(self.achievements_btn)

    def validateCertificatetxt(self):
        self.actions.is_visible(self.certificate_txt, "Certificate")

    def clickOnNotificationsBtn(self):
        self.actions.click(self.notification_btn)

    def validatePenidngItemstxt(self):
        self.actions.is_visible(self.pendingItems_txt, "Pending Items")

    def clickOnProfileDrpDwn(self):
        self.actions.click(self.profile_drpdwn)

    def validateLogoutbtn(self):
        self.actions.is_visible(self.logout_btn, "Logout Button")

    def clickOnLogoutBtn(self):
        self.actions.click(self.logout_btn)

    def clickWelcomeTxt(self):
        self.actions.is_visible(self.welcome_txt, "Welcome")

