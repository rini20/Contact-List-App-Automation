from selenium.webdriver.common.by import By
from utilities.base_class import BaseClass
from contact_list_PageObjects.delete_page import DeleteContact
import random


class TestDelete(BaseClass):

    def test_delete(self):

        # select a row to delete
        log = self.get_logs()
        delete_contact = DeleteContact(self.driver)
        contact_rows = delete_contact.get_contact()
        initial_row_count = len(contact_rows)
        contact = random.choice(contact_rows)
        contact.click()

        # verify the delete contact button is displayed and click delete

        self.wait_for_element_visibility(delete_contact.delete_button)
        delete_contact.get_delete().click()

        # switch to confirmation pop-up and confirm delete

        alert = delete_contact.switch_to_alert()
        alert_text = alert.text
        assert 'delete this contact' in alert_text
        alert.accept()

        # Verify the row count is decreased by 1

        self.wait_for_text_presence((By.CSS_SELECTOR, ".main-content h1"),"Contact List")
        final_row_count = len(delete_contact.get_contact())
        assert final_row_count == initial_row_count - 1
        log.info(f"Initial row count: {initial_row_count} Final row count: {final_row_count} ")

