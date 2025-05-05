from playwright.sync_api import Page
import pytest
import random
import string
from pages.book_page import BookPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.nav_menu import NavMenu
from pages.new_user_page import NewUserPage
from pages.search_results_page import SearchResultsPage
import allure

from utils.config_reader import ConfigReader


@pytest.fixture(scope="function")
def setup_page(request, page: Page):
    page.goto("https://e-vrit.co.il/")
    request.cls.home_page = HomePage(page)
    request.cls.book_page = BookPage(page)
    request.cls.login_page = LoginPage(page)
    request.cls.nav_menu = NavMenu(page)
    request.cls.new_user_page = NewUserPage(page)
    request.cls.search_results_page = SearchResultsPage(page)
    yield
    page.close()


@allure.step("Generate random email")
def generate_random_email(email_vendor):
    local_part_length = random.randint(8, 15)
    allowed_chars = string.ascii_lowercase + "._-"
    local_part = ''.join(random.choice(allowed_chars) for _ in range(local_part_length))
    while local_part.endswith('.'):
        local_part = local_part[:-1]
        allure.attach(body=f"generated email address: {local_part}@{email_vendor}", name="email address",
                      attachment_type=allure.attachment_type.TEXT)
    return f"{local_part}@{email_vendor}"


@pytest.fixture(scope="session")
def registration_email(request):
    email_vendor = ConfigReader.read_config("pytest", "email_vendor")
    if not email_vendor:
        email_vendor = "example.com"

    random_email = generate_random_email(email_vendor)
    print(f"\nGenerated registration email for session: {random_email}")
    return random_email


@pytest.fixture(scope="session")
def password(request):
    return ConfigReader.read_config("pytest", "password")


def pytest_exception_interact(node, report):
    if report.failed:
        driver = getattr(node.cls, "driver", None)
        if driver:
            allure.attach(body=driver.get_screenshot_as_png(), name="failure screenshot",
                          attachment_type=allure.attachment_type.PNG)
