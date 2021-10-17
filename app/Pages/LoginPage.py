from app.Base.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    _username = (By.ID, "user-name")
    _password = (By.ID, "password")
    _login_button = (By.ID, "login-button")
    _assert_item = (By.CLASS_NAME, 'app_logo')

    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username):
        self.do_send_keys(self._username, username)

    def enter_password(self, password):
        self.do_send_keys(self._password, password)

    def click_login_button(self):
        self.do_click(self._login_button)

    def verify_login(self):
        return self.do_visibility_check(self._assert_item)