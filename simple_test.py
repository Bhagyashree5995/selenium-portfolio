from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

driver.get("https://example.com")

page_title = driver.title

if "Example Domain" in page_title:
    print("Test passed")
else:
    print("Test failed")

driver.quit()