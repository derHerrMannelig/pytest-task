import pytest

from pages.authorization_page import Authorization
from pages.base_page import Base

class TestAuthorization:

  @pytest.fixture
  def test_setup(self, page):
    self.page = page
    self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
    self.base = Base(self.page)
    self.authorization = Authorization(self.page)
    self.base.url("")
    assert self.page.url == 'https://automationexercise.com/'

  def test_register(self, test_setup):
    print('smth')