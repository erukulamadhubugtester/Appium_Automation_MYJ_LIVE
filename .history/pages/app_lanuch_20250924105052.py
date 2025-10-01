from selenium.common.exceptions import NoSuchElementException
from locators import LOCATORS


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

    def is_bell_icon_displayed(self):
        try:
            el = self.driver.find_element(*LOCATORS["bell_icon"])
            return el.is_displayed()
        except NoSuchElementException:
            return False
