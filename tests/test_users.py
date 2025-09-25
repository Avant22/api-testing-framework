import requests
import allure

@allure.feature("Users API")
@allure.story("Get Users - Positive Case")
def test_get_users(base_url, headers):
    response = requests.get(f"{base_url}/users", headers=headers)
    assert response.status_code == 200
    users = response.json()
    assert isinstance(users, list)
    assert "id" in users[0]
    assert "name" in users[0]
