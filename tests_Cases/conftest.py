import pytest
from selenium import webdriver
from source.data.url_config import active_url


@pytest.fixture()
def setup():
    print("Method level setUp...")
    yield
    print("Method level TearDown...")


@pytest.fixture(scope='class')
def one_time_setup(browser, request, base_url=active_url):
    print("One time class level setup..")

    if browser == 'chrome':
        driver_location = '/Users/Documents/PycharmProjects/drivers/chromedriver'
        driver = webdriver.Chrome(driver_location)
        driver.maximize_window()
    else:
        driver_location = '/Users/Documents/PycharmProjects/drivers/chromedriver'
        driver = webdriver.Chrome(driver_location)
        driver.maximize_window()
    driver.get(base_url)

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    print("One time class level TearDown")
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", help="This is a Browser name in which you need to run your test cases")
    parser.addoption("--osType", help="This is a Operating System Type in which you need to run your test cases")


@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")
