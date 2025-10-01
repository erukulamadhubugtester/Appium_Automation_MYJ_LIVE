import pytest
from pages.user_login_page import User_login_Page
from pages.user_home_page import HomePage


@pytest.mark.usefixtures("driver")
def test_home_page_after_login(driver):
    # # Step 1: Login
    # login_page = User_login_Page(driver)
    # login_page.login()  # ✅ works now

    # # Step 2: Validate home page icons
    # home = HomePage(driver)
    # assert home.validate_all_icons(), "❌ Home page icons are missing"
    # print("🎉 Test Passed: All home page icons are visible")

    # assert home.is_user_image_displayed(), "❌ User image is not displayed"
    # print("🎉 Test Passed: User image is visible on home screen")

    # # ✅ Step 2: Get full Welcome text
    # welcome_text = home.get_user_welcome_text()
    # print(f"📌 Full Welcome Text: {welcome_text}")

    # # ✅ Step 3: Extract username only
    # username = home.get_logged_in_username()
    # print(f"📌 Logged in Username: {username}")

    # assert username != "", "❌ Username is empty"
    # print("🎉 Test Passed: Username displayed correctly")

    # # ✅ User ID
    # user_id = home.get_user_id()
    # print(f"📌 User ID: {user_id}")
    # assert "User ID:" in user_id, "❌ User ID not displayed"

    # # ✅ View Profile
    # assert home.is_view_profile_icon_displayed(), "❌ View Profile icon not visible"
    # assert home.is_view_profile_text_displayed(), "❌ View Profile text not visible"
    # print("🎉 View Profile section is visible")

    # # # ✅ Requests section
    # # received = home.get_requests_received_count()
    # # sent = home.get_requests_sent_count()
    # # print(f"📌 Requests Received: {received}, Sent: {sent}")
    # # assert received >= 0, "❌ Received count invalid"
    # # assert sent >= 0, "❌ Sent count invalid"

    # # # ✅ Members section
    # # connected = home.get_members_connected_count()
    # # print(f"📌 Members Connected: {connected}")
    # # assert connected >= 0, "❌ Connected count invalid"

    # # print("🎉 Test Passed: All sections validated successfully")

    # received = home.get_requests_received_count()
    # sent = home.get_requests_sent_count()
    # connected = home.get_members_connected_count()

    # assert received >= 0, "❌ Received count missing"
    # assert sent >= 0, "❌ Sent count missing"
    # assert connected >= 0, "❌ Connected count missing"

    # print(f"🎉 Test Passed: Received={received}, Sent={sent}, Connected={connected}")

    # ✅ Step 1: Login
    login_page = User_login_Page(driver)
    login_page.login()

    # ✅ Step 2: Home page actions
    home = HomePage(driver)
    received, sent, connected = home.home_page()

    # ✅ Step 3: Assertions
    assert received >= 0, "❌ Received count missing"
    assert sent >= 0, "❌ Sent count missing"
    assert connected >= 0, "❌ Connected count missing"

    print(f"🎉 Test Passed: Received={received}, Sent={sent}, Connected={connected}")

    title_text = home.get_promoted_profiles_title()
    assert title_text != "", "❌ Promoted Profiles title not visible"
    assert title_text == "Promoted Profiles", f"❌ Unexpected title: {title_text}"

    print(
        f"🎉 Test Passed: Promoted Profiles title is visible with text = '{title_text}'"
    )
