# 📚 E-Vrit Automation Project

Automated tests for the E-Vrit website using **Python**, **Playwright**, and **Pytest**.

---

## 📂 Project Structure

    The project follows a standard structure:

```
.
├── pages/        # Page Object classes (BasePage, LoginPage, BookPage, etc.)
├── tests/        # Test cases (user creation tests and more)
├── utils/        # Utilities (ConfigReader for pytest.ini)
├── .venv/        # Virtual environment
├── allure-results/  # Allure test results (excluded from Git)
├── pytest.ini    # Configuration file for pytest (email vendor, fixed password, etc.)
├── requirements.txt  # Python dependencies
└── README.md
```


---

## ⚙️ How to Run

1. Create a virtual environment:
    ```bash
    python -m venv .venv
    .venv\Scripts\activate  # Windows
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run tests:
    - Run all tests in a specific file:
      ```bash
      pytest tests/login_test.py
      ```
       Headed mode (open browser window):
      ```bash
      pytest tests/login_test.py --headed
      ```
    - Run tests with Allure report generation:
      ```bash
      pytest tests/login_test.py --headed --alluredir=allure-results
      ```

4. Run a specific test:
    ```bash
    pytest tests/login_test.py::test_login_valid_user
    ```

## 📝 Viewing Allure Report

After running your tests with the `--alluredir=allure-results` flag, you can generate and view the test reports in a user-friendly format. Simply run the following command to launch the Allure report:

 **Generate and open Allure report**:
```bash
allure serve allure-results

---

## 📌 Notes

- `pytest.ini` contains configuration values (like email and password).
- Pages are organized using the Page Object Model (POM) design pattern.
- Dependencies are listed in `requirements.txt`.

---

## 🛠 Versions

| Tool          | Version  |
|---------------|----------|
| Python        | 3.11.x   |
| Playwright    | 1.44.x   |
| Pytest        | 8.3.x    |
| Allure-pytest | 2.13.x   |

---