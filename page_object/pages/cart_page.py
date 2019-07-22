from page_object.pages.locators import CartPageLocators
from .base_page import BasePage


class CartPage(BasePage):

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*CartPageLocators.ITEM_IN_BASKET), \
            "Product item is displayed, but should not be"

    def get_basket_content_message(self):
         return self.browser.find_element(*CartPageLocators.BASKET_CONTENT).text

    def should_be_message_empty_basket(self):
        actual_message = self.get_basket_content_message()
        assert "Your basket is empty" in actual_message, "Message about empty basket should be displayed"