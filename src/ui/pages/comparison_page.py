import allure
from playwright.sync_api import Page, expect

from src.ui.const import Data
from src.ui.helper.urls import BASE_URL, COMPARISON_URL
from src.ui.page_elements.element import Element
from src.ui.pages.base_page import BasePage


class ComparisonPage(BasePage):
    """Логика для страницы 'Сравнение товара'"""

    def __init__(self, page: Page, url=BASE_URL + COMPARISON_URL):
        super().__init__(page, url)
        self.summary_compare_1 = Element(page, strategy="locator", selector="(//td[@class='description'])[1]",
                                         allure_name="Первое описание товара")
        self.summary_compare_2 = Element(page, strategy="locator", selector="(//td[@class='description'])[2]",
                                         allure_name="Второе описание товара")

    def text_verification(self):
        """Сверяет текст в описании товара"""
        with allure.step("Проверим, что выполнен переход на страницу 'Сравнение товара'"):
            expect(self.page).to_have_url(BASE_URL + COMPARISON_URL)
        text_1 = self.summary_compare_1.get_text()
        with allure.step("Проверим, что описание первого товара соответствует"):
            assert Data.BORN_TO in text_1
        text_2 = self.summary_compare_2.get_text()
        with allure.step("Проверим, что описание второго товара соответствует"):
            assert Data.INTEL_CORE in text_2
