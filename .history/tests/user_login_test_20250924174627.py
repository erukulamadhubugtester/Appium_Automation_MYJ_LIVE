import pytest
from pages.user_login_page import User_login_Page


@pytest.mark.usefixtures("driver")
def user_login_test(driver):
    app = User_login_Page(driver)

    app.enter_phone_number()
    print("🎉 Test Passed: Phone number entered successfully")

    app.enter_password()
    print("🎉 Test Passed: Password entered successfully")

    app.click_continue()
    print("🎉 Test Passed: Continue button clicked")

    app.dismiss_password_popup()

    assert app.is_home_screen_displayed(), "❌ Home screen not visible"
    print("🎉 Test Passed: User successfully logged in and reached Home screen")
