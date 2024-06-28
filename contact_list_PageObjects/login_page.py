from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# login


class Login:
    username = (By.ID, "email")
    password = (By.XPATH, "//input[@id='password']")
    submit_button = (By.CSS_SELECTOR, "#submit")
    logout_button = (By.ID, "logout")
    login_page = (By.CSS_SELECTOR, ".main-content p")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self):
        return self.driver.find_element(*Login.username)

    def enter_password(self):
        return self.driver.find_element(*Login.password)

    def submit(self):
        return self.driver.find_element(*Login.submit_button)

    def wait(self, locator, text):
        return WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(locator, text))

    def logout(self):
        return self.driver.find_element(*Login.logout_button)


