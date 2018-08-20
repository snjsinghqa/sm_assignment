from base.BasePage import BasePage


class LoginPage(BasePage):

        def __init__(self, driver):
            super().__init__(driver)
            self.driver = driver

        #  Locators -------------------------------------
        login_link = "//li/a[contains(text(),'LOG IN')]"
        user_name = "username"
        user_password = "password"
        login_button = "//button[contains(text(),'LOG IN')]"
        home_page = "svg_logo"

        # Validate ---------------------------------------
        useraccount_menulink = "userAcctTab_MainMenu"
        invalid_user_error_ele = "//div[@class='error-message']/ul/li[1]"
        blank_username_error_ele = "//input[@id='username']/following-sibling::div"
        blank_password_error_ele = "//input[@id='password']/following-sibling::div"

        # Clicker Methods ----------------------------------

        def click_loginlink(self):
            self.element_click(self.login_link, "xpath")

        def click_loginbutton(self):
            self.element_click(self.login_button, "xpath")

        # Setter Mehods ----------------------------------

        def set_username(self, username):
            self.set_sendkeys(username, self.user_name)

        def set_userpassword(self, password):
            self.set_sendkeys(password, self.user_password)

        # Actions Method ----------------------------------

        def user_login(self, username, password):
            self.click_loginlink()
            self.set_username(username)
            self.set_userpassword(password)
            self.click_loginbutton()

        def verify_login(self):
            result = self.is_elementpresent(self.useraccount_menulink)
            return result

        def verify_loginfail_error(self):
            result = self.is_elementpresent(self.invalid_user_error_ele, 'xpath')
            return result

        def verify_username_error(self):
            result = self.is_elementpresent(self.blank_username_error_ele, 'xpath')
            return result

        def verify_password_error(self):
            result = self.is_elementpresent(self.blank_password_error_ele, 'xpath')
            return result

        def get_url(self):
            url = self.get_current_url()
            return url

        def click_on_url(self, url):
            self.driver.get(url)

        def verify_password_error_msg(self):
            msg = self.get_text(self.blank_password_error_ele, 'xpath')
            return msg

        def verify_username_error_msg(self):
            msg = self.get_text(self.blank_username_error_ele, "xpath")
            msg = str(msg)
            return msg
