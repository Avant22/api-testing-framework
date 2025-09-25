from faker import Faker
fake = Faker()

def fake_user():
    return {
        "id": fake.random_int(min=1000, max=9999),
        "name": fake.name(),
        "email": fake.email()
    }
