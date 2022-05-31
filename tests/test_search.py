"""
Tests covers DuckDuckGo search
"""
import pytest

from page_objects.search import DuckDuckGoSearch
from page_objects.results import DuckDuckGoResults


@pytest.mark.parametrize("phrase", ["panda", "icecream", "samosa"])
def test_basic_duck_duck_go_search(open_browser, phrase):
    print("--- Starting tests for panda phrase search ---")

    go_search = DuckDuckGoSearch(open_browser)
    go_results = DuckDuckGoResults(open_browser)

    # phrase = "Panda"

    # Open DuckDuckGo website
    # go_search.load()

    # User searches for Panda
    print(f"Search for phrase: {phrase}")
    go_search.search(phrase)

    # Search result query is Panda
    assert phrase == go_results.search_input_value()
    print(f"Result page input box had {phrase}")

    # Search results title contains Panda
    assert phrase in go_results.title()
    print(f"Search was successfull!!!")

    # Search results links pertains to Panda
    result_list = go_results.result_link_titles()
    # assert len(result_list) > 0
    for titles in result_list:
        reformed_title = "".join([words for words in titles.lower().split(" ")])
        print(f"Original title: {titles}")
        print(f"Adjusted title: {reformed_title}")
        assert phrase.lower() in reformed_title

    print("All result links/titles successfully verified")

    print("--- Test ended ---")

    # raise Exception("--- Incomplete test ---")
    
def test_dummy():
    # Feature-1
    pass
