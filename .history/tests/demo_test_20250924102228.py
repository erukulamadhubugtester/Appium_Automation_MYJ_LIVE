from appium import webdriver
from appium.options.android import UiAutomator2Options
import time


def test_login():
    caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "automationName": "UiAutomator2",
        "appPackage": "com.meriteye.makeyourjodi",
        "appActivity": ".MainActivity",
        "noReset": True,
        "autoGrantPermissions": True,
    }

    # Create options object
    options = UiAutomator2Options().load_capabilities(caps)

    # Start driver with options
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    time.sleep(5)

    # Example: click app icon
    # driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Make Your Jodi").click()

    driver.quit()
