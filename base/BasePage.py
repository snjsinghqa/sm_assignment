from base.webdriver_page import WebDriver


class BasePage(WebDriver):

    def __init__(self, driver):
        self.driver = driver

