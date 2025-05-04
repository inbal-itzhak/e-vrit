from playwright.sync_api import Page
from pages.base_page import BasePage


class SearchResultsPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    _SEARCH_INPUT_FIELD = ".navbar  .inner-search-menu .txtSearch"
    _SEARCH_RESULTS_ = ".searchResultsAutoComplete .item-result"
    _SEARCH_RESULTS = ".details-result>.spnName"

    def search_book(self, book_name):
        search_field = self.page.locator(self._SEARCH_INPUT_FIELD)
        self.click(search_field)
        self.fill_text(search_field, book_name)

    def search_results(self, book_name):
        try:
            search_results = self.page.locator(self._SEARCH_RESULTS)
            if search_results.count() > 1:
                for i in range(search_results.count()):
                    sr_book_name = self.get_text(search_results.nth(i))
                    # sr_book_name = search_results.nth(i).get_attribute("alt")
                    print(f"search result {i} book name is {sr_book_name}")
                    if book_name in sr_book_name:
                        print(f"search result book name is {sr_book_name}")
                        self.click(search_results.nth(i))
                        return True
            else:
                print(f"no results for search '{book_name}'")
        except Exception as e:
            print(f"error in search results: {e}")





