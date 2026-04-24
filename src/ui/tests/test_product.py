import allure

from src.ui.const import Data


@allure.story("Страница c товарами")
class TestProductPage:
    @allure.title("Проверка формирования хлебных крошек")
    def test_breadcrumb(self, product_page):
        product_page.open()
        product_page.checkout_card_apple_shuffle()
        product_page.check_breads_crumb(Data.BREADCRUMB)
