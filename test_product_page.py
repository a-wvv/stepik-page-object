from pages.product_page import ProductPageObject
import pytest
import time
product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(0,10)]
@pytest.mark.parametrize('link', urls)
def test_user_should_add_to_basker(browser, link):
    browser.delete_all_cookies()
    page= ProductPageObject(browser, link)
    page.open()
    page.should_add_to_basket()
