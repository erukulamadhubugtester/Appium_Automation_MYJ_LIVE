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
# import logging
# from pages.user_profiles_page import ProfilesPage
# from pages.user_login_page import User_login_Page

# logger = logging.getLogger(__name__)


# @pytest.mark.usefixtures("driver")
# def test_profiles_navigation(driver):
#     """Original test structure - enhanced with scrolling"""

#     # Login
#     login = User_login_Page(driver)
#     login.login()

#     profiles = ProfilesPage(driver)

#     # 1. Open Profiles
#     header = profiles.open_profiles()
#     assert "Profiles" in header
#     logger.info(f"✅ Opened: {header}")

#     # 2. Preferred Tab - with scrolling
#     logger.info("\n📋 Collecting Preferred Profiles...")
#     profiles.open_preferred()
#     preferred_profiles, preferred_count = profiles.get_all_profiles_with_scroll()
#     logger.info(f"✅ Preferred Profiles: {preferred_count} found")
#     assert preferred_count > 0, "Should have preferred profiles"

#     # Print preferred profiles
#     for i, profile in enumerate(preferred_profiles[:5], 1):
#         logger.info(f"   {i}. {profile['name_age']}")
#     if preferred_count > 5:
#         logger.info(f"   ... and {preferred_count - 5} more")

#     profiles.scroll_back_to_top()

#     # 3. Recent Visitors - with scrolling
#     logger.info("\n📋 Collecting Recent Visitors...")
#     profiles.open_recent_visitors()

#     if profiles.is_upgrade_banner():
#         logger.warning("⚠️ Free user - Upgrade banner shown, no profiles")
#     else:
#         visitors, visitors_count = profiles.get_all_profiles_with_scroll()
#         logger.info(f"✅ Recent Visitors: {visitors_count} found")

#         if visitors_count > 0:
#             for i, profile in enumerate(visitors[:5], 1):
#                 logger.info(f"   {i}. {profile['name_age']}")
#             if visitors_count > 5:
#                 logger.info(f"   ... and {visitors_count - 5} more")

#         profiles.scroll_back_to_top()

#     # 4. Promoted - with scrolling
#     logger.info("\n📋 Collecting Promoted Profiles...")
#     profiles.open_promoted()
#     promoted_profiles, promoted_count = profiles.get_all_profiles_with_scroll()
#     logger.info(f"✅ Promoted Profiles: {promoted_count} found")
#     assert promoted_count > 0, "Should have promoted profiles"

#     # Print promoted profiles
#     for i, profile in enumerate(promoted_profiles[:5], 1):
#         logger.info(f"   {i}. {profile['name_age']}")
#     if promoted_count > 5:
#         logger.info(f"   ... and {promoted_count - 5} more")

#     profiles.scroll_back_to_top()

#     # Final Summary
#     logger.info("\n" + "=" * 60)
#     logger.info("📊 SUMMARY")
#     logger.info("=" * 60)
#     logger.info(f"Preferred Profiles: {preferred_count}")
#     logger.info(f"Promoted Profiles: {promoted_count}")
#     logger.info("=" * 60)
#     logger.info("✅ Test completed successfully!")


# @pytest.mark.usefixtures("driver")
# def test_profiles_complete_collection(driver):
#     """Collect everything from all tabs automatically"""

#     login = User_login_Page(driver)
#     login.login()

#     profiles = ProfilesPage(driver)
#     profiles.open_profiles()

#     # One function call to collect everything
#     all_data = profiles.collect_all_profiles_data()

#     # Verify data
#     assert all_data["main_profiles"]["total_count"] > 0
#     assert all_data["preferred"]["total_count"] > 0
#     assert all_data["promoted"]["total_count"] > 0

#     logger.info("✅ Complete collection test passed!")

