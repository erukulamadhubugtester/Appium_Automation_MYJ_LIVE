import pytest
from pages.app_lanuch_page import AppLaunched
from pages.login_page import LoginPage


@pytest.mark.usefixtures("driver")
def test_app_launch_and_login(driver):
    # Launch page object
    app = AppLaunched(driver)

    # Step 1: Wait for login screen
    assert app.wait_for_login_screen(), "❌ App did not launch correctly"

    # Step 2: Verify login title/logo is displayed
    assert app.is_login_title_displayed(), "❌ Login title not visible"
    print("🎉 Test Passed: App launched successfully and Login title is visible")

    # Step 3: Verify login image
    assert app.wait_for_login_image_logo_check(), "❌ Login image not visible"
    print("🎉 Test Passed: Login image is visible")

    # Step 4: Print and verify login page text
    text = app.login_page_text()
    assert (
        text == "Enter registered mobile number and password "
    ), f"❌ Login page text mismatch. Found: {text}"
    print("🎉 Test Passed: Login page text is correct")

    # Step 5: Perform login
    login = LoginPage(driver)
    login.enter_phone_number()
    print("🎉 Test Passed: Phone number entered successfully")

    login.enter_password()
    print("🎉 Test Passed: Password entered successfully")

    login.click_continue()
    print("🎉 Test Passed: Continue button clicked")

    # Step 6: Verify Home screen is displayed
    assert login.is_home_screen_displayed(), "❌ Home screen not visible"
    print("🎉 Test Passed: User successfully logged in and reached Home screen")


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
