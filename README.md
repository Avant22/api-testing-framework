![Python](https://img.shields.io/badge/python-3.11-blue?logo=python)
![Pytest](https://img.shields.io/badge/pytest-framework-green?logo=pytest)
![Allure](https://img.shields.io/badge/reporting-allure-orange)
![Locust](https://img.shields.io/badge/load--testing-locust-brightgreen)
![CI/CD](https://github.com/Avant22/api-testing-framework/actions/workflows/tests.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

API Testing Framework

A **professional-grade API Testing Framework** built with **Python, Pytest, Requests, Allure, Locust, and GitHub Actions**.  
It demonstrates **end-to-end QA skills**: manual strategy, automated functional tests, contract validation, performance benchmarking, and load testing — all wrapped with CI/CD and reporting.

---

## ✨ Features
- **Test Types**
  - ✅ Positive & Negative API tests
  - ✅ Data-driven testing with Faker
  - ✅ Contract testing with Pact
  - ✅ Performance benchmarking (pytest-benchmark)
  - ✅ Mocked API tests
  - ✅ Load testing with Locust
  - ✅ AI-generated tests (OpenAI integration)

- **Automation & CI/CD**
  - ✅ GitHub Actions with Allure reporting
  - ✅ Slack & Email notifications
  - ✅ GitHub Pages deployment for reports
  - ✅ Dockerized test runs
  - ✅ Nightly scheduled test suite

---

## 📊 Allure Report
👉 [View Live Report](https://avant22.github.io/api-testing-framework/)  

Example Screenshot:  
![Allure Report Screenshot](assets/images/allure dashboard.png)


---

## ⚙️ Tech Stack
| Tool            | Purpose |
|-----------------|------------------------------------------------|
| **Python 3.11** | Base language |
| **Pytest**      | Test runner & assertions |
| **Requests**    | API calls |
| **Allure**      | Rich test reports |
| **Locust**      | Load testing |
| **Pact**        | Contract testing |
| **Faker**       | Random data generation |
| **GitHub Actions** | CI/CD pipeline |
| **Docker**      | Containerized test runs |

---

## 📂 Project Structure
api-testing-framework/
│── tests/ # API test cases
│ ├── test_users.py # Positive tests
│ ├── test_negative.py # Negative tests
│ ├── test_data_driven.py # Faker tests
│ ├── test_contract.py # Pact contract tests
│ ├── test_mocked_users.py# Mocked API tests
│ └── test_performance.py # Benchmark tests
│
│── utils/ # Helpers (fixtures, AI test generator)
│── locust/ # Load testing scripts
│── reports/ # Allure + Locust reports
│── docs/ # Test strategy + regression docs
│── .github/workflows/ # CI/CD pipelines
│── requirements.txt
│── pytest.ini
│── Dockerfile
│── README.md

yaml
Copy code

---

## 🚀 Run Locally
```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests with Allure results
pytest --alluredir=reports

# Serve the report locally
allure serve reports
🌐 CI/CD Pipeline
On push/PR → GitHub Actions runs full test suite

Allure report is deployed to GitHub Pages

Notifications sent to Slack + Email

Nightly scheduled run executes at 00:00 UTC

🧪 Test Strategy
See full docs:

Test Strategy

Regression Plan

📸 Portfolio Value
This project demonstrates:

Manual QA planning + Automated QA execution

CI/CD + DevOps awareness

Scalable test design (data-driven, mocked, contract, performance)

Professional reporting (Allure, Locust, Slack/Email, GitHub Pages)