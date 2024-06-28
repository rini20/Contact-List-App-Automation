import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import inspect



@pytest.mark.usefixtures("setup", "login")
class BaseClass:

    def wait_for_element_visibility(self, locator):
        wait = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))
        return wait

    def wait_for_text_presence(self, locator, text):
        wait = WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(locator, text))
        return wait

    def wait_for_element_clickable(self, locator):
        wait = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        return wait

    def get_logs(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        filehandler = logging.FileHandler("logs_and_report\\logfile.log")
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s ")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)

        logger.setLevel(logging.INFO)
        return logger


