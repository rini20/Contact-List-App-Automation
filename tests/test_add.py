import pytest
from selenium.webdriver.common.by import By
from testdata.ContactApp_test_data import TestData
from utilities.base_class import BaseClass
from contact_list_PageObjects.home_add_page import AddContact


class TestAdd(BaseClass):

    def test_add_contact(self, get_data):

        # count rows before adding contacts
        log = self.get_logs()
        add_contact = AddContact(self.driver)
        initial_row_count = add_contact.count_rows()
        print(initial_row_count)

        # wait for the form to be displayed after clicking of add button

        add_contact.click_add().click()
        self.wait_for_text_presence((By.TAG_NAME, 'h1'), "Add Contact")

        # fill the form for add contact

        add_contact.enter_firstname().send_keys(get_data["firstName"])
        add_contact.enter_lastname().send_keys(get_data["lastName"])
        add_contact.enter_birthdate().send_keys(get_data["birthdate"])
        add_contact.enter_email().send_keys(get_data["email"])
        add_contact.enter_phone().send_keys(get_data["phone"])
        add_contact.enter_street1().send_keys(get_data["street1"])
        add_contact.enter_street2().send_keys(get_data["street2"])
        add_contact.enter_city().send_keys(get_data["city"])
        add_contact.enter_state_province().send_keys(get_data["stateProvince"])
        add_contact.enter_postalcode().send_keys(get_data["postalCode"])
        add_contact.enter_country().send_keys(get_data["country"])
        add_contact.submit().click()

        # wait for the homepage to be displayed and rows to be counted

        self.wait_for_text_presence((By.TAG_NAME, "h1"), "Contact List")
        add_contact.refresh()
        self.wait_for_element_visibility((By.TAG_NAME, "tr"))

        # assert row for new contact is added to the contacts table

        final_row_count = add_contact.count_rows()
        print(final_row_count)
        assert final_row_count == initial_row_count + 1
        log.info(f"Final row count {final_row_count} is equal to {initial_row_count + 1}")

    @pytest.fixture(params=TestData.add_test_data)
    def get_data(self, request):
        return request.param

