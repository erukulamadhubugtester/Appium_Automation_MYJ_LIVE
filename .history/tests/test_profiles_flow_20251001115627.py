import pytest
from pages.profiles_page import ProfilesPage
from pages.user_login_page import User_login_Page


@pytest.mark.usefixtures("driver")
def test_profiles_navigation(driver):
    # Login
    login = User_login_Page(driver)
    login.login()

    profiles = ProfilesPage(driver)

    # 1. Open Profiles
    header = profiles.open_profiles()
    assert "Profiles" in header

    # 2. Preferred Tab
    profiles.open_preferred()
    preferred_profiles = profiles.get_profiles()
    assert len(preferred_profiles) > 0
    print("\n--- Preferred Profiles ---")
    for p in preferred_profiles:
        print(p)

    # 3. Recent Visitors
    profiles.open_recent_visitors()
    if profiles.is_upgrade_banner():
        print("\n⚠️ Free user - Upgrade banner shown, no profiles")
    else:
        visitors = profiles.get_profiles()
        print("\n--- Recent Visitors ---")
        for v in visitors:
            print(v)

    # 4. Promoted
    profiles.open_promoted()
    promoted = profiles.get_profiles()
    print("\n--- Promoted Profiles ---")
    for p in promoted:
        print(p)
