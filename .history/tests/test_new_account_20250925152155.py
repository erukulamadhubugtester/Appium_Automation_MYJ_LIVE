# tests/test_new_account.py
import pytest
import time
from appium.webdriver.common.appiumby import AppiumBy
from utils.driver_factory import create_driver


@pytest.mark.parametrize(
    "phone_number", [str(n) for n in range(23585893536, 2000000020)]
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
        print(f"📩 Sent OTP for {phone_number}")

        time.sleep(2)

    finally:
        driver.quit()
