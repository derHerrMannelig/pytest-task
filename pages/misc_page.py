from playwright.sync_api import Page
from pages.base_page import Base

casesNav = 'li > a[href="/test_cases"]'

class Miscellaneous():
  def __init__(self, page: Page):
    self.page = page
    self.base = Base(self.page)

  def clickCasesNav(self):
    self.base.click(casesNav)