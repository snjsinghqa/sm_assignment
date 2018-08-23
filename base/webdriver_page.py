from selenium import webdriver
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import utillities.custom_logger as cl
import logging


class WebDriver():

    log = cl.customLogger(logging.DEBUG)

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
            self.log.info("Locator type " + locatortype + " not correct/supported")
        return False

    def get_element(self, locator, locator_type = "id"):
        element = None
        try:
            locatortype = locator_type.lower()
            by_type = self.get_bytype(locatortype)
            element = self.driver.find_element(by_type, locator)
            self.log.info("Element Found")
        except:
            self.log.info("Element not found")
        return element

    def element_click(self, locator, locator_type = "id"):
        try:
            element = self.wait_until_element_to_be_clickable(locator, locator_type)
            # element = self.get_element(locator, locator_type)
            element.click()
            self.log.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locator_type)
        except:
            self.log.info("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locator_type)
            print_stack()

    def set_send_keys(self, data, locator, locator_type = "id"):
        try:
            element = self.wait_until_element_located(locator, locator_type)
            # element = self.get_element(locator, locator_type)
            element.clear()
            element.send_keys(data)
            self.log.info("Send data on element with locator: " + locator +
                          " locatorType: " + locator_type)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                          " locatorType: " + locator_type)

    def get_title(self):
        return self.driver.title

    def is_elementpresent(self, locator, locator_type = "id"):
        try:
            element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element is present with locator: " + locator +
                              " locatorType: " + locator_type)
                return True
            else:
                self.log.info("Element is not present with locator: " + locator +
                              " locatorType: " + locator_type)
                return False
        except:
            self.log.info("Element not found")
            return False

    def is_elements_presence_check(self, locator, locator_type = "id"):
        try:
            element_list = self.get_element(locator_type, locator)
            if len(element_list) > 0:
                self.log.info("Elements are present with locator: " + locator +
                              " locatorType: " + locator_type)
                return True
            else:
                self.log.info("Elements are not present with locator: " + locator +
                              " locatorType: " + locator_type)
                return False
        except:
            return False

    def get_current_url(self):
        url = self.driver.current_url
        return url

    def get_text(self, locator, locator_type = 'id'):
        try:
            element = self.get_element(locator, locator_type)
            msg = element.text()
            msg = str(msg)
            self.log.info("Element is present with locator: " + locator +
                          " locatorType: " + locator_type)
            return msg
        except:
            self.log.info("Element is not present with locator: " + locator +
                          " locatorType: " + locator_type)

    def wait_until_element_to_be_clickable(self, locator, locator_type = 'id'):
        try:
            wait = WebDriverWait(self.driver, 30)
            element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
            self.log.info("Element is present with locator: " + locator +
                          " locatorType: " + locator_type)
            return element
        except:
            self.log.info("Element is not present with locator: " + locator +
                          " locatorType: " + locator_type)

    def wait_until_element_located(self, locator, locator_type = 'id'):
        try:
            wait = WebDriverWait(self.driver, 30)
            element = wait.until(EC.presence_of_element_located((locator_type, locator)))
            self.log.info("Element is present with locator: " + locator +
                          " locatorType: " + locator_type)
            return element
        except:
            self.log.info("Element is not present with locator: " + locator +
                          " locatorType: " + locator_type)

    def set_dropdown_value(self,input_data, locator, locator_type = 'id'):
        try:
            ac = ActionChains(self.driver)
            ac.click(self.get_element(locator, locator_type)).send_keys(input_data, Keys.RETURN).perform()
            self.log.info("Element is present with locator: " + locator +
                          " locatorType: " + locator_type)
        except:
            self.log.info("Element is not present with locator: " + locator +
                          " locatorType: " + locator_type)

    def select_value_by_index(self, index_number, locator, locator_type = 'id'):
        try:
            element = Select(self.get_element(locator, locator_type))
            element.select_by_index(index_number)
            self.log.info("Element is present with locator: " + locator +
                          " locatorType: " + locator_type)
        except:
            self.log.info("Element is not present with locator: " + locator +
                          " locatorType: " + locator_type)

    def select_by_value(self, value_name, locator, locator_type = 'id'):
        try:
            element = Select(self.get_element(locator, locator_type))
            element.select_by_value(value_name)
            self.log.info("Element is present with locator: " + locator +
                          " locatorType: " + locator_type)
        except:
            self.log.info("Element is not present with locator: " + locator +
                          " locatorType: " + locator_type)

    def select_by_visible_text(self, visible_text, locator, locator_type = 'id'):
        try:
            element = Select(self.wait_until_element_located(locator, locator_type))
            element.select_by_visible_text(visible_text)
            self.log.info("Element is present with locator: " + locator +
                          " locatorType: " + locator_type)
        except:
            self.log.info("Element is not present with locator: " + locator +
                          " locatorType: " + locator_type)

    def set_inputvalue_by_action(self, input_data, locator, locator_type = 'id'):
        try:
            ac = ActionChains(self.driver)
            ac.move_to_element(self.wait_until_element_located(locator, locator_type)).send_keys(input_data)
            self.log.info("Element is present with locator: " + locator +
                          " locatorType: " + locator_type)
        except:
            self.log.info("Element is not present with locator: " + locator +
                          " locatorType: " + locator_type)

    def hover_on_element(self, locator, locator_type = 'id'):
        try:
            ac = ActionChains(self.driver)
            ac.move_to_element(self.wait_until_element_located(locator, locator_type)).perform()
            self.log.info("Element is present with locator: " + locator +
                          " locatorType: " + locator_type)
        except:
            self.log.info("Element is not present with locator: " + locator +
                          " locatorType: " + locator_type)

    def set_multi_options(self, input_data, locator, locator_type = 'id'):
        try:
            ac = ActionChains(self.driver)
            ac.click(self.get_element(locator, locator_type)).send_keys(input_data, Keys.TAB).perform()
            self.log.info("Element is present with locator: " + locator +
                      " locatorType: " + locator_type)
        except:
            self.log.info("Element is present with locator: " + locator +
                          " locatorType: " + locator_type)
