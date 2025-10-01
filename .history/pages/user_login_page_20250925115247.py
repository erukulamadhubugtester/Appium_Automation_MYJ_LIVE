from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.locators import LOCATORS
from utils.config import PHONE_NUMBER, PASSWORD


class User_login_Page:
    def __init__(self, driver):
        self.driver = driver
        # your methods here

    def enter_phone_number(self):
        """Click on phone number field and type number from config"""
        strategy, value = LOCATORS["PHONE_NUMBER_FIELD"]
        field = self.driver.find_element(strategy, value)
        field.click()
        field.send_keys(PHONE_NUMBER)
        print(f"📌 Entered phone number: {PHONE_NUMBER}")

    def enter_password(self):
        """Click on password field and type password from config"""
        strategy, value = LOCATORS["PASSWORD_FIELD"]
        field = self.driver.find_element(strategy, value)
        field.click()
        field.send_keys(PASSWORD)
        print("📌 Entered password")

    def click_continue(self):
        """Click on Continue button"""
        strategy, value = LOCATORS["CONTINUE_BUTTON"]
        button = self.driver.find_element(strategy, value)
        button.click()
        print("📌 Clicked Continue button")
        # ✅ Automatically dismiss popup after clicking Continue
        self.dismiss_password_popup()

    def dismiss_password_popup(self):
        """Dismiss Google Password Manager popup if it appears"""
        try:
            popup_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Not now")')
                )
            )
            popup_button.click()
            print("📌 Dismissed Google Password Manager popup [Not now]")
        except:
            try:
                popup_button = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located(
                        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Never")')
                    )
                )
                popup_button.click()
                print("📌 Dismissed Google Password Manager popup [Never]")
            except:
                print("✅ No password popup appeared")

    def is_home_screen_displayed(self):
        """Check if Home screen is displayed"""
        strategy, value = LOCATORS["HOME_SCREEN_TITLE"]
        try:
            el = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((strategy, value))
            )
            return el.is_displayed()
        except Exception:
            return False
