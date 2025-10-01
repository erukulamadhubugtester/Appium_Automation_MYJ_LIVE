from selenium.common.exceptions import NoSuchElementException
from utils.locators import LOCATORS  # ✅ FIXED import


class App_lanuched:
    def __init__(self, driver):
        self.driver = driver

    def click_make_your_jodi(self):
        try:
            el = self.driver.find_element(*LOCATORS["make_your_jodi_btn"])
            el.click()
            print("✅ 'Make Your Jodi' clicked")
        except NoSuchElementException:
            print("❌ 'Make Your Jodi' not found")

    