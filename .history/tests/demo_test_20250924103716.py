# from appium import webdriver
# from appium.options.android import UiAutomator2Options
# import time


# def test_login():
#     caps = {
#         "platformName": "Android",
#         "deviceName": "emulator-5554",
#         "automationName": "UiAutomator2",
#         "appPackage": "com.meriteye.makeyourjodi",
#         "appActivity": ".MainActivity",  # change if dumpsys shows different
#         "noReset": True,
#         "autoGrantPermissions": True,
#         "appWaitActivity": "*",
#     }

#     options = UiAutomator2Options().load_capabilities(caps)
#     driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

#     driver.implicitly_wait(10)

#     # check current activity
#     print("App launched. Current activity:", driver.current_activity)

#     # wait to actually see the app open
#     time.sleep(15)

#     # example: find your "Make Your Jodi" element by accessibility id
#     el = driver.find_element("accessibility id", "Make Your Jodi")
#     el.click()

#     time.sleep(5)

#     driver.quit()


from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.common.exceptions import NoSuchElementException


def test_login():
    caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "automationName": "UiAutomator2",
    "appPackage": "com.meriteye.makeyourjodi",
    "appActivity": ".MainActivity",
    "noReset": False,          # always start fresh
    "fullReset": True,         # reinstall app (optional, slower)
    "autoGrantPermissions": True,
    "appWaitActivity": "*",
}


    options = UiAutomator2Options().load_capabilities(caps)
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    driver.implicitly_wait(10)

    # check current activity
    print("✅ App launched. Current activity:", driver.current_activity)

    # wait to actually see the app open
    time.sleep(5)

    # Example: click on "Make Your Jodi" element
    try:
        el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Make Your Jodi")
        el.click()
        print("✅ 'Make Your Jodi' clicked.")
    except NoSuchElementException:
        print("❌ 'Make Your Jodi' element not found.")

    # Now check if the bell icon is displayed
    try:
        bell_icon = driver.find_element(
            AppiumBy.XPATH,
            "//android.widget.ImageView[@resource-id='com.android.permissioncontroller:id/permission_icon']",
        )
        if bell_icon.is_displayed():
            print("✅ Bell icon is displayed")
        else:
            print("❌ Bell icon element found but not visible")
    except NoSuchElementException:
        print("❌ Bell icon not found on screen")

    time.sleep(3)
    driver.quit()
