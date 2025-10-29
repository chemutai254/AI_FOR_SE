from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time
import os


# ===========================================================
# Utility: Create and configure a Chrome WebDriver instance
# ===========================================================
def create_driver(headless=True):
    opts = Options()
    # Prefer the newer headless mode where available
    if headless:
        # --headless=new is the newer headless implementation for recent Chrome
        try:
            opts.add_argument("--headless=new")
        except Exception:
            opts.add_argument("--headless")
        opts.add_argument("--disable-gpu")

    # Reduce background network activity and features that can cause extra logs
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-background-networking")
    opts.add_argument("--disable-features=NetworkService,NetworkServiceInProcess")
    opts.add_argument("--disable-sync")
    opts.add_argument("--disable-extensions")
    opts.add_argument("--disable-default-apps")
    opts.add_argument("--disable-component-update")
    opts.add_argument("--no-first-run")
    opts.add_argument("--no-default-browser-check")
    opts.add_argument("--window-size=1200,800")

    # Hide automation infobar and some telemetry
    opts.add_experimental_option("excludeSwitches", ["enable-automation"])
    opts.add_experimental_option("useAutomationExtension", False)

    # Install chromedriver and suppress chromedriver log output by sending it to os.devnull
    chromedriver_path = ChromeDriverManager().install()
    service = Service(chromedriver_path, log_path=os.devnull)

    driver = webdriver.Chrome(service=service, options=opts)
    return driver


# ===========================================================
# Core Function: Perform login and detect success/failure
# ===========================================================
def login_and_check(url, email, password, selectors, success_selector,
                    timeout=10, headless=True):
    """
    Attempts login and returns True if success_selector or dashboard detected.
    Saves screenshot + HTML if login fails.
    selectors: dict with keys 'email', 'password', 'submit' (each is a (By, value) tuple)
    success_selector: (By, value) tuple expected after successful login.
    """
    driver = create_driver(headless=headless)
    try:
        driver.get(url)

        # Wait for and fill email
        email_el = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(selectors['email'])
        )
        email_el.clear()
        email_el.send_keys(email)

        # Wait for and fill password
        pass_el = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(selectors['password'])
        )
        pass_el.clear()
        pass_el.send_keys(password)

        # Click submit
        submit_el = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(selectors['submit'])
        )
        submit_el.click()

        # Wait for login success
        try:
            WebDriverWait(driver, timeout).until(
                EC.any_of(
                    EC.presence_of_element_located(success_selector),
                    EC.url_contains("dashboard"),
                    EC.url_contains("home")
                )
            )
            return True
        except TimeoutException:
            driver.save_screenshot("login_failure.png")
            with open("login_failure.html", "w", encoding="utf-8") as f:
                f.write(driver.page_source)
            print("❌ Login failed — saved login_failure.png & login_failure.html")
            return False

    finally:
        time.sleep(1)
        driver.quit()


# ===========================================================
# CONFIGURATION (edit these for your app)
# ===========================================================
login_url = "https://academy.powerlearnprojectafrica.org/login"

selectors = {
    # update these locators by inspecting the login page
    "email": (By.NAME, "email"),        # often it's By.ID or By.NAME = "email"
    "password": (By.NAME, "password"),
    "submit": (By.CSS_SELECTOR, "button[type='submit']"),
}

# element visible after successful login (adjust based on your site)
success_selector = (By.XPATH, "//a[contains(text(), 'Logout') or contains(text(), 'Dashboard')]")

# ===========================================================
# TEST CREDENTIALS (uses env vars for safety)
# ===========================================================
valid_email = os.getenv("TEST_EMAIL", "example@gmail.com")
valid_pass = os.getenv("TEST_PASS", "Password")
invalid_email = "fake_email@example.com"
invalid_pass = "wrong_password"


# ===========================================================
# RUN TESTS
# ===========================================================
if __name__ == "__main__":
    print("🔍 Testing with VALID credentials...")
    valid_result = login_and_check(
        login_url, valid_email, valid_pass,
        selectors, success_selector, headless=True
    )

    print("🔍 Testing with INVALID credentials...")
    invalid_result = login_and_check(
        login_url, invalid_email, invalid_pass,
        selectors, success_selector, headless=True
    )

    print("\n========= RESULTS =========")
    print(f"✅ Valid credentials test: {'PASS' if valid_result else 'FAIL'}")
    print(f"🚫 Invalid credentials test: {'PASS' if not invalid_result else 'UNEXPECTED PASS'}")
