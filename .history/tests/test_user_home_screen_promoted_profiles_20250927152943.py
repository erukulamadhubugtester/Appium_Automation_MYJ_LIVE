import pytest
from pages.user_login_page import User_login_Page
from pages.user_home_screen_promoted_profiles_page import (
    User_home_screen_promoted_profiles_page,
)


@pytest.mark.usefixtures("driver")
def test_home_screen_promoted_profiles(driver):
    # Step 1: Login
    promoted_profiles = User_login_Page(driver)
    promoted_profiles.login()

    # Step 2: Home page actions
    home = User_home_screen_promoted_profiles_page(driver)

   

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
    driver.implicitly_wait(10)

