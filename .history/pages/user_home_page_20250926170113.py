from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import LOCATORS
from appium.webdriver.common.appiumby import AppiumBy


class HomePage:
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
    def scroll_profiles_to_view_more(self):
        strategy, value = LOCATORS["PROFILE_SCROLL_CONTAINER"]
        container = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((strategy, value))
        )

        location = container.location
        size = container.size
        start_x = location["x"] + size["width"] * 0.9
        end_x = location["x"] + size["width"] * 0.1
        y = location["y"] + size["height"] // 2

        # ✅ use W3C Actions
        actions = self.driver.create_pointer_input("touch", "finger1")
        actions.create_pointer_move(x=start_x, y=y, duration=0)
        actions.create_pointer_down()
        actions.create_pointer_move(x=end_x, y=y, duration=600)
        actions.create_pointer_up()
        self.driver.perform([actions])

        print("👉 Swiped profiles horizontally to reveal more items")

    def is_view_more_card_displayed(self):
        strategy, value = LOCATORS["VIEW_MORE_CARD"]
        try:
            el = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((strategy, value))
            )
            return el.is_displayed()
        except:
            return False

    def get_view_more_text(self):
        strategy, value = LOCATORS["VIEW_MORE_TEXT"]
        try:
            el = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((strategy, value))
            )
            text = el.text.strip()
            print(f"📌 View More Text: {text}")
            return text
        except:
            return ""

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

        received = self.get_requests_received_count()
        sent = self.get_requests_sent_count()
        connected = self.get_members_connected_count()

        print("🎉 Home successful")
        return received, sent, connected
