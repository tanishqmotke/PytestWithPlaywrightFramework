class LandingPage:
    
    def __init__(self,page):
        self.page = page
        self.search_product = page.get_by_placeholder("Search Amazon.co.uk")
        self.search_button = self.page.locator(".nav-search-submit")

    def search_for_product(self,product_name):
        self.search_product.fill(product_name)
        self.search_button.click()
        
        
        