from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(object):
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")

class ProductPageLocators(object):
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    SUCCESS_ADDING_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner")
    BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner p:first-child")