import pytest
from pages.user_login_page import User_login_Page
from pages.user_chat_page import ChatPage


@pytest.mark.usefixtures("driver")
def test_chat_profiles_flow(driver):
    """Login, open chat, check elements, scroll and print profiles"""
    login = User_login_Page(driver)
    login.login()

    chat = ChatPage(driver)
    chat.open_chat_module()

    # Check if free member restriction exists
    if chat.is_free_member_restriction():
        print("\n" + "=" * 60)
        print("⚠️ FREE MEMBER ACCOUNT DETECTED")
        print("=" * 60)
        print("This account has limited access to chat profiles.")
        print("Profile completion or upgrade required to view all profiles.")
        print("=" * 60 + "\n")
        pytest.skip("Skipping test - Free member restriction detected")

    # Check UI elements (only if not restricted)
    three_dots_visible = chat.is_three_dots_displayed()
    search_field_visible = chat.is_search_field_displayed()

    print(f"\n✅ Three dots visible: {three_dots_visible}")
    print(f"✅ Search field visible: {search_field_visible}")

    # Only assert if we expect these elements (not restricted)
    if not chat.is_free_member_restriction():
        assert three_dots_visible, "Three dots not displayed"
        assert search_field_visible, "Search field not displayed"

    # Scroll and collect profiles
    print("\n📋 Collecting profiles...")
    profiles = chat.get_profiles(max_scrolls=10)

    print("\n" + "=" * 60)
    print(f"📊 TOTAL PROFILES COLLECTED: {len(profiles)}")
    print("=" * 60)

    if profiles:
        print("\n👥 Profile List:")
        for idx, profile in enumerate(profiles, 1):
            print(f"{idx}. {profile}")
    else:
        print("\n⚠️ No profiles collected (possibly due to free member restriction)")

    print("\n" + "=" * 60 + "\n")
