# # utils/driver_factory.py
# from appium import webdriver
# from appium.options.android import UiAutomator2Options


# def create_driver():
#     caps = {
#         "platformName": "Android",
#         "deviceName": "emulator-5554",
#         "automationName": "UiAutomator2",
#         "appPackage": "com.meriteye.makeyourjodi",
#         "appActivity": ".MainActivity",
#         "noReset": False,  # reset app data every run
#         "fullReset": False,  # don’t reinstall APK
#         "autoGrantPermissions": True,
#         "appWaitActivity": "*",
#     }
#     options = UiAutomator2Options().load_capabilities(caps)
#     # 👉 Add deviceName here
#     options.set_capability("deviceName", "RZ8R905MK6H")

#     options.set_capability("unicodeKeyboard", True)
#     options.set_capability("resetKeyboard", True)

#     driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
#     driver.implicitly_wait(10)
#     return driver

======================================================== 1 code  ========================================================