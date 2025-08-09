from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, "The substring 'login' is missing from the URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        register_form_email = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        register_form_email.send_keys(email)
        register_form_password = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD)
        register_form_password.send_keys(password)
        register_form_password_repeat = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_REPEAT)
        register_form_password_repeat.send_keys(password)
        button_submit = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        button_submit.click()
