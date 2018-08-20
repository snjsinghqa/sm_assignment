import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Survey():

    driverLocation = '/Users/Documents/PycharmProjects/drivers/chromedriver'
    driver = webdriver.Chrome(driverLocation)
    base_url = "https://www.monkeytest1.com/"
    # base_url = "https://www.surveymonkey.com/"
    ac = ActionChains(driver)
    wait = WebDriverWait(driver, 10)

# ------------------Driver Section-----------------------------------
    def driver_setup(self, driver):
        return driver

    def comman(self, base_url, driver, wait):
        driver.get(base_url)
        home_page=driver.current_url
        print(home_page)
# -----------------------Locator--------------------------------------
        login_link = "//li/a[contains(text(),'LOG IN')]"
        user_name = "username"
        user_password = "password"
        login_button = "//button[contains(text(),'LOG IN')]"
        home_page = "svg_logo"
        move_to_survey_page_btn = "//a[@class='create-survey alt btn SL_split']"

        survey_title = "surveyTitle"
        survey_category = "//div[contains(text(),'Survey category')]"
        create_survey_btn = "//button[contains(text(),'CREATE SURVEY')]"
        create_from_scratch ='scratch'

        mwindow_close = "//div[@class = 'modal-view scratch-modal-view']"
        mwindow_survey_title = "//div/input[@id='surveyTitle']"
        mwindow_survey_category = "//span/div[contains(text(),'Survey category')]"
        mwindow_create_survey_btn = "//div/button[contains(text(),'CREATE SURVEY')]"

        driver.find_element(By.XPATH, login_link).click()
        driver.find_element(By.ID, user_name).send_keys("qa.user")
        driver.find_element(By.ID, user_password).send_keys("Pass_123")
        driver.find_element(By.XPATH, login_button).click()

        home = driver.find_element(By.ID, home_page)
        log_varify = home.is_displayed()
        assert log_varify == True

        driver.find_element(By.XPATH, move_to_survey_page_btn).click()
        try:
            survey_scratch_ele = driver.find_element(By.ID, create_from_scratch)
            survey_scratch_option = survey_scratch_ele.is_displayed()
            if survey_scratch_option == True:
                survey_scratch_ele.click()
                time.sleep(2)
                driver.find_element(By.XPATH, mwindow_survey_title).send_keys("Demo")
                time.sleep(2)
                mw_survey_category_field = driver.find_element(By.XPATH, mwindow_survey_category)
                ac = ActionChains(driver)
                ac.click(mw_survey_category_field).send_keys("Other", Keys.RETURN).perform()
                time.sleep(2)
                driver.find_element(By.XPATH, mwindow_create_survey_btn).click()
        except:
            print("Element not find")
            driver.find_element(By.ID, survey_title).send_keys("Demo")
            time.sleep(3)
            category_field = driver.find_element(By.XPATH, survey_category)
            ac = ActionChains(driver)
            ac.click(category_field).send_keys("Other", Keys.RETURN).perform()
            time.sleep(2)
            driver.find_element(By.XPATH, create_survey_btn).click()
            pass

        # Survey Monkey Design Page
        logo_btn = "//span[@class = 'add-logo-btn wds-button wds-button--sm wds-button--icon-left wds-button--ghost-filled']"
        from_pc = "//a[@tab-target='from-computer']"
        from_lib = "//a[@tab-target='from-library']"
        import_link = "//span[@class = 'qq-upload-button-selector browse-for-file import-link']"
        ques_bank = "//li[@title='Question Bank']"
        builder = "//li[@title='Builder']"
        builder = "//li[@title='Themes']"
        builder = "//li[@title='Logic']"
        builder = "//li[@title='Options']"
        title_container = "//div[@class = 'survey-title-table-wrapper']"
        print(title_container)

        time.sleep(3)

        title_con = wait.until(EC.element_to_be_clickable((By.XPATH, title_container)))
        # title_con = driver.find_element(By.XPATH, title_container)
        # print(title_con)
        title_con.click()
        time.sleep(5)
        e_survey_title = "surveyTitle"
        e_survey_category = "surveyCategory"
        e_survey_save = "//form[@id='surveyTitleForm']/div" \
                        "/a[@class='wds-button wds-button--sm save']"
        e_survey_cancel = "//form[@id='surveyTitleForm']/div" \
                          "/a[@class='wds-button wds-button--sm wds-button--ghost-filled cancel']"

        e_survey_title_field = driver.find_element(By.ID, e_survey_title)
        e_survey_title_field.clear()
        e_survey_title_field.send_keys("My Demo")
        time.sleep(3)
        select_category = Select(driver.find_element(By.ID, e_survey_category))
        select_category.select_by_index(14)
        time.sleep(2)
        driver.find_element(By.XPATH, e_survey_save).click()
        time.sleep(2)

        # Add question
        add_question = "//*[@id='questionTitleWrap']/table/tbody/tr[1]/td[2]/div[1]/span"
        change_fieldtype = "changeQType"
        single_text = "//a[@data-action='SingleTextboxQuestion']"
        add_next_question = "//*[@id='editQuestion']/section[2]/div[3]/div/div/a[1]"
        time.sleep(2)
        driver.find_element(By.XPATH, add_question).send_keys("Enter your email.")
        driver.find_element(By.ID, change_fieldtype).click()
        wait.until(EC.element_to_be_clickable(By.XPATH, single_text))
        driver.find_element(By.XPATH, add_next_question)

        add_q2 = wait.until(EC.element_to_be_clickable(By.XPATH, add_question))
        print(add_q2)

    def close(self,driver):
        driver.quit()

s = Survey()
driver = s.driver_setup(s.driver)
s.comman(s.base_url, driver, s.wait)
s.close(s.driver)
