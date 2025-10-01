

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

# ======================================================== 1 code  ========================================================


from appium import webdriver
from appium.options.android import UiAutomator2Options
import subprocess


def get_emulator_udid():
    """Return running emulator udid if available"""
    result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    for line in result.stdout.splitlines():
        if "emulator" in line and "device" in line:
            return line.split()[0]
    return None


def create_driver(use_emulator=True):
    if use_emulator:
        udid = get_emulator_udid()
        if not udid:
            raise Exception("❌ No emulator found! Start an emulator first.")
        device_name = udid
        print(f"✅ Using emulator: {device_name}")
    else:
        device_name = "RZ8R905MK6H"  # your phone serial
        print(f"✅ Using real device: {device_name}")

    caps = {
        "platformName": "Android",
        "deviceName": device_name,
        "automationName": "UiAutomator2",
        "appPackage": "com.meriteye.makeyourjodi",
        "appActivity": ".MainActivity",
        "noReset": False,
        "fullReset": False,
        "autoGrantPermissions": True,
        "appWaitActivity": "*",
        "unicodeKeyboard": True,
        "resetKeyboard": True,
    }

    options = UiAutomator2Options().load_capabilities(caps)
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(10)
    return driver
