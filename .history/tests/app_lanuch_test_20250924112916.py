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


from pages.app_lanuch_page import App_lanuched


def test_app_launch(driver):
    app_l = App_lanuched(driver)

    # Action
    app_l.click_make_your_jodi()

    # Assertion
    # assert app_l.is_bell_icon_displayed(), "❌ Bell icon should be visible"
    # assert app_l.is_login_title_displayed()
