
from faker import Faker

faker = Faker("th_TH")

def generate_thai_user(faker: Faker) -> dict:
    """Return a single fake user record as a dictionary for Thai locale."""
    return {
        "name": faker.name(),
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "username": faker.user_name(),
        "email": faker.email(),
        "address": faker.address().replace("\n", ", "),
        "street": faker.street_name(),
        "tambon": faker.tambon(),
        "amphoe": faker.amphoe(),
        "province": faker.province(),
        "country": faker.country(),
        "phone": faker.phone_number(),
        "company": faker.company(),
        "job": faker.job(),
        "vat_id": faker.vat_id(),
        "license_plate": faker.license_plate(),
        "date_of_birth": faker.date_of_birth(minimum_age=18, maximum_age=90).isoformat(),
    }

user = generate_thai_user(faker)
print(user)
