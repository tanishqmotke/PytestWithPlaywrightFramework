class ResultPage:

    def __init__(self,page):
        self.page = page
        self.all_search_result = page.locator(".puisg-col-inner")
        
    def verify_the_result(self,product_name):
        print(self.all_search_result.count())
        self.page.wait_for_load_state("networkidle")
        
        titles = self.all_search_result.locator("h2 span")
        for i in range(titles.count()):
            title = titles.nth(i).text_content()
            if product_name.lower() in title.lower():
                print(f"Found: {title}")
            else:
                print(f"This title doesn't have the product name: {title}")
        print("End of the script")
