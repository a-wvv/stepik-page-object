from selenium.webdriver.common.by import By


class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group .btn.btn-default')

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group .btn.btn-default')
    EMPTY_BACKET = (By.CSS_SELECTOR, '.basket-items"')
    EMPTY_BACKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner>p')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIT_FIELD = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFRIM_PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register_form > button:nth-child(7)')


class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ITEM_NAME = (By.CSS_SELECTOR, '.product_main h1')
    ADDED_ITEM = (
        By.CSS_SELECTOR, 'div.alert:nth-child(1) > div:nth-child(2) > strong:nth-child(1)')
    PRICE_FOR_ITEM = (By.CSS_SELECTOR, '.product_main p.price_color')
    PRICE_FOR_ADDED_ITEM = (By.CSS_SELECTOR, '#messages p:nth-child(1) > strong')
    SUCESS_MESAGES = (By.CSS_SELECTOR, '.alertinner strong')
    DISAPPEARED_MESSAGE = (
        By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-warning.fade.in')
