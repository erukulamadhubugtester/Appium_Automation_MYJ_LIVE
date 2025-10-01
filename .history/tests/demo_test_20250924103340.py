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
