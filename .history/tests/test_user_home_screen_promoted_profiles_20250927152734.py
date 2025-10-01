import pytest
from pages.user_login_page import User_login_Page
from pages.user_home_page import HomePage


@pytest.mark.usefixtures("driver")
def test_home_page_after_login(driver):