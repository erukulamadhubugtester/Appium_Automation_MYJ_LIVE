# == code 2.a
import pytest
from pages.user_profiles_data_scroll_page import ProfilesPage2
from pages.user_login_page import User_login_Page


@pytest.mark.usefixtures("driver")
def test_profiles_full_flow(driver):
    """Login once, collect all tabs with scrolling, verify & print profiles"""

    # 1. Login
    login = User_login_Page(driver)
    login.login()

    # 2. Open Profiles
    profiles = ProfilesPage2(driver)
    header = profiles.open_profiles()
    assert "Profiles" in header
    print(f"\n✅ Profiles Page Opened: {header}")

    # 3. Collect all profiles from all tabs
    all_data = profiles.collect_all_profiles_data()

    # 4. Print first 3 profiles per tab
    for tab, data in all_data.items():
        print(f"\n📋 {tab.upper()} - Total: {data['total_count']}")

        for i, profile in enumerate(data["profiles"][:3], 1):
            print(f"   {i}. Name: {profile['name']}, Age: {profile['age']}")

        if data["total_count"] > 3:
            print(f"   ... and {data['total_count'] - 3} more")

    print("\n✅ Test completed successfully with scrolling across all tabs!")
