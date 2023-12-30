from playwright.sync_api import Page

body = 'body'

class Base():
  def __init__(self, page: Page):
    self.page = page

  def url(self, url):
    self.page.goto(url)
    self.page.wait_for_load_state()

  def get(self, locator):
    self.page.wait_for_load_state()
    return self.page.locator(locator)

  def click(self, locator):
    self.page.wait_for_load_state()
    self.get(locator).click()

  def getBody(self):
    self.page.wait_for_load_state()
    return self.get(body)