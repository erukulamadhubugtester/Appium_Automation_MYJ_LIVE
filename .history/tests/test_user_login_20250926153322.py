import pytest
from pages.user_login_page import User_login_Page


@pytest.mark.usefixtures("driver")
def test_user_login(driver):  # ✅ starts with test_
    app = User_login_Page(driver)

    # 
    
