from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPageObject(BasePage):
    def should_add_to_basket(self):
        self.should_be_name()
        self.should_be_price()
        self.should_be_add_button()
        self.add_to_basket()
        self.should_add_with_correct_name()
        self.should_add_with_correct_price()
        self.should_be_success()

    def should_be_name(self):
        assert self.browser.find_element(*ProductPageLocators.ITEM_NAME)

    def should_be_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_FOR_ITEM)

    def should_be_add_button(self):
        assert self.browser.find_element(*ProductPageLocators.ADD_BUTTON)

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(
            *ProductPageLocators.ADD_BUTTON)
        add_to_basket_button.click()

    def should_add_with_correct_name(self):
        assert self.browser.find_element(*ProductPageLocators.ADDED_ITEM)
        assert self.browser.find_element(
            *ProductPageLocators.ADDED_ITEM).text == self.browser.find_element(
            *ProductPageLocators.ITEM_NAME).text

    def should_add_with_correct_price(self):
        assert self.browser.find_element(
            *ProductPageLocators.PRICE_FOR_ADDED_ITEM)
        assert self.browser.find_element(
            *ProductPageLocators.PRICE_FOR_ITEM).text == self.browser.find_element(*ProductPageLocators.PRICE_FOR_ADDED_ITEM).text

    def should_be_success(self):
        assert self.browser.find_element(*ProductPageLocators.SUCESS_MESAGES)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCESS_MESAGES)

    def should_disappear(self):
        assert self.is_disappeared(ProductPageLocators.DISAPPEARED_MESSAGE)

    def get_success_message(self):
        added_book = self.browser.find_element(
            *ProductPageLocators.ITEM_NAME).text
        store_book = self.browser.find_element(
            *ProductPageLocators.ADDED_ITEM).text
        assert store_book == added_book, 'Wrong book!'
