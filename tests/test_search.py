import pytest
from pages.user_search_page import SearchPage
from pages.user_login_page import User_login_Page


@pytest.mark.usefixtures("driver")
def test_search_icon_click(driver):
    """Verify search functionality returns profiles for 'India' search"""

    # Login
    login = User_login_Page(driver)
    login.login()

    # Open Search
    search = SearchPage(driver)
    search.open_search()

    # Verify Promoted Profiles section
    promoted_title = search.get_promoted_profiles_title()
    assert (
        promoted_title == "Promoted Profiles"
    ), f"Expected 'Promoted Profiles', got '{promoted_title}'"

    # Verify VIP Profiles section
    vip_title = search.get_vip_profiles_title()
    assert vip_title == "VIP Profiles", f"Expected 'VIP Profiles', got '{vip_title}'"

    # Search for profiles
    search.enter_search_text("India")
    search.click_search_icon()

    # Verify results
    profiles = search.get_profiles()
    assert len(profiles) > 0, "No profiles found for 'India' search"
    print(f"\n✅ Found {len(profiles)} profiles: {profiles}")
