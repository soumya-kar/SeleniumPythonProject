"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoSearchPage:
    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')
    SEARCH_BTTN = (By.ID, 'search_button_homepage')
    URL = 'https://www.duckduckgo.com'
    
    def __init__(self, browser):
        self.browser= browser

    def load(self):
        self.browser.get(self.URL)
    
    def search(self, phrase):
        search_input= self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase)
        search_button= self.browser.find_element(*self.SEARCH_BTTN)
        search_button.click()

    