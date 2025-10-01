import pytest
from pages.user_login_page import User_login_Page
from pages.user_home_page import HomePage


@pytest.mark.usefixtures("driver")
def test_home_screen_prom(driver):
    # Step 1: Login
    login_page = User_login_Page(driver)
    login_page.login()

    # Step 2: Home page actions
    home = HomePage(driver)
    received, sent, connected = home.home_page()

    # Step 3: Assertions
    assert received >= 0, "❌ Received count missing"
    assert sent >= 0, "❌ Sent count missing"
    assert connected >= 0, "❌ Connected count missing"
    print(f"🎉 Test Passed: Received={received}, Sent={sent}, Connected={connected}")

    # Promoted Profiles
    title_text = home.get_promoted_profiles_title()
    assert title_text == "Promoted Profiles", f"❌ Unexpected title: {title_text}"
    print(f"🎉 Test Passed: Promoted Profiles title = '{title_text}'")

    # Scroll & View More
    assert (
        home.scroll_profiles_to_view_more()
    ), "❌ 'View More' card not visible even after scrolling"
    text = home.get_view_more_text()
    assert text == "View More", f"❌ Unexpected text: {text}"
    print("🎉 Test Passed: 'View More' card is visible with correct text")

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
