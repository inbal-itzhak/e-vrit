import pytest
from tests.base_test import BaseTest
from utils.config_reader import ConfigReader
import allure


@pytest.mark.usefixtures("setup_page")
class TestCreateUser(BaseTest):

    @allure.description("create a new valid user")
    @allure.title("create a new valid user")
    def test_create_valid_user(self, registration_email, password):
        self.nav_menu.click_on_my_account()
        assert self.login_page.check_login_modal_open() is True
        self.new_user_page.click_create_account_btn()
        self.new_user_page.fill_in_email_for_registration(registration_email)
        self.new_user_page.fill_in_password_for_registratoin(password)
        self.new_user_page.checkbox_t_and_c_cb()
        self.new_user_page.click_on_register_btn()
        assert self.new_user_page.assert_registration_success()

    @allure.description("login with created user")
    @allure.title("login")
    def test_login(self, registration_email, password):
        self.nav_menu.click_on_my_account()
        assert self.login_page.check_login_modal_open() is True
        self.login_page.valid_login(registration_email, password)
        assert self.login_page.check_logged_in_user() == registration_email

    data = ["הילד שהציל את הקשת", "המתווך"]

    @pytest.mark.parametrize("text", data)
    @allure.description("search book {text}")
    @allure.title("search book {text}")
    def test_search_book(self, registration_email, password, text):
        self.nav_menu.click_on_my_account()
        self.login_page.valid_login(registration_email, password)
        self.search_results_page.search_book(text)
        self.search_results_page.search_results(text)
        book_title = self.book_page.get_book_title()
        assert text in book_title


