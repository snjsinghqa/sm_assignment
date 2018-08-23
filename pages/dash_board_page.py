from base.BasePage import BasePage
import time
import utillities.custom_logger as cl
import logging


class DashBoard(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # User Account Locators -------------------------------------

    useraccount_menulink = "userAcctTab_MainMenu"
    my_account_submenu = "//li[@id='dd-my-account']/ul/li/a[contains(text(),'My Account')]"
    library_submenu = "//li[@id='dd-my-account']/ul/li[2]/a[contains(text(),'Library')]"
    contact_submenu = "//li[@id='dd-my-account']/ul/li[3]/a[contains(text(),'Contacts')]"
    signout_submenu = "//div[@class='content-wrapper']//ul[@class='nav-submenu']//li[5]"

    # Survey List-------------------------------------------------

    survey_list = "//div[@class='dw-container survey-list']"
    first_survey = "//ul[@class='survey-items-list']/li[1]"
    edit_options = "//*[@id='row_3']/div/div/div[2]/ul/li[1]/div/ul[2]/div[1]/li[1]/div[2]/a/div[2]"

    # Validate ---------------------------------------

    login_link = "//li/a[contains(text(),'LOG IN')]"

    # Clicker Methods ----------------------------------

    def click_useraccount_menu(self):
        self.element_click(self.useraccount_menulink)

    def click_myaccount_submenu(self):
        self.element_click(self.my_account_submenu, "xpath")

    def click_libraryv_submenu(self):
        self.element_click(self.library_submenu, "xpath")

    def click_contact_submenu(self):
        self.element_click(self.contact_submenu, "xpath")

    def click_signout_submenu(self):
        self.element_click(self.signout_submenu, "xpath")

    def click_edit_option(self):
        self.element_click(self.edit_options, "xpath")

    # Move to Method ----------------------------------

    def move_to_firstsurvey(self):
        self.hover_on_element(self.first_survey, "xpath")

    # Actions Method ----------------------------------

    def signout_account(self):
        self.click_useraccount_menu()
        self.click_signout_submenu()

    def verify_signout(self):
        result = self.is_elementpresent(self.login_link, "xpath")
        return result
