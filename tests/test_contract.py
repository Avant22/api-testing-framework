import requests
import allure
from jsonschema import validate

@allure.feature("Users API")
@allure.story("Contract Test with JSON Schema")
def test_contract_with_users_api(base_url):
    response = requests.get(f"{base_url}/users/1")
    assert response.status_code == 200
    body = response.json()

    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "email": {"type": "string"},
        },
        "required": ["id", "name", "email"]
    }

    validate(instance=body, schema=schema)
