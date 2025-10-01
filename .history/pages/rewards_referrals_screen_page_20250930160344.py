# # pages/rewards_referrals_page.py
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import (
#     TimeoutException,
#     StaleElementReferenceException,
# )
# from appium.webdriver.common.appiumby import AppiumBy
# from utils.locators import LOCATORS
# import time


# class RewardsReferralsPage:
#     def __init__(self, driver, long_wait=20):
#         self.driver = driver
#         # long_wait used for slow screens
#         self.long_wait = long_wait
#         self.short_wait = 5

#     # ---- helpers ----
#     def _wait_for(self, locator, timeout=None):
#         timeout = timeout if timeout is not None else self.long_wait
#         strategy, value = locator
#         return WebDriverWait(self.driver, timeout).until(
#             EC.presence_of_element_located((strategy, value))
#         )

#     def _get_text(self, locator, timeout=None, retries=2):
#         strategy, value = locator
#         for attempt in range(retries):
#             try:
#                 el = WebDriverWait(self.driver, timeout or self.short_wait).until(
#                     EC.presence_of_element_located((strategy, value))
#                 )
#                 txt = el.text.strip()
#                 return txt
#             except StaleElementReferenceException:
#                 print(
#                     f"⚠️ Stale while reading text for {value}, retry {attempt+1}/{retries}"
#                 )
#             except TimeoutException:
#                 # if not found return None
#                 return None
#         return None

#     def _is_displayed(self, locator, timeout=None):
#         try:
#             el = WebDriverWait(self.driver, timeout or self.short_wait).until(
#                 EC.presence_of_element_located(locator)
#             )
#             return el.is_displayed()
#         except Exception:
#             return False

#     def _click(self, locator, timeout=None, retries=2):
#         strategy, value = locator
#         for attempt in range(retries):
#             try:
#                 el = WebDriverWait(self.driver, timeout or self.short_wait).until(
#                     EC.element_to_be_clickable((strategy, value))
#                 )
#                 el.click()
#                 return True
#             except StaleElementReferenceException:
#                 print(
#                     f"⚠️ Stale element while clicking {value}, retry {attempt+1}/{retries}"
#                 )
#             except TimeoutException:
#                 return False
#             except Exception as e:
#                 print(f"⚠️ Click error for {value}: {e}")
#                 return False
#         return False

#     # ---- public actions / checks ----
#     def open_rr_module(self):
#         """Click the R&R entry tile and wait for the R&R screen to appear."""
#         print("➡️ Opening Rewards & Referrals module...")
#         if self._click(LOCATORS["RR_MODULE_IMAGE"], timeout=self.long_wait):
#             # wait for title
#             try:
#                 WebDriverWait(self.driver, self.long_wait).until(
#                     EC.presence_of_element_located(LOCATORS["RR_TITLE"])
#                 )
#                 print("✅ R&R screen loaded (title detected).")
#                 return True
#             except TimeoutException:
#                 print("❌ R&R screen did not load within timeout after click.")
#                 return False
#         else:
#             # fallback: try tap center of element if available (coordinates)
#             try:
#                 el = self.driver.find_element(*LOCATORS["RR_MODULE_IMAGE"])
#                 r = el.rect
#                 x = r["x"] + r["width"] // 2
#                 y = r["y"] + r["height"] // 2
#                 print(f"🎯 Falling back to tap at {x},{y}")
#                 self.driver.tap([(x, y)])
#                 # wait for title
#                 WebDriverWait(self.driver, self.long_wait).until(
#                     EC.presence_of_element_located(LOCATORS["RR_TITLE"])
#                 )
#                 print("✅ R&R screen loaded after fallback tap.")
#                 return True
#             except Exception as e:
#                 print("❌ Failed to open R&R module (fallback too):", e)
#                 return False

#     def get_title_text(self):
#         txt = self._get_text(LOCATORS["RR_TITLE"], timeout=self.long_wait)
#         print("📌 RR Title:", txt)
#         return txt

#     def is_banner_image_displayed(self):
#         # use UiAutomator selector
#         strategy, value = LOCATORS["RR_BANNER_IMAGE_UIA"]
#         try:
#             el = WebDriverWait(self.driver, self.long_wait).until(
#                 EC.presence_of_element_located((strategy, value))
#             )
#             shown = el.is_displayed()
#             print("📌 Banner image displayed:", shown)
#             return shown
#         except Exception:
#             print("📌 Banner image not found.")
#             return False

#     def get_balance_label(self):
#         txt = self._get_text(LOCATORS["RR_BALANCE_LABEL"], timeout=self.long_wait)
#         print("📌 Balance label:", txt)
#         return txt

#     def get_balance_value(self):
#         txt = self._get_text(LOCATORS["RR_BALANCE_VALUE"], timeout=self.long_wait)
#         print("📌 Balance value:", txt)
#         return txt

#     def is_points_label_displayed(self):
#         shown = self._is_displayed(LOCATORS["RR_POINTS_LABEL"], timeout=self.short_wait)
#         print("📌 Points label displayed:", shown)
#         return shown

#     def get_referral_description(self):
#         txt = self._get_text(LOCATORS["RR_REF_DESC"], timeout=self.long_wait)
#         print("📌 Referral description:", txt)
#         return txt

#     def is_roadmap_displayed(self):
#         shown = self._is_displayed(
#             LOCATORS["RR_ROADMAP_IMAGE"], timeout=self.short_wait
#         )
#         print("📌 Roadmap image displayed:", shown)
#         return shown

#     def get_referral_code(self):
#         # try exact first, then generic contains
#         txt = self._get_text(LOCATORS["RR_REF_CODE_EXACT"], timeout=self.short_wait)
#         if txt:
#             print("📌 Referral code (exact):", txt)
#             return txt
#         txt = self._get_text(LOCATORS["RR_REF_CODE_GENERIC"], timeout=self.short_wait)
#         print("📌 Referral code (generic):", txt)
#         return txt

#     def is_invite_now_displayed(self):
#         shown = self._is_displayed(LOCATORS["RR_INVITE_NOW"], timeout=self.short_wait)
#         print("📌 Invite/Share area displayed:", shown)
#         return shown

#     def is_redemption_history_displayed(self):
#         shown = self._is_displayed(
#             LOCATORS["RR_REDEMPTION_HISTORY"], timeout=self.short_wait
#         )
#         print("📌 Redemption history text displayed:", shown)
#         return shown

#     def collect_all_info(self):
#         """Fetch all important texts/flags and return a dict.
#         Uses longer wait for primary elements because screen can be slow.
#         """
#         out = {}
#         # Ensure the screen is ready (title presence)
#         try:
#             WebDriverWait(self.driver, self.long_wait).until(
#                 EC.presence_of_element_located(LOCATORS["RR_TITLE"])
#             )
#         except TimeoutException:
#             print("⚠️ R&R title not present (screen may not be opened).")

#         out["title"] = self.get_title_text()
#         out["banner_present"] = self.is_banner_image_displayed()
#         out["balance_label"] = self.get_balance_label()
#         out["balance_value"] = self.get_balance_value()
#         out["points_label_present"] = self.is_points_label_displayed()
#         out["referral_description"] = self.get_referral_description()
#         out["roadmap_present"] = self.is_roadmap_displayed()
#         out["referral_code"] = self.get_referral_code()
#         out["invite_now_present"] = self.is_invite_now_displayed()
#         out["redemption_history_present"] = self.is_redemption_history_displayed()

#         return out


# ============ #CODE 2 ============


import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from appium.webdriver.common.appiumby import AppiumBy
from utils.locators import LOCATORS

# setup logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
if not logger.handlers:  # avoid duplicate logs
    console = logging.StreamHandler()
    console.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(console)


class RewardsReferralsPage:
    def __init__(self, driver, long_wait=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, long_wait)
        self.long_wait = long_wait
        self.short_wait = 5

    # ---- helpers ----
    def _wait_for(self, locator, timeout=None):
        timeout = timeout or self.long_wait
        strategy, value = locator
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((strategy, value))
        )

    def _get_text(self, locator, timeout=None, retries=2):
        strategy, value = locator
        for attempt in range(retries):
            try:
                el = WebDriverWait(self.driver, timeout or self.short_wait).until(
                    EC.presence_of_element_located((strategy, value))
                )
                return el.text.strip()
            except StaleElementReferenceException:
                logger.warning(
                    f"Stale element for {value}, retry {attempt+1}/{retries}"
                )
            except TimeoutException:
                return None
        return None

    def _is_displayed(self, locator, timeout=None):
        try:
            el = WebDriverWait(self.driver, timeout or self.short_wait).until(
                EC.presence_of_element_located(locator)
            )
            return el.is_displayed()
        except Exception:
            return False

    def _click(self, locator, timeout=None, retries=2):
        strategy, value = locator
        for attempt in range(retries):
            try:
                el = WebDriverWait(self.driver, timeout or self.short_wait).until(
                    EC.element_to_be_clickable((strategy, value))
                )
                el.click()
                return True
            except StaleElementReferenceException:
                logger.warning(
                    f"Stale element while clicking {value}, retry {attempt+1}/{retries}"
                )
            except TimeoutException:
                return False
            except Exception as e:
                logger.error(f"Click error for {value}: {e}")
                return False
        return False

    # ---- public actions ----
    def open_rr_module(self):
        logger.info("Opening Rewards & Referrals module...")
        if self._click(LOCATORS["RR_MODULE_IMAGE"], timeout=self.long_wait):
            try:
                WebDriverWait(self.driver, self.long_wait).until(
                    EC.presence_of_element_located(LOCATORS["RR_TITLE"])
                )
                logger.info("✅ R&R screen loaded")
                return True
            except TimeoutException:
                logger.error("❌ R&R screen did not load in time")
                return False
        return False

    def get_title_text(self):
        txt = self._get_text(LOCATORS["RR_TITLE"], timeout=self.long_wait)
        logger.info(f"RR Title: {txt}")
        return txt

    def get_balance_label(self):
        return self._get_text(LOCATORS["RR_BALANCE_LABEL"])

    def get_balance_value(self):
        return self._get_text(LOCATORS["RR_BALANCE_VALUE"])

    def get_referral_code(self):
    # Try dynamic locator first
      code = self._get_text(LOCATORS["RR_REF_CODE_GENERIC"])
    if not code:
        # fallback exact locator (demo/test environment)
        code = self._get_text(LOCATORS["RR_REF_CODE_EXACT"])
    logger.info(f"Referral Code: {code}")
    return code


    # ---- collect all info ----
    def collect_all_info(self):
        logger.info("Collecting all R&R info...")
        data = {
            "title": self.get_title_text(),
            "balance_label": self.get_balance_label(),
            "balance_value": self.get_balance_value(),
            "referral_code": self.get_referral_code(),
        }
        logger.info(f"Collected data: {data}")
        return data

    # ---- policy flow ----
    def open_rewards_policy(self):
        logger.info("Clicking three dots menu...")
        self.wait.until(
            EC.presence_of_element_located(tuple(LOCATORS["THREE_DOTS_MENU"]))
        ).click()

        logger.info("Clicking Rewards & Referrals policy...")
        self.wait.until(
            EC.presence_of_element_located(tuple(LOCATORS["REWARDS_POLICY_MENU"]))
        ).click()

        title = self.wait.until(
            EC.presence_of_element_located(tuple(LOCATORS["REWARDS_POLICY_TITLE"]))
        )
        logger.info(f"Policy title: {title.text}")
        return title.text

    def read_policy_text(self):
        number = self.wait.until(
            EC.presence_of_element_located(tuple(LOCATORS["REWARDS_POLICY_NUMBER"]))
        )
        text = self.wait.until(
            EC.presence_of_element_located(tuple(LOCATORS["REWARDS_POLICY_TEXT"]))
        )
        combined = f"{number.text} {text.text}"
        logger.info(f"Policy rule: {combined}")
        return combined

    def back_from_policy(self):
        logger.info("Clicking back arrow...")
        self.wait.until(
            EC.presence_of_element_located(tuple(LOCATORS["BACK_ARROW"]))
        ).click()

    # ---- history flow ----
    def open_rewards_history(self):
        logger.info("Opening rewards redemption history...")
        self.wait.until(
            EC.presence_of_element_located(tuple(LOCATORS["REWARDS_HISTORY_MENU"]))
        ).click()

        title = self.wait.until(
            EC.presence_of_element_located(tuple(LOCATORS["REWARDS_HISTORY_TITLE"]))
        )
        logger.info(f"History title: {title.text}")
        return title.text

    def get_history_items(self):
        logger.info("Fetching history items...")
        items = self.driver.find_elements(*LOCATORS["HISTORY_ITEM_TEXT"])
        times = self.driver.find_elements(*LOCATORS["HISTORY_ITEM_TIME"])
        points = self.driver.find_elements(*LOCATORS["HISTORY_ITEM_POINTS"])

        history = []
        for i in range(len(items)):
            entry = {
                "action": items[i].text if i < len(items) else "",
                "time": times[i].text if i < len(times) else "",
                "points": points[i].text if i < len(points) else "",
            }
            logger.info(f"History entry: {entry}")
            history.append(entry)
        return history
