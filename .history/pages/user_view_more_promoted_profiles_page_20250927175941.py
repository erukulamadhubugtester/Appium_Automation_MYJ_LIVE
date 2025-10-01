from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import LOCATORS
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException


class User_view_more_promoted_profiles:
    def __init__(self, driver):
        self.driver = driver
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
            print(f"📌 Promoted Profiles Title: {text}")
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
                print("✅ 'View More' card is visible")
                return True
            self.driver.swipe(start_x, y, end_x, y, 800)
            print(f"👉 Swiped horizontally ({i+1}/{max_swipes})")

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

    # ================= VERTICAL SCROLL & COUNT ==================
    def count_all_profile_cards(self):
        """
        Keep scrolling until no new profiles appear.
        Returns total unique profile count.
        Uses child TextView inside each card as identifier.
        """
        cards_locator = (
            AppiumBy.XPATH,
            "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup",
        )
        seen = set()
        total = 0

        while True:
            cards = self.driver.find_elements(*cards_locator)

            if not cards:
                print("⚠️ No profile cards found, stopping.")
                break

            before_count = len(seen)

            for card in cards:
                try:
                    # ✅ Get profile name/age text from first child TextView
                    name_elem = card.find_element(
                        AppiumBy.XPATH, ".//android.widget.TextView"
                    )
                    identifier = name_elem.text.strip()
                except Exception:
                    # fallback if no text view inside
                    rect = card.rect
                    identifier = (
                        f"{rect['x']}_{rect['y']}_{rect['width']}_{rect['height']}"
                    )

                if identifier and identifier not in seen:
                    seen.add(identifier)
                    total += 1
                    self.highlight(card)
                    print(f"🔦 Found profile {total}: {identifier}")

            after_count = len(seen)

            # ✅ stop if no new profiles in this scroll
            if after_count == before_count:
                print("✅ No new profiles after this scroll, exiting.")
                break

            self.scroll_down_once()

        print(f"📌 Final total profiles: {total}")
        return total

    def scroll_down_once(self):
        size = self.driver.get_window_size()
        start_y = size["height"] * 0.8
        end_y = size["height"] * 0.3
        x = size["width"] * 0.5
        self.driver.swipe(x, start_y, x, end_y, 800)

    # ================= WRAPPER ==================
    def user_home_screen_promoted_profiles_page(self):
        """Complete Home flow in one call, return profile count"""
        self.is_user_image_displayed()
        self.get_user_welcome_text()
        self.get_logged_in_username()
        self.get_user_id()
        self.get_promoted_profiles_title()
        self.scroll_profiles_to_view_more()
        self.click_view_more()
        self.highlight_profiles_title()
        self.click_promoted_card()
        return self.count_all_profile_cards()
