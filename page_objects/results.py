"""
Module contains results of DuckDuckGo search
"""
from selenium.webdriver.common.by import By


class DuckDuckGoResults:
    # Locators
    SEARCH_INPUT = (By.ID, "search_form_input")
    SEARCH_RESULTS_LINK = (By.XPATH, "//*[@data-testid='result-title-a']")

    def __init__(self, browser):
        self.browser = browser

    # Page element interactions

    def result_link_titles(self):
        """
        Return all search result links/titles
        :return:
        """
        search_result_links = self.browser.find_elements(*self.SEARCH_RESULTS_LINK)
        all_result_links = [links.text for links in search_result_links]
        return all_result_links

    def title(self):
        """
        Returns title
        :return:
        """
        return self.browser.title

    def search_input_value(self):
        """
        Returns the text from search result page input box
        :return:
        """
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute("value")
        return value
