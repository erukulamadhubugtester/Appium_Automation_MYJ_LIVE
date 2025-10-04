# import pytest
# from pages.user_connections_page import ConnectionsPage
# from pages.user_login_page import User_login_Page


# @pytest.mark.usefixtures("driver")
# def test_connections(driver):
#     # Login
#     login = User_login_Page(driver)
#     login.login()

#     connections = ConnectionsPage(driver)
#     connections.open_connections()

#     title = connections.get_connections_title()
#     assert "Connections" in title

#     sent_text = connections.get_sent_tab_text()
#     print("Sent Tab:", sent_text)

#     profiles = connections.get_profiles_name_age()
#     print("Profiles:", profiles)

#     assert len(profiles) > 0

# ======== 1.a code =======


# import pytest
# from pages.user_connections_page import ConnectionsPage
# from pages.user_login_page import User_login_Page


# @pytest.mark.usefixtures("driver")
# def test_connections(driver):
#     """Verify that connections screen loads and profiles are displayed."""

#     # Step 1: Login
#     login = User_login_Page(driver)
#     login.login()

#     # Step 2: Open Connections
#     connections = ConnectionsPage(driver)
#     connections.open_connections()

#     # Step 3: Verify title
#     title = connections.get_connections_title()
#     assert "Connections" in title, f"❌ Expected 'Connections' in title, got '{title}'"

#     # Step 4: Verify Sent tab text is displayed
#     sent_text = connections.get_sent_tab_text()
#     print(f"📌 Sent Tab Text: {sent_text}")
#     assert sent_text, "❌ Sent tab text not found"

#     # Step 5: Collect Profiles with scroll
#     profiles = connections.get_profiles_name_age()
#     print(f"👤 Profiles Collected ({len(profiles)}): {profiles}")

#     # Step 6: Validation
#     assert len(profiles) > 0, "❌ No profiles found on connections screen"


# ======== 1.b ===


# === test_connections.py ===
import pytest
from pages.user_connections_page import ConnectionsPage
from pages.user_login_page import User_login_Page


@pytest.mark.usefixtures("driver")
@pytest.mark.usefixtures("driver")
def test_connections_all_tabs(driver):
    login = User_login_Page(driver)
    login.login()

    connections = ConnectionsPage(driver)
    connections.open_connections()
    assert "Connections" in connections.get_connections_title()

    # Sent
    connections.click_tab("Sent")
    sent_profiles = connections.get_profiles()
    print("Sent Profiles:", sent_profiles)

    # Received
    connections.click_tab("Received")
    received_profiles = connections.get_profiles()
    print("Received Profiles:", received_profiles)

    # Connected
    connections.click_tab("Connected")
    connected_profiles = connections.get_profiles()
    print("Connected Profiles:", connected_profiles)
