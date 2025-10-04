# import time
# import logging
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, NoSuchElementException
# from appium.webdriver.common.appiumby import AppiumBy
# from selenium.webdriver.common.actions import interaction
# from selenium.webdriver.common.actions.action_builder import ActionBuilder
# from selenium.webdriver.common.actions.pointer_input import PointerInput
# from utils.locators import LOCATORS

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)


# class ChatPage:
#     def __init__(self, driver, wait_time=20):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, wait_time)

#     # ---- Open Chat Module ----
#     def open_chat_module(self):
#         logger.info("👉 Clicking Chat Module...")
#         chat_icon = self.wait.until(
#             EC.element_to_be_clickable((AppiumBy.XPATH, LOCATORS["CHAT_MODULE_ICON"]))
#         )
#         chat_icon.click()
#         self.wait.until(
#             EC.presence_of_element_located((AppiumBy.XPATH, LOCATORS["CHAT_TITLE"]))
#         )
#         logger.info("✅ Chat screen loaded")

#     # ---- Check elements ----
#     def is_three_dots_displayed(self):
#         try:
#             el = self.wait.until(
#                 EC.presence_of_element_located(
#                     (AppiumBy.XPATH, LOCATORS["CHAT_OPTIONS_THREE_DOTS"])
#                 )
#             )
#             logger.info("✅ Three dots displayed")
#             return True
#         except TimeoutException:
#             logger.warning("⚠️ Three dots not displayed")
#             return False

#     def is_search_field_displayed(self):
#         try:
#             el = self.wait.until(
#                 EC.presence_of_element_located(
#                     (AppiumBy.XPATH, LOCATORS["SEARCH_USERS_FIELD"])
#                 )
#             )
#             logger.info("✅ Search field displayed")
#             return True
#         except TimeoutException:
#             logger.warning("⚠️ Search field not displayed")
#             return False

#     # ---- Scroll and get profiles ----
#     def get_profiles(self, max_scrolls=20):
#         all_profiles = []
#         seen_profiles = set()
#         scroll_count = 0
#         no_new_count = 0

#         while scroll_count < max_scrolls:
#             containers = self.driver.find_elements(
#                 AppiumBy.XPATH, LOCATORS["PROFILE_CONTAINER"]
#             )
#             logger.info(f"👤 Found {len(containers)} profile containers on screen")

#             new_found = 0
#             for container in containers:
#                 try:
#                     name_el = container.find_element(
#                         AppiumBy.XPATH, LOCATORS["PROFILE_NAME"]
#                     )
#                     name = name_el.text.strip()
#                     if name and name not in seen_profiles:
#                         all_profiles.append(name)
#                         seen_profiles.add(name)
#                         new_found += 1
#                         logger.info(f"📝 Profile found: {name}")
#                 except NoSuchElementException:
#                     continue

#             if new_found == 0:
#                 no_new_count += 1
#                 if no_new_count >= 2:
#                     logger.info(
#                         "✅ No new profiles found after scrolling twice, stopping"
#                     )
#                     break
#             else:
#                 no_new_count = 0

#             self.scroll_down()
#             scroll_count += 1
#             time.sleep(1)

#         logger.info(f"✅ Total profiles collected: {len(all_profiles)}")
#         return all_profiles

#     # ---- Scrolling ----
#     def scroll_down(self, duration=800):
#         """Scroll down using W3C Actions API"""
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
#             actions.pointer_action.pause(duration / 1000)
#             actions.pointer_action.move_to_location(start_x, end_y)
#             actions.pointer_action.release()
#             actions.perform()
#             logger.info("⬇️ Scrolled down")
#         except Exception as e:
#             logger.warning(f"⚠️ Scroll down failed: {e}")
#         time.sleep(0.5)

# ========= free and vip =========


