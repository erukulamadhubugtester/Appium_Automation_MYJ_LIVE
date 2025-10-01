from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import LOCATORS


class HomePage:
    def __init__(self, driver):
        self.driver = driver

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

    # ✅ NEW helper method
    def validate_all_icons(self):
        return (
            self.is_search_icon_visible()
            and self.is_bell_icon_visible()
            and self.is_settings_icon_visible()
        )

    def is_user_image_displayed(self):
        """Check if main user image is visible on home/live screen"""
        strategy, value = LOCATORS["USER_IMAGE"]
        try:
            el = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((strategy, value))
            )
            return el.is_displayed()
        except:
            return False

    def get_user_welcome_text(self):
        """Return the Welcome text (e.g., 'Welcome Pushpanjali!')"""
        strategy, value = LOCATORS["USER_WELCOME_TEXT"]
        el = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((strategy, value))
        )
        return el.text

    def get_logged_in_username(self):
        """Extract only the username from Welcome text"""
        full_text = self.get_user_welcome_text()
        if full_text.startswith("Welcome"):
            return full_text.replace("Welcome", "").strip(" !")
        return full_text

        # ✅ User ID

    def get_user_id(self):
        strategy, value = LOCATORS["USER_ID"]
        el = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((strategy, value))
        )
        return el.text

    # ✅ View Profile
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

    # ✅ Requests section
    def get_requests_received_count(self):
        strategy, value = LOCATORS["REQUESTS_RECEIVED"]
        el = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((strategy, value))
        )
        # Example: "Received 5" → extract number
        return int(el.find_element_by_xpath("..").text.split()[-1])

    def get_requests_sent_count(self):
        strategy, value = LOCATORS["REQUESTS_SENT"]
        el = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((strategy, value))
        )
        return int(el.find_element_by_xpath("..").text.split()[-1])

    # ✅ Members section
    def get_members_connected_count(self):
        strategy, value = LOCATORS["MEMBERS_CONNECTED"]
        el = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((strategy, value))
        )
        return int(el.find_element_by_xpath("..").text.split()[-1])
