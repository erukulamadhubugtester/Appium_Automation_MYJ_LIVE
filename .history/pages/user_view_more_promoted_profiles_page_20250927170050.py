from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import LOCATORS
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException


class User_view_more_promoted_profiles:
    def __init__(self, driver):
        self.driver = driver
        # ✅ Initialize explicit wait once for the whole class
        self.wait = WebDriverWait(driver, 15)

    # ================= USER INFO ==================
    def is_user_image_displayed(self):
        strategy, value = LOCATORS["USER_IMAGE"]
        try:
            el = self.wait.until(EC.presence_of_element_located((strategy, value)))
            return el.is_displayed()
        except TimeoutException:
            return False

    def get_user_welcome_text(self):
        strategy, value = LOCATORS["USER_WELCOME_TEXT"]
        el = self.wait.until(EC.presence_of_element_located((strategy, value)))
        return el.text

    def get_logged_in_username(self):
        full_text = self.get_user_welcome_text()
        if full_text.startswith("Welcome"):
            return full_text.replace("Welcome", "").strip(" !")
        return full_text

    def get_user_id(self):
        strategy, value = LOCATORS["USER_ID"]
        el = self.wait.until(EC.presence_of_element_located((strategy, value)))
        return el.text

    # ================= PROMOTED PROFILES ==================
    def get_promoted_profiles_title(self):
        strategy, value = LOCATORS["PROMOTED_PROFILES_TITLE"]
        try:
            el = self.wait.until(EC.presence_of_element_located((strategy, value)))
            text = el.text.strip()
            print(f"📌 Promoted Profiles Title Text: {text}")
            return text
        except TimeoutException:
            print("❌ Promoted Profiles title not found")
            return ""

    # ================= HORIZONTAL SCROLL ==================
    def scroll_profiles_to_view_more(self, max_swipes=5):
        """Keep swiping horizontally until 'View More' is visible or max_swipes reached"""
        strategy, value = LOCATORS["PROFILE_SCROLL_CONTAINER"]
        container = self.wait.until(EC.presence_of_element_located((strategy, value)))

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
        strategy, value = LOCATORS["VIEW_MORE_CARD"]
        try:
            el = self.wait.until(EC.presence_of_element_located((strategy, value)))
            return el.is_displayed()
        except TimeoutException:
            return False

    def get_view_more_text(self):
        strategy, value = LOCATORS["VIEW_MORE_TEXT"]
        try:
            el = self.wait.until(EC.presence_of_element_located((strategy, value)))
            return el.text.strip()
        except TimeoutException:
            return ""

    # ================= ACTIONS ==================
    def highlight(self, element):
        """Highlight element (works in webview; fallback = log)"""
        try:
            self.driver.execute_script(
                "arguments[0].style.border='3px solid red'", element
            )
        except Exception:
            print(f"🔦 Highlighting: {element}")

    def click_view_more(self):
        strategy, value = LOCATORS["VIEW_MORE"]
        el = self.wait.until(EC.element_to_be_clickable((strategy, value)))
        self.highlight(el)
        el.click()
        print("✅ Clicked View More")

    def highlight_profiles_title(self):
        strategy, value = LOCATORS["PROFILES_TITLE"]
        el = self.wait.until(EC.presence_of_element_located((strategy, value)))
        self.highlight(el)
        print("✅ Profiles title highlighted")
        return el.text

    def click_promoted_card(self):
        strategy, value = LOCATORS["PROMOTED_CARD"]
        el = self.wait.until(EC.element_to_be_clickable((strategy, value)))
        self.highlight(el)
        el.click()
        print("✅ Clicked Promoted card")

    def count_all_profile_cards(self, max_scrolls=5):
        """
        Scroll vertically to collect all profile cards.
        Works in native app context - highlights by logging.
        """
        strategy, value = LOCATORS["PROFILE_CARDS"]  # Example: (AppiumBy.ID, "com.app:id/profileCard")
        seen = set()
        total = 0

        for i in range(max_scrolls):
         cards = self.driver.find_elements(strategy, value)

        for card in cards:
            card_id = card.id
            if card_id not in seen:
                seen.add(card_id)
                total += 1
                print(f"🔦 Highlighted profile card {total}: {card}")

        # Try to scroll down to load more profiles
        try:
            self.driver.swipe(
                start_x=200, start_y=1000, end_x=200, end_y=300, duration=800
            )
            print(f"👉 Scrolled down ({i+1}/{max_scrolls})")
        except Exception as e:
            print(f"⚠️ Scroll failed: {e}")
            break

    print(f"📌 Total profile cards found across scrolls: {total}")
    return total





    # ================= WRAPPER ==================
    def user_home_screen_promoted_profiles_page(self):
        """Complete Home flow in one call, return counts"""
        self.is_user_image_displayed()
        self.get_user_welcome_text()
        self.get_logged_in_username()
        self.get_user_id()
