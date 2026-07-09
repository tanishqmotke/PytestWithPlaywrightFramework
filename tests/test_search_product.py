from pages.landing import LandingPage
from pages.search_result import ResultPage
from utils.data_helper import data_convert
#AMZQA - 1
# Given a user is on the Amazon UK homepage
# When they search for "wireless mouse"
# Then the results page shows at least 1 product, and each visible product title contains "mouse" (case-insensitive)

filepath = "data/data.json"
data = data_convert(filepath)
product_name = data["product_name"]
keyword = data["keyword"]
invalid_product_name = data["invalid_product_name"]



def test_search_valid_product_shows_matching_results(page):
    page.goto("/")
    landingpage = LandingPage(page)
    landingpage.search_for_product(product_name)
    searchresult = ResultPage(page)
    searchresult.verify_the_result(keyword)

"""
Given a user is on the Amazon UK homepage
When they search for a nonsense term with no matching products (e.g. "zzxxqq123nonsense")
Then the page displays a "no results found" message and no product cards are rendered
"""

def test_search_invalid_product_shows_no_results(page):
    page.goto("/")
    landingpage = LandingPage(page) 
    landingpage.search_for_product(invalid_product_name)
    searchresult = ResultPage(page)
    searchresult.verify_no_result_found()
    
