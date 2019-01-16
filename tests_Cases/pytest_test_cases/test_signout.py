from pages.dash_board_page import DashBoard
from pages.login_page import LoginPage
from source.data.user_conf import *
import pytest


@pytest.mark.usefixtures("setup", "one_time_setup")
class TestSignOut():

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
       self.log_p = LoginPage(self.driver)
       self.Dash_p = DashBoard(self.driver)

    @pytest.mark.slow
    def test_sign_out_case(self):
        c_url = self.log_p.get_current_url()
        self.log_p.user_login(valid_username, valid_password)
        self.Dash_p.signout_account()
        result = self.Dash_p.verify_signout()
        print(result)
        assert result == True
        self.log_p.click_on_url(c_url)

