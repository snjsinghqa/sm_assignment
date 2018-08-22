from pages.login_page import LoginPage
import pytest
from utillities.read_csv_data import getCSVData
# import pdb


@pytest.mark.usefixtures("setup", "one_time_setup")
class TestsLogin():

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        self.lp = LoginPage(self.driver)
        c_url = self.lp.get_current_url()
        yield
        self.lp.click_on_url(c_url)

    @pytest.mark.run(order=4)
    def test_valid_user_credentials(self, user_name = "snjsingh", password = "Pass_123"):
        c_url = self.lp.get_current_url()
        self.lp.user_login(user_name, password)
        log_result = self.lp.verify_login()
        assert log_result == True
        self.lp.click_on_url(c_url)

    @pytest.mark.run(order=1)
    def test_invalid_user_credentials(self, user_name = "mohit", password = "Pass_123"):

        self.lp.user_login(user_name, password)
        log_result = self.lp.verify_loginfail_error()
        assert log_result == True

    @pytest.mark.run(order=2)
    def test_LoginWithOutUsername(self, user_name = None, password = "Pass_123"):

        self.lp.user_login(user_name, password)
        log_result = self.lp.verify_username_error()
        assert log_result == True

    @pytest.mark.run(order=3)
    def test_login_without_password(self, user_name = "qa.user", password = None):
        self.lp.user_login(user_name, password)
        # pdb.set_trace()
        log_result = self.lp.verify_password_error()
        assert log_result == True
