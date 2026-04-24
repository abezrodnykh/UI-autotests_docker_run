import time

import allure
from playwright.sync_api import Page

from src.ui.helper.urls import BASE_URL, APPLE_DEVICES_URL
from src.ui.page_elements.button import Button
from src.ui.page_elements.text import Text
from src.ui.pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, page: Page, url=BASE_URL + APPLE_DEVICES_URL):
        super().__init__(page, url)
        self.ipod_shuffle = Text(page, strategy="locator", selector="//*[text()='iPod Shuffle']",
                                 allure_name="iPod Shuffle")
        self.ipod_shuffle_icon = Text(page, strategy="locator",
                                      selector="//*[text()='iPod Shuffle']/../../..//div[@class='product-thumb-top']",
                                      allure_name="Изображение iPod Shuffle")
        self.macbook_icon = Text(page, strategy="locator",
                                 selector="//*[text()='MacBook']/../../..//div[@class='product-thumb-top']",
                                 allure_name="Изображение MacBook")
        self.product_compare = Text(page, strategy="by_title", value="Product Compare (2)",
                                    allure_name="Product Compare (2)")
        self.btm_compare_ipod = Button(page, strategy="locator", selector=".compare-34",
                                       allure_name="Добавить к сравнению первый товар")
        self.btm_compare_macbook = Button(page, strategy="locator", selector=".compare-43",
                                          allure_name="Добавить к сравнению второй товар")

    def checkout_card_apple_shuffle(self):
        """Переходит в карточку товара"""
        self.ipod_shuffle.click()

    def mov_to_product_compare(self):
        """Добавляет товары к сравнению"""
        with allure.step("Добавляем для сравнения товары"):
            self.ipod_shuffle_icon.hover()
            self.btm_compare_ipod.click()
            self.macbook_icon.hover()
            self.btm_compare_macbook.click()
            self.product_compare.click()

    def screenshot(self):
        """Производит скриншот товара"""
        time.sleep(3)
        self.ipod_shuffle_icon.compare_screenshots(mse_threshold=500)
