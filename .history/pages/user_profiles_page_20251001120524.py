# import logging
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from utils.locators import LOCATORS

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)


# class ProfilesPage:
#     def __init__(self, driver, wait_time=20):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, wait_time)

#     # ---- Navigation ----
#     def open_profiles(self):
#         logger.info("Clicking on Profiles icon...")
#         self.wait.until(EC.element_to_be_clickable(LOCATORS["PROFILES_ICON"])).click()
#         txt = self.wait.until(
#             EC.presence_of_element_located(LOCATORS["PROFILES_TEXT"])
#         ).text
#         logger.info(f"✅ Profiles opened, header text: {txt}")
#         return txt

#     def open_recent_visitors(self):
#         logger.info("Clicking Recent Visitors...")
#         self.wait.until(
#             EC.element_to_be_clickable(LOCATORS["RECENT_VISITORS_TAB"])
#         ).click()

#     def open_promoted(self):
#         logger.info("Clicking Promoted tab...")
#         self.wait.until(EC.element_to_be_clickable(LOCATORS["PROMOTED_TAB"])).click()

#     def open_preferred(self):
#         logger.info("Clicking Preferred tab...")
#         self.wait.until(EC.element_to_be_clickable(LOCATORS["PREFERRED_TAB"])).click()

#     # ---- Profile data ----
#     def get_profiles(self):
#         """Return list of dicts {name_age, location}"""
#         profiles = []
#         names = self.driver.find_elements(*LOCATORS["PROFILE_NAME_AGE"])
#         locs = self.driver.find_elements(*LOCATORS["PROFILE_LOCATION"])

#         for i in range(len(names)):
#             profile = {
#                 "name_age": names[i].text if i < len(names) else "",
#                 "location": locs[i].text if i < len(locs) else "",
#             }
#             logger.info(f"Profile: {profile}")
#             profiles.append(profile)
#         return profiles

#     def is_upgrade_banner(self):
#         """Check if Upgrade Plan banner is shown"""
#         try:
#             el = self.driver.find_element(*LOCATORS["UPGRADE_PLAN_BUTTON"])
#             logger.info("⚠️ Upgrade banner detected")
#             return el.is_displayed()
#         except:
#             return False


======== # code 2 

import logging
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from utils.locators import LOCATORS

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class ProfilesPage:
    def __init__(self, driver, wait_time=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_time)

    # ---- Navigation ----
    def open_profiles(self):
        logger.info("Clicking on Profiles icon...")
        self.wait.until(EC.element_to_be_clickable(LOCATORS["PROFILES_ICON"])).click()
        txt = self.wait.until(
            EC.presence_of_element_located(LOCATORS["PROFILES_TEXT"])
        ).text
        logger.info(f"✅ Profiles opened, header text: {txt}")
        return txt

    def open_recent_visitors(self):
        logger.info("Clicking Recent Visitors...")
        self.wait.until(
            EC.element_to_be_clickable(LOCATORS["RECENT_VISITORS_TAB"])
        ).click()

    def open_promoted(self):
        logger.info("Clicking Promoted tab...")
        self.wait.until(EC.element_to_be_clickable(LOCATORS["PROMOTED_TAB"])).click()

    def open_preferred(self):
        logger.info("Clicking Preferred tab...")
        self.wait.until(EC.element_to_be_clickable(LOCATORS["PREFERRED_TAB"])).click()

    # ---- Profile data ----
    def get_profiles(self, max_retries=3):
        """
        Return list of dicts {name_age, location}
        Handles StaleElementReferenceException by retrying.
        """
        attempts = 0
        profiles = []

        while attempts < max_retries:
            try:
                # Wait until at least one profile name is present
                self.wait.until(
                    EC.presence_of_all_elements_located(LOCATORS["PROFILE_NAME_AGE"])
                )

                names = self.driver.find_elements(*LOCATORS["PROFILE_NAME_AGE"])
                locs = self.driver.find_elements(*LOCATORS["PROFILE_LOCATION"])

                for i in range(max(len(names), len(locs))):
                    name_text = names[i].text if i < len(names) else ""
                    loc_text = locs[i].text if i < len(locs) else ""
                    profile = {"name_age": name_text, "location": loc_text}
                    logger.info(f"Profile: {profile}")
                    profiles.append(profile)

                return profiles

            except StaleElementReferenceException:
                attempts += 1
                logger.warning(
                    f"⚠️ StaleElementReferenceException → retrying {attempts}/{max_retries}"
                )
                time.sleep(1)  # small wait before retry
            except TimeoutException:
                logger.warning("⚠️ No profiles loaded within wait time")
                return []

        logger.error("❌ Failed to fetch profiles after retries")
        return []

    def is_upgrade_banner(self):
        """Check if Upgrade Plan banner is shown"""
        try:
            el = self.driver.find_element(*LOCATORS["UPGRADE_PLAN_BUTTON"])
            if el.is_displayed():
                logger.info("⚠️ Upgrade banner detected")
                return True
            return False
        except Exception:
            return False
