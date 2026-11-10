import re
from playwright.sync_api import Page, expect
import pytest

# import the DashboardPage class from the pages/orangehrm_dashboard_page.py file
from pages.orangehrm_dashboard_page import DashboardPage

from pages.orangehrm_login_page import LoginPage


def test_dashboard_heading(logged_in_page: Page) -> None:
    # retrieve ui elements from the dashboard page
    dashboard_page = DashboardPage(logged_in_page) # logged_in_page is from conftest.py starting on dashboard page.
    
    # verify that we are on the dashboard page
    expect(logged_in_page).to_have_url(re.compile(r"/dashboard"))
    
    # verify that the dashboard heading is visible
    expect(dashboard_page.heading).to_be_visible()
    
def test_logging_out(logged_in_page: Page) -> None:
    # retrieve ui elements from the dashboard page
    dashboard_page = DashboardPage(logged_in_page)
    
    login_page = LoginPage(logged_in_page) # needed for later in test
    
    # click on the user dropdown menu
    dashboard_page.click_account_dropdown()
    
    # click on the logout button
    dashboard_page.click_logout()
    
    # verify that we are back on the login page
    expect(logged_in_page).to_have_url(re.compile(r"/login"))
    expect(login_page.login_button).to_be_visible()
    
    
# UI navigation tests
@pytest.mark.parametrize("menu_item, url_part", [
    pytest.param("Admin", "/admin", id="admin"),
    pytest.param("PIM", "/pim", id="pim"),
    pytest.param("Leave", "/leave", id="leave"),
    pytest.param("Time", "/time", id="time"),
    pytest.param("Recruitment", "/recruitment", id="recruitment"),
    pytest.param("My Info", "/viewPersonalDetails", id="viewPersonalDetails"), # redirect to pim/viewPersonalDetails, its a subsection of pim so myinfo doesnt exist
    pytest.param("Performance", "/performance", id="performance"),
    pytest.param("Directory", "/directory", id="directory"),
    pytest.param("Maintenance", "/maintenance", id="maintenance"),
    pytest.param("Claim", "/claim", id="claim"),
    pytest.param("Buzz", "/buzz", id="buzz"),
])
def test_sidebar_navigation(logged_in_page, menu_item, url_part):
    dashboard_page = DashboardPage(logged_in_page)
    dashboard_page.go_to(menu_item)
    expect(logged_in_page).to_have_url(re.compile(url_part))
    