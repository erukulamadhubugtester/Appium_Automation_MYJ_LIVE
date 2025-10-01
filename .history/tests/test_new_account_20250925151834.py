import pytest
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


def create_driver():
    caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "automationName": "UiAutomator2",
        "appPackage": "com.meriteye.makeyourjodi",
        "appActivity": ".MainActivity",
        "noReset": True,
        "autoGrantPermissions": True,
        "unicodeKeyboard": True,
        "resetKeyboard": True,
    }
    return webdriver.Remote("http://127.0.0.1:4723", options=caps)


@pytest.mark.parametrize(
    "phone_number", [str(i) for i in range(1000000000, 1000000020)]
)
def test_new_account(phone_number):
    driver = create_driver()
    driver.implicitly_wait(10)

    try:
        # Step 1: Click "Create new account"
        create_btn = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text(" Create new account ")',
        )
        create_btn.click()
        print("✅ Clicked 'Create new account'")

        # Step 2: Enter phone number
        phone_field = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter Phone Number")'
        )
        phone_field.clear()
        phone_field.send_keys(phone_number)
        print(f"📌 Entered phone number: {phone_number}")

        # Step 3: Click "Send OTP"
        send_btn = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Send OTP")'
        )
        send_btn.click()
        print(f"📩 Clicked Send OTP for {phone_number}")

    finally:
        driver.quit()
