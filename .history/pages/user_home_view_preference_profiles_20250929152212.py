from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException


class PreferenceProfilesPage:
    def __init__(self, driver):
        self.driver = driver

    def _get_text_safe(self, locator, timeout=10):
        """Fetch element text safely, retrying if stale."""
        for _ in range(3):  # retry max 3 times
            try:
                el = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located(locator)
                )
                return el.text.strip()
            except StaleElementReferenceException:
                print("⚠️ Stale element → retrying...")
        raise TimeoutException(f"❌ Could not fetch text for {locator}")

    def get_username(self):
        return self._get_text_safe(
            ("xpath", "//android.widget.TextView[contains(@text, ',')]")
        )

    def get_age(self):
        return self._get_text_safe(
            ("xpath", "//android.widget.TextView[contains(@text, 'yrs')]")
        )

    def get_location(self):
        return self._get_text_safe(
            ("xpath", "//android.widget.TextView[contains(@text, ',')][last()]")
        )

    def click_next_arrow(self):
        el = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                ("xpath", "//android.widget.TextView[@text='']")
            )
        )
        el.click()
        print("👉 Forward arrow clicked → Next profile")
