from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.add_to_basket()
        self.should_be_cost_basket()
        self.should_be_add_to_basket()

    def add_to_basket(self):
        button_add = self.browser.find_element(*ProductPageLocators.LINK_ADD)
        button_add.click()

    def should_be_add_to_basket(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        assert self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT).text == name_product, "Other product was added"

    def should_be_cost_basket(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert self.browser.find_element(
            *ProductPageLocators.ADDED_PRICE_PRODUCT).text in price_product, "Other price"

    def should_be_is_not_element_present(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_PRODUCT), "Found"

