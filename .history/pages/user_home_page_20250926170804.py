# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from utils.locators import LOCATORS
# from appium.webdriver.common.appiumby import AppiumBy


# class HomePage:
#     def __init__(self, driver):
#         self.driver = driver

#     def is_search_icon_visible(self):
#         strategy, value = LOCATORS["SEARCH_ICON"]
#         el = WebDriverWait(self.driver, 5).until(
#             EC.presence_of_element_located((strategy, value))
#         )
#         return el.is_displayed()

#     def is_bell_icon_visible(self):
#         strategy, value = LOCATORS["BELL_ICON"]
#         el = WebDriverWait(self.driver, 5).until(
#             EC.presence_of_element_located((strategy, value))
#         )
#         return el.is_displayed()

#     def is_settings_icon_visible(self):
#         strategy, value = LOCATORS["SETTINGS_ICON"]
#         el = WebDriverWait(self.driver, 5).until(
#             EC.presence_of_element_located((strategy, value))
#         )
#         return el.is_displayed()

#     # ✅ NEW helper method
#     def validate_all_icons(self):
#         return (
#             self.is_search_icon_visible()
#             and self.is_bell_icon_visible()
#             and self.is_settings_icon_visible()
#         )

#     def is_user_image_displayed(self):
#         """Check if main user image is visible on home/live screen"""
#         strategy, value = LOCATORS["USER_IMAGE"]
#         try:
#             el = WebDriverWait(self.driver, 5).until(
#                 EC.presence_of_element_located((strategy, value))
#             )
#             return el.is_displayed()
#         except:
#             return False

#     def get_user_welcome_text(self):
#         """Return the Welcome text (e.g., 'Welcome Pushpanjali!')"""
#         strategy, value = LOCATORS["USER_WELCOME_TEXT"]
#         el = WebDriverWait(self.driver, 5).until(
#             EC.presence_of_element_located((strategy, value))
#         )
#         return el.text

#     def get_logged_in_username(self):
#         """Extract only the username from Welcome text"""
#         full_text = self.get_user_welcome_text()
#         if full_text.startswith("Welcome"):
#             return full_text.replace("Welcome", "").strip(" !")
#         return full_text

#         # ✅ User ID

#     def get_user_id(self):
#         strategy, value = LOCATORS["USER_ID"]
#         el = WebDriverWait(self.driver, 5).until(
#             EC.presence_of_element_located((strategy, value))
#         )
#         return el.text

#     # ✅ View Profile
#     def is_view_profile_icon_displayed(self):
#         strategy, value = LOCATORS["VIEW_PROFILE_ICON"]
#         try:
#             el = WebDriverWait(self.driver, 5).until(
#                 EC.presence_of_element_located((strategy, value))
#             )
#             return el.is_displayed()
#         except:
#             return False

#     def is_view_profile_text_displayed(self):
#         strategy, value = LOCATORS["VIEW_PROFILE_TEXT"]
#         try:
#             el = WebDriverWait(self.driver, 5).until(
#                 EC.presence_of_element_located((strategy, value))
#             )
#             return el.is_displayed()
#         except:
#             return False

#     # # ✅ Requests section
#     # def get_requests_received_count(self):
#     #     strategy, value = LOCATORS["REQUESTS_RECEIVED"]
#     #     el = WebDriverWait(self.driver, 5).until(
#     #         EC.presence_of_element_located((strategy, value))
#     #     )
#     #     text = el.text.strip()
#     #     print(f"📌 Requests Received Text: {text}")
#     #     # Example: "Received 5"
#     #     parts = text.split()
#     #     return int(parts[-1]) if parts and parts[-1].isdigit() else 0

#     # def get_requests_sent_count(self):
#     #     strategy, value = LOCATORS["REQUESTS_SENT"]
#     #     el = WebDriverWait(self.driver, 5).until(
#     #         EC.presence_of_element_located((strategy, value))
#     #     )
#     #     text = el.text.strip()
#     #     print(f"📌 Requests Sent Text: {text}")
#     #     return int(text.split()[-1]) if text.split()[-1].isdigit() else 0

#     # def get_members_connected_count(self):
#     #     strategy, value = LOCATORS["MEMBERS_CONNECTED"]
#     #     el = WebDriverWait(self.driver, 5).until(
#     #         EC.presence_of_element_located((strategy, value))
#     #     )
#     #     text = el.text.strip()
#     #     print(f"📌 Members Connected Text: {text}")
#     #     return int(text.split()[-1]) if text.split()[-1].isdigit() else 0

#     # =========================================================
#     # def get_requests_received_count(self):
#     #     strategy, value = LOCATORS["REQUESTS_RECEIVED_COUNT"]
#     #     el = WebDriverWait(self.driver, 5).until(
#     #         EC.presence_of_element_located((strategy, value))
#     #     )
#     #     count = int(el.text.strip())
#     #     print(f"📌 Requests Received Count: {count}")
#     #     return count

#     # def get_requests_sent_count(self):
#     #     strategy, value = LOCATORS["REQUESTS_SENT_COUNT"]
#     #     el = WebDriverWait(self.driver, 5).until(
#     #         EC.presence_of_element_located((strategy, value))
#     #     )
#     #     count = int(el.text.strip())
#     #     print(f"📌 Requests Sent Count: {count}")
#     #     return count

