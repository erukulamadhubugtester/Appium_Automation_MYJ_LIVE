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
    # --- Profile completion popup ---
    "PROFILE_POPUP_TITLE": (
        AppiumBy.XPATH,
        "//android.widget.TextView[@text='Complete Your Profile']",
    ),
    "PROFILE_POPUP_CONTENT": (
        AppiumBy.XPATH,
        "//android.widget.TextView[@text='Get the best matches and boost your visibility on our platform by completing your profile and sharing more about yourself.']",
    ),
    "PROFILE_POPUP_PROGRESS": (
        AppiumBy.XPATH,
        "//android.widget.TextView[contains(@text,'%')]",
    ),
    "PROFILE_POPUP_COMPLETE_BTN": (
        AppiumBy.XPATH,
        "//android.view.ViewGroup[@content-desc='Complete Profile']",
    ),
    "PROFILE_POPUP_SKIP_BTN": (
        AppiumBy.XPATH,
        "//android.view.ViewGroup[@content-desc='Skip for Now']",
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
    # User Info
    "USER_ID": (
        AppiumBy.XPATH,
        '//android.widget.TextView[contains(@text,"User ID:")]',
    ),
    "VIEW_PROFILE_ICON": (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@content-desc="View Profile"]/android.widget.ImageView',
    ),
    "VIEW_PROFILE_TEXT": (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="View Profile"]',
    ),
    # # Requests section
    # "REQUESTS_TITLE": (AppiumBy.XPATH, '//android.widget.TextView[@text="Requests"]'),
    # "REQUESTS_RECEIVED": (
    #     AppiumBy.XPATH,
    #     '//android.widget.TextView[@text="Received"]',
    # ),
    # "REQUESTS_SENT": (AppiumBy.XPATH, '//android.widget.TextView[@text="Sent"]'),
    # # Members section
    # "MEMBERS_TITLE": (AppiumBy.XPATH, '//android.widget.TextView[@text="Members"]'),
    # "MEMBERS_CONNECTED": (
    #     AppiumBy.XPATH,
    #     '//android.widget.TextView[@text="Connected"]',
    # ),
    # ✅ Requests Section
    "REQUESTS_RECEIVED_TEXT": (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Received"]',
    ),
    "REQUESTS_RECEIVED_COUNT": (
        AppiumBy.XPATH,
        '(//android.widget.TextView[@text="Received"]/following-sibling::android.widget.TextView)[1]',
    ),
    "REQUESTS_SENT_TEXT": (AppiumBy.XPATH, '//android.widget.TextView[@text="Sent"]'),
    "REQUESTS_SENT_COUNT": (
        AppiumBy.XPATH,
        '(//android.widget.TextView[@text="Sent"]/following-sibling::android.widget.TextView)[1]',
    ),
    # ✅ Members Section
    "MEMBERS_CONNECTED_TEXT": (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Connected"]',
    ),
    "MEMBERS_CONNECTED_COUNT": (
        AppiumBy.XPATH,
        '(//android.widget.TextView[@text="Connected"]/following-sibling::android.widget.TextView)[1]',
    ),
    "PROMOTED_PROFILES_TITLE": (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Promoted Profiles"]',
    ),
    "PROFILE_SCROLL_CONTAINER": (
        AppiumBy.XPATH,
        "//android.widget.HorizontalScrollView/android.view.ViewGroup",
    ),
    "VIEW_MORE_CARD": (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@content-desc="View More"]/android.view.ViewGroup',
    ),
    "VIEW_MORE_TEXT": (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="View More"]',
    ),
    "HOME_IMAGEVIEW_14": (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.ImageView").instance(14)',
    ),
    # "HOME_IMAGEVIEW_13": (
    #     AppiumBy.ANDROID_UIAUTOMATOR,
    #     'new UiSelector().className("android.widget.ImageView").instance(13)',
    # ),
    "HOME_IMAGEVIEW_13": [
        (AppiumBy.ID, "com.yourapp.package:id/profileImage"),  # safest
        (AppiumBy.ACCESSIBILITY_ID, "Profile Image"),  # second option
        (AppiumBy.XPATH, "(//android.widget.ImageView)[14]"),  # fallback
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.ImageView").instance(13)',
        ),  # last resort
    ],
    "VIEW_PROFILES_TEXT": (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().textContains("View Profiles")',
    ),
    # Profile Username (dynamic)
    "PROFILE_USERNAME_DYNAMIC": (
        AppiumBy.XPATH,
        '//android.widget.TextView[contains(@text, ",")]',
    ),
    # Profile Age (dynamic)
    "PROFILE_AGE_DYNAMIC": (
        AppiumBy.XPATH,
        '//android.widget.TextView[contains(@text, "yrs")]',
    ),
}
