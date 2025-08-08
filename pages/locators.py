from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    LINK_ADD = (By.CSS_SELECTOR, "#add_to_basket_form")
    NAME_PRODUCT = (By.CSS_SELECTOR, "[class='col-sm-6 product_main'] h1")
    ADDED_PRODUCT = (By.CSS_SELECTOR, ".alertinner strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p[class='price_color']")
    ADDED_PRICE_PRODUCT = (By.CSS_SELECTOR, ".alertinner p strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "[class='btn-group'] a")


class BasketPageLocators:
    BASKET_TOTALS = (By.CSS_SELECTOR, "#basket_totals")

