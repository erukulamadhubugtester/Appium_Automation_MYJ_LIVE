# import logging
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from appium.webdriver.common.appiumby import AppiumBy
# from utils.locators import LOCATORS

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)


# class ConnectionsPage:
#     def __init__(self, driver, wait_time=20):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, wait_time)

#     # 1. Open Connections
#     def open_connections(self):
#         try:
#             logger.info("👉 Clicking Connections...")
#             self.wait.until(
#                 EC.element_to_be_clickable(LOCATORS["CONNECTIONS_ICON"])
#             ).click()
#             self.wait.until(
#                 EC.presence_of_element_located(LOCATORS["CONNECTIONS_TITLE"])
#             )
#             logger.info("✅ Connections page opened")
#         except TimeoutException:
#             logger.error("❌ Connections page not loaded")
#             raise

#     # 2. Title
#     def get_connections_title(self):
#         el = self.wait.until(
#             EC.presence_of_element_located(LOCATORS["CONNECTIONS_TITLE"])
#         )
#         logger.info(f"📌 Title: {el.text}")
#         return el.text

#     # 3. Sent tab
#     def get_sent_tab_text(self):
#         el = self.wait.until(EC.presence_of_element_located(LOCATORS["SENT_TAB"]))
#         logger.info(f"📌 Sent tab: {el.text}")
#         return el.text

#     # 4. Profiles count
#     def get_profiles_count(self):
#         els = self.driver.find_elements(*LOCATORS["PROFILE_CONTAINER"])
#         logger.info(f"👤 Profiles found: {len(els)}")
#         return els, len(els)

#     # 5. Names & Ages
#     def get_profiles_name_age(self):
#         els = self.driver.find_elements(*LOCATORS["PROFILE_NAME_AGE"])
#         profiles = []
#         for i, el in enumerate(els, 1):
#             text = el.text
#             if "," in text:
#                 name, age = text.split(",", 1)
#                 name = name.strip()
#                 age = age.strip()
#             else:
#                 name, age = text, "N/A"
#             profiles.append({"name": name, "age": age})
#             logger.info(f"📝 Profile {i}: Name={name}, Age={age}")
#         return profiles

# ======== 1.a code ================= #

# import logging
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from appium.webdriver.common.appiumby import AppiumBy
# from utils.locators import LOCATORS

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)


# class ConnectionsPage:
#     def __init__(self, driver, wait_time=20):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, wait_time)

#     # 1. Open Connections
#     def open_connections(self):
#         try:
#             logger.info("👉 Clicking Connections...")
#             self.wait.until(
#                 EC.element_to_be_clickable(LOCATORS["CONNECTIONS_ICON"])
#             ).click()
#             self.wait.until(
#                 EC.presence_of_element_located(LOCATORS["CONNECTIONS_TITLE"])
#             )
#             logger.info("✅ Connections page opened")
#         except TimeoutException:
#             logger.error("❌ Connections page not loaded")
#             raise

#     # 2. Title
#     def get_connections_title(self):
#         el = self.wait.until(
#             EC.presence_of_element_located(LOCATORS["CONNECTIONS_TITLE"])
#         )
#         logger.info(f"📌 Title: {el.text}")
#         return el.text

#     # ========>>>>>>=====>>>>>>=======>>>>>>=====  Sent tab
#     def get_sent_tab_text(self):
#         el = self.wait.until(EC.presence_of_element_located(LOCATORS["SENT_TAB"]))
#         text = el.text or el.get_attribute("content-desc")
#         logger.info(f"📌 Sent tab: {text}")
#         return text

#     # 4. Profiles count
#     def get_profiles_count(self):
#         els = self.driver.find_elements(*LOCATORS["PROFILE_CONTAINER"])
#         logger.info(f"👤 Profiles found: {len(els)}")
#         return els, len(els)

#     # 5. Scroll Down utility
#     def _scroll_down(self):
#         size = self.driver.get_window_size()
#         start_x = size["width"] // 2
#         start_y = int(size["height"] * 0.8)
#         end_y = int(size["height"] * 0.2)
#         self.driver.swipe(start_x, start_y, start_x, end_y, 800)
#         time.sleep(1)

#     # 6. Names & Ages with Scroll
#     def get_profiles_name_age(self):
#         profiles = []
#         seen = set()
#         scroll_attempts = 0
#         max_scrolls = 10  # safeguard

