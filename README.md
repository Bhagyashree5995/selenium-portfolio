# Selenium + Python Test Suite

A small UI and API test suite built with Selenium WebDriver, pytest and the Page Object Model, running in GitHub Actions on every push and pull request.

## What is tested

| Area | File | Covers |
| --- | --- | --- |
| Login (Page Object) | `tests/test_login.py` | Valid and invalid login on the-internet.herokuapp.com, asserting the flash message, not just the URL |
| UI | `tests/test_ui.py` | SauceDemo login and add-to-cart, asserting the cart badge count |
| API | `tests/test_api.py` | GET list, GET single, POST, PUT, DELETE and a 404 case against a mock REST API |
| Combined | `tests/test_combined.py` | An API call followed by a UI journey in one test |

11 tests in total.

## Structure

- `conftest.py` — pytest fixture: headless Chrome, created and closed per test
- `tests/pages/` — page objects (LoginPage: locators, actions, assertions)
- `tests/test_*.py` — the tests
- `.github/workflows/` — GitHub Actions workflow

## Running it locally

```
git clone https://github.com/Bhagyashree5995/selenium-portfolio.git
cd selenium-portfolio
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest -v
```

## CI

The workflow runs the suite on Ubuntu with Python 3.11 on every push and pull request to `main`, using headless Chrome.

## Design notes

- Waiting is handled only by explicit waits (`WebDriverWait`). An implicit wait was removed, because mixing the two makes wait times unpredictable.
- `LoginPage` keeps locators as class constants and asserts on the page's flash message, so a blank or broken page fails the test instead of passing.

## Known limitations

- The API tests run against a mock service that does not persist data, so POST, PUT and DELETE confirm the response contract only, not stored state.
- The SauceDemo tests create their own driver and do not yet use the shared fixture or a page object; moving them is the next planned change.
- Coverage is deliberately small and focused on framework structure rather than full application coverage.