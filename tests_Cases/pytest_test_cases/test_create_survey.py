from pages.login_page import LoginPage
from source.data.question_config import *
from pages.create_survey_page import CreateSurveyPage
from pages.design_page import SurveyDesignPage
from pages.dash_board_page import DashBoard
import pytest
from source.data.user_conf import *
from source.data.survey_title_category_config import *
from flaky import flaky

# import pdb


@pytest.mark.usefixtures("setup", "one_time_setup")
class TestCreateSurvey:

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        self.log_p = LoginPage(self.driver)
        self.c_survey_p = CreateSurveyPage(self.driver)
        self.c_survey_design = SurveyDesignPage(self.driver)
        self.dash_p = DashBoard(self.driver)

    @ flaky
    @pytest.mark.run(order=4)
    def test_create_survey(self):
        self.log_p.user_login(valid_username, valid_password)
        self.c_survey_p.create_survey(survey_title, survey_category)
        self.c_survey_design.add_question_with_single_text_option(question1)
        self.c_survey_design.add_question_with_dropdown_option(question2, q2_value1, q2_value2, q2_value3)
        self.c_survey_design.add_question_with_date_option(question3)
        self.c_survey_design.add_question_with_rating_option(question4)
        self.c_survey_design.add_question_with_drop_by_selected_vale_option(question5, q5_visible_text)
        self.c_survey_design.add_question_with_checkboxes_option(question6, q6_value1,
                                                                 q6_value2, q6_value3, q6_value4, q6_value5)
        self.c_survey_design.add_question_with_matrix_rating_option(question7, q7_value1, q7_value2, q7_value3,
                                                                    q7_column1, q7_column2, q7_column3, q7_column4)
        self.c_survey_design.add_question_with_multi_textbox_option(question8, q8_label1, q8_label2, q8_label3)
        self.c_survey_design.add_question_with_radio_option(question9, q9_visible_text)
        self.c_survey_design.add_question_with_text_area_option(question10)
        self.c_survey_design.previewsurvey()

    @flaky
    def test_edit_survey_title(self):
        self.log_p.user_login(valid_username, valid_password )
        self.c_survey_p.create_survey(survey_title, survey_category)
        self.c_survey_design.edit_survey_title(new_survey_title)

    @flaky
    def test_edit_survey_category(self):
        self.log_p.user_login(valid_username, valid_password )
        self.c_survey_p.create_survey(survey_title, survey_category)
        self.c_survey_design.edit_survey_title(new_survey_category)
