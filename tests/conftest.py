# conftest.py
import pytest
from playwright.sync_api import sync_playwright

# Fixture to launch a browser with parametrization
@pytest.fixture(scope="session", params=["chromium", "firefox"])
def browser(request):
    with sync_playwright() as p:
        if request.param == "chromium":
            browser = p.chromium.launch(headless=False)
        elif request.param == "firefox":
            browser = p.firefox.launch(headless=False)
        else:
            raise ValueError("Unsupported browser: {}".format(request.param))
        yield browser
        browser.close()

# Fixture to set up a new page for each test
@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

    import pytest

# Pytest hook to add custom test reporting
def pytest_runtest_makereport(item, call):
    if call.when == "call":
        if call.excinfo is None:
            # Test passed
            print(f"Test '{item.name}' PASSED")
        else:
            # Test failed
            print(f"Test '{item.name}' FAILED")

