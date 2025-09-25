import requests
import allure

@allure.feature("Users API")
@allure.story("Get User - Negative Case")
def test_user_not_found(base_url, headers):
    response = requests.get(f"{base_url}/users/9999", headers=headers)
    assert response.status_code == 404
