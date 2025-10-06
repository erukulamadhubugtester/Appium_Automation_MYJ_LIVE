# import logging
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.actions import interaction
# from selenium.webdriver.common.actions.action_builder import ActionBuilder
# from selenium.webdriver.common.actions.pointer_input import PointerInput
# from utils.locators import LOCATORS

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)


# class SearchPage:
#     def __init__(self, driver, wait_time=20):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, wait_time)

#     def _tap_element(self, element):
#         """Tap on an element using W3C actions"""
#         actions = ActionBuilder(
#             self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
#         )
#         actions.pointer_action.move_to(element)
#         actions.pointer_action.pointer_down()
#         actions.pointer_action.pointer_up()
#         actions.perform()

#     # ---- Open Search ----
#     def open_search(self):
#         """Click on the Search icon and wait for the input field to appear"""
#         logger.info("👉 Clicking Search icon...")
#         try:
#             search_icon = self.wait.until(
#                 EC.element_to_be_clickable(LOCATORS["SEARCH_ICON"])
#             )
#             self._tap_element(search_icon)
#             logger.info("✅ Search icon clicked")
#         except TimeoutException:
#             logger.error("❌ SEARCH_ICON not found or clickable")
#             raise

#         # Wait for input field
#         self.wait.until(EC.presence_of_element_located(LOCATORS["SEARCH_INPUT"]))
#         logger.info("✅ Search input visible")

#     # ---- Titles ----
#     def get_promoted_profiles_title(self):
#         try:
#             el = self.wait.until(
#                 EC.presence_of_element_located(LOCATORS["PROMOTED_PROFILES_TITLE"])
#             )
#             logger.info(f"📌 Promoted Profiles Title: {el.text}")
#             return el.text
#         except TimeoutException:
#             logger.warning("⚠️ Promoted Profiles title not found")
#             return None

#     def get_vip_profiles_title(self):
#         try:
#             el = self.wait.until(
#                 EC.presence_of_element_located(LOCATORS["VIP_PROFILES_TITLE"])
#             )
#             logger.info(f"📌 VIP Profiles Title: {el.text}")
#             return el.text
#         except TimeoutException:
#             logger.warning("⚠️ VIP Profiles title not found")
#             return None

#     # ---- Search ----
#     def enter_search_text(self, text):
#         """Type into the search input field"""
#         search_input = self.wait.until(
#             EC.presence_of_element_located(LOCATORS["SEARCH_INPUT"])
#         )
#         search_input.clear()
#         search_input.send_keys(text)
#         logger.info(f"🔎 Entered text: {text}")
#         time.sleep(1)

#     def click_search_icon(self):
#         """Click search button after entering text"""
#         try:
#             search_icon = self.wait.until(
#                 EC.element_to_be_clickable(LOCATORS["SEARCH_ICON2"])
#             )
#             self._tap_element(search_icon)
#             logger.info("✅ Search icon clicked")
#             time.sleep(2)
#         except TimeoutException:
#             logger.warning("⚠️ Search icon not found or clickable")

#     # ---- Get Profiles ----
#     def get_profiles(self, max_scrolls=10):
#         all_profiles = []
#         seen_profiles = set()
#         scroll_count = 0

#         while scroll_count < max_scrolls:
#             containers = self.driver.find_elements(*LOCATORS["PROFILE_CONTAINER"])
#             if not containers:
#                 logger.info("✅ No profile container found, stopping scroll")
#                 break

#             new_found = 0
#             for container in containers:
#                 try:
#                     name_el = container.find_element(*LOCATORS["PROFILE_NAME"])
#                     name = name_el.text.strip()
#                     if name not in seen_profiles:
#                         all_profiles.append(name)
#                         seen_profiles.add(name)
#                         new_found += 1
#                         logger.info(f"📝 Profile found: {name}")
#                 except:
#                     continue

#             if new_found == 0:
#                 logger.info("✅ No new profiles found, reached end of list")
#                 break

#             self.scroll_down()
#             scroll_count += 1
#             time.sleep(1)

#         logger.info(f"✅ Total profiles collected: {len(all_profiles)}")
#         return all_profiles

#     # ---- Scroll ----
#     def scroll_down(self, duration=800):
#         """Simple swipe down"""
#         size = self.driver.get_window_size()
#         start_x = size["width"] // 2
#         start_y = int(size["height"] * 0.8)
#         end_y = int(size["height"] * 0.2)
#         self.driver.swipe(start_x, start_y, start_x, end_y, duration)
#         logger.info("⬇️ Scrolled down")
#         time.sleep(0.5)


# ======= top code less data showing


# ========= code 2 printed all profile

