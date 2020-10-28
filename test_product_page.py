from pages.product_page import ProductPageObject
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest
import time
urls = ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/']


@pytest.mark.parametrize('link', urls)
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser, link):
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.go_to_login_page()
        self.page.register_new_user()
        self.page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_to_basket(self, browser, link):
        self.page = ProductPageObject(browser, link)
        self.page.open()
        self.page.should_add_to_basket()
        self.page.should_add_with_correct_name()
        self.page.should_add_with_correct_price()
        self.page.should_be_success()

    def test_user_cant_see_success_message(self, browser, link):
        self.page = ProductPageObject(browser, link)
        self.page.open()
        self.page.should_not_be_success_message()


@pytest.mark.parametrize('link', urls)
@pytest.mark.need_review
def test_guest_can_add_to_basket(browser, link):
    page = ProductPageObject(browser, link)
    page.open()
    page.should_add_to_basket()
    page.should_add_with_correct_name()
    page.should_add_with_correct_price()
    page.should_be_success()


@pytest.mark.parametrize('link', urls)
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    page = ProductPageObject(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_message_busket_empty()


@pytest.mark.parametrize('link', urls)
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    page = ProductPageObject(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_form()


@pytest.mark.xfail
@pytest.mark.parametrize('link', urls)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    browser.delete_all_cookies()
    page = ProductPageObject(browser, link)
    page.open()
    page.should_add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail
@pytest.mark.parametrize('link', urls)
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    browser.delete_all_cookies()
    page = ProductPageObject(browser, link)
    page.open()
    page.should_add_to_basket()
    page.should_disappear()
