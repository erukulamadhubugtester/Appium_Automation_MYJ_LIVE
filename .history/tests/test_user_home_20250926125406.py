import pytest
from pages.user_login_page import User_login_Page
from pages.user_home_page import HomePage


@pytest.mark.usefixtures("driver")
def test_home_page_after_login(driver):
    # Step 1: Login
    login_page = User_login_Page(driver)
    login_page.login()  # ✅ works now

    # Step 2: Validate home page icons
    home = HomePage(driver)
    assert home.validate_all_icons(), "❌ Home page icons are missing"
    print("🎉 Test Passed: All home page icons are visible")

    assert home.is_user_image_displayed(), "❌ User image is not displayed"
    print("🎉 Test Passed: User image is visible on home screen")

    # ✅ Step 2: Get full Welcome text
    welcome_text = home.get_user_welcome_text()
    print(f"📌 Full Welcome Text: {welcome_text}")

    # ✅ Step 3: Extract username only
    username = home.get_logged_in_username()
    print(f"📌 Logged in Username: {username}")

    assert username != "", "❌ Username is empty"
    print("🎉 Test Passed: Username displayed correctly")