#         while scroll_attempts < max_scrolls:
#             els = self.driver.find_elements(*LOCATORS["PROFILE_NAME_AGE"])
#             new_profiles_found = False

#             for el in els:
#                 text = el.text
#                 if text and text not in seen:
#                     seen.add(text)
#                     if "," in text:
#                         name, age = text.split(",", 1)
#                         name = name.strip()
#                         age = age.strip()
#                     else:
#                         name, age = text, "N/A"

#                     profiles.append({"name": name, "age": age})
#                     logger.info(f"📝 Profile: Name={name}, Age={age}")
#                     new_profiles_found = True

#             # Try scroll
#             old_count = len(seen)
#             self._scroll_down()
#             time.sleep(1)

#             # After scroll, check if new profiles loaded
#             if len(seen) == old_count:
#                 scroll_attempts += 1
#                 logger.info("⚠️ No new profiles loaded after scroll")
#             else:
#                 scroll_attempts = 0  # reset if new profiles loaded

#         logger.info(f"✅ Total profiles collected: {len(profiles)}")
#         return profiles


# ======== 1.b ======

# ========>>>>>>=====>>>>>>=======>>>>>>=====  Received tab

# import logging
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
# from selenium.webdriver.common.actions import interaction
# from selenium.webdriver.common.actions.action_builder import ActionBuilder
# from selenium.webdriver.common.actions.pointer_input import PointerInput
# from utils.locators import LOCATORS

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)


# class ConnectionsPage:
#     def __init__(self, driver, wait_time=20):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, wait_time)

#     # ---- Open Connections ----
#     def open_connections(self):
#         logger.info("👉 Clicking Connections...")
#         self.wait.until(
#             EC.element_to_be_clickable(LOCATORS["CONNECTIONS_ICON"])
#         ).click()
#         self.wait.until(EC.presence_of_element_located(LOCATORS["CONNECTIONS_TITLE"]))
#         logger.info("✅ Connections page opened")

#     def get_connections_title(self):
#         el = self.wait.until(
#             EC.presence_of_element_located(LOCATORS["CONNECTIONS_TITLE"])
#         )
#         logger.info(f"📌 Title: {el.text}")
#         return el.text

#     # ---- Tab Handling ----
#     def click_tab(self, tab_name):
#         """
#         Click a tab safely ('Sent', 'Received', 'Connected') and return its text.
#         Handles stale elements by retrying.
#         """
#         locator_key = f"{tab_name.upper()}_TAB"
#         if locator_key not in LOCATORS:
#             raise ValueError(f"Locator for tab '{tab_name}' not found")

#         for attempt in range(3):
#             try:
#                 el = self.wait.until(EC.element_to_be_clickable(LOCATORS[locator_key]))
#                 el.click()
#                 time.sleep(1)  # wait for tab content
#                 # re-locate element after click
#                 el = self.wait.until(
#                     EC.presence_of_element_located(LOCATORS[locator_key])
#                 )
#                 text = el.text or el.get_attribute("content-desc")
#                 logger.info(f"📌 Clicked {tab_name} tab, text: {text}")
#                 return text
#             except StaleElementReferenceException:
#                 logger.warning(f"⚠️ Stale element, retrying click on {tab_name} tab...")
#                 time.sleep(1)
#         raise TimeoutException(f"❌ Unable to click {tab_name} tab after retries")

#     # ---- Profile Handling ----
#     def get_profiles(self, max_scrolls=20):
#         """
#         Collect all profiles in current tab, scrolling down if needed.
#         Returns list of dicts: [{'name': 'X', 'age': 'Y yrs'}, ...]
#         """
#         all_profiles = []
#         seen_profiles = set()
#         scroll_count = 0
#         no_new_profiles_count = 0

#         while scroll_count < max_scrolls:
#             els = self.driver.find_elements(*LOCATORS["PROFILE_CONTAINER"])
#             logger.info(f"👤 Found {len(els)} profile containers on screen")