#     # def get_members_connected_count(self):
#     #     strategy, value = LOCATORS["MEMBERS_CONNECTED_COUNT"]
#     #     el = WebDriverWait(self.driver, 5).until(
#     #         EC.presence_of_element_located((strategy, value))
#     #     )
#     #     count = int(el.text.strip())
#     #     print(f"📌 Members Connected Count: {count}")
#     #     return count

#     def get_requests_received_count(self):
#         """Return count of requests received, default 0 if not found"""
#         strategy, value = LOCATORS["REQUESTS_RECEIVED_COUNT"]
#         try:
#             el = WebDriverWait(self.driver, 5).until(
#                 EC.presence_of_element_located((strategy, value))
#             )
#             count = int(el.text.strip() or 0)
#         except:
#             count = 0
#         print(f"📌 Requests Received Count: {count}")
#         return count

#     def get_requests_sent_count(self):
#         """Return count of requests sent, default 0 if not found"""
#         strategy, value = LOCATORS["REQUESTS_SENT_COUNT"]
#         try:
#             el = WebDriverWait(self.driver, 5).until(
#                 EC.presence_of_element_located((strategy, value))
#             )
#             count = int(el.text.strip() or 0)
#         except:
#             count = 0
#         print(f"📌 Requests Sent Count: {count}")
#         return count

#     def get_members_connected_count(self):
#         """Return count of connected members, default 0 if not found"""
#         strategy, value = LOCATORS["MEMBERS_CONNECTED_COUNT"]
#         try:
#             el = WebDriverWait(self.driver, 5).until(
#                 EC.presence_of_element_located((strategy, value))
#             )
#             count = int(el.text.strip() or 0)
#         except:
#             count = 0
#         print(f"📌 Members Connected Count: {count}")
#         return count

#     def get_promoted_profiles_title(self):
#         """Return Promoted Profiles title text if visible, else ''"""
#         strategy, value = LOCATORS["PROMOTED_PROFILES_TITLE"]
#         try:
#             el = WebDriverWait(self.driver, 5).until(
#                 EC.presence_of_element_located((strategy, value))
#             )
#             text = el.text.strip()
#             print(f"📌 Promoted Profiles Title Text: {text}")
#             return text
#         except:
#             print("❌ Promoted Profiles title not found")
#             return ""


# def scroll_profiles_to_view_more(self):
#     """Scroll horizontally until 'View More' is visible"""
#     strategy, value = LOCATORS["PROFILE_SCROLL_CONTAINER"]
#     container = WebDriverWait(self.driver, 5).until(
#         EC.presence_of_element_located((strategy, value))
#     )

#     # Get container bounds
#     location = container.location
#     size = container.size
#     start_x = location["x"] + size["width"] * 0.9  # right side
#     end_x = location["x"] + size["width"] * 0.1  # left side
#     y = location["y"] + size["height"] // 2

#     # ✅ Use W3C Actions instead of TouchAction
#     actions = self.driver.create_pointer_input("touch", "finger1")
#     actions.create_pointer_move(x=start_x, y=y, duration=0)
#     actions.create_pointer_down()
#     actions.create_pointer_move(x=end_x, y=y, duration=600)  # swipe speed
#     actions.create_pointer_up()
#     self.driver.perform([actions])

#     print("👉 Swiped profiles horizontally to reveal more items")


# def is_view_more_card_displayed(self):
#     """Check if 'View More' card is visible after scroll"""
#     strategy, value = LOCATORS["VIEW_MORE_CARD"]
#     try:
#         el = WebDriverWait(self.driver, 5).until(
#             EC.presence_of_element_located((strategy, value))
#         )
#         return el.is_displayed()
#     except:
#         return False


# def get_view_more_text(self):
#     """Return 'View More' text if visible"""
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

#     # ✅ NEW wrapper method
#     def home_page(self):
#         """Complete Home flow in one call, return counts"""
#         self.validate_all_icons()
#         self.is_user_image_displayed()
#         self.get_user_welcome_text()
#         self.get_logged_in_username()
#         self.get_user_id()
#         self.is_view_profile_icon_displayed()
#         self.is_view_profile_text_displayed()

#         received = self.get_requests_received_count()
#         sent = self.get_requests_sent_count()
#         connected = self.get_members_connected_count()
#         # self.is_promoted_profiles_title_displayed()

#         print("🎉 Home successful")
#         return received, sent, connected


# ======================== 2 code

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import LOCATORS
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


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


def scroll_profiles_to_view_more(self):
    """Scroll horizontally until 'View More' is visible"""
    strategy, value = LOCATORS["PROFILE_SCROLL_CONTAINER"]
    container = WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located((strategy, value))
       )

       location = container.location
       size = container.size
       start_x = location["x"] + size["width"] * 0.9
       end_x = location["x"] + size["width"] * 0.1
       y = location["y"] + size["height"] // 2

       # ✅ W3C Touch Action
       actions = ActionBuilder(self.driver)
       finger = PointerInput(PointerInput.TOUCH, "finger1")
       actions.add_action(finger)

       actions.pointer_action.move_to_location(start_x, y)
       actions.pointer_action.pointer_down()
       actions.pointer_action.move_to_location(end_x, y)
       actions.pointer_action.pointer_up()

       actions.perform()
       print("👉 Swiped profiles horizontally to reveal more items")

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
