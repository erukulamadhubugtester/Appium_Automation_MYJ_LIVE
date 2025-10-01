import logging
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    StaleElementReferenceException,
    TimeoutException,
)
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
        Return list of dicts {name_age}, retry on stale element.
        Location removed completely.
        """
        attempts = 0
        while attempts < max_retries:
            try:
                self.wait.until(
                    EC.presence_of_all_elements_located(LOCATORS["PROFILE_CARD"])
                )
                cards = self.driver.find_elements(*LOCATORS["PROFILE_CARD"])
                profiles = []

                for card in cards:
                    try:
                        name_age = card.get_attribute("content-desc") or ""
                        profiles.append({"name_age": name_age.strip()})
                        logger.info(f"Profile name_age: {name_age.strip()}")
                    except Exception as e:
                        logger.warning(f"⚠️ Failed to parse card: {e}")

                return profiles

            except StaleElementReferenceException:
                attempts += 1
                logger.warning(f"⚠️ Stale → retry {attempts}/{max_retries}")
                time.sleep(1)
            except TimeoutException:
                logger.warning("⚠️ No profiles loaded within wait")
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
