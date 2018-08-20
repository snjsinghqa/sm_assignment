from pages.login_page import LoginPage
from pages.create_survey_page import CreateSurveyPage
from pages.design_page import SurveyDesignPage
import unittest
import pytest
import time
from ddt import ddt, data, unpack
from utillities.read_csv_data import getCSVData
# import pdb


@pytest.mark.usefixtures("setup", "one_time_setup")
@ddt
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        self.log_p = LoginPage(self.driver)
        self.c_survey_p = CreateSurveyPage(self.driver)
        self.c_survey_design = SurveyDesignPage(self.driver)

    @pytest.mark.run(order=4)
    @data(*getCSVData("/Users/Documents/PycharmProjects/SurveyMonkey/source/Login_test_codex.csv"))
    @unpack
    def test_valid_user_credentials(self, user_name, password):
        self.log_p.user_login(user_name, password)
        self.c_survey_p.create_survey("Demo", "Other")
        url = self.c_survey_p.get_current_url()
        time.sleep(2)
        self.c_survey_design.driver.get(url)
        self.c_survey_design.edit_survey_title("New demo", "Events")
        self.c_survey_design.add_question("This is ?")
        time.sleep(8)

