import pytest

@pytest.fixture()
def setUp():
    print("Method level SetUp call...")

    yield
    print("Method level Teardown call...")

@pytest.fixture(scope="class")
def oneTimeSetup(browser,osType):
    print("Module level one Time SetUp..!!!!!")

    if browser=='chrome':
        print("SetUp Chrome driver here ..")
    elif browser=='firefox':
        print("SetUp Firefox driver here..")
    else:
        print("setup default chrome driver here ..")

    yield
    print("Module level one Time Teardown..!!!!!")

def pytest_addoption(parser):
    parser.addoption("--browser", help="This is a Browser name in which you need to run your test cases")
    parser.addoption("--osType", help="This is a Operating System Type in which you need to run your test cases")

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope='session')
def osType(request):
    return request.config.getoption("--osType")

