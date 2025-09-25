import os
import pytest

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")

@pytest.fixture(scope="session")
def headers():
    api_key = os.getenv("API_KEY", None)
    hdrs = {"Content-Type": "application/json"}
    if api_key:
        hdrs["Authorization"] = f"Bearer {api_key}"
    return hdrs
