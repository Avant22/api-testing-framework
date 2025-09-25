import requests
import allure
from faker import Faker

fake = Faker()

@allure.feature("Users API")
@allure.story("Data Driven Testing with Faker")
def test_create_fake_user(base_url, headers):
    payload = {
        "name": fake.name(),
        "email": fake.email()
    }
    response = requests.post(f"{base_url}/users", json=payload, headers=headers)
    assert response.status_code in [200, 201]
    body = response.json()
    assert body["name"] == payload["name"]
    assert body["email"] == payload["email"]
