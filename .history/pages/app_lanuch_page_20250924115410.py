from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import LOCATORS


class App_lanuched:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_app_title(self):
        """Wait until the splash/title is visible (Make Your Jodi)."""
        try:
            print("⏳ Waiting for app title 'Make Your Jodi'...")
            el = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(LOCATORS["make_your_jodi_btn"])
            )
            print("✅ 'Make Your Jodi' app title is visible")
            return True
        except TimeoutException:
            print("❌ 'Make Your Jodi' app title not found in time")
            return False

    def is_login_title_displayed(self):
        """Check if Login screen title is displayed (after launch)."""
        try:
            el = self.driver.find_element(*LOCATORS["login_title"])
            if el.is_displayed():
                self.driver.execute_script(
                    "mobile: longClickGesture", {"elementId": el.id, "duration": 800}
                )
                print("✅ Login title is displayed and highlighted")
                return True
            else:
                print("⚠️ Login title found but not visible")
                return False
        except NoSuchElementException:
            print("❌ Login title not found")
            return False
