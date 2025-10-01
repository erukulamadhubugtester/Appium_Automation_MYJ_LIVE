from appium.webdriver.common.appiumby import AppiumBy

LOCATORS = {
    
    "make_your_jodi_btn": (AppiumBy.ACCESSIBILITY_ID, "Make Your Jodi"),
    "bell_icon": (AppiumBy.XPATH, "//android.widget.ImageView[@resource-id='com.android.permissioncontroller:id/permission_icon']"),
}
