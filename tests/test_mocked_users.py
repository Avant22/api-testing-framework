import json
import requests
import responses
import allure
from utils.allure_logger import log_request_response

@allure.feature("Users API - Mocked")
@allure.story("Get Users (Stubbed Response)")
@responses.activate
def test_mocked_get_users():
    fake_users = [
        {"id": 1, "name": "Mock User", "username": "mockuser", "email": "mock@example.com"}
    ]

    responses.add(
        method=responses.GET,
        url="https://jsonplaceholder.typicode.com/users",
        json=fake_users,
        status=200
    )

    response = requests.get("https://jsonplaceholder.typicode.com/users")
    log_request_response("Mocked Get Users", response)
    assert response.status_code == 200
    data = response.json()
    assert data == fake_users

@allure.feature("Users API - Mocked")
@allure.story("User Not Found (Stubbed 404)")
@responses.activate
def test_mocked_user_not_found():
    responses.add(
        method=responses.GET,
        url="https://jsonplaceholder.typicode.com/users/9999",
        json={"error": "User not found"},
        status=404
    )

    response = requests.get("https://jsonplaceholder.typicode.com/users/9999")
    log_request_response("Mocked User Not Found", response)
    assert response.status_code == 404
    assert response.json()["error"] == "User not found"
