# 🏦 Parabank Automation Framework

A robust **test automation framework** for the [Parabank Dummy Banking Website](https://parabank.parasoft.com/parabank/index.htm) built with **Python**, **Pytest**, **Selenium**, and **Requests**.  
The framework covers **UI Testing, REST API Testing, Database Validation**, and supports **CI/CD integration**.

---

## 🚀 Features
- ✅ **UI Testing** with Selenium & Page Object Model (POM)  
- ✅ **API Testing** with Python `requests` library & Pytest  
- ✅ **Database Integration** for backend validation (SQL queries)  
- ✅ **Test Data Management** using JSON  
- ✅ **Positive & Negative Test Scenarios**  
- ✅ **Custom HTML/Allure Reports**  
- ✅ **CI/CD ready** (Jenkins/GitHub Actions/GitLab CI)  

---
## 📂 Project Structure

ParaBank_Testing/
│
├── Data/                     # Test data files (JSON, CSV, etc.)
│   ├── test_data.json
│   └── config.yaml
│
├── Page_Pom/                  # Page Object Model classes
│   └── login_page.py
│
├── Reports/                   # Test execution reports
│   └── allure_reports/
│
├── Tests/                     # Test cases
│   ├── Positive_Testing/      # Positive test cases
│   │   ├── test_login_positive.py
│   │   └── test_account_positive.py
│   │
│   ├── Negative_Testing/      # Negative test cases
│   │   ├── test_login_negative.py
│   │   └── test_account_negative.py
│   │
│   ├── API/                   # API test cases
│   │   ├── test_get_api.py
│   │   ├── test_post_api.py
│   │   └── __init__.py
│   │
│   └── __init__.py
│
├── api_clients/               # API client utilities
│   ├── get_api.py
│   ├── post_api.py
│   └── __init__.py
│
├── capture_screenshot/        # Screenshots on failure
│   └── screenshot_utils.py
│
├── Utils/                     # Helper utilities
│   ├── logger.py
│   ├── file_reader.py
│   └── __init__.py
│
├── conftest.py                # Pytest fixtures
├── requirements.txt           # Python dependencies
├── main.py                    # Entry point (if needed)
├── README.md                  # Project documentation
└── LICENSE                    # License info
