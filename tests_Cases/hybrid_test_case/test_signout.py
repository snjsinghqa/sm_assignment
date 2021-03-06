from pages.dash_board_page import DashBoard
from pages.login_page import LoginPage
import pytest
import unittest
from ddt import ddt, data, unpack
from utillities.read_csv_data import getCSVData


@ddt
@pytest.mark.usefixtures("setup", "one_time_setup")
class SignOutTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
       self.log_p = LoginPage(self.driver)
       self.Dash_p = DashBoard(self.driver)

    @pytest.mark.slow
    @data(*getCSVData("/Users/Documents/PycharmProjects/SurveyMonkey/source/Login_test_codex.csv"))
    @unpack
    def test_sign_out_case(self, username, password):
        c_url = self.log_p.get_current_url()
        self.log_p.user_login(username, password)
        self.Dash_p.signout_account()
        result = self.Dash_p.verify_signout()
        print(result)
        assert result == True
        self.log_p.click_on_url(c_url)

