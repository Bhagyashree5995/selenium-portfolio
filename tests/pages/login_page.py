from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH = (By.ID, "flash")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.driver.get(self.URL)

    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME)).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD)).send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def flash_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.FLASH)).text

    def is_login_successful(self):
        self.wait.until(EC.url_contains("/secure"))
        return "You logged into a secure area!" in self.flash_message()

    def is_login_failed(self):
        message = self.flash_message()
        return "Your username is invalid!" in message or "Your password is invalid!" in message
