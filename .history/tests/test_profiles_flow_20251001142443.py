# import pytest
# from pages.user_profiles_page import ProfilesPage
# from pages.user_login_page import User_login_Page


# @pytest.mark.usefixtures("driver")
# def test_profiles_navigation(driver):
#     # Login
#     login = User_login_Page(driver)
#     login.login()

#     profiles = ProfilesPage(driver)

#     # 1. Open Profiles
#     header = profiles.open_profiles()
#     assert "Profiles" in header

#     # 2. Preferred Tab
#     profiles.open_preferred()
#     preferred_profiles = profiles.get_profiles()
#     assert len(preferred_profiles) > 0
#     print("\n--- Preferred Profiles ---")
#     for p in preferred_profiles:
#         print(p)

#     # 3. Recent Visitors
#     profiles.open_recent_visitors()
#     if profiles.is_upgrade_banner():
#         print("\n⚠️ Free user - Upgrade banner shown, no profiles")
#     else:
#         visitors = profiles.get_profiles()
#         print("\n--- Recent Visitors ---")
#         for v in visitors:
#             print(v)

#     # 4. Promoted
#     profiles.open_promoted()
#     promoted = profiles.get_profiles()
#     print("\n--- Promoted Profiles ---")
#     for p in promoted:
#         print(p)


# ====== code 2

# import pytest
# from pages.user_profiles_page import ProfilesPage
# from pages.user_login_page import User_login_Page


# @pytest.mark.usefixtures("driver")
# def test_profiles_navigation(driver):
#     # Login
#     login = User_login_Page(driver)
#     login.login()

#     profiles = ProfilesPage(driver)

#     # 1. Open Profiles
#     header = profiles.open_profiles()
#     assert "Profiles" in header

#     # 2. Preferred Tab
#     profiles.open_preferred()
#     preferred_profiles = profiles.get_all_profiles_with_count("Preferred Profiles")
#     assert len(preferred_profiles) > 0

#     # 3. Recent Visitors
#     profiles.open_recent_visitors()
#     if profiles.is_upgrade_banner():
#         print("\n⚠️ Free user - Upgrade banner shown, no profiles")
#     else:
#         visitors = profiles.get_all_profiles_with_count("Recent Visitors")
#         assert len(visitors) > 0

#     # 4. Promoted
#     profiles.open_promoted()
#     promoted_profiles = profiles.get_all_profiles_with_count("Promoted Profiles")
#     assert len(promoted_profiles) > 0


import pytest
import logging
from pages.profiles import ProfilesPage

logger = logging.getLogger(__name__)


def test_collect_all_profiles(driver):
    """
    Test to collect all profiles from all tabs with scrolling
    """
    logger.info("🚀 Starting profile collection test...")

    # Initialize ProfilesPage
    profiles_page = ProfilesPage(driver)

    # Open profiles section
    profiles_page.open_profiles()

    # Collect all profiles from all tabs
    results = profiles_page.collect_all_profiles_data()

    # Assertions
    assert results is not None, "Results should not be None"
    assert "main_profiles" in results, "Should have main profiles"
    assert "recent_visitors" in results, "Should have recent visitors"
    assert "promoted" in results, "Should have promoted profiles"
    assert "preferred" in results, "Should have preferred profiles"

    # Verify counts
    assert results["main_profiles"]["total_count"] >= 0
    assert results["recent_visitors"]["total_count"] >= 0
    assert results["promoted"]["total_count"] >= 0
    assert results["preferred"]["total_count"] >= 0

    logger.info("✅ Profile collection test completed successfully!")


def test_single_tab_profiles(driver):
    """
    Test to collect profiles from just one tab
    """
    profiles_page = ProfilesPage(driver)
    profiles_page.open_profiles()

    # Just collect from main profiles
    logger.info("📋 Collecting main profiles only...")
    profiles, count = profiles_page.get_all_profiles_with_scroll()

    logger.info(f"✅ Collected {count} profiles")
    for i, profile in enumerate(profiles, 1):
        logger.info(f"{i}. {profile['name_age']}")

    assert count > 0, "Should have at least some profiles"


def test_recent_visitors_only(driver):
    """
    Test to collect only recent visitors
    """
    profiles_page = ProfilesPage(driver)
    profiles_page.open_profiles()

    # Go to recent visitors
    profiles_page.open_recent_visitors()

    # Collect profiles
    profiles, count = profiles_page.get_all_profiles_with_scroll()

    logger.info(f"✅ Recent Visitors Count: {count}")
    for profile in profiles:
        logger.info(f"  - {profile['name_age']}")

    # Scroll back to top
    profiles_page.scroll_back_to_top()

    assert count >= 0, "Count should be non-negative"
