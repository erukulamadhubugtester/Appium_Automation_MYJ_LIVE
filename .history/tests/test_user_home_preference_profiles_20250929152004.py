import pytest
from pages.user_login_page import User_login_Page
from pages.user_home_view_preference_profiles import PreferenceProfilesPage


@pytest.mark.usefixtures("driver")
def test_loop_through_preference_profiles(driver):
    # Step 1: Login
    login_page = User_login_Page(driver)
    login_page.login()

    # Step 2: Open profiles
    page = PreferenceProfilesPage(driver)
    page.click_home_imageview_13()

    # Step 3: Loop through profiles using the page object method
    profiles = page.loop_profiles(max_profiles=200)

    # Print all collected profiles
    for idx, p in enumerate(profiles, start=1):
        print(f"🔎 Profile {idx}: {p['username']}, {p['age']}, {p['location']}")

    print(f"📌 Total unique profiles visited: {len(profiles)}")

    # ✅ Assertion
    assert len(profiles) > 0, "❌ No profiles found"
