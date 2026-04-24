import allure

@allure.story("Скриншот-тестирование")
class TestScreenShot:
    @allure.title("Проверка скриншота товара")
    def test_screenshot(self, product_page):
        product_page.open()
        product_page.screenshot()
