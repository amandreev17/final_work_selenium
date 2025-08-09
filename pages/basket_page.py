from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasketPage(BasePage):
    def basket_is_not_empty(self):
        try:
            self.browser.find_element(*BasketPageLocators.BASKET_TOTALS)
        except NoSuchElementException:
            return False
        return True

    def basket_is_empty(self, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((BasketPageLocators.BASKET_TOTALS[0],
                                                                                       BasketPageLocators.BASKET_TOTALS[1])))
        except TimeoutException:
            return True

        return False

    def should_be_basket_is_empty(self):
        assert self.basket_is_empty(), "Basket is not empty"



