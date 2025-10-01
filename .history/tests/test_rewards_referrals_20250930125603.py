# tests/test_rewards_referrals.py
import pytest
from pages.rewards_referrals_screen_page import RewardsReferralsPage
from pages.user_login_page import User_login_Page  # your existing login page


@pytest.mark.usefixtures("driver")
def test_rewards_referrals_flow(driver):
    # Login (re-uses your existing login page)
    login = User_login_Page(driver)
    login.login()

    rr = RewardsReferralsPage(driver, long_wait=25)

    assert rr.open_rr_module(), "❌ Could not open Rewards & Referrals module"

    data = rr.collect_all_info()

    # print all values in a readable way
    print("\n--- Rewards & Referrals collected data ---")
    for k, v in data.items():
        print(f"{k}: {v}")

    # quick sanity checks (tweak to match your app expectations)
    assert data["title"] == "Rewards and Referrals", "Unexpected title"
    assert data["balance_label"] == "Balance", "Balance label missing"
    assert data["balance_value"] is not None, "Balance value missing"
    assert data["referral_code"] is not None, "Referral code missing"

     # Open and check policy
        policy_title = rewards.open_rewards_policy()
        assert "Rewards and Referrals Policy" in policy_title

        policy_rule = rewards.read_policy_text()
        print("✅ Policy Rule:", policy_rule)

        rewards.back_from_policy()

        # Open and check history
        history_title = rewards.open_rewards_history()
        assert "Rewards Redemption History" in history_title
        print("✅ History Title:", history_title)

        history = rewards.get_history_items()
        for entry in history:
            print(f"➡️ {entry['action']} | {entry['time']} | {entry['points']}")
