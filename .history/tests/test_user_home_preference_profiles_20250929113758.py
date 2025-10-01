import pytest
from pages.user_login_page import User_login_Page
from pages.user import HomePage


@pytest.mark.usefixtures("driver")
def test_home_page_after_login(driver):

    # Step 1: Login
    login_page = User_login_Page(driver)
    login_page.login()

    # Step 2: Home page actions
    home = HomePage(driver)
    received, sent, connected = home.home_page()

    #  Validate ImageView[14]
    assert (
        home.is_home_imageview_14_displayed()
    ), "❌ ImageView[14] is not visible on home screen"
    print("🎉 Test Passed: ImageView[14] is displayed on home screen")

    # Step 4: Click on ImageView[13]
    assert home.click_imageview_13(), "❌ Failed to click ImageView[13]"
    print("🎉 Test Passed: Clicked ImageView[13] successfully")

    driver.implicitly_wait(10)

    # ✅ Check profile details
    username = home.get_profile_username()
    age = home.get_profile_age()

    assert username is not None, "❌ Profile username not found"
    assert age is not None, "❌ Profile age not found"

    print(f"📌 First Profile => Username: {username}, Age: {age}")
