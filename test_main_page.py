from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest
urls = ['http://selenium1py.pythonanywhere.com/']


class TestLoginFromMainPage():
    @pytest.mark.parametrize('link', urls)
    def test_guest_can_go_to_login_page(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    @pytest.mark.parametrize('link', urls)
    def test_guest_should_see_login_link(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


@pytest.mark.parametrize('link', urls)
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    page.should_be_empty_basket()
    page.should_be_message_busket_empty()
