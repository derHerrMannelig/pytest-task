import pytest

from playwright.sync_api import Playwright

disable_loggers = []

@pytest.fixture(scope='function')
def new_page(playwright: Playwright, request):
  browser_name = request.config.getoption('--browser_name')
  headless = False if request.config.getoption("--headed") else True
  if browser_name == "chromium":
    browser = playwright.chromium.launch(headless=headless)
  if browser_name == "firefox":
    browser = playwright.firefox.launch(headless=headless)
  if browser_name == "webkit":
    browser = playwright.webkit.launch(headless=headless)
  context = browser.new_context(viewport={"width": 1920, "height": 1080})
  def block_ads(route):
    if route.request.url.startswith("https://googleads."):
      route.abort()
    else:
      route.continue_()
  context.route("**/*", block_ads)
  page = context.new_page()
  page.goto(f'http://automationexercise.com')
  page.wait_for_load_state()
  yield page
  browser.close()

def pytest_addoption(parser):
  parser.addoption('--browser_name', action='store', default='chromium')