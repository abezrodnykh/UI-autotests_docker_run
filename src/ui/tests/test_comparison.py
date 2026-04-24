import allure

from src.ui.const import Data


@allure.story("Страница сравнения товаров")
class TestComparisonPage:
    @allure.title("Проверка страницы сравнения товаров")
    def test_comparison(self, product_page, comparison_page):
        product_page.open()
        product_page.mov_to_product_compare()
        comparison_page.text_verification()