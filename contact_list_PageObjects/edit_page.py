from selenium.webdriver.common.by import By


class EditContact:

    row_count = (By.CSS_SELECTOR, ".contactTableBodyRow")
    edit_button = (By.CSS_SELECTOR, '#edit-contact')
    first_name = (By.XPATH, "//input[@id='firstName']")
    last_name = (By.XPATH, "//input[@id='lastName']")
    submit_button = (By.ID, "submit")

    def __init__(self, driver):
        self.driver = driver

    def get_contact(self):
        rows = self.driver.find_elements(*EditContact.row_count)
        return rows

    def get_edit(self):
        return self.driver.find_element(*EditContact.edit_button)

    def clear_field(self, field):
        self.driver.execute_script("arguments[0].value = '';", field)

    def get_firstname(self):
        first_name_element = self.driver.find_element(*EditContact.first_name)
        return first_name_element.get_attribute('value')

    def get_lastname(self):
        last_name_element = self.driver.find_element(*EditContact.last_name)
        return last_name_element.get_attribute('value')

    def submit(self):
        return self.driver.find_element(*EditContact.submit_button)














