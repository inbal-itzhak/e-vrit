import allure
from playwright.sync_api import Page, Locator
from pages.base_page import BasePage

class BookPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    _BOOK_TITLE = ".headlines__book-name"
    _BOOK_AUTHOR = ".headlines__book-author a"
    _BOOK_COPIES = ".general-info__product .price-btn__inner.NotPurchased"
    _BOOK_PRICE = f"{_BOOK_COPIES} .price__final"
    _digital_book_attr = "digital-btn"
    _printed_book_attr = "printed-btn"

    @allure.step("Validate book title")
    def get_book_title(self):
        self.page.wait_for_selector(self._BOOK_TITLE)
        return self.get_text(self._BOOK_TITLE)

    def is_digital_copy(self, book_copy_locator: Locator):
        is_digital = book_copy_locator.get_attribute(self._digital_book_attr)
        if is_digital is not None:
            return True

    def is_printed_copy(self, book_copy_locator: Locator):
        is_printed = book_copy_locator.get_attribute(self._printed_book_attr)
        if is_printed is not None:
            return True

    def get_book_price(self):
        book_price_txt = self.get_text(self._BOOK_PRICE)
        try:
            return int(book_price_txt)
        except ValueError:
            print(f"value error {ValueError}")

    def add_book_to_cart(self, book_copy_locator: Locator):
        self.click(book_copy_locator)
