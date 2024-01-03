from playwright.sync_api import Page
from pages.base_page import Base

buttonHome = 'a.btn.btn-success'
casesNav = 'li > a[href="/test_cases"]'
contactNav = 'a[href="/contact_us"]'
footer = 'footer#footer'
subHeader = 'div.single-widget > h2'
contactHeader = 'div.contact-form > h2.title'
subInput = 'input[type="email"]'
submit = 'button#subscribe'
alertSuccess = 'div.alert.alert-success'
contactAlert = 'div.contact-form > div.alert.alert-success'
nameContact = 'input[data-qa="name"]'
emailContact = 'input[data-qa="email"]'
subjectContact = 'input[data-qa="subject"]'
messageContact = 'textarea[data-qa="message"]'
fileUpload = 'input[type="file"]'
contactSubmit = 'input[data-qa="submit-button"]'

class Miscellaneous():
  def __init__(self, page: Page):
    self.page = page
    self.base = Base(self.page)

  def clickCasesNav(self):
    self.base.click(casesNav)

  def clickContactNav(self):
    self.base.click(contactNav)

  def clickContactSubmit(self):
    self.page.on("dialog", lambda dialog: dialog.accept())
    self.base.click(contactSubmit)

  def clickButtonHome(self):
    self.base.click(buttonHome)

  def clickSubmit(self):
    self.base.click(submit)

  def getFooter(self):
    return self.base.get(footer)

  def getSubHeader(self):
    return self.base.get(subHeader)

  def getContactHeader(self):
    return self.base.get(contactHeader)

  def getAlertSuccess(self):
    return self.base.get(alertSuccess)

  def getContactAlert(self):
    return self.base.get(contactAlert)

  def fillSubForm(self, email):
    self.base.get(subInput).fill(email)
    self.clickSubmit()

  def fillContactForm(self, name, email, subject, message):
    self.base.get(nameContact).fill(name)
    self.base.get(emailContact).fill(email)
    self.base.get(subjectContact).fill(subject)
    self.base.get(messageContact).fill(message)

  def fileSelect(self, file):
    with self.page.expect_file_chooser() as fc_info:
      self.base.click(fileUpload)
    file_chooser = fc_info.value
    file_chooser.set_files(file)
