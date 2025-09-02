import allure
import json

def log_request_response(name, response):
    """
    Attach request and response details to Allure report.

    :param name: Label for the request (e.g., 'Get Users')
    :param response: requests.Response object
    """
    allure.attach(
        f"{response.request.method} {response.request.url}\nHeaders: {response.request.headers}",
        name=f"{name} - Request",
        attachment_type=allure.attachment_type.TEXT
    )

    try:
        # Pretty-print JSON if possible
        body = json.dumps(response.json(), indent=2)
        attachment_type = allure.attachment_type.JSON
    except Exception:
        # Fallback to raw text
        body = response.text
        attachment_type = allure.attachment_type.TEXT

    allure.attach(
        f"Status Code: {response.status_code}\n\n{body}",
        name=f"{name} - Response",
        attachment_type=attachment_type
    )
