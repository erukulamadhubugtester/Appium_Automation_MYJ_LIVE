from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import LOCATORS
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.common.exceptions import TimeoutException


class Promoted_profiles:
    def __init__(self, driver):
        self.driver = driver

    # ================= ICONS ==================
    def is_search_icon_visible(self):
        strategy, value = LOCATORS["SEARCH_ICON"]
        el = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((strategy, value))
        )
        return el.is_displayed()

    def is_bell_icon_visible(self):
        strategy, value = LOCATORS["BELL_ICON"]
        el = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((strategy, value))
        )
        return el.is_displayed()

    def is_settings_icon_visible(self):
        strategy, value = LOCATORS["SETTINGS_ICON"]
        el = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((strategy, value))
        )
        return el.is_displayed()

    def validate_all_icons(self):
        return (
            self.is_search_icon_visible()
            and self.is_bell_icon_visible()
            and self.is_settings_icon_visible()
        )

    # ================= USER INFO ==================
    def is_user_image_displayed(self):
        strategy, value = LOCATORS["USER_IMAGE"]
        try:
            el = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((strategy, value))
            )
            return el.is_displayed()
        except:
            return False

    def get_user_welcome_text(self):
        strategy, value = LOCATORS["USER_WELCOME_TEXT"]
        el = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((strategy, value))
        )
        return el.text

    def get_logged_in_username(self):
        full_text = self.get_user_welcome_text()
        if full_text.startswith("Welcome"):
            return full_text.replace("Welcome", "").strip(" !")
        return full_text

    def get_user_id(self):
        strategy, value = LOCATORS["USER_ID"]
        el = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((strategy, value))
        )
        return el.text

    # ================= VIEW PROFILE ==================
    def is_view_profile_icon_displayed(self):
        strategy, value = LOCATORS["VIEW_PROFILE_ICON"]
        try:
            el = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((strategy, value))
            )
            return el.is_displayed()
        except:
            return False

    def is_view_profile_text_displayed(self):
        strategy, value = LOCATORS["VIEW_PROFILE_TEXT"]
        try:
            el = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((strategy, value))
            )
            return el.is_displayed()
        except:
            return False

    # ================= REQUESTS ==================
    def get_requests_received_count(self):
        strategy, value = LOCATORS["REQUESTS_RECEIVED_COUNT"]
        try:
            el = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((strategy, value))
            )
            count = int(el.text.strip() or 0)
        except:
            count = 0
        print(f"📌 Requests Received Count: {count}")
        return count

    def get_requests_sent_count(self):
        strategy, value = LOCATORS["REQUESTS_SENT_COUNT"]
        try:
            el = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((strategy, value))
            )
            count = int(el.text.strip() or 0)
        except:
            count = 0
        print(f"📌 Requests Sent Count: {count}")
        return count

    def get_members_connected_count(self):
        strategy, value = LOCATORS["MEMBERS_CONNECTED_COUNT"]
        try:
            el = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((strategy, value))
            )
            count = int(el.text.strip() or 0)
        except:
            count = 0
        print(f"📌 Members Connected Count: {count}")
        return count

    # ================= PROMOTED PROFILES ==================
    def get_promoted_profiles_title(self):
        strategy, value = LOCATORS["PROMOTED_PROFILES_TITLE"]
        try:
            el = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((strategy, value))
            )
            text = el.text.strip()
            print(f"📌 Promoted Profiles Title Text: {text}")
            return text
        except:
            print("❌ Promoted Profiles title not found")
            return ""

    # ================= HORIZONTAL SCROLL ==================
    # def scroll_profiles_to_view_more(self):
    #     strategy, value = LOCATORS["PROFILE_SCROLL_CONTAINER"]
    #     container = WebDriverWait(self.driver, 5).until(
    #         EC.presence_of_element_located((strategy, value))
    #     )

    #     location = container.location
    #     size = container.size
    #     start_x = location["x"] + size["width"] * 0.9
    #     end_x = location["x"] + size["width"] * 0.1
    #     y = location["y"] + size["height"] // 2

    #     # ✅ use W3C Actions
    #     actions = self.driver.create_pointer_input("touch", "finger1")
    #     actions.create_pointer_move(x=start_x, y=y, duration=0)
    #     actions.create_pointer_down()
    #     actions.create_pointer_move(x=end_x, y=y, duration=600)
    #     actions.create_pointer_up()
    #     self.driver.perform([actions])

    #     print("👉 Swiped profiles horizontally to reveal more items")

    # def is_view_more_card_displayed(self):
    #     strategy, value = LOCATORS["VIEW_MORE_CARD"]
    #     try:
    #         el = WebDriverWait(self.driver, 5).until(
    #             EC.presence_of_element_located((strategy, value))
    #         )
    #         return el.is_displayed()
    #     except:
    #         return False

    # def get_view_more_text(self):
    #     strategy, value = LOCATORS["VIEW_MORE_TEXT"]
    #     try:
    #         el = WebDriverWait(self.driver, 5).until(
    #             EC.presence_of_element_located((strategy, value))
    #         )
    #         text = el.text.strip()
    #         print(f"📌 View More Text: {text}")
    #         return text
    #     except:
    #         return ""

    def scroll_profiles_to_view_more(self, max_swipes=5):
        """Keep swiping horizontally until 'View More' is visible or max_swipes reached"""
        strategy, value = LOCATORS["PROFILE_SCROLL_CONTAINER"]
        container = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((strategy, value))
        )

        location = container.location
        size = container.size
        start_x = location["x"] + size["width"] * 0.9
        end_x = location["x"] + size["width"] * 0.1
        y = location["y"] + size["height"] // 2

        for i in range(max_swipes):
            if self.is_view_more_card_displayed():
                print("✅ 'View More' card is now visible")
                return True
            self.driver.swipe(start_x, y, end_x, y, 800)
            print(f"👉 Swiped profiles horizontally ({i+1}/{max_swipes})")

        return self.is_view_more_card_displayed()

    def is_view_more_card_displayed(self):
        """Check if 'View More' card is visible"""
        strategy, value = LOCATORS["VIEW_MORE_CARD"]
        try:
            el = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((strategy, value))
            )
            return el.is_displayed()
        except:
            return False

    def get_view_more_text(self):
        """Return 'View More' text if visible"""
        strategy, value = LOCATORS["VIEW_MORE_TEXT"]
        try:
            el = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((strategy, value))
            )
            return el.text.strip()
        except:
            return ""

    def is_home_imageview_14_displayed(self, timeout=5):
        """Check if ImageView[14] is displayed on home screen (with scroll)"""
        strategy, value = LOCATORS["HOME_IMAGEVIEW_14"]
        try:
            # Try to scroll into view first (in case it's not visible)
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().className("android.widget.ImageView").instance(14))',
            )

            el = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((strategy, value))
            )
            return el.is_displayed()
        except TimeoutException:
            return False

    # def get_view_profiles_text(self, timeout=5):
    #     """Get the text 'View Profiles related to your preference'"""
    #     strategy, value = LOCATORS["VIEW_PROFILES_TEXT"]
    #     try:
    #         el = WebDriverWait(self.driver, timeout).until(
    #             EC.presence_of_element_located((strategy, value))
    #         )
    #         return el.text
    #     except TimeoutException:
    #         return None

    def click_imageview_13(self, timeout=10):
        """Click on ImageView[13] with scroll and fallback tap"""
        try:
            # ✅ Ensure it's scrolled into view
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                "new UiScrollable(new UiSelector().scrollable(true))"
                '.scrollIntoView(new UiSelector().className("android.widget.ImageView").instance(13))',
            )
            print("👉 Scrolled to ImageView[13]")

            for strategy, value in LOCATORS["HOME_IMAGEVIEW_13"]:
                try:
                    el = WebDriverWait(self.driver, timeout).until(
                        EC.element_to_be_clickable((strategy, value))
                    )
                    el.click()
                    print(f"🎉 Clicked ImageView[13] using {strategy}: {value}")

                    # ✅ Wait for profile to load
                    profile_strategy, profile_value = LOCATORS[
                        "PROFILE_USERNAME_DYNAMIC"
                    ]
                    WebDriverWait(self.driver, timeout).until(
                        EC.presence_of_element_located(
                            (profile_strategy, profile_value)
                        )
                    )
                    print("✅ Profile screen loaded successfully")
                    return True
                except Exception:
                    print(f"⚠️ Failed with {strategy}: {value}, trying next...")

            # ✅ Fallback: tap by coordinates
            el = self.driver.find_element(*LOCATORS["HOME_IMAGEVIEW_13"][0])
            bounds = el.rect
            x = bounds["x"] + bounds["width"] // 2
            y = bounds["y"] + bounds["height"] // 2
            self.driver.tap([(x, y)])
            print(f"🎯 Fallback tap on ImageView[13] at ({x},{y})")

            return True

        except Exception as e:
            print(f"❌ Failed to click ImageView[13]: {e}")
            return False

    # ✅ Get first profile username
    def get_profile_username(self, timeout=5):
        strategy, value = LOCATORS["PROFILE_USERNAME_DYNAMIC"]
        try:
            el = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((strategy, value))
            )
            username = el.text.strip()
            print(f"📌 Profile Username Found: {username}")
            return username
        except Exception as e:
            print(f"❌ Failed to get profile username: {e}")
            return None

    # ✅ Get first profile age
    def get_profile_age(self, timeout=5):
        strategy, value = LOCATORS["PROFILE_AGE_DYNAMIC"]
        try:
            el = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((strategy, value))
            )
            age = el.text.strip()
            print(f"📌 Profile Age Found: {age}")
            return age
        except Exception as e:
            print(f"❌ Failed to get profile age: {e}")
            return None

    # ================= WRAPPER ==================
    def home_page(self):
        """Complete Home flow in one call, return counts"""
        self.validate_all_icons()
        self.is_user_image_displayed()
        self.get_user_welcome_text()
        self.get_logged_in_username()
        self.get_user_id()
        self.is_view_profile_icon_displayed()
        self.is_view_profile_text_displayed()
