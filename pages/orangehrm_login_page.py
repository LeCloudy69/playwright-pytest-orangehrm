from playwright.sync_api import Page

class LoginPage:
    URL = "/web/index.php/auth/login"
    
    def open(self):
        # base url is in pytest.ini, ...com/URL variable is used to use our baseurl to navigate to the login page
        self.page.goto(self.URL)
        # self.URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")
        
        self.invalid_credentials_message = page.get_by_text("Invalid credentials") # Now we can use 'to be visible' to see failed login
        self.missing_credentials_message = page.get_by_text("Required") # Now we can use 'to be visible' to see missing login info
       
        
    def enter_username(self, username: str):
        self.username_input.fill(username)

    def enter_password(self, password: str):
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()
        
    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        