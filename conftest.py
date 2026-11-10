import os
import re
import pytest
from playwright.sync_api import expect
from pages.orangehrm_login_page import LoginPage

from dotenv import load_dotenv
load_dotenv()

ADMIN_USER = os.getenv("ADMIN_USER", "Admin")
ADMIN_PASS = os.getenv("ADMIN_PASS", "admin123")


@pytest.fixture
def logged_in_page(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(ADMIN_USER, ADMIN_PASS)
    expect(page).to_have_url(re.compile(r"/dashboard"))
    return page