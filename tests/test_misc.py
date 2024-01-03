import pytest
import os

from pages.misc_page import Miscellaneous
from pages.base_page import Base
from faker import Faker
fake = Faker()

emailSub = fake.email()

nameContact = fake.name()
emailContact = fake.email()
subjectContact = fake.word()
messageContact = fake.paragraph(nb_sentences=5)

scriptPath = os.path.abspath(__file__)
filePath = os.path.join(os.path.dirname(scriptPath), '..', 'data', 'doge.jpg')

class TestMiscellaneous:

  @pytest.fixture
  def test_setup(self, page):
    self.page = page
    self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
    self.base = Base(self.page)
    self.misc = Miscellaneous(self.page)
    self.base.url("")
    assert self.base.getBody().is_visible()

  def test_contact(self, test_setup):
    self.misc.clickContactNav()
    assert self.misc.getContactHeader().is_visible()
    self.misc.fillContactForm(nameContact, emailContact, subjectContact, messageContact)
    self.misc.fileSelect(filePath)
    self.misc.clickContactSubmit()
    assert self.misc.getContactAlert().is_visible()
    assert self.misc.getContactAlert().inner_text() == 'Success! Your details have been submitted successfully.'
    self.misc.clickButtonHome()
    assert self.page.url == 'https://automationexercise.com/'

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