import time
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options  # ✅ new import
from pages.login_page import LoginPage





def test_login(driver):
    login = LoginPage(driver)
    time.sleep(5)  # Wait for app to load
    login.enter_phone("6303481147")
    login.enter_password("Qwerty@1")
    login.click_login()
    time.sleep(5)
    # Verify login success
    success_msg = driver.find_element(
        by="id", value="com.example:id/successMessage"
    ).text
    assert "Welcome" in success_msg
