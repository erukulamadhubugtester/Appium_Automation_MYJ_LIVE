# tests/test_loop_through_preference_profiles.py
import pytest
from pages.user_login_page import User_login_Page
from pages.user_home_view_preference_profiles import PreferenceProfilesPage


@pytest.mark.usefixtures("driver")
def test_loop_through_preference_profiles(driver):
    """
    Test to loop through preference profiles and collect details
    """

    # Step 1: Login
    login = User_login_Page(driver)
    login.login()

    # Step 2: Navigate to Preference Profiles
    profiles_page = PreferenceProfilesPage(driver)
    assert (
        profiles_page.click_home_imageview_13()
    ), "❌ Could not open Preference Profiles section"

    # Step 3: Loop through profiles
    profiles = profiles_page.loop_profiles(max_profiles=200)

    # Step 4: Print collected profile details
    print("\n--- Collected Preference Profiles ---")
    for idx, profile in enumerate(profiles, start=1):
        print(
            f"🔎 Profile {idx}: {profile['username']}, {profile['age']}, {profile['location']}"
        )

    print(f"📌 Total unique profiles visited: {len(profiles)}")

    # Step 5: Assertions
    assert len(profiles) > 0, "❌ No profiles found"
