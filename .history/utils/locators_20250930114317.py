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
    #
    # "HOME_IMAGEVIEW_13": [
    #     (AppiumBy.XPATH, "(//android.widget.ImageView)[13]"),
    #     (
    #         AppiumBy.ANDROID_UIAUTOMATOR,
    #         'new UiSelector().className("android.widget.ImageView").instance(13)',
    #     ),
    # ],
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
    # ========= Home screen view more  Promoted  locators ==================================#
    "VIEW_MORE": (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@content-desc="View More"]/android.view.ViewGroup',
    ),
    "PROFILES_TITLE": (
        AppiumBy.XPATH,
        '(//android.widget.TextView[@text="Profiles"])[1]',
    ),
    "PROMOTED_CARD": (
        AppiumBy.XPATH,
        '//android.view.View[@content-desc="Promoted"]/android.view.ViewGroup/android.view.ViewGroup',
    ),
    "PROFILE_CARDS": (
        AppiumBy.XPATH,
        "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup",
    ),
    # ========= Home screen  Promoted  locators ==================================#
    "HOME_IMAGEVIEW_13": [
        "xpath",
        "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[9]/android.widget.ImageView",
    ],
    "PROFILE_FORWARD_ARROW": ["xpath", "//android.widget.TextView[@text='']"],
    "PROFILE_USERNAME": [
        "xpath",
        "//android.widget.TextView[substring(@text,string-length(@text))= ',']",
    ],
    "PROFILE_AGE": ["xpath", "//android.widget.TextView[contains(@text,'yrs')]"],
    "PROFILE_LOCATION": [
        "xpath",
        "//android.widget.TextView[contains(@text,',') and not(substring(@text,string-length(@text))= ',')]",
    ],
    "PROFILE_BACKWARD_ARROW": ["xpath", "//android.widget.TextView[@text='']"],
    # ========= R&R Screen  locators ==================================#
    # 1. R&R module entry
    "RR_MODULE_IMAGE": (
        AppiumBy.XPATH,
        '//android.view.View[@content-desc="R&R"]/android.widget.ImageView',
    ),
    # 2. Title
    "RR_TITLE": (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Rewards and Referrals"]',
    ),
    # 3. Banner image (UiAutomator)
    "RR_BANNER_IMAGE_UIA": (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.ImageView").instance(1)',
    ),
    # 4. "Balance" label
    "RR_BALANCE_LABEL": (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Balance"]',
    ),
    # 5. Balance value (exact example you gave). If value is dynamic you can
    #     add a contains variant in locators or update later.
    "RR_BALANCE_VALUE": (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="150"]',
    ),
    # 6. "Points" label
    "RR_POINTS_LABEL": (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Points"]',
    ),
    # 7. Referral description text (exact string you supplied)
    "RR_REF_DESC": (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Share your referral link and invite your family and friends through Email or other network"]',
    ),
    # 8. Roadmap image inside ScrollView
    "RR_ROADMAP_IMAGE": (
        AppiumBy.XPATH,
        "//android.widget.ScrollView/android.view.ViewGroup/android.widget.ImageView[1]",
    ),
    # 9. "Your Referral Code" title
    "RR_REF_CODE_LABEL": (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Your Referral Code"]',
    ),
    # 10. Referral code example (exact). Provide generic fallback below.
    "RR_REF_CODE_EXACT": (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="y15JPO"]',
    ),
    # generic contains (in case value changes)
    "RR_REF_CODE_GENERIC": (
        AppiumBy.XPATH,
        '//android.widget.TextView[contains(@text,"y")]',
    ),
    # 11. Invite/Share button area
    "RR_INVITE_NOW": (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@content-desc=", Invite now"]/android.view.ViewGroup',
    ),
    # 12. Rewards redemption history text
    "RR_REDEMPTION_HISTORY": (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Rewards redemption history"]',
    ),
}
