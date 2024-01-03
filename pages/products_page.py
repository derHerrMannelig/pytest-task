from playwright.sync_api import Page
from pages.base_page import Base

productsNav = 'a[href="/products"]'
productsList = 'div.features_items'
productsView = 'div.choose > ul > li > a'
productsNames = 'div.productinfo > p'
productName = 'div.product-information > h2'
productCategory = '// *[contains(text(), "Category:")]'
productPrice = 'div.product-information > span > span'
productAvailability = '// *[contains(text(), "Availability:")]'
productCondition = '// *[contains(text(), "Condition:")]'
productBrand = '// *[contains(text(), "Brand:")]'
productSearch = 'input#search_product'
submitSearch = 'button#submit_search'
searchedProducts = 'h2.title'

class Products():
  def __init__(self, page: Page):
    self.page = page
    self.base = Base(self.page)

  def clickProductsNav(self):
    self.base.click(productsNav)

  def clickFirstProductView(self):
    self.base.get(productsView).first.click()

  def getProductsList(self):
    return self.base.get(productsList)

  def getProductName(self):
    return self.base.get(productName)

  def getProductCategory(self):
    return self.base.get(productCategory)

  def getProductPrice(self):
    return self.base.get(productPrice)

  def getProductAvailability(self):
    return self.base.get(productAvailability)

  def getProductCondition(self):
    return self.base.get(productCondition)

  def getProductBrand(self):
    return self.base.get(productBrand)

  def getProductsNames(self):
    return self.base.get(productsNames).all()

  def getSearchedProducts(self):
    return self.base.get(searchedProducts)

  def getSearchResult(self):
    return self.base.get(productsNames)

  def searchProduct(self, prompt):
    self.base.get(productSearch).fill(prompt)
    self.base.click(submitSearch)
