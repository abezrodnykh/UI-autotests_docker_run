import json
import os
import time

import allure
from playwright.sync_api import Page, expect

from src.ui.browser.browser import Browser
from src.ui.helper.urls import BASE_URL
from src.ui.page_elements.button import Button
from src.ui.page_elements.element import Element
from src.ui.page_elements.input import Input
from src.ui.page_elements.text import Text


class BasePage:
    """Логика для тестов на главной странице"""

    def __init__(self, page: Page, url=BASE_URL):
        self.content_text = None
        self.page = page
        self.url = url
        self.browser = Browser(page)
        self.button_all_category = Button(page, strategy="by_role", role="button", value="All Categories",
                                          allure_name="All Categories")
        self.button_desktop = Button(page, strategy="locator", selector="(//a[text()='Desktops'])[1]",
                                     allure_name="Desktop")
        self.input_search = Input(page, strategy="locator", selector="(//input[@name='search'])[1]",
                                  allure_name="Поле ввода")
        self.button_search = Button(page, strategy="by_role", role="button", value="Search",
                                    allure_name="Search")
        self.element_card = Element(page, strategy="locator", selector=".caption", allure_name="Карточки с товаром")
        self.element_breadcrumb = Element(page, strategy="locator", selector=".breadcrumb-item",
                                          allure_name="Хлебные крошки")
        self.htc_touch = Text(page, strategy="locator", selector="(//*[text()='HTC Touch HD'])[2]", allure_name="HTC")
        self.button_add_to_cart = Button(page, strategy="by_role", role="button", value="Add To Cart",
                                         allure_name="Add To Cart")
        self.button_view_cart = Button(page, strategy="by_text", value="View Cart")
        self.account_icon = Element(page, strategy="locator", selector=".fa-user", allure_name="Иконка авторизации")
        self.login_email = Input(page, strategy="locator", selector="[name='email']",
                                 allure_name="Логин")
        self.login_password = Input(page, strategy="locator", selector="[name='password']",
                                    allure_name="Пароль")
        self.btm_ok = Button(page, strategy="locator", selector="[value='Login']", allure_name="Ok")

    def open(self):
        """Открывает страницу по URL"""
        return self.browser.go_to_url(self.url)

    def user_login(self, login, password):
        """Авторизирует пользователя"""
        if not os.path.exists("state.json"):
            with allure.step("Шаг авторизации пользователя"):
                login = os.getenv(login)
                password = os.getenv(password)
                self.account_icon.click()
                self.login_email.fill(login, secure=True)
                self.login_password.fill(password, secure=True)
                self.btm_ok.click()
                time.sleep(3)
                context = self.page.context
                storage_state = context.storage_state()
                with open('state.json', "w") as f:
                    json.dump(storage_state, f)

    def check_breads_crumb(self, bread_crumb: list):
        """Проверяет формирование хлебных крошек
        :param bread_crumb: хлебные крошки, в нужном порядке(например: [Главная, Вторая, Третья]
        :type bread_crumb: list"""
        with allure.step("Проверяет формирование хлебных крошек"):
            for idx in range(1, self.element_breadcrumb.get_element().count() + 1):
                loc = self.element_breadcrumb.get_element().nth(idx)
                expect(loc).to_have_text(bread_crumb[idx])

    def check_desktop_apple(self, search_name, cards=15):
        """Проверяет переход в карточки товара"""
        with allure.step("Выберем Desktop из списка"):
            self.button_all_category.click()
            self.button_desktop.click()
            time.sleep(2)
        with allure.step("Введем название поля ввода"):
            self.input_search.fill(search_name)

        self.button_search.click()

        with allure.step("Проверим, что карточки доступны"):
            self.element_card.get_element().first.wait_for(state="visible")
            counter_card = self.element_card.get_element().count()
            assert counter_card == cards

    def checkout_htc_and_ad_to_card(self, search_name):
        with allure.step("Выбираем второй в списке элемент HTC"):
            self.input_search.fill(search_name)
            self.htc_touch.click()
        with allure.step("Добавим девайс в корзину"):
            self.button_add_to_cart.click()
            self.button_view_cart.click()
