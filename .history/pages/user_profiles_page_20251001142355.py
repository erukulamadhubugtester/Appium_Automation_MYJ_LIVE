# import logging
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import (
#     StaleElementReferenceException,
#     TimeoutException,
# )
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
#     def get_profiles(self, max_retries=3):
#         """
#         Return list of dicts {name_age}, retry on stale element.
#         Location removed completely.
#         """
#         attempts = 0
#         while attempts < max_retries:
#             try:
#                 self.wait.until(
#                     EC.presence_of_all_elements_located(LOCATORS["PROFILE_CARD"])
#                 )
#                 cards = self.driver.find_elements(*LOCATORS["PROFILE_CARD"])
#                 profiles = []

#                 for card in cards:
#                     try:
#                         name_age = card.get_attribute("content-desc") or ""
#                         profiles.append({"name_age": name_age.strip()})
#                         logger.info(f"Profile name_age: {name_age.strip()}")
#                     except Exception as e:
#                         logger.warning(f"⚠️ Failed to parse card: {e}")

#                 return profiles

#             except StaleElementReferenceException:
#                 attempts += 1
#                 logger.warning(f"⚠️ Stale → retry {attempts}/{max_retries}")
#                 time.sleep(1)
#             except TimeoutException:
#                 logger.warning("⚠️ No profiles loaded within wait")
#                 return []

#         logger.error("❌ Failed to fetch profiles after retries")
#         return []

#     def is_upgrade_banner(self):
#         """Check if Upgrade Plan banner is shown"""
#         try:
#             el = self.driver.find_element(*LOCATORS["UPGRADE_PLAN_BUTTON"])
#             if el.is_displayed():
#                 logger.info("⚠️ Upgrade banner detected")
#                 return True
#             return False
#         except Exception:
#             return False


# # ======== # code 2 scroll all print profiules


import pytest
import logging
from pages.profiles_page import ProfilesPage

logger = logging.getLogger(__name__)


def test_collect_all_profiles(driver):
    """
    Test to collect all profiles from all tabs with scrolling
    """
    logger.info("🚀 Starting profile collection test...")
    
    # Initialize ProfilesPage
    profiles_page = ProfilesPage(driver)
    
    # Open profiles section
    profiles_page.open_profiles()
    
    # Collect all profiles from all tabs
    results = profiles_page.collect_all_profiles_data()
    
    # Assertions
    assert results is not None, "Results should not be None"
    assert "main_profiles" in results, "Should have main profiles"
    assert "recent_visitors" in results, "Should have recent visitors"
    assert "promoted" in results, "Should have promoted profiles"
    assert "preferred" in results, "Should have preferred profiles"
    
    # Verify counts
    assert results["main_profiles"]["total_count"] >= 0
    assert results["recent_visitors"]["total_count"] >= 0
    assert results["promoted"]["total_count"] >= 0
    assert results["preferred"]["total_count"] >= 0
    
    logger.info("✅ Profile collection test completed successfully!")


def test_single_tab_profiles(driver):
    """
    Test to collect profiles from just one tab
    """
    profiles_page = ProfilesPage(driver)
    profiles_page.open_profiles()
    
    # Just collect from main profiles
    logger.info("📋 Collecting main profiles only...")
    profiles, count = profiles_page.get_all_profiles_with_scroll()
    
    logger.info(f"✅ Collected {count} profiles")
    for i, profile in enumerate(profiles, 1):
        logger.info(f"{i}. {profile['name_age']}")
    
    assert count > 0, "Should have at least some profiles"


def test_recent_visitors_only(driver):
    """
    Test to collect only recent visitors
    """
    profiles_page = ProfilesPage(driver)
    profiles_page.open_profiles()
    
    # Go to recent visitors
    profiles_page.open_recent_visitors()
    
    # Collect profiles
    profiles, count = profiles_page.get_all_profiles_with_scroll()
    
    logger.info(f"✅ Recent Visitors Count: {count}")
    for profile in profiles:
        logger.info(f"  - {profile['name_age']}")
    
    # Scroll back to top
    profiles_page.scroll_back_to_top()
    
    assert count >= 0, "Count should be non-negative"