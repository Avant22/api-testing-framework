import allure
import json

def log_request_response(name, response):
    with allure.step(f"{name} - Request"):
        allure.attach(
            f"{response.request.method} {response.request.url}\nHeaders: {response.request.headers}\nBody: {response.request.body}",
            name="Request",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step(f"{name} - Response"):
        try:
            body = json.dumps(response.json(), indent=2)
        except Exception:
            body = response.text
        allure.attach(
            f"Status: {response.status_code}\nHeaders: {response.headers}\nBody:\n{body}",
            name="Response",
            attachment_type=allure.attachment_type.JSON
        )
