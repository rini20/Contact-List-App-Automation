from faker import Faker
import json

fake = Faker()

dataset = []

for _ in range(6):
    data = {
        'firstName': fake.first_name(),
        'lastName': fake.last_name(),
        'birthdate': fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d'),
        'email': fake.email(),
        'phone': fake.phone_number(),
        'street1': fake.street_address(),
        'street2': fake.secondary_address(),
        'city': fake.city(),
        'stateProvince': fake.state(),
        'postalCode': fake.zipcode(),
        'country': fake.country()
    }
    dataset.append(data)

json_data = json.dumps(dataset, indent=4)

with open("sample_testdata", "w") as file:
    file.write(json_data)
