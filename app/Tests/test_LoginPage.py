import pytest

from app.Base.BaseTest import BaseTest
from app.Pages.LoginPage import LoginPage
from app.Configs.Config import TestData


class TestLoginPage(BaseTest):

    @pytest.fixture(autouse=True)
    def page_initialize(self):
        self.login_page = LoginPage(self.driver)

    def test_verify_user_can_login(self):
        self.login_page.enter_username(TestData.USERNAME)
        self.login_page.enter_password(TestData.PASSWORD)
        self.login_page.click_login_button()
        assert self.login_page.verify_login()

