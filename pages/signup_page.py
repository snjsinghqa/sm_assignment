from base.BasePage import BasePage
import utillities.custom_logger as cl
import logging


class SignUpPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #  Locators
    signup_link = "//a[contains(text(),'SIGN UP')]"
    user_name = "username"
    user_password = "password"
    user_email = "email"
    user_firstname = "first_name"
    user_lastname = "last_name"
    createaccount_button = "//button[contains(text(),'CREATE ACCOUNT')]"

    # Clicker Methods ----------------------------------
    def click_signup_link(self):
        self.element_click(self.signup_link, "xpath")

    def click_createaccount(self):
        self.element_click(self.createaccount_button, "xpath")

    # Setter Mehods ----------------------------------
    def set_username(self, username):
        self.set_send_keys(username, self.user_name)

    def set_userpassword(self, password):
        self.set_send_keys(password, self.user_password)

    def set_useremail(self, email):
        self.set_send_keys(email, self.user_email)

    def set_userfirst_name(self, fname):
        self.set_send_keys(fname, self.user_firstname)

    def set_userlast_name(self, lname):
        self.set_send_keys(lname, self.user_lastname)

    # Actions Method ----------------------------------
    def user_signup(self, username, password, email, fname, lname):
        self.click_signup_link()
        self.set_username(username)
        self.set_userpassword(password)
        self.set_useremail(email)
        self.set_userfirst_name(fname)
        self.set_userlast_name(lname)
        self.click_createaccount()
