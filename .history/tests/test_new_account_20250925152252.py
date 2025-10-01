import pytest
import time
import random
from appium.webdriver.common.appiumby import AppiumBy
from utils.driver_factory import create_driver

# Generate 10 random numbers in the given range
random_numbers = [str(random.randint(1253784647, 5997486438736)) for _ in range(10)]


@pytest.mark.parametrize("phone_number", random_numbers)
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
