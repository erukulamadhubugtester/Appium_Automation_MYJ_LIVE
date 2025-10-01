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

    def is_bell_icon_displayed(self):
        try:
            el = self.driver.find_element(*LOCATORS["bell_icon"])
            if el.is_displayed():
                # highlight with long press
                action = any(
                    self.driver
                )  # pyright: ignore[reportUndefinedVariable]
                action.long_press(el, duration=1000).release().perform()
                print("✅ Bell icon is displayed and highlighted")
                return True
            else:
                print("⚠️ Bell icon element found but not visible")
                return False
        except NoSuchElementException:
            print("❌ Bell icon not found on screen! (Popup not shown)")
            return False
