from base.BasePage import BasePage


class Create_Survey_Page(BasePage):

        def __init__(self, driver):
            super().__init__(driver)
            self.driver = driver

        #  Locators
        move_to_survey_page_btn = "//a[@class='create-survey alt btn SL_split']"
        survey_title = "surveyTitle"
        survey_category = "//div[contains(text(),'Survey category')]"
        create_survey_btn = "//button[contains(text(),'CREATE SURVEY')]"
        create_from_scratch = 'scratch'
        mwindow_close = "//div[@class = 'modal-view scratch-modal-view']"
        mwindow_survey_title = "//div/input[@id='surveyTitle']"
        mwindow_survey_category = "//span/div[contains(text(),'Survey category')]"
        mwindow_create_survey_btn = "//div/button[contains(text(),'CREATE SURVEY')]"

        # Clicker Methods ----------------------------------

        def click_move_to_survey_page_btn(self):
            self.element_click(self.move_to_survey_page_btn, "xpath")

        def click_create_from_scratch(self):
            self.element_click(self.create_from_scratch)

        def click_create_survey_btn(self):
            self.element_click(self.create_survey_btn, "xpath")

        def click_create_survey_window_close(self):
            self.element_click(self.mwindow_close, "xpath")

        def click_mwindow_create_survey_btn(self):
            self.element_click(self.mwindow_create_survey_btn, "xpath")

        # Setter Mehods ----------------------------------

        def set_survey_title(self, surveytitle):
            self.set_sendkeys(surveytitle, self.survey_title)

        def set_survey_category(self, surveycategory):
            self.set_dropdown_value(surveycategory, self.survey_category, "xpath")

        def set_mwindow_survey_title(self, mw_survey_title):
            self.set_sendkeys(mw_survey_title, self.mwindow_survey_title, "xpath")

        def set_mwindow_survey_category(self, mw_survey_category):
            self.set_dropdown_value(mw_survey_category, self.mwindow_survey_category, "xpath")

        # Actions Method ----------------------------------

        def survey_from_scratch(self, survey_title, survey_category):
            self.click_move_to_survey_page_btn()
            result = self.is_elementpresent(self.create_from_scratch)
            if result == True:
                self.click_create_from_scratch()
                self.wait_until_element_to_be_clickable(self.mwindow_survey_title, "xpath")
                self.set_mwindow_survey_title(survey_title)
                self.wait_until_element_to_be_clickable(self.mwindow_survey_category, "xpath")
                self.set_mwindow_survey_category(survey_category)
                self.click_mwindow_create_survey_btn()
            else:
                self.click_move_to_survey_page_btn()
                self.wait_until_element_to_be_clickable(self.survey_title)
                self.set_survey_title(survey_title)
                self.wait_until_element_to_be_clickable(self.survey_category, "xpath")
                self.set_survey_category(survey_category)
                self.click_mwindow_create_survey_btn()

        def survey(self, survey_title, survey_category):
            self.click_move_to_survey_page_btn()
            self.wait_until_element_to_be_clickable(self.survey_title)
            self.set_survey_title(survey_title)
            self.wait_until_element_to_be_clickable(self.survey_category, "xpath")
            self.set_survey_category(survey_category)
            self.click_mwindow_create_survey_btn()

        def create_survey(self, survey_title, survey_category):
            self.click_move_to_survey_page_btn()

            try:
                self.survey_from_scratch(survey_title, survey_category)
            except:
                self.survey(survey_title, survey_category)
                pass







