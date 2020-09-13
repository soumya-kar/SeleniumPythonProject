"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""
from selenium.webdriver.common.by import By

class DuckDuckGoResultPage:
    RESULT_LINKS = (By.CSS_SELECTOR, 'h2 *.result__a')
    SEARCH_INPUT_RESULT = (By.NAME, 'q')
    
    def __init__(self, browser):
        self.browser= browser

    def result_link_titles(self):
        links= self.browser.find_elements(*self.RESULT_LINKS)
        titles=[]
        for link in links:
           titles.append(link.text)
        return titles

    def search_input_value(self):
        search_input= self.browser.find_element(*self.SEARCH_INPUT_RESULT)
        value= search_input.get_attribute('value')
        return value

    def get_title(self):
        return self.browser.title

    def click_on_first_link(self):
        links=self.browser.find_elements(*self.RESULT_LINKS)
        links[0].click()
    