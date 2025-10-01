import pytest
from pages.rewards_referrals_screen_page import RewardsReferralsPage
from pages.user_login_page import User_login_Page


@pytest.mark.usefixtures("driver")
def test_rewards_referrals_flow(driver):
    # Login
    login = User_login_Page(driver)
    login.login()

    rr = RewardsReferralsPage(driver, long_wait=25)

    # ✅ Open R&R module
    assert rr.open_rr_module(), "❌ Could not open Rewards & Referrals module"

    # ✅ Collect and print data
    data = rr.collect_all_info()
    print("\n--- Rewards & Referrals collected data ---")
    for k, v in data.items():
        print(f"{k}: {v}")

    # ✅ Sanity checks
    assert data["title"] == "Rewards and Referrals"
    assert data["balance_label"] == "Balance"
    assert data["balance_value"] is not None
    assert data["referral_code"] is not None

    # ✅ Policy flow
    policy_title = rr.open_rewards_policy()
    assert "Rewards and Referrals Policy" in policy_title

    policy_rule = rr.read_policy_text()
    print("✅ Policy Rule:", policy_rule)
    rr.back_from_policy()

    # ✅ History flow
    history_title = rr.open_rewards_history()
    assert "Rewards Redemption History" in history_title
    print("✅ History Title:", history_title)

    history = rr.get_history_items()
    for entry in history:
        print(f"➡️ {entry['action']} | {entry['time']} | {entry['points']}")