import time
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from utils.locators import LOCATORS

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class ChatPage:
    def __init__(self, driver, wait_time=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_time)

    # ---- Open Chat Module ----
    def open_chat_module(self):
        logger.info("👉 Clicking Chat Module...")
        chat_icon = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, LOCATORS["CHAT_MODULE_ICON"]))
        )
        chat_icon.click()
        time.sleep(2)  # Wait for screen transition

        # Check for free member restriction first
        if self.is_free_member_restriction():
            logger.warning("⚠️ Free member restriction detected on chat screen")

        self.wait.until(
            EC.presence_of_element_located((AppiumBy.XPATH, LOCATORS["CHAT_TITLE"]))
        )
        logger.info("✅ Chat screen loaded")

    # ---- Check elements ----
    def is_three_dots_displayed(self):
        try:
            # First check if free member restriction is blocking
            if self.is_free_member_restriction():
                logger.warning(
                    "⚠️ Cannot check three dots - Free member restriction active"
                )
                return False

            el = self.wait.until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, LOCATORS["CHAT_OPTIONS_THREE_DOTS"])
                )
            )
            logger.info("✅ Three dots displayed")
            return True
        except TimeoutException:
            logger.warning("⚠️ Three dots not displayed")
            # Print page source for debugging
            logger.debug("📋 Current page source (first 500 chars):")
            logger.debug(self.driver.page_source[:500])
            return False

    def is_search_field_displayed(self):
        try:
            # First check if free member restriction is blocking
            if self.is_free_member_restriction():
                logger.warning(
                    "⚠️ Cannot check search field - Free member restriction active"
                )
                return False

            el = self.wait.until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, LOCATORS["SEARCH_USERS_FIELD"])
                )
            )
            logger.info("✅ Search field displayed")
            return True
        except TimeoutException:
            logger.warning("⚠️ Search field not displayed")
            return False

    # ---- Check for free member restriction ----
    def is_free_member_restriction(self):
        """Check if profile completion message is displayed (free member restriction)"""
        try:
            # Check for "Complete Your Profile" title
            complete_profile = self.driver.find_elements(
                AppiumBy.XPATH,
                "//android.widget.TextView[contains(@text, 'Complete Your Profile')]",
            )

            # Check for percentage complete message
            percentage_complete = self.driver.find_elements(
                AppiumBy.XPATH,
                "//android.widget.TextView[contains(@text, '% complete')]",
            )

            if complete_profile or percentage_complete:
                logger.warning("⚠️ FREE MEMBER DETECTED - Profile completion required")
                logger.warning("⚠️ Cannot view all profiles - upgrade needed")
                return True
            return False
        except Exception as e:
            logger.debug(f"No restriction message found: {e}")
            return False

    # ---- Scroll and get profiles ----
    def get_profiles(self, max_scrolls=20):
        all_profiles = []
        seen_profiles = set()
        scroll_count = 0
        no_new_count = 0

        # Check for free member restriction at the start
        if self.is_free_member_restriction():
            logger.info(
                "🚫 Stopping profile collection - Free member restriction active"
            )
            return all_profiles

        while scroll_count < max_scrolls:
            # Check for restriction during scrolling
            if self.is_free_member_restriction():
                logger.info("🚫 Free member restriction appeared during scrolling")
                break

            containers = self.driver.find_elements(
                AppiumBy.XPATH, LOCATORS["PROFILE_CONTAINER"]
            )
            logger.info(f"👤 Found {len(containers)} profile containers on screen")

            new_found = 0
            for container in containers:
                try:
                    name_el = container.find_element(
                        AppiumBy.XPATH, LOCATORS["PROFILE_NAME"]
                    )
                    name = name_el.text.strip()
                    if name and name not in seen_profiles:
                        all_profiles.append(name)
                        seen_profiles.add(name)
                        new_found += 1
                        logger.info(f"📝 Profile found: {name}")
                except NoSuchElementException:
                    continue

            if new_found == 0:
                no_new_count += 1
                if no_new_count >= 2:
                    logger.info(
                        "✅ No new profiles found after scrolling twice, stopping"
                    )
                    break
            else:
                no_new_count = 0

            self.scroll_down()
            scroll_count += 1
            time.sleep(1)

        logger.info(f"✅ Total profiles collected: {len(all_profiles)}")
        return all_profiles

    # ---- Scrolling ----
    def scroll_down(self, duration=800):
        """Scroll down using W3C Actions API"""
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
            logger.info("⬇️ Scrolled down")
        except Exception as e:
            logger.warning(f"⚠️ Scroll down failed: {e}")
        time.sleep(0.5)
