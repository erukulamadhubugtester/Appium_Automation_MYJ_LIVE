from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

def test_login():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "automationName": "UiAutomator2",
        "appPackage": "com.meriteye.makeyourjodi",
        "appActivity": ".MainActivity",
        "noReset": True,
        "autoGrantPermissions": True
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    # Step 1: Tap "Make Your Jodi" app icon
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Make Your Jodi").click()
    time.sleep(5)

    # Step 2: Enter phone number (locator from Inspector)
    driver.find_element(AppiumBy.ID, "com.meriteye.makeyourjodi:id/phoneNumber").send_keys("9876543210")

    # Step 3: Tap Login button
    driver.find_element(AppiumBy.ID, "com.meriteye.makeyourjodi:id/btnLogin").click()

    time.sleep(5)
    driver.quit()
