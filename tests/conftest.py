import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from contact_list_PageObjects.login_page import Login
import os

CONTACT_LIST_URL = 'https://thinking-tester-contact-list.herokuapp.com/'
driver = 'None'
username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    # setup
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        option = webdriver.ChromeOptions()
        option.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=option)
    elif browser_name == 'firefox':
        option = webdriver.FirefoxOptions()
        option.add_argument("--start-maximized")
        driver = webdriver.Firefox(options=option)

    driver.get(CONTACT_LIST_URL)
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield driver
    # tear down
    driver.quit()


@pytest.fixture(scope="class")
def login(setup):
    # setup
    login = Login(setup)
    login.enter_username().send_keys(username)
    login.enter_password().send_keys(password)
    login.submit().click()
    login.wait((By.CSS_SELECTOR, "div.main-content h1"), "Contact List")
    yield
    # tear down
    login.logout().click()
    login.wait((By.CSS_SELECTOR,".main-content p"), "Log In:")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style = "width:340px;height:228px"' \
                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extras = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


