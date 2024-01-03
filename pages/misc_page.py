from playwright.sync_api import Page
from pages.base_page import Base

casesNav = 'li > a[href="/test_cases"]'
footer = 'footer#footer'
subHeader = 'div.single-widget > h2'
subInput = 'input[type="email"]'
submit = 'button#subscribe'
alertSuccess = 'div.alert.alert-success'

class Miscellaneous():
  def __init__(self, page: Page):
    self.page = page
    self.base = Base(self.page)

  def clickCasesNav(self):
    self.base.click(casesNav)

  def clickSubmit(self):
    self.base.click(submit)

  def getFooter(self):
    return self.base.get(footer)

  def getSubHeader(self):
    return self.base.get(subHeader)

  def getAlertSuccess(self):
    return self.base.get(alertSuccess)

  def fillSubForm(self, email):
    self.base.get(subInput).fill(email)
    self.clickSubmit()
