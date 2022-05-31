"""
Module contains elements/actions pertaining to DuckDuckGo search/home page.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoSearch:
    # Locators
    SEARCH_INPUT = (By.ID, "search_form_input_homepage")
    SEARCH_BUTTON = (By.ID, "search_button_homepage")

    def __init__(self, browser):
        self.browser = browser

    # Page element interactions

    def load(self):
        """
        Implementation not required as application url will be loaded in conftest.py fixture
        :return:
        """
        # TODO
        pass

    def search(self, phrase):
        """
        Enters "phrase" in input text box and clicks on ENTER button
        :param phrase:
        :return:
        """
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)

    def click_search_button(self):
        """
        Clicks on search button
        :return:
        """
        search_button = self.browser.find_element(*self.SEARCH_BUTTON)
        search_button.click()
