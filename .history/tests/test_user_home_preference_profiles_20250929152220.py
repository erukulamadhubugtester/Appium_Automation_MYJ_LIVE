def test_loop_through_preference_profiles(driver):
    login_page = User_login_Page(driver)
    login_page.login()

    page = PreferenceProfilesPage(driver)
    page.click_home_imageview_13()

    profiles = page.loop_profiles(max_profiles=200)

    for idx, p in enumerate(profiles, start=1):
        print(f"🔎 Profile {idx}: {p['username']}, {p['age']}, {p['location']}")

    print(f"📌 Total unique profiles visited: {len(profiles)}")
    assert len(profiles) > 0, "❌ No profiles found"
