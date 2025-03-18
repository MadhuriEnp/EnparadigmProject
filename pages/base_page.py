from playwright.sync_api import Page
from loguru import logger

from features.environment import browser_context


class BasePage:

    def __init__(self, page, browser_context):
        self.page = page
        self.page2 = None
        self.page3 = None
        self.browser_context = browser_context

    def go_to(self, url: str, browser_context):
        self.page.goto(url,timeout=60000)
        logger.info(f'Navigating to {url}')

    def go_to_en(self,en_url:str):
        self.page.goto(en_url)

    def go_to_admin(self,admin_en_url:str):
        self.page.goto(admin_en_url)

    def go_to_simstudioadmin(self,simStudio_admin:str):
        self.page.goto(simStudio_admin)

    def get_title(self) -> str:
        return self.page.title()

    def fill(self, locator: str, text: str):
        self.page.locator(locator).fill(text)





