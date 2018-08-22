from base.webdriver_page import SeleniumDriver


class BasePage(SeleniumDriver):

    def __init__(self, driver):
        self.driver = driver

