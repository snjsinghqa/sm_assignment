from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver_location = '/Users/Documents/PycharmProjects/drivers/chromedriver'
driver = webdriver.Chrome(driver_location)
driver.maximize_window()
driver.get("https://www.google.com/")

c_window = driver.current_window_handle
time.sleep(5)
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'n')
# You can use (Keys.CONTROL + 't') on other OSs

# Load a page
driver.get('http://stackoverflow.com/')
# Make the tests...
time.sleep(5)
# close the tab
driver.switch_to_window(c_window)
# (Keys.CONTROL + 'w') on other OSs.
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')


driver.close()




