import requests
import allure
from utils.allure_logger import log_request_response

BASE_URL = "https://jsonplaceholder.typicode.com"

@allure.feature("Users API")
@allure.story("Get User - Negative Case")
def test_user_not_found():
    with allure.step("Send GET /users/9999 request"):
        response = requests.get(f"{BASE_URL}/users/9999")
        log_request_response("Get User Not Found", response)

    with allure.step("Validate response"):
        assert response.status_code == 404
