from selenium.webdriver.common.by import By
from utilities.base_class import BaseClass
from contact_list_PageObjects.edit_page import EditContact
from testdata.ContactApp_test_data import TestData
from time import sleep
import random


class TestEdit(BaseClass):

    def test_edit_contact(self):

        # select contact to edit
        log = self.get_logs()
        edit_contact = EditContact(self.driver)
        contact_rows = edit_contact.get_contact()
        contact = random.choice(contact_rows)
        contact.click()

        # click on edit contact button
        self.wait_for_element_visibility((By.CSS_SELECTOR, '#edit-contact'))
        edit_contact.get_edit().click()

        # update random field for the selected contact

        locator, new_value = TestData.get_field_to_edit()
        print(locator, new_value)
        update_field = self.wait_for_element_visibility((By.ID, locator))
        # update_field.click()
        sleep(2)
        edit_contact.clear_field(update_field)
        update_field.send_keys(new_value)
        update_field_value = update_field.get_attribute('value')
        print(update_field_value)

        # Check if mandatory fields firstname and lastname are not empty

        first_name = edit_contact.get_firstname()
        last_name = edit_contact.get_lastname()
        if first_name and last_name:
            edit_contact.submit().click()
        else:
            print("Form submission aborted due to missing values.")

        # Verify that the field is successfully updated with the new value.

        self.wait_for_text_presence((By.TAG_NAME, "h1"), 'Contact Details')
        verify_update = self.wait_for_element_visibility((By.CSS_SELECTOR, f"span#{locator}"))
        print(verify_update.text)
        assert verify_update.text == new_value
        log.info(f"Validate the field {locator} value is {new_value} for {first_name} {last_name}")







