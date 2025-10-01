import time
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options  # ✅ new import
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"  # your connected device/emulator
    options.app = "/Users/madhu/Downloads/app-release.apk"  # Path to your APK
    options.automation_name = "UiAutomator2"

    driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
    yield driver
    driver.quit()

def test_login(driver):
    login = LoginPage(driver)
    time.sleep(5)  # Wait for app to load
    login.enter_phone("6555555555")
    login.enter_password("Qwerty@1")
    login.click_login()
    time.sleep(5)
    # Verify login success
    success_msg = driver.find_element(by="id", value="com.example:id/successMessage").text
    assert "Welcome" in success_msg
