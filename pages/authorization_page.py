from playwright.sync_api import Page
from pages.base_page import Base

loginNav = 'a[href="/login"]'
deleteNav = 'a[href="/delete_account"]'
signupHeader = 'div.signup-form > h2'
registerHeaders = 'h2.title.text-center > b'
inputName = 'input[data-qa="signup-name"]'
inputEmail = 'input[data-qa="signup-email"]'
buttonSignup = 'button[data-qa="signup-button"]'
buttonCreateAccount = 'button[data-qa="create-account"]'
radioGender1 = 'input#id_gender1'
radioGender2 = 'input#id_gender2'
inputPassword = 'input[data-qa="password"]'
selectDay = 'select[data-qa="days"]'
selectMonth = 'select[data-qa="months"]'
selectYear = 'select[data-qa="years"]'
selectCountry = 'select[data-qa="country"]'
dayOptions = 'select[data-qa="days"] > option'
monthOptions = 'select[data-qa="months"] > option'
yearOptions = 'select[data-qa="years"] > option'
checkboxNewsletter = 'input#newsletter'
checkboxOptin = 'input#optin'
inputFName = 'input#first_name'
inputLName = 'input#last_name'
inputCompany = 'input#company'
inputAddress1 = 'input#address1'
inputAddress2 = 'input#address2'
countryOptions = 'select[data-qa="country"] > option'
inputState ='input#state'
inputCity = 'input#city'
inputZipcode = 'input#zipcode'
inputPhone = 'input#mobile_number'
headerSignupSuccess = 'h2[data-qa="account-created"]'
headerDeleteSuccess = 'h2[data-qa="account-deleted"] > b'
buttonContinue = 'a[data-qa="continue-button"]'
username = 'li > a > b'

class Authorization():
  def __init__(self, page: Page):
    self.page = page
    self.base = Base(self.page)

  def clickLoginNav(self):
    self.base.click(loginNav)

  def clickDeleteNav(self):
    self.base.click(deleteNav)

  def clickButtonSignup(self):
    self.base.click(buttonSignup)

  def clickGender1(self):
    self.base.click(radioGender1)

  def clickGender2(self):
    self.base.click(radioGender2)

  def clickCheckboxNewsletter(self):
    self.base.click(checkboxNewsletter)

  def clickCheckboxOptin(self):
    self.base.click(checkboxOptin)

  def clickButtonCreateAccount(self):
    self.base.click(buttonCreateAccount)

  def clickButtonContinue(self):
    self.base.click(buttonContinue)

  def getSignupHeader(self):
    return self.base.get(signupHeader)

  def getRegisterHeaders(self):
    return self.base.get(registerHeaders)

  def getSelectDay(self):
    return self.base.get(selectDay)

  def getSelectMonth(self):
    return self.base.get(selectMonth)

  def getSelectYear(self):
    return self.base.get(selectYear)

  def getSelectCountry(self):
    return self.base.get(selectCountry)

  def getHeaderSignupSuccess(self):
    return self.base.get(headerSignupSuccess)

  def getHeaderDeleteSuccess(self):
    return self.base.get(headerDeleteSuccess)

  def getUsername(self):
    return self.base.get(username)

  def getDayOptions(self):
    return self.base.get(dayOptions).all()

  def getMonthOptions(self):
    return self.base.get(monthOptions).all()

  def getYearOptions(self):
    return self.base.get(yearOptions).all()

  def getCountryOptions(self):
    return self.base.get(countryOptions).all()

  def fillSignupForm(self, name, email):
    self.base.get(inputName).fill(name)
    self.base.get(inputEmail).fill(email)

  def completeSignupForm(self, gender, password, day, month, year):
    if gender == 1:
      self.clickGender1()
    elif gender == 2:
      self.clickGender2()
    self.base.get(inputPassword).fill(password)
    self.getSelectDay().select_option(index=day)
    self.getSelectMonth().select_option(index=month)
    self.getSelectYear().select_option(index=year)

  def fillPersonalData(self, fname, lname, company, address1, address2, country, state, city, zipcode, phone):
    self.base.get(inputFName).fill(fname)
    self.base.get(inputLName).fill(lname)
    self.base.get(inputCompany).fill(company)
    self.base.get(inputAddress1).fill(address1)
    self.base.get(inputAddress2).fill(address2)
    if country == 0:
      pass
    else:
      self.getSelectCountry().select_option(index=country)
    self.base.get(inputState).fill(state)
    self.base.get(inputCity).fill(city)
    self.base.get(inputZipcode).fill(zipcode)
    self.base.get(inputPhone).fill(phone)
