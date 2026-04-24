from collections import namedtuple
from pathlib import Path

import pytest

from src.ui.browser.browser_launcher import BrowserLauncher
from src.ui.pages.base_page import BasePage
from src.ui.pages.cart_page import CartPage
from src.ui.pages.comparison_page import ComparisonPage
from src.ui.pages.payment_page import PaymentPage
from src.ui.pages.product_page import ProductPage

config_yml_path = Path(__file__).parent.parent / "config_browser.yaml"


UserPageData = namedtuple("UesrPageData", ["login", "password"])

@pytest.fixture
def user_page(request):
    login, password = request.param
    yield UserPageData(login, password)


@pytest.fixture
def browser():
    brw = BrowserLauncher(config_yml_path)
    new_page = brw.create_page()
    yield new_page
    brw.close()


@pytest.fixture
def base_page(browser):
    """Фикстура с методами Главной страницы"""
    return BasePage(browser)

@pytest.fixture
def product_page(browser):
    """Фикстура с методами на странице 'Товары'"""
    return ProductPage(browser)

@pytest.fixture
def cart_page(browser):
    """Фикстура с методами на странице 'Корзина'"""
    return CartPage(browser)

@pytest.fixture
def payment_page(browser):
    """Фикстура с методами на странице 'Оплата'"""
    return PaymentPage(browser)

@pytest.fixture
def comparison_page(browser):
    """Фикстура с методами на странице 'Сравнение товара'"""
    return ComparisonPage(browser)

