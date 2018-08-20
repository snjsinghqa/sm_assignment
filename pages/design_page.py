from base.BasePage import BasePage
import time

class SurveyDesignPage(BasePage):

        def __init__(self, driver):
            super().__init__(driver)
            self.driver = driver

        #  Locators ------------------------------------
        logo_btn = "//span[@class = 'add-logo-btn wds-button " \
                   "wds-button--sm wds-button--icon-left wds-button--ghost-filled']"
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
        question = "//*[@id='questionTitleWrap']/table/tbody/tr[1]/td[2]/div[1]/span"
        change_fieldtype = "changeQType"
        single_text = "//a[@data-action='SingleTextboxQuestion']"
        multiple_choice = "//a[@data-action='MultipleChoiceQuestion']"
        checkbox = "//a[@data-action='CheckboxQuestion']"
        matrix = "//a[@data-action='MatrixQuestion']"
        comment_box = "//a[@data-action='CommentBoxQuestion']"
        dropdown = "//a[@data-action='DropdownQuestion']"
        star_rating = "//a[@data-action='StarRatingQuestion']"
        multiple_textbox = "//a[@data-action='MultipleTextboxQuestion']"

        add_next_question = "//*[@id='editQuestion']/section[2]/div[3]/div/div/a[1]"

        # Clicker Methods ---------------------------------

        def click_on_title_container(self):
            self.element_click(self.title_container, "xpath")

        def click_on_save_edit_survey_btn(self):
            self.element_click(self.e_survey_save, "xpath")

        def click_on_cancle_edit_survey_btn(self):
            self.element_click(self.e_survey_cancel, "xpath")

        def click_change_fieldtype(self):
            self.element_click(self.change_fieldtype)

        def click_single_text_opt(self):
            self.element_click(self.single_text, "xpath")

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

        # Setter Mehods ----------------------------------

        def set_esurvey_title(self, title):
            self.set_send_keys(title, self.e_survey_title)

        def set_ecategory(self, visible_text):
            self.select_by_visible_text(visible_text, self.e_survey_category)

        def set_question(self, question):
            self.set_send_keys(question, self.question, "xpath")
        # Actions ----------------------------------------------

        def edit_survey_title(self, survey_title, survey_category):
            self.click_on_title_container()
            time.sleep(3)
            self.set_esurvey_title(survey_title)
            self.set_ecategory(survey_category)
            self.click_on_save_edit_survey_btn()

        def add_question(self, question_title):
            self.set_question(question_title)
            self.click_change_fieldtype()
            self.click_single_text_opt()




