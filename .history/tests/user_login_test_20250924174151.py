import pytest

# from pages.demo_login_page_page import AppLaunched
from pages.demo_login_page_page import LoginPage


@pytest.mark.usefixtures("driver")
def test_app_launch_and_login(driver):
    app = LoginPage(driver)

    # Step 1 use app instead of LoginPage
    app.enter_phone_number()
    print("🎉 Test Passed: Phone number entered successfully")

    app.enter_password()
    print("🎉 Test Passed: Password entered successfully")

    app.click_continue()
    print("🎉 Test Passed: Continue button clicked")
    # Step 7.1: Handle Google Password popup
    app.dismiss_password_popup()

    # Step 8
    assert app.is_home_screen_displayed(), "❌ Home screen not visible"
    print("🎉 Test Passed: User successfully logged in and reached Home screen")

