from pages.login_page import LoginPage
import unittest
import pytest
from ddt import ddt, data, unpack
from utillities.read_csv_data import getCSVData
from source.data.user_conf import *
# import pdb


@pytest.mark.usefixtures("setup", "one_time_setup")
@ddt
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        self.lp = LoginPage(self.driver)
        c_url = self.lp.get_current_url()
        yield
        self.lp.click_on_url(c_url)

    @pytest.mark.run(order=4)
    @data(*getCSVData("/Users/Documents/PycharmProjects/SurveyMonkey/source/Login_test_codex.csv"))
    @unpack
    def test_valid_user_credentials(self, user_name, password):
        c_url = self.lp.get_current_url()
        self.lp.user_login(user_name, password)
        log_result = self.lp.verify_login()
        assert log_result == True
        self.lp.click_on_url(c_url)

    @pytest.mark.run(order=1)
    def test_invalid_user_credentials(self):

        self.lp.user_login(invalid_username, invalid_password)
        log_result = self.lp.verify_loginfail_error()
        assert log_result == True

    @pytest.mark.run(order=2)
    def test_LoginWithOutUsername(self):

        self.lp.user_login(None, valid_password)
        log_result = self.lp.verify_username_error()
        assert log_result == True

    @pytest.mark.run(order=3)
    def test_login_without_password(self):
        self.lp.user_login(valid_username, None)
        # pdb.set_trace()
        log_result = self.lp.verify_password_error()
        assert log_result == True
