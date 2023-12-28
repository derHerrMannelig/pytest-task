from playwright.sync_api import Page
from pages.base_page import Base

class Authorization():
  def __init__(self, page: Page):
    self.page = page
    self.base = Base(self.page)

