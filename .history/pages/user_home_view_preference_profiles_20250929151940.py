from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import LOCATORS
from selenium.common.exceptions import TimeoutException


class PreferenceProfilesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_home_imageview_13(self):
        """Click entry point ImageView[13]"""
        strategy, value = LOCATORS["HOME_IMAGEVIEW_13"]
        el = self.wait.until(EC.element_to_be_clickable((strategy, value)))
        el.click()
        print("✅ Clicked ImageView[13] to open profiles")

    def get_username(self):
        """Fetch username freshly each time (avoid stale element)"""
        strategy, value = LOCATORS["PROFILE_USERNAME"]
        el = self.wait.until(EC.presence_of_element_located((strategy, value)))
        text = el.text.strip()
        # clean duplicated comma cases like "Harsh Joshi,,"
        if text.endswith(","):
            text = text[:-1]
        return text

    def get_age(self):
        strategy, value = LOCATORS["PROFILE_AGE"]
        el = self.wait.until(EC.presence_of_element_located((strategy, value)))
        return el.text.strip()

    def get_location(self):
        strategy, value = LOCATORS["PROFILE_LOCATION"]
        el = self.wait.until(EC.presence_of_element_located((strategy, value)))
        return el.text.strip()

    def click_next_arrow(self):
        """Click forward arrow to load next profile"""
        strategy, value = LOCATORS["PROFILE_FORWARD_ARROW"]
        el = self.wait.until(EC.element_to_be_clickable((strategy, value)))
        el.click()
        print("👉 Forward arrow clicked → Next profile")

    def loop_profiles(self, max_profiles=100):
        """
        Loop through profiles until first profile repeats
        or until max_profiles reached.
        Returns list of dicts with profile info.
        """
        seen = set()
        profiles = []

        while True:
            try:
                username = self.get_username()
                age = self.get_age()
                location = self.get_location()

                profile_id = f"{username}-{age}-{location}"

                # stop if we already saw this profile (looped back)
                if profile_id in seen:
                    print("✅ First profile reached again → Exit loop")
                    break

                seen.add(profile_id)
                profiles.append(
                    {"username": username, "age": age, "location": location}
                )
                print(f"🔎 Profile {len(profiles)}: {username}, {age}, {location}")

                if len(profiles) >= max_profiles:
                    print("⚠️ Reached max profile limit, stopping")
                    break

                self.click_next_arrow()

            except TimeoutException:
                print("⚠️ No more profiles or element not found, stopping")
                break

        return profiles
