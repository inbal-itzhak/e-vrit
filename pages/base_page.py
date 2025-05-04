from playwright.sync_api import Page, Locator
import yaml


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def click(self, locator):
        try:
            if isinstance(locator, str):
                self.page.locator(locator).click()
            elif isinstance(locator, Locator):
                locator.click()
        except Exception as e:
            print(f"unable to click element, {e}")

    def fill_text(self, locator, text):
        try:
            if isinstance(locator, str):
                self.page.locator(locator).fill(text)
            elif isinstance(locator, Locator):
                locator.fill(text)
        except Exception as e:
            print(f"exception in fill text: {e}")

    def get_text(self, locator):
        try:
            if isinstance(locator, str):
                return self.page.locator(locator).inner_text()
            elif isinstance(locator, Locator):
                return locator.inner_text()
        except TypeError:
            print(f"Type error: {TypeError}")

    def type_text(self, locator, text):
        new_text = text + " "
        self.page.locator(locator).focus()
        self.page.locator(locator).type(new_text, delay=100)

    def load_login_messages_yaml(self, filename: str) -> dict:
        with open(filename, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
