from playwright.sync_api import Page

class Base():
  def __init__(self, page: Page):
    self.page = page

  def url(self, url):
    self.page.goto(url)
    self.page.wait_for_load_state()

  def get(self, locator):
    return self.page.locator(locator)

  def click(self, locator):
    self.get(locator).click()