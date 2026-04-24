import allure
from playwright.sync_api import Page

from src.ui.helper.urls import BASE_URL, CART_URL
from src.ui.page_elements.button import Button
from src.ui.page_elements.element import Element
from src.ui.pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page, url=BASE_URL + CART_URL):
        super().__init__(page, url)
        self.image_column = Element(page, strategy="locator", selector="//tr//td[@class='text-center']//a",
                                    allure_name="Изображение товара")
        self.button_checkout = Button(page, strategy="locator", selector="//a[text()='Checkout']",
                                      allure_name="Checkout")

    def check_number_devices(self, devices=1):
        """Проверяет количество девайсов в корзине"""
        with allure.step("Проверим количество девайсов в корзине"):
            self.image_column.get_element().first.wait_for(state="visible")
            devices_column = self.image_column.get_element().count()
            assert devices_column == devices

    def checkout_product(self):
        """Переходит в оплату товара"""
        self.button_checkout.click()
