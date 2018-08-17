from selenium.webdriver.common.by import By
from traceback import print_stack
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import *


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_bytype(self, locator_type):
        locatortype = locator_type.lower()
        if locatortype == "id":
            return By.ID
        elif locatortype == "name":
            return By.NAME
        elif locatortype == "xpath":
            return By.XPATH
        elif locatortype == "css":
            return By.CSS_SELECTOR
        elif locatortype == "classname":
            return By.CLASS_NAME
        elif locatortype == "linktext":
            return By.LINK_TEXT
        else:
            print("Locator type " + locatortype + " not correct/supported")
        return False

    def get_element(self, locator, locator_type = "id"):
        element = None
        try:
            locatortype = locator_type.lower()
            by_type = self.get_bytype(locatortype)
            element = self.driver.find_element(by_type, locator)
            print("Element Found")
        except:
            print("Element not found")
        return element

    def element_click(self, locator, locator_type = "id"):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            print("Clicked on element with locator: " + locator + " locatorType: " + locator_type)
        except:
            print("Cannot click on the element with locator: " + locator + " locatorType: " + locator_type)
            print_stack()

    def set_sendkeys(self, data, locator, locator_type = "id"):
        try:
            element = self.get_element(locator, locator_type)
            element.clear()
            element.send_keys(data)
            print("Send data on element with locator: " + locator + " locatorType: " + locator_type)
        except:
            print("Cannot send data on the element with locator: " + locator + " locatorType: " + locator_type)

    def get_title(self):
        return self.driver.title

    def is_elementpresent(self, locator, locator_type = "id"):
        try:
            element = self.get_element(locator, locator_type)
            if element is not None:
                return True
            else:
                return False
        except:
            print("Element not found")
            return False

    def is_elements_PresenceCheck(self, locator, locator_type = "id"):
        try:
            element_list = self.get_element(locator_type, locator)
            if len(element_list) > 0:
                return True
            else:
                return False
        except:
            return False

    def get_current_url(self):
        url = self.driver.current_url
        return url

    def get_text(self, locator, locator_type = 'id'):
        element = self.get_element(locator, locator_type)
        msg = element.text()
        msg = str(msg)
        return msg
