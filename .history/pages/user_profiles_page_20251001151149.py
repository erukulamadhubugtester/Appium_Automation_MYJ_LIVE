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


# import logging
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import (
#     StaleElementReferenceException,
#     TimeoutException,
# )
# from appium.webdriver.common.appiumby import AppiumBy
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions import interaction
# from selenium.webdriver.common.actions.action_builder import ActionBuilder
# from selenium.webdriver.common.actions.pointer_input import PointerInput
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
#         time.sleep(1)

#     def open_promoted(self):
#         logger.info("Clicking Promoted tab...")
#         self.wait.until(EC.element_to_be_clickable(LOCATORS["PROMOTED_TAB"])).click()
#         time.sleep(1)

#     def open_preferred(self):
#         logger.info("Clicking Preferred tab...")
#         self.wait.until(EC.element_to_be_clickable(LOCATORS["PREFERRED_TAB"])).click()
#         time.sleep(1)

#     # ---- Scrolling Functions ----
#     def scroll_down(self, duration=800):
#         """Scroll down on the screen"""
#         size = self.driver.get_window_size()
#         start_x = size["width"] // 2
#         start_y = int(size["height"] * 0.8)
#         end_y = int(size["height"] * 0.2)

#         actions = ActionChains(self.driver)
#         actions.w3c_actions = ActionBuilder(
#             self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
#         )
#         actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
#         actions.w3c_actions.pointer_action.pointer_down()
#         actions.w3c_actions.pointer_action.pause(0.1)
#         actions.w3c_actions.pointer_action.move_to_location(start_x, end_y)
#         actions.w3c_actions.pointer_action.release()
#         actions.perform()
#         time.sleep(0.5)

#     def scroll_up(self, duration=800):
#         """Scroll up on the screen"""
#         size = self.driver.get_window_size()
#         start_x = size["width"] // 2
#         start_y = int(size["height"] * 0.2)
#         end_y = int(size["height"] * 0.8)

#         actions = ActionChains(self.driver)
#         actions.w3c_actions = ActionBuilder(
#             self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
#         )
#         actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
#         actions.w3c_actions.pointer_action.pointer_down()
#         actions.w3c_actions.pointer_action.pause(0.1)
#         actions.w3c_actions.pointer_action.move_to_location(start_x, end_y)
#         actions.w3c_actions.pointer_action.release()
#         actions.perform()
#         time.sleep(0.5)

#     # ---- Profile data with scrolling ----
#     def get_current_visible_profiles(self):
#         """Get profiles currently visible on screen"""
#         try:
#             self.wait.until(
#                 EC.presence_of_all_elements_located(LOCATORS["PROFILE_CARD"])
#             )
#             cards = self.driver.find_elements(*LOCATORS["PROFILE_CARD"])
#             profiles = []

#             for card in cards:
#                 try:
#                     name_age = card.get_attribute("content-desc") or ""
#                     if name_age.strip():
#                         profiles.append({"name_age": name_age.strip()})
#                 except Exception as e:
#                     logger.warning(f"⚠️ Failed to parse card: {e}")

#             return profiles
#         except Exception as e:
#             logger.warning(f"⚠️ Error getting profiles: {e}")
#             return []

#     def get_all_profiles_with_scroll(self, max_scrolls=20):
#         """
#         Scroll down and collect all unique profiles
#         Returns: list of profile dicts and total count
#         """
#         logger.info("📜 Starting to collect all profiles with scrolling...")
#         all_profiles = []
#         seen_profiles = set()
#         no_new_profiles_count = 0
#         scroll_count = 0

#         while scroll_count < max_scrolls:
#             # Get current visible profiles
#             current_profiles = self.get_current_visible_profiles()

#             # Track new profiles
#             new_profiles_found = 0
#             for profile in current_profiles:
#                 profile_id = profile["name_age"]
#                 if profile_id not in seen_profiles:
#                     seen_profiles.add(profile_id)
#                     all_profiles.append(profile)
#                     new_profiles_found += 1
#                     logger.info(f"📝 Profile {len(all_profiles)}: {profile_id}")

#             # Check if we found new profiles
#             if new_profiles_found == 0:
#                 no_new_profiles_count += 1
#                 logger.info(
#                     f"⚠️ No new profiles found (attempt {no_new_profiles_count}/3)"
#                 )
#                 if no_new_profiles_count >= 3:
#                     logger.info("✅ Reached end of profiles")
#                     break
#             else:
#                 no_new_profiles_count = 0

#             # Scroll down
#             scroll_count += 1
#             logger.info(f"⬇️ Scrolling down ({scroll_count}/{max_scrolls})...")
#             self.scroll_down()
#             time.sleep(1)

#         logger.info(f"✅ Total profiles collected: {len(all_profiles)}")
#         return all_profiles, len(all_profiles)

#     def scroll_back_to_top(self, max_scrolls=10):
#         """Scroll back to top of the list"""
#         logger.info("⬆️ Scrolling back to top...")
#         for i in range(max_scrolls):
#             self.scroll_up()
#             time.sleep(0.3)
#         logger.info("✅ Scrolled back to top")

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

#     # ---- Complete Profile Collection Flow ----
#     def collect_all_profiles_data(self):
#         """
#         Complete flow: collect profiles from all tabs
#         Returns: dict with all tab data
#         """
#         results = {}

#         # 1. Main Profiles Tab
#         logger.info("\n" + "=" * 60)
#         logger.info("📋 COLLECTING: Main Profiles")
#         logger.info("=" * 60)
#         profiles, count = self.get_all_profiles_with_scroll()
#         results["main_profiles"] = {"profiles": profiles, "total_count": count}
#         self.scroll_back_to_top()
#         time.sleep(2)

#         # 2. Recent Visitors Tab
#         logger.info("\n" + "=" * 60)
#         logger.info("📋 COLLECTING: Recent Visitors")
#         logger.info("=" * 60)
#         self.open_recent_visitors()
#         time.sleep(2)
#         profiles, count = self.get_all_profiles_with_scroll()
#         results["recent_visitors"] = {"profiles": profiles, "total_count": count}
#         self.scroll_back_to_top()
#         time.sleep(2)

#         # 3. Promoted Tab
#         logger.info("\n" + "=" * 60)
#         logger.info("📋 COLLECTING: Promoted Profiles")
#         logger.info("=" * 60)
#         self.open_promoted()
#         time.sleep(2)
#         profiles, count = self.get_all_profiles_with_scroll()
#         results["promoted"] = {"profiles": profiles, "total_count": count}
#         self.scroll_back_to_top()
#         time.sleep(2)

#         # 4. Preferred Tab
#         logger.info("\n" + "=" * 60)
#         logger.info("📋 COLLECTING: Preferred Profiles")
#         logger.info("=" * 60)
#         self.open_preferred()
#         time.sleep(2)
#         profiles, count = self.get_all_profiles_with_scroll()
#         results["preferred"] = {"profiles": profiles, "total_count": count}
#         self.scroll_back_to_top()

#         # Print Summary
#         self._print_summary(results)

#         return results

#     def _print_summary(self, results):
#         """Print summary of all collected profiles"""
#         logger.info("\n" + "=" * 60)
#         logger.info("📊 COLLECTION SUMMARY")
#         logger.info("=" * 60)

#         for tab_name, data in results.items():
#             logger.info(f"\n{tab_name.upper().replace('_', ' ')}:")
#             logger.info(f"  Total Count: {data['total_count']}")
#             logger.info(f"  Profiles:")
#             for i, profile in enumerate(data["profiles"], 1):
#                 logger.info(f"    {i}. {profile['name_age']}")

#         logger.info("\n" + "=" * 60)
#         total = sum(data["total_count"] for data in results.values())
#         logger.info(f"🎯 GRAND TOTAL: {total} profiles")
#         logger.info("=" * 60 + "\n")


