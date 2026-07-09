class LandingPage:
    
    def __init__(self,page):
        self.page = page
        self.search_product = page.get_by_placeholder("Search Amazon.co.uk")
        self.accept_cookies = page.get_by_role("button",name="Accept")
        self.search_button = self.page.locator(".nav-search-submit")

    def search_for_product(self,product_name):
        if self.accept_cookies.is_visible():
            self.accept_cookies.click()
        self.search_product.fill(product_name)
        self.search_button.click()
        
        
        