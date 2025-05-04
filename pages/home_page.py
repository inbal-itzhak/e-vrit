from playwright.sync_api import Page
from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    _LOGO = ".logo"
    _MY_ACCOUNT_LINK = ".icon-bar.myAccount"
    _WISHLIST_LINK = ".a-wishlist.menu-rel"
    _SHOPPING_CART_LINK = ".a-myShoppingCart.menu-rel"
    _NUM_OF_ITEMS_IN_CART = ".num-of-items-icon"
    _NUM_OF_GIFTS_IN_CART = ".num-of-items-icon.show-icon.gift-shopping-cart"
    _SEARCH_INPUT_FIELD = ".navbar-search .search-input-div"
    _SEARCH_RESULTS = ".searchResultsAutoComplete .item-result"

    def click_on_my_account(self):
        self.click(self._MY_ACCOUNT_LINK)

    def click_on_wishlist(self):
        self.click(self._WISHLIST_LINK)

    def get_num_of_items_in_cart(self):
        num_of_items_txt = self.get_text(self._NUM_OF_ITEMS_IN_CART)
        try:
            return int(num_of_items_txt)
        except TypeError:
            print(f"unable to parse num of items txt, {TypeError}")

    def click_on_shopping_cart(self):
        self.click(self._SHOPPING_CART_LINK)

    def search_book(self, book_name):
        search_field = self.page.locator(self._SEARCH_INPUT_FIELD)
        search_field.focus()
        self.fill_text(search_field, book_name)
        search_results = self.page.locator(self._SEARCH_RESULTS)
        if search_results.count()>1:
            for i in range(search_results.count()):
                sr_book_name = search_results.nth(i).get_attribute("alt")
                if book_name in sr_book_name:
                    self.click(search_results.nth(i))




