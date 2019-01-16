from base.BasePage import BasePage
import time
import utillities.custom_logger as cl
import logging


class SurveyDesignPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #  Locators ------------------------------------

    logo_btn = "//span[@class = 'add-logo-btn wds-button" \
               " wds-button--sm wds-button--icon-left wds-button--ghost-filled']"
    from_pc = "//a[@tab-target='from-computer']"
    from_lib = "//a[@tab-target='from-library']"
    import_link = "//span[@class = 'qq-upload-button-selector browse-for-file import-link']"
    ques_bank = "//li[@title='Question Bank']"
    builder = "//li[@title='Builder']"
    themes = "//li[@title='Themes']"
    logic = "//li[@title='Logic']"
    options = "//li[@title='Options']"
    title_container = "//div[@class = 'survey-title-table-wrapper']"

    # Edit Survey Title ----------------------------

    e_survey_title = "surveyTitle"
    e_survey_category = "surveyCategory"
    e_survey_save = "//form[@id='surveyTitleForm']/div" \
                    "/a[@class='wds-button wds-button--sm save']"
    e_survey_cancel = "//form[@id='surveyTitleForm']/div" \
                      "/a[@class='wds-button wds-button--sm wds-button--ghost-filled cancel']"

    # Add Question Locators ------------------------

    question = "//div[@class='rte sm-input sm-input--stretch" \
               " mce-content-body mce-edit-focus']"
    change_fieldtype = "changeQType"
    single_text = "//a[@data-action='SingleTextboxQuestion']"
    multiple_choice = "//a[@data-action='MultipleChoiceQuestion']"
    checkbox = "//a[@data-action='CheckboxQuestion']"
    matrix = "//a[@data-action='MatrixQuestion']"
    matrix_filed = "//div[@class='rteToolbarContainer empty']" \
                   "/div[@data-rte='answer' and contains(@id,'newChoice')]"
    matrix_column = "//div[@class='rteToolbarContainer empty']/div[@data-rte=" \
                    "'column' and contains(@id,'newChoice')]"
    comment_box = "//a[@data-action='CommentBoxQuestion']"
    date_time = "//a[@data-action='DateTimeQuestion']"
    dropdown = "//a[@data-action='DropdownQuestion']"
    dropdown_select_type = "//div[@id='editQuestionContent']//select" \
                           "[@id='answerBankCategorySelect']"
    option_input_field = "//div[@class='rteToolbarContainer empty']/div[contains" \
                         "(@id,'newChoice')]"
    star_rating = "//a[@data-action='StarRatingQuestion']"
    multiple_textbox = "//a[@data-action='MultipleTextboxQuestion']"
    add_next_question = "//*[@id='editQuestion']/section[2]/div[3]/div/div/a[1]"
    add_next_question_mwindow = "//div[@id='editQuestionContent']/following-sibling" \
                                "::div/div/div/a[contains(text(),'NEXT QUESTION')]"
    preview_survey = "previewSurvey"
    send_survey = "sendSurvey"

    # Clicker Methods ---------------------------------

    def click_on_title_container(self):
        self.move_to_element_and_click(self.title_container, "xpath")

    def click_on_save_edit_survey_btn(self):
        self.element_click(self.e_survey_save, "xpath")

    def click_on_cancle_edit_survey_btn(self):
        self.element_click(self.e_survey_cancel, "xpath")

    def click_change_fieldtype(self):
        self.element_click(self.change_fieldtype)

    def click_single_text_opt(self):
        self.element_click(self.single_text, "xpath")

    def click_date_opt(self):
        self.element_click(self.date_time, "xpath")

    def click_multiple_choice_opt(self):
        self.element_click(self.multiple_choice, "xpath")

    def click_checkbox_opt(self):
        self.element_click(self.checkbox, "xpath")

    def click_matrix_opt(self):
        self.element_click(self.matrix, "xpath")

    def click_comment_box_opt(self):
        self.element_click(self.comment_box, "xpath")

    def click_dropdown_opt(self):
        self.element_click(self.dropdown, "xpath")

    def click_star_rating_opt(self):
        self.element_click(self.star_rating, "xpath")

    def click_add_new_question(self):
        self.element_click(self.add_next_question, "xpath")

    def click_add_new_question_in_detail(self):
        self.element_click(self.add_next_question_mwindow, "xpath")

    def click_multi_textboxe(self):
        self.element_click(self.multiple_textbox, "xpath")

    def click_next_preview_survey(self):
        self.element_click(self.preview_survey)

    # Setter Mehods ----------------------------------

    def set_esurvey_title(self, title):
        self.set_send_keys(title, self.e_survey_title)

    def set_ecategory(self, visible_text):
        self.select_by_visible_text(visible_text, self.e_survey_category)

    def set_question(self, question):
        self.set_send_keys(question, self.question, "xpath")

    def set_dropdown_field_value(self, value):
        self.set_multi_options(value, self.option_input_field, "xpath")

    def set_value_in_dropdown(self, visible_text):
        self.select_by_visible_text(visible_text, self.dropdown_select_type, "xpath")

    def set_checkboxes_field_value(self, value):
        self.set_multi_options(value, self.option_input_field, "xpath")

    def set_matrix_field_value(self, value):
        self.set_multi_options(value, self.matrix_filed, "xpath")

    def set_matrix_column_value(self, value):
        self.set_multi_options(value, self.matrix_column, "xpath")

    def set_multi_line_label(self, label):
        self.set_multi_options(label, self.option_input_field, "xpath")

    # Actions ----------------------------------------------

    def edit_survey(self, survey_title, survey_category):
        self.click_on_title_container()
        time.sleep(2)
        self.set_esurvey_title(survey_title)
        self.set_ecategory(survey_category)
        self.click_on_save_edit_survey_btn()

    def edit_survey_title(self, survey_title):
        self.click_on_title_container()
        time.sleep(2)
        self.set_esurvey_title(survey_title)
        self.click_on_save_edit_survey_btn()

    def edit_survey_category(self, survey_category):
        self.click_on_title_container()
        time.sleep(2)
        self.set_ecategory(survey_category)
        self.click_on_save_edit_survey_btn()

    def add_field_type(self, field_type="text_box"):
        self.click_change_fieldtype()
        if field_type == "text_box":
            self.click_single_text_opt()
        elif field_type == "drop_down":
            self.click_dropdown_opt()
        elif field_type == "date":
            self.click_date_opt()
        elif field_type == "star_rating":
            self.click_star_rating_opt()
        elif field_type == "drop_down_select":
            self.click_dropdown_opt()
        elif field_type == "checkboxes":
            self.click_checkbox_opt()
        elif field_type == "matrix_rating":
            self.click_matrix_opt()
        elif field_type == "multi_textbox":
            self.click_multi_textboxe()
        elif field_type == "radio":
            self.click_multiple_choice_opt()
        elif field_type == "text_area":
            self.click_comment_box_opt()
        else:
            print("invalid Field type : "+field_type)

    def add_question_with_single_text_option(self, question_title):
        self.add_field_type("text_box")
        # self.click_add_new_question()
        self.set_question(question_title)
        self.click_add_new_question_in_detail()

    def add_question_with_dropdown_option(self, question_title, *args):
        self.set_question(question_title)
        self.add_field_type("drop_down")
        for arg in args:
            self.set_dropdown_field_value(arg)
        self.click_add_new_question_in_detail()

    def add_question_with_date_option(self, question_title):
        self.set_question(question_title)
        self.add_field_type("date")
        self.click_add_new_question_in_detail()

    def add_question_with_rating_option(self, question_title):
        self.set_question(question_title)
        self.add_field_type("star_rating")
        self.click_add_new_question_in_detail()

    def add_question_with_drop_by_selected_vale_option(self, question_title, visible_text):
        self.set_question(question_title)
        self.add_field_type("drop_down_select")
        self.set_value_in_dropdown(visible_text)
        self.click_add_new_question_in_detail()

    def add_question_with_checkboxes_option(self, question_title, *args):
        self.set_question(question_title)
        self.add_field_type("checkboxes")
        for arg in args:
            self.set_checkboxes_field_value(arg)
        self.click_add_new_question_in_detail()

    def add_question_with_matrix_rating_option(self, question_title, value1, value2, value3, *column):
        self.set_question(question_title)
        self.add_field_type("matrix_rating")
        self.set_matrix_field_value(value1)
        self.set_matrix_field_value(value2)
        self.set_matrix_field_value(value3)
        for col in column:
            self.set_matrix_column_value(col)
        self.click_add_new_question_in_detail()

    def add_question_with_multi_textbox_option(self, question_title, *label):
        self.set_question(question_title)
        self.add_field_type("multi_textbox")
        for lab in label:
            self.set_multi_line_label(lab)
        self.click_add_new_question_in_detail()

    def add_question_with_radio_option(self, question_title, visible_text):
        self.set_question(question_title)
        self.add_field_type("radio")
        self.set_value_in_dropdown(visible_text)
        self.click_add_new_question_in_detail()

    def add_question_with_text_area_option(self, question_title):
        self.set_question(question_title)
        self.add_field_type("text_area")
        self.click_add_new_question_in_detail()

    def previewsurvey(self):
        self.click_next_preview_survey()
