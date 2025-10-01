from selenium.common.exceptions import NoSuchElementException
from utils.locators import LOCATORS


class App_lanuched:
    def __init__(self, driver):
        self.driver = driver

    def click_make_your_jodi(self):
        try:
        el = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(LOCATORS["make_your_jodi_btn"])
        )
        el.click()
        print("✅ 'Make Your Jodi' clicked")
    except Exception as e:
        print(f"❌ 'Make Your Jodi' not found → {e}")

    def is_login_title_displayed(self):
        try:
            el = self.driver.find_element(*LOCATORS["login_title"])
            if el.is_displayed():
                # ✅ Highlight using longClickGesture (works in Appium Python client v2+)
                self.driver.execute_script(
                    "mobile: longClickGesture", {"elementId": el.id, "duration": 800}
                )
                print("✅ Login title is displayed and highlighted")
                return True
            else:
                print("⚠️ Login title found but not visible")
                return False
        except NoSuchElementException:
            print("❌ Login title not found on screen")
            return False
