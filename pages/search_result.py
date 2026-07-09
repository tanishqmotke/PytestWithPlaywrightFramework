from playwright.sync_api import expect
class ResultPage:

    def __init__(self,page):
        self.page = page
        self.all_search_result = page.locator(".puisg-col-inner")
        
    def verify_the_result(self,keyword):
        expect(self.all_search_result.first).to_be_visible()
        
        titles = self.all_search_result.locator("h2 span")
        count = titles.count()
        assert count>=1
        for i in range(count):
            title_locator = titles.nth(i)
            if not title_locator.is_visible():
                continue
            title = title_locator.text_content()
            assert keyword.lower() in title.lower(), f"Title does not contain '{keyword}' : {title}"
