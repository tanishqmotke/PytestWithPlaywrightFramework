import pytest
from playwright.sync_api import expect,TimeoutError as PlaywrightTimeoutError
@pytest.fixture
def browser_context_args(browser_context_args):
    return {
       **browser_context_args,
       "base_url" :"https://www.amazon.co.uk/"        
    }

@pytest.fixture
def page(page):
    page.goto("/")
    try:
        accept_cookies = page.get_by_role("button", name="Accept")
        expect(accept_cookies).to_be_visible(timeout=5000)
        accept_cookies.click()
    except PlaywrightTimeoutError:
        pass  # cookie banner didn't appear, nothing to dismiss
    return page