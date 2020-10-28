from pages.base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.EMPTY_BACKET), 'Item in basket'

    def should_be_message_busket_empty(self):
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_BACKET_MESSAGE), 'This basket is not empty'
