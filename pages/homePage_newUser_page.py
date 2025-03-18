from pages.base_page import BasePage
from playwright.sync_api import Page

from pages.WebActions import WebActions


class HomePage:
    def __init__(self, page, browser_context):

        self.actions = WebActions(page, browser_context)

        self.en_homeFilter_btn = "//div[@id='highlightFilter_btn']"
        self.en_notStarted_txt = "//p[text()='Not Started']"
        self.en_inprogress_txt = "//p[text()='In Progress']"
        self.en_completed_txt = "//p[text()='Completed']"
        self.en_homeSort_btn = "//img[@id='highlightSortingIcon']"
        self.en_recentlyAccssed_txt = "//p[text()='Recently Accessed']"
        self.en_AZ_txt = "//p[text()='Title: A-Z']"
        self.en_ZA_txt = "//p[text()='Title: Z-A']"
        self.start_btn = "(//span[text()='Start'])[2]"
        self.resume_btn = "(//span[text()='Resume'])[2]"
        self.enterpath_btn = "//span[text()='Enter Path']"

    def click_homeFilter(self):
        self.actions.click(self.en_homeFilter_btn)

    def click_recentlyAccessed(self):
        self.actions.click(self.en_recentlyAccssed_txt)

    def click_AZtext(self):
        self.actions.click(self.en_AZ_txt)

    def click_ZAtext(self):
        self.actions.click(self.en_ZA_txt)

    def validate_homeFilterOptions(self):
        self.actions.is_visible(self.en_notStarted_txt, "Not Started")
        self.actions.is_visible(self.en_inprogress_txt, "In Progess")
        self.actions.is_visible(self.en_completed_txt, "Completed")

    def click_homeSort(self):
        self.actions.wait_for_timeout(3000)
        self.actions.click(self.en_homeSort_btn)

    def validate_homeFilterOptions(self):
        self.actions.is_visible(self.en_recentlyAccssed_txt, "Recently Accessed")
        self.actions.is_visible(self.en_AZ_txt, "A-Z")
        self.actions.is_visible(self.en_ZA_txt, "Z-A")

    def click_Notstarted(self):
        self.actions.wait_for_timeout(2000)
        self.actions.click(self.en_notStarted_txt)

    def validate_start(self):
        self.actions.is_visible(self.start_btn, "Start")
        self.actions.click(self.en_notStarted_txt)

    def click_Inprogress(self):
        # self.page.click(self.en_homeFilter_btn)
        self.actions.click(self.en_inprogress_txt)

    def validate_resume(self):
        self.actions.is_visible(self.resume_btn, "Resume")
        # self.page.click(self.en_inprogress_txt)

    def click_Completed(self):
        # self.page.click(self.en_homeFilter_btn)
        self.actions.click(self.en_completed_txt)

    def validate_enterpath(self):
        self.actions.is_visible(self.enterpath_btn, "Enter Path")
        self.actions.click(self.en_completed_txt)

    def en_homepagevalidation(self):
        message_elements = self.actions.text_content(self.en_homepagetext)
        return message_elements
