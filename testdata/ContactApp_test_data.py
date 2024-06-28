import random

class TestData:
    add_test_data = [
        {
            "firstName": "Richard",
            "lastName": "Ashley",
            "birthdate": "2000-01-23",
            "email": "rmccoy@example.net",
            "phone": "3454443578",
            "street1": "83892 Cantrell Forge Apt. 372",
            "street2": "Suite 770",
            "city": "West Markbury",
            "stateProvince": "North Dakota",
            "postalCode": "89920",
            "country": "Saint Kitts and Nevis"
        },
        {
            "firstName": "Richard",
            "lastName": "Garrison",
            "birthdate": "1933-09-30",
            "email": "jennifer03@example.net",
            "phone": "427-997-4486",
            "street1": "4552 Monica Meadow Suite 692",
            "street2": "Suite 429",
            "city": "Robertsland",
            "stateProvince": "Georgia",
            "postalCode": "58447",
            "country": "Northern Mariana Islands"
        },

        {
            "firstName": "Jeremy",
            "lastName": "Haley",
            "birthdate": "1999-03-20",
            "email": "emilylong@example.com",
            "phone": "(283)423-1940",
            "street1": "2411 Michael Mews Apt. 090",
            "street2": "Apt. 795",
            "city": "Wardborough",
            "stateProvince": "Rhode Island",
            "postalCode": "85340",
            "country": "Jordan"
        },
        {
            "firstName": "Jose",
            "lastName": "Flores",
            "birthdate": "1974-11-27",
            "email": "christine30@example.org",
            "phone": "(273)294-8907",
            "street1": "5004 Amanda Corners Apt. 904",
            "street2": "Apt. 793",
            "city": "Jadeshire",
            "stateProvince": "New Mexico",
            "postalCode": "87403",
            "country": "Reunion"
        },
        {
            "firstName": "Casey",
            "lastName": "Merritt",
            "birthdate": "1968-09-24",
            "email": "brittneybrewer@example.org",
            "phone": "(273)294-8907",
            "street1": "530 Eric Glens",
            "street2": "Suite 845",
            "city": "West Eric",
            "stateProvince": "Idaho",
            "postalCode": "64987",
            "country": "Suriname"
        }
    ]

    @staticmethod
    def get_field_to_edit():
        fields = [

            {"id": "birthdate", "new_value": "1980-01-01"},
            {"id": "email", "new_value": "new.email@example.com"},
            {"id": "phone", "new_value": "1234567890"},
            {"id": "street1", "new_value": "123 New Address St"},
            {"id": "street2", "new_value": "Suite 100"},
            {"id": "city", "new_value": "New City"},
            {"id": "stateProvince", "new_value": "New State"},
            {"id": "postalCode", "new_value": "12345"},
            {"id": "country", "new_value": "New Country"}
        ]
        select_field = random.choice(fields)
        locator = select_field['id']
        new_value = select_field['new_value']
        return locator, new_value
