import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://reqres.in/api"


def test_api_then_ui():
    # ---- PART 1: API TEST ----
    print("\n🔌 Starting API check...")

    response = requests.get(f"{BASE_URL}/users/2")
    assert response.status_code == 200

    user_data = response.json()["data"]
    user_email = user_data["email"]
    assert "@" in user_email

    print(f"✅ API returned user: {user_email}")

    # ---- PART 2: UI TEST ----
    print("\n🌐 Starting UI test...")

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

        print("✅ Combined test passed! API + UI both working!")

    finally:
        driver.quit()