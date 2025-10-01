import pytest
from pages.user_login_page import User_login_Page
from pages.user_home_preference_profiles import PreferenceProfilesPage


@pytest.mark.usefixtures("driver")
def test_loop_through_preference_profiles(driver):
    # Step 1: Login
    login_page = User_login_Page(driver)
    login_page.login()

    # Step 2: Open profiles
    page = PreferenceProfilesPage(driver)
    page.click_home_imageview_13()

    seen = set()
    count = 0

    while True:
        username = page.get_username()
        age = page.get_age()
        location = page.get_location()

        profile_id = f"{username}-{age}-{location}"

        if profile_id in seen:
            print("✅ First profile reached again → Loop complete.")
            break

        seen.add(profile_id)
        count += 1
        print(f"🔎 Profile {count}: {username}, {age}, {location}")

        # Go to next profile
        page.click_next_arrow()

    print(f"📌 Total unique profiles visited: {count}")
    assert count > 0, "❌ No profiles found"
