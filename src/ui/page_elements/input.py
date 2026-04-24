import allure

from src.ui.page_elements.base import Base


class Input(Base):
    """Предоставляет методы для работы с полями ввода"""

    def fill(self, text: str, delay: int | float = None, secure: bool = False):
        """Метод для ввода текста"""
        allure_title = text if secure is False else "***"
        with allure.step(f"Введем текст '{allure_title}' в поле ввода {self.allure_name}"):
            if delay:
                self._element.type(text=text, delay=delay)
            else:
                self._element.fill(value=text)

    def clear(self):
        """Очищает поле ввода"""
        with allure.step(f"Очистим поле ввода '{self.allure_name}'"):
            self._element.clear()


