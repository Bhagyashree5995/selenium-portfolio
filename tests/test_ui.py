from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_to_saucedemo():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        driver.get("https://www.saucedemo.com")
        wait = WebDriverWait(driver, 10)

        wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        ).send_keys("standard_user")

        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        assert "inventory" in driver.current_url
        print("✅ Login test passed!")

    finally:
        driver.quit()


def test_add_to_cart():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        driver.get("https://www.saucedemo.com")
        wait = WebDriverWait(driver, 10)

        wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        ).send_keys("standard_user")

        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "inventory_item")
            )
        )

        add_button = driver.find_element(
            By.XPATH,
            "(//button[text()='Add to cart'])[1]"
        )
        add_button.click()

        cart_badge = driver.find_element(
            By.CLASS_NAME, "shopping_cart_badge"
        )
        assert cart_badge.text == "1"
        print("✅ Add to cart test passed!")

    finally:
        driver.quit()