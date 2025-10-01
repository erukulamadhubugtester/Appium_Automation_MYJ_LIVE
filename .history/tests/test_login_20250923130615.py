import time
import pytest
from appium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",  # Your connected device/emulator
        "app": "/Users/madhu/Downloads/app-release.apk",  # Path to APK
        "automationName": "UiAutomator2"
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
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
    success_msg = driver.find_element_by_id("com.example:id/successMessage").text
    assert "Welcome" in success_msg
