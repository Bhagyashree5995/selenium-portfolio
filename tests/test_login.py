from pages.login_page import LoginPage


def test_valid_login(driver):
    login = LoginPage(driver)
    login.enter_username("tomsmith")
    login.enter_password("SuperSecretPassword!")
    login.click_login()
    assert login.is_login_successful()


def test_invalid_login(driver):
    login = LoginPage(driver)
    login.enter_username("wronguser")
    login.enter_password("wrongpassword")
    login.click_login()
    assert login.is_login_failed()