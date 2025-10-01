from appium.webdriver.common.appiumby import AppiumBy

LOCATORS = {
    #  App_Lunched
    "make_your_jodi_btn": (AppiumBy.ACCESSIBILITY_ID, "Make Your Jodi")

    "bell_icon": (
        AppiumBy.XPATH,
        "//android.widget.ImageView[@resource-id='com.android.permissioncontroller:id/permission_icon']",
    ),
    "login_title": (
        AppiumBy.XPATH,
        "//android.widget.ScrollView/android.view.ViewGroup/android.widget.ImageView[1]",
    ),
}
