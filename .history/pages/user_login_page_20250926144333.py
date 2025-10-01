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
        except:
            try:
                popup_button = WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located(
                        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Never")')
                    )
                )
                popup_button.click()
                print("📌 Dismissed Google Password Manager popup [Never]")
            except:
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
        """Check and handle profile completion popup after login"""
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

        except:
            print("✅ No profile completion popup → Profile is 100% completed")
            return True

    # ✅ NEW wrapper method
    def login(self):
        """Complete login flow in one call"""
        self.enter_phone_number()
        self.enter_password()
        self.click_continue()
        assert self.is_home_screen_displayed(), "❌ Login failed: Home not displayed"
        print("🎉 Login successful, home screen visible")

        
