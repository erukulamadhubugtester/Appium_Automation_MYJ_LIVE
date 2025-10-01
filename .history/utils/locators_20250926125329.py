from appium.webdriver.common.appiumby import AppiumBy

LOCATORS = {
    # =========Login locators ==================================#
    # 1. App Icon (on home screen) – not needed once APK is launched directly
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
    "LOGIN_PAGE_TEXT": (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Enter registered mobile number and password "]',
    ),
    "PHONE_NUMBER_FIELD": (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Phone Number")',
    ),
    "PASSWORD_FIELD": (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("text-input-outlined")',
    ),
    "CONTINUE_BUTTON": (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Continue")',
    ),
    "HOME_SCREEN_TITLE": (  # 👈 Change this to something unique in your Home page
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.ViewGroup").instance(11)',
    ),
    # ========= Home page  locators ==================================#
    # Home icons
    "SEARCH_ICON": (AppiumBy.XPATH, '//android.widget.TextView[@text=""]'),
    "BELL_ICON": (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc=""]'),
    "SETTINGS_ICON": (AppiumBy.XPATH, '//android.widget.TextView[@text=""]'),
    "USER_IMAGE": (
        AppiumBy.XPATH,
        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[1]/android.widget.ImageView',
    ),
    # Dynamic user welcome text
    "USER_WELCOME_TEXT": (
        AppiumBy.XPATH,
        '//android.widget.TextView[contains(@text,"Welcome")]',
    ),
}
