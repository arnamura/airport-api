from playwright.sync_api import Page
from locators.global_locators import locator

class globalPage:
    def __init__(self, page: Page):
        self.page = page

    def click_button_sidebar(self):
        self.page.locator(locator.button_sidebar).click()

    def click_button_sidebar_logout(self):
        self.page.get_by_role(locator.button_sidebar_logout[0], name=locator.button_sidebar_logout[1]).click()
    