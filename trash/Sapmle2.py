from selenium import webdriver
from selenium.webdriver.common.by import By


class Sample():

    driverLocation = '/Users/Documents/PycharmProjects/drivers/chromedriver'
    driver = webdriver.Chrome(driverLocation)
    base_url = "https://www.monkeytest1.com/"

# ------------------Driver Section-----------------------------------
    def driver_setup(self, driver):
        return driver

    def comman(self, base_url, driver):
        driver.get(base_url)
        home_page=driver.current_url
        print(home_page)
# -----------------------Locator--------------------------------------
        login_link = "//li/a[contains(text(),'LOG IN')]"
        user_name = "username"
        user_password = "password"
        login_button = "//button[contains(text(),'LOG IN')]"
        home_page = "svg_logo"



        driver.find_element(By.XPATH,login_link).click()
        driver.find_element(By.ID, user_name).send_keys("qa.user")
        driver.find_element(By.ID,user_password).send_keys("Pass_123")
        ele = driver.find_element(By.XPATH, "//input[@id='username']/following-sibling::div")
        ele.get_attribute('text')
        print(ele.get_attribute('text'))
        if ele.text() is not None:
            print(ele.text())
        else:
            print("Unable to get text >>>>>>>>>>>>")
        return ele.text()

    def close(self,driver):
        driver.quit()

s = Sample()
driver = s.driver_setup(s.driver)
s.comman(s.base_url, driver)
s.close(s.driver)
