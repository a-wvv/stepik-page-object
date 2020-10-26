from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR,".btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR,'.product_main h1')
    ADDED_ITEM = (By.CSS_SELECTOR,'div.alert:nth-child(1) > div:nth-child(2) > strong:nth-child(1)')
    PRICE_FOR_ITEM = (By.CSS_SELECTOR,'.product_main p.price_color')
    SUCESS_MESAGES = (By.CSS_SELECTOR, ".alertinner strong")
    

