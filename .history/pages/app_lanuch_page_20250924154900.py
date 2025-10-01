from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.locators import LOCATORS
from selenium.common.exceptions import NoSuchElementException
from 


class AppLaunched:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_login_screen(self):
        """Wait until Login screen logo/title is visible after app launch."""
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
        """Check if login title/logo is displayed."""
        try:
            el = self.driver.find_element(*LOCATORS["login_title"])
            return el.is_displayed()
        except Exception:
            return False

    def wait_for_login_image_logo_check(self):
        """Wait until the splash/title image is visible (ImageView[2])."""
        try:
            print("⏳ Waiting for app title (ImageView[2])...")
            el = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(LOCATORS["login_title"])
            )
            if el.is_displayed():
                print("✅ App title image is displayed")
                return True
            else:
                print("⚠️ App title image found but not visible")
                return False
        except NoSuchElementException:
            print("❌ App title image not found")
            return False
        except Exception as e:
            print(f"❌ Error while waiting for app title: {e}")
            return False

    def login_page_text(self):
        """Get and return the login text on the login page"""
        try:
            strategy, value = LOCATORS["LOGIN_PAGE_TEXT"]
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((strategy, value))
            )
            text = element.text
            print(f"📌 Login Page Text: {text}")
            return text
        except TimeoutException:
            print("❌ Login page text not found in time")
            return None

    def enter_phone_number(self):
        """Click on phone number field and type number from config"""
        strategy, value = LOCATORS["PHONE_NUMBER_FIELD"]
        field = self.driver.find_element(strategy, value)
        field.click()
        field.send_keys(PHONE_NUMBER)
        print(f"📌 Entered phone number: {PHONE_NUMBER}")
