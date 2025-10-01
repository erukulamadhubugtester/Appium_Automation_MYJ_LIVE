from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time


def create_driver():
    caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",  # change if real device
        "automationName": "UiAutomator2",
        "appPackage": "com.meriteye.makeyourjodi",
        "appActivity": ".MainActivity",
        "noReset": True,
        "autoGrantPermissions": True,
        "unicodeKeyboard": True,
        "resetKeyboard": True,
    }
    return webdriver.Remote("http://127.0.0.1:4723", options=caps)


def run_automation():
    driver = create_driver()
    driver.implicitly_wait(10)

    try:
        # Step 1: Click "Create new account"
        create_btn = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text(" Create new account ")'
        )
        create_btn.click()
        print("✅ Clicked 'Create new account'")

        # Step 2: Loop phone numbers
        for i in range(1000000000, 1000000020):  # first 20 numbers
    phone_number = str(i)

    phone_field = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter Phone Number")'
    )
    phone_field.clear()
    phone_field.send_keys(phone_number)
    print(f"📌 Entered phone number: {phone_number}")

    send_btn = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Send OTP")'
    )
    send_btn.click()
    print(f"📩 Clicked Send OTP for {phone_number}")

    time.sleep(2)


    finally:
        driver.quit()


if __name__ == "__main__":
    run_automation()
