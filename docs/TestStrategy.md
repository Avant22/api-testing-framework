# 📘 Test Strategy

## 1. Objectives
- Validate the stability and correctness of the Users API.
- Ensure schema compliance and prevent contract-breaking changes.
- Measure performance and scalability under load.
- Provide actionable test reporting for stakeholders.

## 2. Scope
- Functional API testing (positive, negative, schema).
- Regression testing for critical endpoints.
- Performance and load testing with Locust and pytest-benchmark.
- Mocking/stubbing for unavailable endpoints.
- CI/CD integration with reports and notifications.

## 3. Tools
- Pytest (functional testing)
- Requests (API calls)
- Allure (reporting)
- Locust (load testing)
- pytest-benchmark (performance testing)
- Responses (mocking)
- GitHub Actions (CI/CD)

## 4. Test Levels
- Unit-level: Schema validation
- API-level: Functional tests
- Integration: Mocked endpoints
- Non-functional: Performance & load
- Regression: Automated via CI/CD

## 5. Risks & Mitigation
- API downtime → use mocks/stubs.
- Slow test execution → parallelization.
- Secret leakage → `.env` and GitHub Secrets.

## 6. Exit Criteria
- 95% of planned test cases executed.
- All critical tests pass.
- Reports reviewed and signed off by QA lead.
