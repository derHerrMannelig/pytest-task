import pytest

from pages.products_page import Products
from pages.base_page import Base
import random

class TestProducts:

  @pytest.fixture
  def test_setup(self, page):
    self.page = page
    self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
    self.base = Base(self.page)
    self.products = Products(self.page)
    self.base.url("")
    assert self.base.getBody().is_visible()
    self.products.clickProductsNav()
    assert self.page.url == 'https://automationexercise.com/products'

  def test_product_detail(self, test_setup):
    assert self.products.getProductsList().is_visible()
    self.products.clickFirstProductView()
    assert self.page.url == 'https://automationexercise.com/product_details/1'
    assert self.products.getProductName().is_visible()
    assert self.products.getProductCategory().is_visible()
    assert self.products.getProductPrice().is_visible()
    assert self.products.getProductAvailability().is_visible()
    assert self.products.getProductCondition().is_visible()
    assert self.products.getProductBrand().is_visible()

  def test_search(self, test_setup):
    index = random.randint(0, len(self.products.getProductsNames()) - 1)
    prompt = self.products.getProductsNames()[index].text_content()
    self.products.searchProduct(f'{prompt}')
    assert self.products.getSearchedProducts().is_visible()
    assert self.products.getSearchResult().is_visible()
    assert self.products.getSearchResult().inner_text() == f'{prompt}'