import logging
import time
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from utils.locators import LOCATORS

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class SearchPage:
    def __init__(self, driver, wait_time=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_time)

    def _tap_element(self, element):
        """Tap on an element using W3C actions"""
        actions = ActionBuilder(
            self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
        )
        actions.pointer_action.move_to(element)
        actions.pointer_action.pointer_down()
        actions.pointer_action.pointer_up()
        actions.perform()

    def _is_valid_profile_name(self, text):
        """
        Validate if the text is a valid profile name.
        Expected format: "Name, XX yrs" or similar
        """
        if not text or len(text.strip()) < 3:
            return False

        # Filter out common non-profile texts
        invalid_keywords = [
            "punjab",
            "gujarat",
            "maharashtra",
            "delhi",
            "karnataka",
            "post graduate",
            "graduate",
            "diploma",
            "phd",
            "hindu",
            "muslim",
            "christian",
            "sikh",
            "buddhist",
            "na",
            "n/a",
            "not available",
        ]

        text_lower = text.lower().strip()
        if text_lower in invalid_keywords:
            return False

        # Check if it contains age pattern (XX yrs or XX years)
        age_pattern = r"\d{2,3}\s*(yrs?|years?)"
        if re.search(age_pattern, text, re.IGNORECASE):
            return True

        # If no age but has comma and reasonable length, might be valid
        if "," in text and len(text.split(",")[0].strip()) > 2:
            return True

        return False

    # ---- Open Search ----
    def open_search(self):
        """Click on the Search icon and wait for the input field to appear"""
        logger.info("👉 Clicking Search icon...")
        try:
            search_icon = self.wait.until(
                EC.element_to_be_clickable(LOCATORS["SEARCH_ICON"])
            )
            self._tap_element(search_icon)
            logger.info("✅ Search icon clicked")
        except TimeoutException:
            logger.error("❌ SEARCH_ICON not found or clickable")
            raise

        # Wait for input field
        self.wait.until(EC.presence_of_element_located(LOCATORS["SEARCH_INPUT"]))
        logger.info("✅ Search input visible")

    # ---- Titles ----
    def get_promoted_profiles_title(self):
        try:
            el = self.wait.until(
                EC.presence_of_element_located(LOCATORS["PROMOTED_PROFILES_TITLE"])
            )
            logger.info(f"📌 Promoted Profiles Title: {el.text}")
            return el.text
        except TimeoutException:
            logger.warning("⚠️ Promoted Profiles title not found")
            return None

    def get_vip_profiles_title(self):
        try:
            el = self.wait.until(
                EC.presence_of_element_located(LOCATORS["VIP_PROFILES_TITLE"])
            )
            logger.info(f"📌 VIP Profiles Title: {el.text}")
            return el.text
        except TimeoutException:
            logger.warning("⚠️ VIP Profiles title not found")
            return None

    # ---- Search ----
    def enter_search_text(self, text):
        """Type into the search input field"""
        search_input = self.wait.until(
            EC.presence_of_element_located(LOCATORS["SEARCH_INPUT"])
        )
        search_input.clear()
        search_input.send_keys(text)
        logger.info(f"🔎 Entered text: {text}")
        time.sleep(1)

    def click_search_icon(self):
        """Click search button after entering text"""
        try:
            search_icon = self.wait.until(
                EC.element_to_be_clickable(LOCATORS["SEARCH_ICON2"])
            )
            self._tap_element(search_icon)
            logger.info("✅ Search icon clicked")
            time.sleep(2)
        except TimeoutException:
            logger.warning("⚠️ Search icon not found or clickable")

    # ---- Get Profiles ----
    def get_profiles(self, max_scrolls=100, scroll_pause=2.5, max_no_new_attempts=5):
        """
        Collect ALL profile names by scrolling to the very last profile

        Args:
            max_scrolls: Maximum number of scroll attempts (high limit as safety)
            scroll_pause: Time to wait after each scroll for content to load
            max_no_new_attempts: Stop after this many consecutive scrolls with no new profiles
        """
        all_profiles = []
        seen_profiles = set()
        scroll_count = 0
        no_new_profiles_count = 0
        last_profile_count = 0

        logger.info(
            f"🔍 Starting profile collection - will scroll until the very end..."
        )
        logger.info(
            f"⚙️ Settings: max_scrolls={max_scrolls}, scroll_pause={scroll_pause}s, stop_after={max_no_new_attempts} empty scrolls"
        )

        while scroll_count < max_scrolls:
            # Find all profile containers
            containers = self.driver.find_elements(*LOCATORS["PROFILE_CONTAINER"])

            if not containers:
                logger.info("⚠️ No profile containers found")
                break

            new_found = 0
            for idx, container in enumerate(containers):
                try:
                    # Try to find name element within container
                    name_el = container.find_element(*LOCATORS["PROFILE_NAME"])
                    name = name_el.text.strip()

                    # Validate and add if new
                    if (
                        name
                        and self._is_valid_profile_name(name)
                        and name not in seen_profiles
                    ):
                        all_profiles.append(name)
                        seen_profiles.add(name)
                        new_found += 1
                        logger.info(f"📝 Profile #{len(all_profiles)}: {name}")
                    elif name and not self._is_valid_profile_name(name):
                        logger.debug(f"⏭️ Skipped invalid text: {name}")

                except NoSuchElementException:
                    logger.debug(f"⚠️ Container {idx} has no name element")
                    continue
                except Exception as e:
                    logger.debug(f"⚠️ Error processing container {idx}: {str(e)}")
                    continue

            # Check if we found new profiles
            if new_found == 0:
                no_new_profiles_count += 1
                logger.info(
                    f"⚠️ No new profiles found (attempt {no_new_profiles_count}/{max_no_new_attempts})"
                )

                # Stop if no new profiles for max_no_new_attempts consecutive scrolls
                if no_new_profiles_count >= max_no_new_attempts:
                    logger.info(
                        f"🏁 REACHED THE END! No new profiles for {max_no_new_attempts} consecutive scrolls"
                    )
                    break
            else:
                no_new_profiles_count = 0  # Reset counter
                logger.info(
                    f"✨ Found {new_found} new profiles | Total so far: {len(all_profiles)}"
                )

            # Log progress every 10 scrolls
            if scroll_count % 10 == 0 and scroll_count > 0:
                logger.info(
                    f"📊 Progress: {len(all_profiles)} profiles collected after {scroll_count} scrolls"
                )

            # Scroll and wait
            self.scroll_down()
            scroll_count += 1
            time.sleep(scroll_pause)  # Wait for content to load

        logger.info(f"✅ Profile collection complete!")
        logger.info(f"📊 Total valid profiles collected: {len(all_profiles)}")
        logger.info(f"📊 Total scroll attempts: {scroll_count}")
        logger.info(
            f"📊 Average profiles per scroll: {len(all_profiles)/scroll_count:.2f}"
            if scroll_count > 0
            else "N/A"
        )

        return all_profiles

    def get_all_profile_details(
        self, max_scrolls=100, scroll_pause=2.5, max_no_new_attempts=5
    ):
        """
        Get detailed information for EVERY profile until the very end
        Returns list of dictionaries with profile details

        Args:
            max_scrolls: Maximum scroll attempts (safety limit)
            scroll_pause: Seconds to wait after scrolling
            max_no_new_attempts: Stop after this many empty scrolls
        """
        all_profiles = []
        seen_profile_ids = set()
        scroll_count = 0
        no_new_profiles_count = 0

        logger.info(
            f"🔍 Starting detailed profile collection - scrolling to the very end..."
        )

        while scroll_count < max_scrolls:
            containers = self.driver.find_elements(*LOCATORS["PROFILE_CONTAINER"])

            if not containers:
                break

            new_found = 0
            for container in containers:
                try:
                    # Get profile ID or unique identifier
                    profile_id = container.get_attribute(
                        "resource-id"
                    ) or container.get_attribute("content-desc")

                    if profile_id in seen_profile_ids:
                        continue

                    # Extract profile details
                    profile_data = {}

                    # Name
                    try:
                        name_el = container.find_element(*LOCATORS["PROFILE_NAME"])
                        profile_data["name"] = name_el.text.strip()
                    except:
                        continue  # Skip if no name

                    # Validate name
                    if not self._is_valid_profile_name(profile_data["name"]):
                        continue

                    # Add profile
                    all_profiles.append(profile_data)
                    seen_profile_ids.add(
                        profile_id if profile_id else profile_data["name"]
                    )
                    new_found += 1

                    logger.info(f"📝 Profile #{len(all_profiles)}: {profile_data}")

                except Exception as e:
                    continue

            if new_found == 0:
                no_new_profiles_count += 1
                logger.info(
                    f"⚠️ No new profiles found (attempt {no_new_profiles_count}/{max_no_new_attempts})"
                )
                if no_new_profiles_count >= max_no_new_attempts:
                    logger.info(
                        f"🏁 REACHED THE END! No new profiles for {max_no_new_attempts} consecutive scrolls"
                    )
                    break
            else:
                no_new_profiles_count = 0
                logger.info(
                    f"✨ Found {new_found} new profiles | Total: {len(all_profiles)}"
                )

            # Progress update
            if scroll_count % 10 == 0 and scroll_count > 0:
                logger.info(
                    f"📊 Progress: {len(all_profiles)} profiles after {scroll_count} scrolls"
                )

            self.scroll_down()
            scroll_count += 1
            time.sleep(scroll_pause)

        logger.info(f"✅ Total detailed profiles collected: {len(all_profiles)}")
        logger.info(f"📊 Total scrolls: {scroll_count}")
        return all_profiles

    # ---- Scroll ----
    def scroll_down(self, duration=1000):
        """
        Smooth swipe down to load more content
        Increased duration for better content loading
        """
        size = self.driver.get_window_size()
        start_x = size["width"] // 2
        start_y = int(size["height"] * 0.8)
        end_y = int(size["height"] * 0.2)
        self.driver.swipe(start_x, start_y, start_x, end_y, duration)
        logger.debug("⬇️ Scrolled down")
        time.sleep(0.5)

    def scroll_to_bottom_slowly(self, small_scrolls=3):
        """
        Make multiple small scrolls to ensure content loads properly
        Useful when reaching the end of list
        """
        for i in range(small_scrolls):
            size = self.driver.get_window_size()
            start_x = size["width"] // 2
            start_y = int(size["height"] * 0.7)
            end_y = int(size["height"] * 0.4)
            self.driver.swipe(start_x, start_y, start_x, end_y, 500)
            time.sleep(0.3)
        logger.debug(f"⬇️ Made {small_scrolls} small scrolls")
