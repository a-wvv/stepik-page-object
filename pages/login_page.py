from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        self.register_new_user()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, 'Wrong url'

    def should_be_login_form(self):
        self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_register_form(self):
        self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), 'Register form is not presented'

    def register_new_user(self):
        elemenent = self.browser.find_element(*LoginPageLocators.EMAIT_FIELD)
        elemenent.send_keys(str(time.time()) + '@fakemail.org')
        elemenent = self.browser.find_element(
            *LoginPageLocators.PASSWORD_FIELD)
        elemenent.send_keys('123qwe1234')
        elemenent = self.browser.find_element(
            *LoginPageLocators.CONFRIM_PASSWORD_FIELD)
        elemenent.send_keys('123qwe1234')
        elemenent = self.browser.find_element(
            *LoginPageLocators.REGISTER_BUTTON)
        elemenent.click()
