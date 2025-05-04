from pages.book_page import BookPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.nav_menu import NavMenu
from pages.new_user_page import NewUserPage
from pages.search_results_page import SearchResultsPage


class BaseTest:
    home_page: HomePage
    book_page: BookPage
    login_page: LoginPage
    nav_menu: NavMenu
    new_user_page: NewUserPage
    search_results_page: SearchResultsPage