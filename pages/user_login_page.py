import os
from datetime import datetime
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.locators import LOCATORS
from utils.config import PHONE_NUMBER, PASSWORD


class User_login_Page:
    def __init__(self, driver):
        self.driver = driver

    def enter_phone_number(self):
        strategy, value = LOCATORS["PHONE_NUMBER_FIELD"]
        field = self.driver.find_element(strategy, value)
        field.click()
        field.send_keys(PHONE_NUMBER)
        print(f"📌 Entered phone number: {PHONE_NUMBER}")

    def enter_password(self):
        strategy, value = LOCATORS["PASSWORD_FIELD"]
        field = self.driver.find_element(strategy, value)
        field.click()
        field.send_keys(PASSWORD)
        print("📌 Entered password")

    def click_continue(self):
        strategy, value = LOCATORS["CONTINUE_BUTTON"]
        button = self.driver.find_element(strategy, value)
        button.click()
        print("📌 Clicked Continue button")
        self.dismiss_password_popup()

    def dismiss_password_popup(self):
        try:
            popup_button = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located(
                    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Not now")')
                )
            )
            popup_button.click()
            print("📌 Dismissed Google Password Manager popup [Not now]")
        except TimeoutException:
            try:
                popup_button = WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located(
                        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Never")')
                    )
                )
                popup_button.click()
                print("📌 Dismissed Google Password Manager popup [Never]")
            except TimeoutException:
                print("✅ No password popup appeared")

    def is_home_screen_displayed(self):
        strategy, value = LOCATORS["HOME_SCREEN_TITLE"]
        try:
            el = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((strategy, value))
            )
            return el.is_displayed()
        except Exception:
            return False

    def handle_profile_completion_popup(self):
        try:
            strategy, value = LOCATORS["PROFILE_POPUP_TITLE"]
            popup = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((strategy, value))
            )

            if popup.is_displayed():
                print("📌 Profile Completion popup detected!")
                print(f"📌 Title: {popup.text}")

                # Content
                strategy, value = LOCATORS["PROFILE_POPUP_CONTENT"]
                content = self.driver.find_element(strategy, value).text
                print(f"📌 Content: {content}")

                # Progress %
                strategy, value = LOCATORS["PROFILE_POPUP_PROGRESS"]
                progress = self.driver.find_element(strategy, value).text
                print(f"📌 Profile Completion: {progress}")

                # Buttons
                complete_btn = self.driver.find_element(
                    *LOCATORS["PROFILE_POPUP_COMPLETE_BTN"]
                )
                skip_btn = self.driver.find_element(*LOCATORS["PROFILE_POPUP_SKIP_BTN"])

                print(
                    f"📌 Complete Profile button displayed: {complete_btn.is_displayed()}"
                )
                print(f"📌 Skip for Now button displayed: {skip_btn.is_displayed()}")

                skip_btn.click()
                print("✅ Clicked 'Skip for Now'")
                return False

        except TimeoutException:
            print("✅ No profile completion popup → Profile is 100% completed")
            return True

    # ✅ NEW: Detect login error messages
    def is_login_error_displayed(self):
        try:
            error_element = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().textContains("Unexpected error")',
                    )
                )
            )
            if error_element.is_displayed():
                print(f"❌ Login error detected: {error_element.text}")
                return True
        except TimeoutException:
            pass
        return False

    # ✅ NEW: Capture screenshot for debugging
    def take_screenshot(self, name="login_error"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        os.makedirs("screenshots", exist_ok=True)
        path = f"screenshots/{name}_{timestamp}.png"
        self.driver.save_screenshot(path)
        print(f"📷 Screenshot saved: {path}")

    # ✅ Wrapper method for full login flow
    def login(self):
        """Complete login flow with error handling and screenshots"""
        self.enter_phone_number()
        self.enter_password()
        self.click_continue()

        if self.is_login_error_displayed():
            self.take_screenshot()
            raise AssertionError("❌ Login failed: Unexpected error occurred")

        self.handle_profile_completion_popup()

        if not self.is_home_screen_displayed():
            self.take_screenshot("home_not_displayed")
            raise AssertionError("❌ Login failed: Home screen not visible")

        print("🎉 Login successful, home screen visible")
