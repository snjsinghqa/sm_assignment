from base.BasePage import BasePage


class SignUpPage(BasePage):

        def __init__(self, driver):
            super().__init__(driver)
            self.driver = driver

        #  Locators
        create_surveylink = "//a[contains(text(),'CREATE SURVEY')]"
        survey_name_field = "surveyTitle"
        survey_category = "//span/div[contains(text(),'Survey category')]"