#             new_profiles_found = 0
#             for el in els:
#                 name_age_els = el.find_elements(*LOCATORS["PROFILE_NAME_AGE"])
#                 for na in name_age_els:
#                     text = na.text
#                     if "," in text:
#                         name, age = text.split(",", 1)
#                         name = name.strip()
#                         age = age.strip()
#                         profile_id = f"{name}_{age}"
#                         if profile_id not in seen_profiles:
#                             all_profiles.append({"name": name, "age": age})
#                             seen_profiles.add(profile_id)
#                             new_profiles_found += 1
#                             logger.info(f"📝 Profile: Name={name}, Age={age}")

#             if new_profiles_found == 0:
#                 no_new_profiles_count += 1
#                 if (
#                     no_new_profiles_count >= 2
#                 ):  # stop if no new profiles after 2 scrolls
#                     logger.info("✅ No new profiles found, reached end of list")
#                     break
#             else:
#                 no_new_profiles_count = 0

#             if len(els) > 0:
#                 self.scroll_down()
#                 scroll_count += 1
#                 time.sleep(1)
#             else:
#                 break

#         logger.info(f"✅ Total profiles collected: {len(all_profiles)}")
#         return all_profiles

#     # ---- Scrolling (Updated to W3C Actions) ----
#     def scroll_down(self, duration=800):
#         """
#         Scroll down the screen using W3C Actions API.
#         duration in ms, default 800ms.
#         """
#         size = self.driver.get_window_size()
#         start_x = size["width"] // 2
#         start_y = int(size["height"] * 0.8)
#         end_y = int(size["height"] * 0.2)

#         try:
#             actions = ActionBuilder(
#                 self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
#             )
#             actions.pointer_action.move_to_location(start_x, start_y)
#             actions.pointer_action.pointer_down()
#             actions.pointer_action.pause(duration / 1000)  # Convert ms to seconds
#             actions.pointer_action.move_to_location(start_x, end_y)
#             actions.pointer_action.release()
#             actions.perform()
#             logger.info(f"⬇️ Scrolled down from y={start_y} to y={end_y}")
#         except Exception as e:
#             logger.warning(f"⚠️ Scroll down failed: {e}")
#         time.sleep(0.5)

#     def scroll_up(self, duration=800):
#         """Scroll up using W3C Actions API"""
#         size = self.driver.get_window_size()
#         start_x = size["width"] // 2
#         start_y = int(size["height"] * 0.2)
#         end_y = int(size["height"] * 0.8)

#         try:
#             actions = ActionBuilder(
#                 self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
#             )
#             actions.pointer_action.move_to_location(start_x, start_y)
#             actions.pointer_action.pointer_down()
#             actions.pointer_action.pause(duration / 1000)  # Convert ms to seconds
#             actions.pointer_action.move_to_location(start_x, end_y)
#             actions.pointer_action.release()
#             actions.perform()
#             logger.info(f"⬆️ Scrolled up from y={start_y} to y={end_y}")
#         except Exception as e:
#             logger.warning(f"⚠️ Scroll up failed: {e}")
#         time.sleep(0.5)

#     # ---- Scroll to Top ----
#     def scroll_to_top(self, max_scrolls=5):
#         logger.info("⬆️ Scrolling back to top...")
#         for _ in range(max_scrolls):
#             self.scroll_up()


