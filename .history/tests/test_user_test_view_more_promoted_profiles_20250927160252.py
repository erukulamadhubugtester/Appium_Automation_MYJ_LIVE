import pytest
from pages.user_login_page import User_login_Page
from pages.user_view_more_promoted_profiles_page import User_view_more_promoted_profiles


@pytest.mark.usefixtures("driver")
def test_home_screen_promoted_profiles(driver):
    # Step 1: Login
    promoted_profiles = User_login_Page(driver)
    promoted_profiles.login()

    # Step 2: Home page actions
    home = User_view_more_promoted_profiles(driver)

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

    # 1️⃣ Click on "View More"
    home.click_view_more()

    # 2️⃣ Highlight Profiles title
    title = home.highlight_profiles_title()
    assert "Profiles" in title, "❌ Profiles title not visible"

    # 3️⃣ Click on Promoted card
    home.click_promoted_card()

    # 4️⃣ Count profile cards
    total_profiles = home.count_profile_cards()
    assert total_profiles > 0, "❌ No profiles found"

    # 4️⃣ Count profile cards across scrolls
    total_profiles = home.count_all_profile_cards(max_scrolls=10)
assert total_profiles > 0, "❌ No profiles found"
  