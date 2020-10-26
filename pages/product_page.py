from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPageObject(BasePage):
    product_name = ''
    product_price = ''

    def should_add_to_basket(self):
        self.should_be_name()
        self.should_be_price()
        self.should_be_add_button()
        add_to_basket = self.browser.find_element(
            *ProductPageLocators.BASKET_BUTTON)
        add_to_basket.click()
        self.solve_quiz_and_get_code()
        self.should_add_correct_product()
        self.should_be_sucess()
        self.get_sucess_message()
        
    def should_be_name(self):
        assert self.browser.find_element(*ProductPageLocators.ITEM_NAME)
        self.product_name = self.browser.find_element(
            *ProductPageLocators.ITEM_NAME).text

    def should_be_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_FOR_ITEM)
        self.product_price = self.browser.find_element(
            *ProductPageLocators.PRICE_FOR_ITEM).text

    def should_be_add_button(self):
        assert self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)

    def should_add_correct_product(self):
        assert self.browser.find_element(*ProductPageLocators.ADDED_ITEM)
        assert self.browser.find_element(
            *ProductPageLocators.ADDED_ITEM).text == self.browser.find_element(
            *ProductPageLocators.ITEM_NAME).text
    def should_be_sucess(self):
        assert self.browser.find_element(*ProductPageLocators.SUCESS_MESAGES)

    def get_sucess_message(self):
        pass
        added_book = self.browser.find_element(
            *ProductPageLocators.ITEM_NAME).text
        store_book = self.browser.find_element(
            *ProductPageLocators.ADDED_ITEM).text
        assert store_book == added_book, 'Wrong book!'
