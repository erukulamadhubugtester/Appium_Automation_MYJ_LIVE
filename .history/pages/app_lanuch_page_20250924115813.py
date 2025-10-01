from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.locators import LOCATORS


class AppLaunched:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_login_screen(self):
        """Wait until the Login screen is visible after app launch."""
        try:
            print("⏳ Waiting for Login screen to appear...")
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(LOCATORS["login_title"])
            )
            print("✅ Login screen is visible")
            return True
        except TimeoutException:
            print("❌ Login screen not found in time")
            return False

    def is_login_title_displayed(self):
        """Check if login title is displayed."""
        try:
            el = self.driver.find_element(*LOCATORS["login_title"])
            return el.is_displayed()
        except Exception:
            return False
