from pages.LoginPage import LoginPage
import unittest
import pytest
from ddt import ddt, data, unpack
from utillities.read_csv_data import getCSVData
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
    @data(("mohit", "Pass_123"))
    @unpack
    def test_invalid_user_credentials(self, user_name, password):

        self.lp.user_login(user_name, password)
        log_result = self.lp.verify_loginfail_error()
        assert log_result == True

    @pytest.mark.run(order=2)
    @data((None, "Pass_123"))
    @unpack
    def test_LoginWithOutUsername(self, user_name, password):

        self.lp.user_login(user_name, password)
        log_result = self.lp.verify_username_error()
        assert log_result == True

    @pytest.mark.run(order=3)
    @data(("qa.user", None))
    @unpack
    def test_login_without_password(self, user_name, password):
        self.lp.user_login(user_name, password)
        # pdb.set_trace()
        log_result = self.lp.verify_password_error()
        assert log_result == True
