import pytest

@pytest.fixture
def browser_context_args(browser_context_args):
    return {
       **browser_context_args,
       "base_url" :"https://www.amazon.co.uk/"        
    }
    