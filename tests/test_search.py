"""
These tests cover DuckDuckGo searches.
"""

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from pages.detail import DuckDuckGoDetailPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest

@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_basic_duckduckgo_search(browser, phrase):
    search_page= DuckDuckGoSearchPage(browser)
    result_page= DuckDuckGoResultPage(browser)
    #PHRASE="panda"
    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for "panda"
    search_page.search(phrase)

    WebDriverWait(browser, 20).until(EC.title_contains(phrase))

    # Then the search result title contains "panda"
    assert phrase in result_page.get_title()
    
    # And the search result links pertain to "panda"
    for title in result_page.result_link_titles():
        if title == "Music and Podcasts, Free and On-Demand | Pandora":
            continue
        assert phrase.lower() in title.lower()

    # And the search result query is "panda"
    assert phrase == result_page.search_input_value()

@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_basic_duckduckgo_search_using_ENTER(browser, phrase):
    search_page= DuckDuckGoSearchPage(browser)
    result_page= DuckDuckGoResultPage(browser)
    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for "panda"
    search_page.search_using_ENTER(phrase)

    WebDriverWait(browser, 20).until(EC.title_contains(phrase))

    # Then the search result title contains "panda"
    assert phrase in result_page.get_title()
    
    # And the search result links pertain to "panda"
    for title in result_page.result_link_titles():
        if title == "Music and Podcasts, Free and On-Demand | Pandora":
            continue
        assert phrase.lower() in title.lower()

    # And the search result query is "panda"
    assert phrase == result_page.search_input_value()

@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_click_on_first_searh_result(browser, phrase):
    search_page= DuckDuckGoSearchPage(browser)
    result_page= DuckDuckGoResultPage(browser)
    detail_page= DuckDuckGoDetailPage(browser)
    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for "panda"
    search_page.search_using_ENTER(phrase)

    # And user click on first search result
    result_page.click_on_first_link()

    #Wait till title is displayed
    WebDriverWait(browser, 20).until(EC.title_contains(phrase))

    # Then user shoud verify new page title
    assert phrase in detail_page.get_detail_page_title() 