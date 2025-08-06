
from faker import Faker

faker = Faker("th_TH")

def generate_thai_user(faker: Faker) -> dict:
    """Return a single fake user record as a dictionary for Thai locale."""
    return {
        "name": faker.name(),
        "username": faker.user_name(),
        "email": faker.email(),
        "address": faker.address().replace("\n", ", "),
        "phone": faker.phone_number(),
        "company": faker.company(),
        "job": faker.job(),
        "date_of_birth": faker.date_of_birth(minimum_age=18, maximum_age=90).isoformat(),
    }

user = generate_thai_user(faker)
print(user)
