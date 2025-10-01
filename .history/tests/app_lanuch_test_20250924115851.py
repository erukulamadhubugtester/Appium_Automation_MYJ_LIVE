# from appium import webdriver
# from appium.options.android import UiAutomator2Options
# from pages.app_lanuch import App_lanuched
# import time


# def test_login():
#     # caps = {
#     #     "platformName": "Android",
#     #     "deviceName": "emulator-5554",
#     #     "automationName": "UiAutomator2",
#     #     "appPackage": "com.meriteye.makeyourjodi",
#     #     "appActivity": ".MainActivity",
#     #     "noReset": False,
#     #     "fullReset": False,
#     #     "autoGrantPermissions": True,
#     #     "appWaitActivity": "*",
#     # }
#     caps = {
#         "platformName": "Android",
#         "deviceName": "emulator-5554",
#         "automationName": "UiAutomator2",
#         "appPackage": "com.meriteye.makeyourjodi",
#         "appActivity": ".MainActivity",
#         "noReset": True,  # always start fresh
#         "fullReset": False,  # reinstall app (optional, slower)
#         "autoGrantPermissions": True,
#         "appWaitActivity": "*",
#     }

#     options = UiAutomator2Options().load_capabilities(caps)
#     driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
#     driver.implicitly_wait(10)

#     print("✅ App launched. Current activity:", driver.current_activity)

#     home = App_lanuched(driver)

#     home.click_make_your_jodi()

#     if home.is_bell_icon_displayed():
#         print("✅ Bell icon is displayed")
#     else:
#         print("❌ Bell icon not found")

#     time.sleep(3)
#     driver.quit()


# import pytest
# from pages.app_lanuch_page import App_lanuched


# @pytest.mark.usefixtures("driver")  # if you’re using a conftest.py fixture
# def test_app_launch(driver):
#     app_l = App_lanuched(driver)

#     # Step 1: Wait for splash/app title
#     assert app_l.wait_for_app_title(), "❌ App title not visible"

#     # Step 2: Validate login screen
#     assert app_l.is_login_title_displayed(), "❌ Login title should be visible"


import pytest
from pages.app_launch_page import AppLaunched


@pytest.mark.usefixtures("driver")  # assuming you have driver fixture in conftest.py
def test_app_launch(driver):
    app = AppLaunched(driver)

    # Step 1: Wait for app to open (login screen)
    assert app.wait_for_login_screen(), "❌ App did not launch correctly"

    # Step 2: Verify login title is visible
    assert app.is_login_title_displayed(), "❌ Login title not visible"
    print("🎉 Test Passed: App launched successfully and Login title is visible")
