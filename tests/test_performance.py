import requests
import pytest
import allure
import time

@pytest.mark.performance
@allure.feature("Users API")
@allure.story("Performance Test")
def test_get_users_performance(base_url):
    start = time.time()
    response = requests.get(f"{base_url}/users")
    elapsed = time.time() - start

    assert response.status_code == 200
    assert elapsed < 1.0  # must respond under 1 second
