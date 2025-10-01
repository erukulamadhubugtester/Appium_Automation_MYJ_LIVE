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

    def is_login_title_displayed(self):
        try:
            el = self.driver.find_element(*LOCATORS["login_title"])
            if el.is_displayed():
                # Highlight by long press (visual feedback)
                action = TouchAction(self.driver)
                action.long_press(el, duration=800).release().perform()
                print("✅ Login title is displayed and highlighted")
                return True
            else:
                print("⚠️ Login title found but not visible")
                return False
        except NoSuchElementException:
            print("❌ Login title not found on screen")
            return False
