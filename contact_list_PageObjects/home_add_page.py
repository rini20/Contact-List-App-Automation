from selenium.webdriver.common.by import By


class AddContact:

    add_button = (By.CSS_SELECTOR, "#add-contact")
    firstName = (By.CSS_SELECTOR, "#firstName")
    lastName = (By.XPATH, "//input[@id='lastName']")
    birthdate = (By.ID, "birthdate")
    email = (By.ID, "email")
    phone = (By.CSS_SELECTOR, "#phone")
    street1 = (By.ID, "street1")
    street2 = (By.ID, "street2")
    city = (By.XPATH, "//input[@id='city']")
    stateProvince = (By.ID, "stateProvince")
    postalCode = (By.ID, "postalCode")
    country = (By.ID, "country")
    submit_button = (By.CSS_SELECTOR, "button#submit")
    row_count = (By.CSS_SELECTOR, ".contactTableBodyRow")

    def __init__(self, driver):
        self.driver = driver

    def count_rows(self):
        return len(self.driver.find_elements(*AddContact.row_count))

    def click_add(self):
        return self.driver.find_element(*AddContact.add_button)

    def enter_firstname(self):
        return self.driver.find_element(*AddContact.firstName)

    def enter_lastname(self):
        return self.driver.find_element(*AddContact.lastName)

    def enter_birthdate(self):
        return self.driver.find_element(*AddContact.birthdate)

    def enter_email(self):
        return self.driver.find_element(*AddContact.email)

    def enter_phone(self):
        return self.driver.find_element(*AddContact.phone)

    def enter_street1(self):
        return self.driver.find_element(*AddContact.street1)

    def enter_street2(self):
        return self.driver.find_element(*AddContact.street2)

    def enter_city(self):
        return self.driver.find_element(*AddContact.city)

    def enter_state_province(self):
        return self.driver.find_element(*AddContact.stateProvince)

    def enter_postalcode(self):
        return self.driver.find_element(*AddContact.postalCode)

    def enter_country(self):
        return self.driver.find_element(*AddContact.country)

    def submit(self):
        return self.driver.find_element(*AddContact.submit_button)

    def refresh(self):
        self.driver.refresh()





























        























