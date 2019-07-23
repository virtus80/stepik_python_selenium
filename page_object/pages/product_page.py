from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()
        self.solve_quiz_and_get_code()

    def get_product_title(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_success_adding_message(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_ADDING_MESSAGE).text

    def get_basket_price_message(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_PRICE_MESSAGE).text

    def should_be_success_adding_product_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ADDING_MESSAGE), \
            "Message about adding product to basket is not displayed"

    def should_be_product_title_in_success_adding_product_message(self, product_title):
        actual_message = self.get_success_adding_message()
        assert "{} has been added to your basket.".format(product_title) == actual_message, \
            "Incorrect success adding product message: {}".format(actual_message)

    def should_be_basket_price_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE_MESSAGE), \
            "Message about basket price is not displayed"

    def should_be_product_price_in_basket_message(self, product_price):
        actual_message = self.get_basket_price_message()
        assert "Your basket total is now {}".format(product_price) == actual_message, \
            "Incorrect basket price message: {}".format(actual_message)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ADDING_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ADDING_MESSAGE), \
            "Success message is not disappeared, but should"
