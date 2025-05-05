import playwright
from playwright.async_api import expect
from playwright.sync_api import Page, Locator
from pages.base_page import BasePage
import random
import string
import allure


class NewUserPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    _CREATE_ACCOUNT_BTN = ".register-btn"
    _EMAIL_FIELD = "#emailRegister"
    _PASSWORD_FIELD = ".input-pass #passwordRegister"
    _REMEMBER_ME_CB = ".checkbox-div [id='#passwordRegister']"
    _NOTIFICATIONS_CB = "#newsletter"
    _T_AND_C_CB = "#tAndC"
    _REGISTER_BTN = ".register.btn-primary"
    _REGISTRATION_SUCCESS = ".modal-box .header__title"
    _MISSING_REG_EMAIL_MESSAGE = "#uw10be47e"
    _MISSING_REG_PASSWORD_MESSAGE = "#uw1a8114d"
    _INVALID_REG_EMAIL_MESSAGE = ".input-div.input-ltr.error .input-toast-error"
    _INVALID_REG_PASSWORD_MESSAGE = ".input-container-pass .input-toast-error"
    _MISSING_T_AND_C_CHECKBOX_MESSAGE = ".checkbox-toast-error"
    _CLOSE_SUCCESS_MODAL = ".modal__closeLink"

    @allure.step("generate random email address")
    def generate_random_email(self, email_vendor):
        local_part_length = random.randint(8, 15)  # Length of the part before '@'
        allowed_chars = string.ascii_lowercase + "._-"
        local_part = ''.join(random.choice(allowed_chars) for _ in range(local_part_length))
        while local_part.endswith('.'):
            local_part = local_part[:-1]
        allure.attach(body=f"generated email address: {local_part}@{email_vendor}", name="email address",
                      attachment_type=allure.attachment_type.TEXT)
        return f"{local_part}@{email_vendor}"

    @allure.step("click on create new account button")
    def click_create_account_btn(self):
        self.click(self._CREATE_ACCOUNT_BTN)

    @allure.step("fill in {email_addr} in email address field")
    def fill_in_email_for_registration(self, email_addr):
        self.fill_text(self._EMAIL_FIELD, email_addr)

    @allure.step("fill in {password} in password field")
    def fill_in_password_for_registratoin(self, password):
        self.fill_text(self._PASSWORD_FIELD, password)

    @allure.step("check the terms and conditions checkbox")
    def checkbox_t_and_c_cb(self, max_retries=3):
        attempts = 0
        while attempts < max_retries:
            try:
                if not self.page.locator(self._T_AND_C_CB).is_checked():
                    self.page.locator(self._T_AND_C_CB).check()
                if self.page.locator(self._T_AND_C_CB).is_checked():
                    return
                else:
                    attempts += 1
                    print(f"Attempt {attempts}/{max_retries} T and C checkbox not checked")
            except Exception as e:
                attempts += 1
                self.page.locator(self._T_AND_C_CB).check()
                if not self.page.locator(self._T_AND_C_CB).is_checked():
                    print(f"Attempt {attempts}/{max_retries} ended in error, {e}")

    @allure.step("click on finish registration button")
    def click_on_register_btn(self):
        self.click(self._REGISTER_BTN)

    @allure.step("verify registration is successful")
    def assert_registration_success(self):
        try:
            test_data = self.load_login_messages_yaml("../pages/login_messages.yml")
            actual_registration_status = self.get_text(self._REGISTRATION_SUCCESS)
            expected_registration_status = test_data["REGISTRATION_SUCCESS_MESSAGE"]
            if expected_registration_status == actual_registration_status:
                return True
        except Exception as e:
            print(f"error: {e}")
            return False

    @allure.step("Close 'finish registration' window")
    def close_success_modal(self):
        self.click(self._CLOSE_SUCCESS_MODAL)

    @allure.step("Validate correct message shows when email is missing in registration")
    def check_missing_email_message(self):
        try:
            test_data = self.load_login_messages_yaml("login_messages.yml")
            actual_message = self.get_text(self._MISSING_REG_EMAIL_MESSAGE)
            expected_message = test_data["MISSING_FIELD"]
            if expected_message == actual_message:
                return True
        except ValueError:
            print(f"value error: {ValueError}")

    @allure.step("Validate correct message shows when password is missing in registration")
    def check_missing_password_message(self):
        try:
            test_data = self.load_login_messages_yaml("login_messages.yml")
            actual_message = self.get_text(self._MISSING_REG_PASSWORD_MESSAGE)
            expected_message = test_data["MISSING_FIELD"]
            if expected_message == actual_message:
                return True
        except ValueError:
            print(f"value error: {ValueError}")
