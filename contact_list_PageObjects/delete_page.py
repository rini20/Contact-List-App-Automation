from selenium.webdriver.common.by import By


class DeleteContact:

    row_count = (By.CSS_SELECTOR, ".contactTableBodyRow")
    delete_button = (By.CSS_SELECTOR, "#delete")

    def __init__(self, driver):
        self.driver = driver

    def get_contact(self):
        rows = self.driver.find_elements(*DeleteContact.row_count)
        return rows

    def get_delete(self):
        return self.driver.find_element(*DeleteContact.delete_button)

    def switch_to_alert(self):
        alert = self.driver.switch_to.alert
        return alert





