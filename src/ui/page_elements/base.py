import os
from abc import ABC
from io import BytesIO

import allure
import numpy as np
from PIL import Image
from playwright.sync_api import Page, expect


class Base(ABC):
    """Базовый класс для взаимодействия с элементами"""

    def __init__(self, page: Page, strategy: str = None, selector: str = None, role=None, value: str = None,
                 allure_name: str = None):
        self.page = page
        self.strategy = strategy
        self.selector = selector
        self.role = role
        self.value = value
        self.allure_name = allure_name

        if strategy == "locator":
            self._element = self.page.locator(self.selector)
        elif strategy == "by_role":
            self._element = self.page.get_by_role(role=self.role, name=self.value)
        elif strategy == "by_text":
            self._element = self.page.get_by_text(text=self.value)
        elif strategy == "by_placeholder":
            self._element = self.page.get_by_placeholder(text=self.value)
        elif strategy == "by_title":
            self._element = self.page.get_by_title(text=self.value)
        else:
            raise ValueError("Указана неверная стратегия")

    def get_element(self):
        """Возвращает локатор элемента"""
        return self._element

    def click(self):
        """Кликает по элементу"""
        with allure.step(f"Кликнем по элементу {self.allure_name}"):
            #self._element.click(force=True)
            self._element.dispatch_event("click")

    def check_visible(self, visible=True):
        """Проверяет видимость элемента
        Передает аргумент visible"""
        if visible:
            status_element = "видимый"
        else:
            status_element = "невидимый"
        with allure.step(f"Проверим, что элемент '{self.allure_name}' {status_element}"):
            expect(self._element).to_be_visible(visible=visible)

    def wait_for(self, state, timeout_msec: int = None):
        """Ожидает, когда _element удовлетворяет условию stete"""
        if (state == "attached") and (state == "visible"):
            status_element = "видимый"
        else:
            status_element = "невидимый"
        with allure.step(f"Ждем, когда элемент '{self.allure_name}' станет {status_element}"):
            self._element.wait_for(state=state, timeout=timeout_msec)

    def get_text(self):
        """Получает текст по элементу"""
        with allure.step("Получим текст элемента"):
            return self._element.text_content()

    def is_enebled(self):
        """Проверяет, что элемент включен"""
        with allure.step(f"Проверим, что элемент '{self.allure_name}' включен"):
            self._element.is_enebled()

    def hover(self):
        """Уставливает ховер на элементе"""
        with allure.step(f"Поставим hover на '{self.allure_name}'"):
            self._element.hover()

    def compare_screenshots(self, mse_threshold: int = 0, screenshot_dir: str = "screenshots"):
        with allure.step(
                f"Сделаем скриншот элемента {self.allure_name} и сравним его с эталонным скриншотом"
        ):
            screenshot = self._element.screenshot()
            screenshot_path = os.path.join(screenshot_dir, f"{self.allure_name}.png")
            os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)

            if not os.path.exists(screenshot_path):
                with open(screenshot_path, "wb") as f:
                    f.write(screenshot)
                assert False, (
                    f"Эталонный скриншот {screenshot_path} не найден. Создан новый. "
                    f"Проверьте его и запустите тест еще раз."
                )

            current_image_io = BytesIO(screenshot)
            reference = Image.open(current_image_io)

            image = Image.open(screenshot_path)
            image_array = np.array(image)
            reference_array = np.array(reference)

            if image.size != reference.size:
                raise ValueError("Изображения должны быть одного размера")
            mse_err = np.sum(
                (image_array.astype("float") - reference_array.astype("float"))
                ** 2
            )
            mse_err /= float(image_array.shape[0] * image_array.shape[1])

            if mse_err > mse_threshold:
                with open(screenshot_path, "rb") as image_file:
                    allure.attach(
                        image_file.read(),
                        name="Эталонный скриншот",
                        attachment_type=allure.attachment_type.PNG,
                    )
                allure.attach(
                    screenshot,
                    name="Фактический скриншот",
                    attachment_type=allure.attachment_type.PNG,
                )
                raise AssertionError(f"Скриншоты отличаются (MSE: {mse_err:.2f} > {mse_threshold}).")
