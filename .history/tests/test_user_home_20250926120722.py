def test_home_page_after_login(driver):
    # Step 1: Login
    login_page = User_login_Page(driver)
    login_page.login()  # ✅ Now this works

    # Step 2: Validate home page icons
    home = HomePage(driver)
    assert home.validate_all_icons(), "❌ Home page icons are missing"
    print("🎉 Test Passed: All home page icons are visible")
