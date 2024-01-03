import pytest

from pages.misc_page import Miscellaneous
from pages.base_page import Base
from faker import Faker
fake = Faker()

emailSub = fake.email()

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

  def test_subscription(self, test_setup):
    self.misc.getFooter().scroll_into_view_if_needed()
    assert self.misc.getSubHeader().is_visible()
    assert self.misc.getSubHeader().inner_text() == 'SUBSCRIPTION'
    self.misc.fillSubForm(emailSub)
    assert self.misc.getAlertSuccess().is_visible()
    assert self.misc.getAlertSuccess().inner_text() == 'You have been successfully subscribed!'