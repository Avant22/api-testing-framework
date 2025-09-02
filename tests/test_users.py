import requests
import allure
from utils.schema_validator import validate_schema
from utils.allure_logger import log_request_response

BASE_URL = "https://jsonplaceholder.typicode.com"

user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "username": {"type": "string"},
        "email": {"type": "string"},
    },
    "required": ["id", "name", "username", "email"]
}

@allure.feature("Users API")
@allure.story("Get Users - Positive Case")
def test_get_users():
    with allure.step("Send GET /users request"):
        response = requests.get(f"{BASE_URL}/users")
        log_request_response("Get Users", response)

    with allure.step("Validate response"):
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        for user in data:
            validate_schema(user, user_schema)
