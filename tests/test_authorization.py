import pytest

from pages.authorization_page import Authorization
from pages.base_page import Base
from data.data import Data
from faker import Faker
import random
fake = Faker()

nameSignup = fake.name()
emailSignup = fake.email()
passwordSignup = fake.password()
genderSignup = random.randint(1, 2)
fnamePersonal = fake.first_name()
lnamePersonal = fake.last_name()
companyPersonal = fake.bs()
address1Personal = fake.address()
address2Personal = fake.secondary_address()
statePersonal = fake.state()
cityPersonal = fake.city()
zipcodePersonal = fake.zipcode()
phonePersonal = fake.basic_phone_number()

nameSignin = Data.user["username"]
emailSignin = Data.user["email"]
passwordSignin = Data.user["password"]

emailInvalid = fake.email()
passwordInvalid = fake.password()

class TestAuthorization:

  @pytest.fixture
  def test_setup(self, new_page):
    self.page = new_page
    self.base = Base(self.page)
    self.authorization = Authorization(self.page)
    assert self.base.getBody().is_visible()
    self.authorization.clickLoginNav()

  def test_register(self, test_setup):
    assert self.authorization.getSignupHeader().is_visible()
    self.authorization.fillSignupForm(nameSignup, emailSignup)
    self.authorization.clickButtonSignup()
    assert self.authorization.getRegisterHeaders().first.is_visible()
    day = random.randint(1, len(self.authorization.getDayOptions()) - 1)
    month = random.randint(1, len(self.authorization.getMonthOptions()) - 1)
    year = random.randint(1, len(self.authorization.getYearOptions()) - 1)
    self.authorization.completeSignupForm(genderSignup, passwordSignup, day, month, year)
    self.authorization.clickCheckboxNewsletter()
    self.authorization.clickCheckboxOptin()
    countryPersonal = random.randint(0, len(self.authorization.getCountryOptions()) - 1)
    self.authorization.fillPersonalData(fnamePersonal, lnamePersonal, companyPersonal, address1Personal, address2Personal, countryPersonal, statePersonal, cityPersonal, zipcodePersonal, phonePersonal)
    self.authorization.clickButtonCreateAccount()
    assert self.authorization.getHeaderSignupSuccess().is_visible()
    self.authorization.clickButtonContinue()
    assert self.authorization.getUsername().is_visible()
    assert self.authorization.getUsername().inner_text() == nameSignup
    self.authorization.clickDeleteNav()
    assert self.authorization.getHeaderDeleteSuccess().is_visible()
    self.authorization.clickButtonContinue()

  def test_valid_login(self, test_setup):
    assert self.authorization.getSigninHeader().is_visible()
    self.authorization.fillSigninForm(emailSignin, passwordSignin)
    self.authorization.clickButtonSignin()
    assert self.authorization.getUsername().is_visible()
    assert self.authorization.getUsername().inner_text() == nameSignin
    """uncomment these code lines if you want to delete account, like it's specified in steps 9-10"""
  # self.authorization.clickDeleteNav()
  # assert self.authorization.getHeaderDeleteSuccess().is_visible()

  def test_invalid_login(self, test_setup):
    assert self.authorization.getSigninHeader().is_visible()
    self.authorization.fillSigninForm(emailInvalid, passwordInvalid)
    self.authorization.clickButtonSignin()
    assert self.authorization.getLoginError().is_visible()
    assert self.authorization.getLoginError().inner_text() == 'Your email or password is incorrect!'

  def test_logout(self, test_setup):
    assert self.authorization.getSigninHeader().is_visible()
    self.authorization.fillSigninForm(emailSignin, passwordSignin)
    self.authorization.clickButtonSignin()
    assert self.authorization.getUsername().is_visible()
    assert self.authorization.getUsername().inner_text() == nameSignin
    self.authorization.clickLogoutNav()
    assert self.page.url == 'https://automationexercise.com/login'

  def test_register_existing(self, test_setup):
    assert self.authorization.getSignupHeader().is_visible()
    self.authorization.fillSignupForm(nameSignin, emailSignin)
    self.authorization.clickButtonSignup()
    assert self.authorization.getSignupError().is_visible()
    assert self.authorization.getSignupError().inner_text() == 'Email Address already exist!'
