from appium.webdriver.common.appiumby import AppiumBy

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_phone(self, phone):
        self.driver.find_element(AppiumBy.ID, "com.example:id/phoneNumber").send_keys(phone)

    def enter_password(self, password):
        self.driver.find_element(AppiumBy.ID, "com.example:id/password").send_keys(password)

    def click_login(self):
        self.driver.find_element(AppiumBy.ID, "com.example:id/loginButton").click()
