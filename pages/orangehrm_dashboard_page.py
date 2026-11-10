from playwright.sync_api import Page, expect

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        
        # account dropdown
        self.account_dropdown = page.locator(".oxd-userdropdown-icon") # dropdown icon. still needs to be clicked
        self.logout_button = page.get_by_role("menuitem", name="Logout")
        
        # UI elements on the dashboard page
        self.heading = page.get_by_role("heading", name="Dashboard")
        
      
    # account dropdown methods  
    def click_account_dropdown(self):
        self.account_dropdown.click()
        
    def click_logout(self):
        self.logout_button.click()
    
        
    # dashboard page methods
    def go_to(self, menu_name: str):
        self.page.locator(".oxd-main-menu-item").filter(has_text=menu_name).click()
        
