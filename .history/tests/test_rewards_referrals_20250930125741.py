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

    # ... keep your other methods (banner, balance, referral, etc.) unchanged ...

    # ---- new flows ----
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
