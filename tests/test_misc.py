import pytest

from pages.misc_page import Miscellaneous
from pages.base_page import Base

class TestMiscellaneous:

  @pytest.fixture
  def test_setup(self, page):
    self.page = page
    self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
    self.base = Base(self.page)
    self.misc = Miscellaneous(self.page)
    self.base.url("")
    assert self.base.getBody().is_visible()

  def test_cases_page(self, test_setup):
    self.misc.clickCasesNav()
    assert self.page.url == 'https://automationexercise.com/test_cases'