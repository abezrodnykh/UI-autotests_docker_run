from http.cookiejar import Cookie

import allure
from playwright.sync_api import Page


class Browser:
    """Класс для взаимодействия с методами браузера, а так же с вкладками и фреймами"""

    def __init__(self, page: Page):
        self.page = page

    def go_to_url(self, url: str):
        """Переходит по указанному URL"""
        with allure.step(f"Переходим на URL: {url}"):
            return self.page.goto(url)

    def reload_page(self):
        """Перезагружает страницу"""
        with allure.step("Перезагрузим страницу"):
            return self.page.reload()

    def get_cookies(self):
        """Получает куки страницы"""
        with allure.step("Получим cookie страницы"):
            return self.page.context.cookies()

    def add_cookies(self, cookies: Cookie):
        """Передаем список куков в хранилище браузера"""
        with allure.step("Передадим cookie страницы"):
            return self.page.context.add_cookies(cookies)

    def close_tab(self, number: int):
        """Закрывает страницу с указанным порядковым номером"""
        with allure.step(f"Закроем страницу: {number}"):
            all_tabs = self.page.context.pages
            all_tabs[number].close()

    def switch_to_tab(self, number: int):
        """Переходит на страницу с указанным номером и закрывает предыдущие вкладки"""
        with allure.step(f"Перейдем на страницу: {number} и закроем предыдущие вкладки"):
            all_tabs = self.page.context.pages
            new_tab = all_tabs[number]
            new_tab.bring_to_front()
            new_tab.wait_for_load_state()
            return new_tab

    def switch_to_iframe_and_click(self, iframe_locator: str, locator_for_click: str):
        """Переходит на iframe и кликает по локатору в iframe"""
        with allure.step("Перейдем на iframe и кликнем"):
            frame = self.page.frame_locator(iframe_locator)
            frame.locator(locator_for_click).click()

    def alert_accept(self):
        """Принимает диалоговое окно и нажимает подтверждение"""
        with allure.step("Подтвердим диалоговое окно"):
            self.page.on("dialog", lambda dialog: dialog.accept())

    def evaluate_javascript(self, script: str):
        """Выполняет javascript на странице"""
        with allure.step("Произведем действие с помощью javascript- кода"):
            return self.page.evaluate(script)

    def check_download_file(self):
        """После действия, которое проверяет загрузку файла, проверяет что файл загрузился"""
        with self.page.expect_download() as download_info:
            download = download_info.value
            with allure.step("Проверим, что файл загрузился"):
                assert download.path() != " "

    def press_keys(self, keys: str):
        """Выполняет нажатие клавиш/сочетания клавиш на клавиатуре"""
        with allure.step(f"Зажмем клавишу/ сочетание клавиш '{keys}'"):
            self.page.keyboard.press(keys)
