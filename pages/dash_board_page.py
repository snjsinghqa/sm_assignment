from base.BasePage import BasePage
import time


class DashBoard(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # User Account Locators -------------------------------------

    useraccount_menulink = "userAcctTab_MainMenu"
    my_account_submenu = "//li[@id='dd-my-account']/ul/li/a[contains(text(),'My Account')]"
    library_submenu = "//li[@id='dd-my-account']/ul/li[2]/a[contains(text(),'Library')]"
    contact_submenu = "//li[@id='dd-my-account']/ul/li[3]/a[contains(text(),'Contacts')]"
    signout_submenu = "//*[@id='dd-my-account']/ul/li[5]/a"

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

    # Actions Method ----------------------------------
    def signout_account(self):
        time.sleep(2)
        self.click_useraccount_menu()
        time.sleep(2)
        self.click_signout_submenu()

    def verify_signout(self):
        result = self.is_elementpresent(self.login_link, "xpath")
        return result
