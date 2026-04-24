import allure
import pytest

from src.ui.const import Data


# @allure.story("Главная страница")
# class TestBasePage:
#     @pytest.mark.regress
#     @pytest.mark.parametrize("user_page", [("USER_LOGIN", "USER_PASSWORD")], indirect=True)
#     @allure.title("Проверка перехода в карточку товара")
#     def test_check_card(self, base_page, user_page):
#         base_page.open()
#         base_page.user_login(user_page.login, user_page.password)
#         base_page.check_desktop_apple(Data.APPLE)

    # @pytest.mark.parametrize("user_page", [("USER_LOGIN", "USER_PASSWORD")], indirect=True)
    # @allure.title("Проверка оплаты товара")
    # def test_by_devices(self, base_page, cart_page, payment_page, user_page):
    #     base_page.open()
    #     base_page.user_login(user_page.login, user_page.password)
    #     base_page.checkout_htc_and_ad_to_card(Data.HTC)
    #     cart_page.check_number_devices()
    #     cart_page.checkout_product()
    #     payment_page.input_field_and_continue()
