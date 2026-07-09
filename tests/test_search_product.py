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

def test_search_for_product(page):
    page.goto("/")
    landingpage = LandingPage(page)
    landingpage.search_for_product(product_name)
    searchresult = ResultPage(page)
    searchresult.verify_the_result(keyword)
    
    