import logging
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from utils.locators import LOCATORS

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class ConnectionsPage:
    def __init__(self, driver, wait_time=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_time)

    # ---- Open Connections ----
    def open_connections(self):
        logger.info("👉 Clicking Connections...")
        self.wait.until(
            EC.element_to_be_clickable(LOCATORS["CONNECTIONS_ICON"])
        ).click()
        self.wait.until(EC.presence_of_element_located(LOCATORS["CONNECTIONS_TITLE"]))
        logger.info("✅ Connections page opened")

    def get_connections_title(self):
        el = self.wait.until(
            EC.presence_of_element_located(LOCATORS["CONNECTIONS_TITLE"])
        )
        logger.info(f"📌 Title: {el.text}")
        return el.text

    # ---- Tab Handling ----
    def click_tab(self, tab_name: str):
        """
        Click a tab safely ('Sent', 'Received', 'Connected') and return its text.
        Handles stale elements by retrying.
        """
        locator_key = f"{tab_name.upper()}_TAB"
        if locator_key not in LOCATORS:
            raise ValueError(f"Locator for tab '{tab_name}' not found in LOCATORS")

        for attempt in range(3):
            try:
                el = self.wait.until(EC.element_to_be_clickable(LOCATORS[locator_key]))
                el.click()
                time.sleep(1)  # wait for tab content to load
                el = self.wait.until(
                    EC.presence_of_element_located(LOCATORS[locator_key])
                )
                text = el.text or el.get_attribute("content-desc")
                logger.info(f"📌 Clicked {tab_name} tab, text: {text}")
                return text
            except StaleElementReferenceException:
                logger.warning(f"⚠️ Stale element, retrying click on {tab_name} tab...")
                time.sleep(1)
        raise TimeoutException(f"❌ Unable to click {tab_name} tab after retries")

    # ---- Profile Handling ----
    def get_profiles(self, max_scrolls=20):
        """
        Collect all profiles in current tab, scrolling down if needed.
        Returns list of dicts: [{'name': 'X', 'age': 'Y yrs'}, ...]
        """
        all_profiles = []
        seen_profiles = set()
        scroll_count = 0
        no_new_profiles_count = 0

        while scroll_count < max_scrolls:
            # ✅ FIX: use AppiumBy explicitly
            els = self.driver.find_elements(
                AppiumBy.XPATH, LOCATORS["PROFILE_CONTAINER"]
            )
            logger.info(f"👤 Found {len(els)} profile containers on screen")

            new_profiles_found = 0
            for el in els:
                try:
                    name_age_els = el.find_elements(
                        AppiumBy.XPATH, LOCATORS["PROFILE_NAME_AGE"]
                    )
                    for na in name_age_els:
                        text = na.text.strip()
                        if "," in text:
                            name, age = text.split(",", 1)
                            name = name.strip()
                            age = age.strip()
                            profile_id = f"{name}_{age}"
                            if profile_id not in seen_profiles:
                                all_profiles.append({"name": name, "age": age})
                                seen_profiles.add(profile_id)
                                new_profiles_found += 1
                                logger.info(f"📝 Profile: Name={name}, Age={age}")
                except Exception as e:
                    logger.warning(f"⚠️ Failed to parse profile container: {e}")
                    continue

            if new_profiles_found == 0:
                no_new_profiles_count += 1
                if no_new_profiles_count >= 2:
                    logger.info("✅ No new profiles found, reached end of list")
                    break
            else:
                no_new_profiles_count = 0

            if els:
                self.scroll_down()
                scroll_count += 1
                time.sleep(1)
            else:
                break

        logger.info(f"✅ Total profiles collected: {len(all_profiles)}")
        return all_profiles

    # ---- Scrolling (W3C Actions) ----
    def scroll_down(self, duration=800):
        """
        Scroll down the screen using W3C Actions API.
        duration in ms (default 800ms).
        """
        size = self.driver.get_window_size()
        start_x = size["width"] // 2
        start_y = int(size["height"] * 0.8)
        end_y = int(size["height"] * 0.2)

        try:
            actions = ActionBuilder(
                self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
            )
            actions.pointer_action.move_to_location(start_x, start_y)
            actions.pointer_action.pointer_down()
            actions.pointer_action.pause(duration / 1000)
            actions.pointer_action.move_to_location(start_x, end_y)
            actions.pointer_action.release()
            actions.perform()
            logger.info(f"⬇️ Scrolled down from y={start_y} to y={end_y}")
        except Exception as e:
            logger.warning(f"⚠️ Scroll down failed: {e}")
        time.sleep(0.5)

    def scroll_up(self, duration=800):
        """Scroll up using W3C Actions API"""
        size = self.driver.get_window_size()
        start_x = size["width"] // 2
        start_y = int(size["height"] * 0.2)
        end_y = int(size["height"] * 0.8)

        try:
            actions = ActionBuilder(
                self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
            )
            actions.pointer_action.move_to_location(start_x, start_y)
            actions.pointer_action.pointer_down()
            actions.pointer_action.pause(duration / 1000)
            actions.pointer_action.move_to_location(start_x, end_y)
            actions.pointer_action.release()
            actions.perform()
            logger.info(f"⬆️ Scrolled up from y={start_y} to y={end_y}")
        except Exception as e:
            logger.warning(f"⚠️ Scroll up failed: {e}")
        time.sleep(0.5)

    # ---- Scroll to Top ----
    def scroll_to_top(self, max_scrolls=5):
        logger.info("⬆️ Scrolling back to top...")
        for _ in range(max_scrolls):
            self.scroll_up()
