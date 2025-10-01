import pytest
from pages.user_login_page import User_login_Page
from pages.home_page import HomePage


@pytest.mark.usefixtures("driver")
def test_home_page_after_login(driver):
    # --- Step 1: Login ---
    login_page = User_login_Page(driver)
    login_page.login()  # you can wrap enter_phone, enter_password, click_continue in one method

    # --- Step 2: Validate Home page icons ---
    home = HomePage(driver)
    assert home.validate_all_icons(), "❌ Home page icons are missing"

    print("🎉 Test Passed: All home page icons are visible")
