from appium.webdriver.common.appiumby import AppiumBy

LOCATORS = {
    # App Icon (on home screen) – not needed once APK is launched directly
    "make_your_jodi_btn": (
        AppiumBy.XPATH,
        '//android.widget.TextView[@content-desc="Make Your Jodi"]',
    ),
    # Android permission dialog bell icon (if permissions popup appears)
    "bell_icon": (
        AppiumBy.XPATH,
        "//android.widget.ImageView[@resource-id='com.android.permissioncontroller:id/permission_icon']",
    ),
    # Login screen title/logo element
    "login_title": (
        AppiumBy.XPATH,
        "//android.widget.ScrollView/android.view.ViewGroup/android.widget.ImageView[1]",
    ),
    "login_image_check": (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.ImageView").instance(2)',
    ),

    ""
}
