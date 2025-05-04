import allure
from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    _MY_ACCOUNT_LINK = ".icon-bar.myAccount"
    _ACCOUNT_MODAL = ".account-modal"
    _REGISTER_BTN = ".register-btn"
    _EMAIL_LOGIN_FIELD = "#emailLogin"
    _PASSWORD_LOGIN_FIELD = "#passwordLogin"
    _REMEMBER_ME_CB = "#rememberMeLogin"
    _LOGIN_BTN = ".login.btn-primary"
    _INVALID_USER_OR_PASS_MESSAGE = ".submit-error"
    _INVALID_EMAIL_MESSAGE = ".input-div.input-ltr.error .input-toast-error"
    _MISSING_EMAIL_MESSAGE = "#uw3c789d6"
    _MISSING_PASS_MESSAGE = "#uw44a18ff"
    _LOGGED_IN_USER = ".header-user-email"

    @allure.step("login with email: {valid_email}. pass: {password} ")
    def valid_login(self, valid_email, password):
        self.click(self._MY_ACCOUNT_LINK)
        display_style = self.check_login_modal_open()
        if display_style:
            self.fill_text(self._EMAIL_LOGIN_FIELD, valid_email)
            self.fill_text(self._PASSWORD_LOGIN_FIELD, password)
            self.click(self._LOGIN_BTN)
        else:
            print(f"user {self.check_logged_in_user()} is already logged in")

    @allure.step("get the logged in user email")
    def check_logged_in_user(self):
        try:
            self.click(self._MY_ACCOUNT_LINK)
            return self.get_text(self._LOGGED_IN_USER)
        except Exception as e:
            print(f"element not found, {e}")

    @allure.step("check login window opens")
    def check_login_modal_open(self):
        account_modal_el = self.page.locator(self._ACCOUNT_MODAL)
        display_style = account_modal_el.evaluate("el => window.getComputedStyle(el).display")
        if display_style != "none":
            return True

    @allure.step("fill in {email_addr} in email address field")
    def fill_in_email_for_registration(self, email_addr):
        self.fill_text(self._EMAIL_LOGIN_FIELD, email_addr)
