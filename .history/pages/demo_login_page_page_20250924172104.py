# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from utils.locators import LOCATORS
# from selenium.common.exceptions import NoSuchElementException
# from utils.config import PHONE_NUMBER
# from utils.config import PASSWORD


# class AppLaunched:
#     def __init__(self, driver):
#         self.driver = driver

#     def wait_for_login_screen(self):
#         """Wait until Login screen logo/title is visible after app launch."""
#         try:
#             print("⏳ Waiting for Login screen to appear...")
#             WebDriverWait(self.driver, 30).until(
#                 EC.presence_of_element_located(LOCATORS["login_title"])
#             )
#             print("✅ Login screen is visible")
#             return True
#         except TimeoutException:
#             print("❌ Login screen not found in time")
#             return False

#     def is_login_title_displayed(self):
#         """Check if login title/logo is displayed."""
#         try:
#             el = self.driver.find_element(*LOCATORS["login_title"])
#             return el.is_displayed()
#         except Exception:
#             return False

#     def wait_for_login_image_logo_check(self):
#         """Wait until the splash/title image is visible (ImageView[2])."""
#         try:
#             print("⏳ Waiting for app title (ImageView[2])...")
#             el = WebDriverWait(self.driver, 20).until(
#                 EC.presence_of_element_located(LOCATORS["login_title"])
#             )
#             if el.is_displayed():
#                 print("✅ App title image is displayed")
#                 return True
#             else:
#                 print("⚠️ App title image found but not visible")
#                 return False
#         except NoSuchElementException:
#             print("❌ App title image not found")
#             return False
#         except Exception as e:
#             print(f"❌ Error while waiting for app title: {e}")
#             return False

#     def login_page_text(self):
#         """Get and return the login text on the login page"""
#         try:
#             strategy, value = LOCATORS["LOGIN_PAGE_TEXT"]
#             element = WebDriverWait(self.driver, 10).until(
#                 EC.presence_of_element_located((strategy, value))
#             )
#             text = element.text
#             print(f"📌 Login Page Text: {text}")
#             return text
#         except TimeoutException:
#             print("❌ Login page text not found in time")
#             return None

#     def enter_phone_number(self):
#         """Click on phone number field and type number from config"""
#         strategy, value = LOCATORS["PHONE_NUMBER_FIELD"]
#         field = self.driver.find_element(strategy, value)
#         field.click()
#         field.send_keys(PHONE_NUMBER)
#         print(f"📌 Entered phone number: {PHONE_NUMBER}")

#     def enter_password(self):
#         strategy, value = LOCATORS["PASSWORD_FIELD"]
#         field = self.driver.find_element(strategy, value)
#         field.click()
#         field.send_keys(PASSWORD)
#         print("📌 Entered password")

#     def click_continue(self):
#         strategy, value = LOCATORS["CONTINUE_BUTTON"]
#         button = self.driver.find_element(strategy, value)
#         button.click()
#         print("📌 Clicked Continue button")

#     def is_home_screen_displayed(self):
#         strategy, value = LOCATORS["HOME_SCREEN_TITLE"]
#         try:
#             return self.driver.find_element(strategy, value).is_displayed()
#         except Exception:
#             return False


# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from selenium.common.exceptions import NoSuchElementException
# from utils.locators import LOCATORS
# from utils.config import PHONE_NUMBER, PASSWORD


# class AppLaunched:  # ⬅️ changed from AppLaunched
#     def __init__(self, driver):
#         self.driver = driver

#     def wait_for_login_screen(self):
#         """Wait until Login screen logo/title is visible after app launch."""
#         try:
#             print("⏳ Waiting for Login screen to appear...")
#             WebDriverWait(self.driver, 30).until(
#                 EC.presence_of_element_located(LOCATORS["login_title"])
#             )
#             print("✅ Login screen is visible")
#             return True
#         except TimeoutException:
#             print("❌ Login screen not found in time")
#             return False

#     def is_login_title_displayed(self):
#         """Check if login title/logo is displayed."""
#         try:
#             el = self.driver.find_element(*LOCATORS["login_title"])
#             return el.is_displayed()
#         except Exception:
#             return False

#     def wait_for_login_image_logo_check(self):
#         """Wait until the splash/title image is visible (ImageView[2])."""
#         try:
#             print("⏳ Waiting for app title (ImageView[2])...")
#             el = WebDriverWait(self.driver, 20).until(
#                 EC.presence_of_element_located(LOCATORS["login_title"])
#             )
#             if el.is_displayed():
#                 print("✅ App title image is displayed")
#                 return True
#             else:
#                 print("⚠️ App title image found but not visible")
#                 return False
#         except NoSuchElementException:
#             print("❌ App title image not found")
#             return False
#         except Exception as e:
#             print(f"❌ Error while waiting for app title: {e}")
#             return False

#     def login_page_text(self):
#         """Get and return the login text on the login page"""
#         try:
#             strategy, value = LOCATORS["LOGIN_PAGE_TEXT"]
#             element = WebDriverWait(self.driver, 10).until(
#                 EC.presence_of_element_located((strategy, value))
#             )
#             text = element.text
#             print(f"📌 Login Page Text: {text}")
#             return text
#         except TimeoutException:
#             print("❌ Login page text not found in time")
#             return None

#     def enter_phone_number(self):
#         """Click on phone number field and type number from config"""
#         strategy, value = LOCATORS["PHONE_NUMBER_FIELD"]
#         field = self.driver.find_element(strategy, value)
#         field.click()
#         field.send_keys(PHONE_NUMBER)
#         print(f"📌 Entered phone number: {PHONE_NUMBER}")

#     def enter_password(self):
#         """Click on password field and type password from config"""
#         strategy, value = LOCATORS["PASSWORD_FIELD"]
#         field = self.driver.find_element(strategy, value)
#         field.click()
#         field.send_keys(PASSWORD)
#         print("📌 Entered password")

#     def click_continue(self):
#         """Click on Continue button"""
#         strategy, value = LOCATORS["CONTINUE_BUTTON"]
#         button = self.driver.find_element(strategy, value)
#         button.click()
#         print("📌 Clicked Continue button")

#     def dismiss_password_popup(self):
#     try:
#         popup_button = WebDriverWait(self.driver, 5).until(
#             EC.presence_of_element_located(
#                 (AppiumBy.ANDROID_UIAUTOMATOR,
#                  'new UiSelector().text("Not now")')
#             )
#         )
#         popup_button.click()
#         print("📌 Dismissed Google Password Manager popup [Not now]")
#     except:
#         try:
#             popup_button = WebDriverWait(self.driver, 5).until(
#                 EC.presence_of_element_located(
#                     (AppiumBy.ANDROID_UIAUTOMATOR,
#                      'new UiSelector().text("Never")')
#                 )
#             )
#             popup_button.click()
#             print("📌 Dismissed Google Password Manager popup [Never]")
#         except:
#             print("✅ No password popup appeared")

#     def is_home_screen_displayed(self):
#         """Check if Home screen is displayed"""
#         strategy, value = LOCATORS["HOME_SCREEN_TITLE"]
#         try:
#             return self.driver.find_element(strategy, value).is_displayed()
#         except Exception:
#             return False


from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.locators import LOCATORS
from utils.config import PHONE_NUMBER, PASSWORD


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
            el = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((strategy, value))
            )
            return el.is_displayed()
        except Exception:
            return False
