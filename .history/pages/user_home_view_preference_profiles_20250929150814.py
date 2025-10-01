# # ======================== 2 code

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from utils.locators import LOCATORS
# from appium.webdriver.common.appiumby import AppiumBy
# from selenium.webdriver.common.actions.action_builder import ActionBuilder
# from selenium.webdriver.common.actions.pointer_input import PointerInput
# from selenium.common.exceptions import TimeoutException


# class HomePage_preference_profiles:
#     def __init__(self, driver):
#         self.driver = driver

#     def is_home_imageview_14_displayed(self, timeout=5):
#         """Check if ImageView[14] is displayed on home screen (with scroll)"""
#         strategy, value = LOCATORS["HOME_IMAGEVIEW_14"]
#         try:
#             # Try to scroll into view first (in case it's not visible)
#             self.driver.find_element(
#                 AppiumBy.ANDROID_UIAUTOMATOR,
#                 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().className("android.widget.ImageView").instance(14))',
#             )

#             el = WebDriverWait(self.driver, timeout).until(
#                 EC.presence_of_element_located((strategy, value))
#             )
#             return el.is_displayed()
#         except TimeoutException:
#             return False

#     def click_imageview_13(self, timeout=10):
#         """Click on ImageView[13] with scroll and fallback tap"""
#         try:
#             # ✅ Ensure it's scrolled into view
#             self.driver.find_element(
#                 AppiumBy.ANDROID_UIAUTOMATOR,
#                 "new UiScrollable(new UiSelector().scrollable(true))"
#                 '.scrollIntoView(new UiSelector().className("android.widget.ImageView").instance(13))',
#             )
#             print("👉 Scrolled to ImageView[13]")

#             for strategy, value in LOCATORS["HOME_IMAGEVIEW_13"]:
#                 try:
#                     el = WebDriverWait(self.driver, timeout).until(
#                         EC.element_to_be_clickable((strategy, value))
#                     )
#                     el.click()
#                     print(f"🎉 Clicked ImageView[13] using {strategy}: {value}")

#                     # ✅ Wait for profile to load
#                     profile_strategy, profile_value = LOCATORS[
#                         "PROFILE_USERNAME_DYNAMIC"
#                     ]
#                     WebDriverWait(self.driver, timeout).until(
#                         EC.presence_of_element_located(
#                             (profile_strategy, profile_value)
#                         )
#                     )
#                     print("✅ Profile screen loaded successfully")
#                     return True
#                 except Exception:
#                     print(f"⚠️ Failed with {strategy}: {value}, trying next...")

#             # ✅ Fallback: tap by coordinates
#             el = self.driver.find_element(*LOCATORS["HOME_IMAGEVIEW_13"][0])
#             bounds = el.rect
#             x = bounds["x"] + bounds["width"] // 2
#             y = bounds["y"] + bounds["height"] // 2
#             self.driver.tap([(x, y)])
#             print(f"🎯 Fallback tap on ImageView[13] at ({x},{y})")

#             return True

#         except Exception as e:
#             print(f"❌ Failed to click ImageView[13]: {e}")
#             return False

#     # ✅ Get first profile username
#     def get_profile_username(self, timeout=5):
#         strategy, value = LOCATORS["PROFILE_USERNAME_DYNAMIC"]
#         try:
#             el = WebDriverWait(self.driver, timeout).until(
#                 EC.presence_of_element_located((strategy, value))
#             )
#             username = el.text.strip()
#             print(f"📌 Profile Username Found: {username}")
#             return username
#         except Exception as e:
#             print(f"❌ Failed to get profile username: {e}")
#             return None

#     # ✅ Get first profile age
#     def get_profile_age(self, timeout=5):
#         strategy, value = LOCATORS["PROFILE_AGE_DYNAMIC"]
#         try:
#             el = WebDriverWait(self.driver, timeout).until(
#                 EC.presence_of_element_located((strategy, value))
#             )
#             age = el.text.strip()
#             print(f"📌 Profile Age Found: {age}")
#             return age
#         except Exception as e:
#             print(f"❌ Failed to get profile age: {e}")
#             return None

#     # ================= WRAPPER ==================
#     def home_page(self):
#         """Complete Home flow in one call, return counts"""
