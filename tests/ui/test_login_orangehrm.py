import re
from playwright.sync_api import Page, expect
import pytest

# import the LoginPage class from the pages/orangehrm_login_page.py file
from pages.orangehrm_login_page import LoginPage

# import the DashboardPage class from the pages/orangehrm_dashboard_page.py file
from pages.orangehrm_dashboard_page import DashboardPage

@pytest.mark.parametrize("username, password", [
    ("Admin", "admin123"),
    ("admin", "admin123"),

])
def test_valid_login(page: Page, username: str, password: str) -> None:
    
    # retrieve ui elements from the login page
    login_page = LoginPage(page)
    
    # go to the login page
    login_page.open()
    
    # login with valid credentials
    login_page.login(username, password)
    
    # retrieve ui elements from the dashboard page
    dashboard_page = DashboardPage(page)
    
    # verify that we logged in successfully
    expect(page).to_have_url(re.compile(r"/dashboard"))
    expect(dashboard_page.heading).to_be_visible()
    
    
@pytest.mark.parametrize("username, password", [
    ("Admin", "wrongpass"),
    ("wronguser", "admin123"),
    ("admin", "admin321"),
    ("Admin", "Admin123"),
])
def test_invalid_login(page: Page, username: str, password: str) -> None:
    # retrieve ui elements from the login page
    login_page = LoginPage(page)
    
    # go to the login page
    login_page.open()
    
    # login with invalid credentials
    login_page.login(username, password)
    
    # verify that we failed to log in
    expect(login_page.invalid_credentials_message).to_be_visible()
    expect(page).to_have_url(re.compile(r"/login"))
 
    
@pytest.mark.parametrize("username, password, expected_count", [
    ("Admin", "", 1),
    ("", "admin123", 1),
    (" ", " ", 2),
])
def test_missing_credentials(page: Page, username: str, password: str, expected_count: int) -> None:
    # retrieve ui elements from the login page
    login_page = LoginPage(page)
    
    # go to the login page
    login_page.open()
    
    # login with missing credentials
    login_page.login(username, password)
    
    # verify that we failed to log in
    expect(login_page.missing_credentials_message).to_have_count(expected_count)
    expect(page).to_have_url(re.compile(r"/login"))