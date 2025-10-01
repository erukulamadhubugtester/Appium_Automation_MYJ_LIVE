# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import (
#     StaleElementReferenceException,
#     TimeoutException,
# )
# from utils.locators import LOCATORS


# class PreferenceProfilesPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)

#     # 🔹 Open entry profile from home
#     def click_home_imageview_13(self):
#         strategy, value = LOCATORS["HOME_IMAGEVIEW_13"]
#         el = self.wait.until(EC.element_to_be_clickable((strategy, value)))
#         el.click()
#         print("✅ Clicked ImageView[13] to open profiles")

#     # 🔹 Helper: retry if stale
#     def _get_text_safe(self, locator, timeout=10):
#         for _ in range(3):
#             try:
#                 el = WebDriverWait(self.driver, timeout).until(
#                     EC.presence_of_element_located(locator)
#                 )
#                 return el.text.strip()
#             except StaleElementReferenceException:
#                 print("⚠️ Stale element → retrying...")
#         raise TimeoutException(f"❌ Could not fetch text for {locator}")

#     def get_username(self):
#         return self._get_text_safe(LOCATORS["PROFILE_USERNAME"])

#     def get_age(self):
#         return self._get_text_safe(LOCATORS["PROFILE_AGE"])

#     def get_location(self):
#         return self._get_text_safe(LOCATORS["PROFILE_LOCATION"])

#     def click_next_arrow(self):
#         strategy, value = LOCATORS["PROFILE_FORWARD_ARROW"]
#         el = self.wait.until(EC.element_to_be_clickable((strategy, value)))
#         el.click()
#         print("👉 Forward arrow clicked → Next profile")

#     # 🔹 Main loop
#     def loop_profiles(self, max_profiles=200):
#         seen = set()
#         profiles = []

#         while len(profiles) < max_profiles:
#             username = self.get_username()
#             age = self.get_age()
#             location = self.get_location()

#             profile_id = f"{username}-{age}-{location}"
#             if profile_id in seen:
#                 print("✅ First profile reached again → Loop complete.")
#                 break

#             seen.add(profile_id)
#             profiles.append({"username": username, "age": age, "location": location})
#             print(f"🔎 Profile {len(profiles)}: {username}, {age}, {location}")

#             self.click_next_arrow()

#         return profiles


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    StaleElementReferenceException,
    TimeoutException,
)
from utils.locators import LOCATORS


class PreferenceProfilesPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # 🔹 Open entry profile from home
    def click_home_imageview_13(self):
        strategy, value = LOCATORS["HOME_IMAGEVIEW_13"]
        el = self.wait.until(EC.element_to_be_clickable((strategy, value)))
        el.click()
        print("✅ Clicked ImageView[13] to open profiles")

    # 🔹 Helper: retry if stale
    def _get_text_safe(self, locator, timeout=10, retries=3):
        strategy, value = locator
        for attempt in range(retries):
            try:
                el = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((strategy, value))
                )
                return el.text.strip()
            except StaleElementReferenceException:
                print(f"⚠️ Stale element → retrying ({attempt+1}/{retries})...")
        raise TimeoutException(f"❌ Could not fetch text for {locator}")

    def get_username(self):
        username = self._get_text_safe(LOCATORS["PROFILE_USERNAME"])
        return username.rstrip(",")  # cleanup trailing comma

    def get_age(self):
        return self._get_text_safe(LOCATORS["PROFILE_AGE"])

    def get_location(self):
    return self._get_text_safe(LOCATORS["PROFILE_LOCATION"])

    def click_next_arrow(self):
        strategy, value = LOCATORS["PROFILE_FORWARD_ARROW"]
        el = self.wait.until(EC.element_to_be_clickable((strategy, value)))
        el.click()
        print("👉 Forward arrow clicked → Next profile")

    # 🔹 Main loop
    def loop_profiles(self, max_profiles=200):
        seen = set()
        profiles = []

        for _ in range(max_profiles):
            username = self.get_username()
            age = self.get_age()
            location = self.get_location()

            profile_id = f"{username}-{age}-{location}"
            if profile_id in seen:
                print("✅ First profile reached again → Loop complete.")
                break

            seen.add(profile_id)
            profiles.append({"username": username, "age": age, "location": location})
            print(f"🔎 Profile {len(profiles)}: {username}, {age}, {location}")

            self.click_next_arrow()

        print(f"📌 Total unique profiles visited: {len(profiles)}")
        return profiles
