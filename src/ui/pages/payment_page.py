import allure
from playwright.sync_api import Page, expect

from src.ui.const import InputData
from src.ui.helper.urls import BASE_URL, PAYMENT_URL, CONFIRM_ORDER_URL, ORDER_SUCCESS_URL
from src.ui.page_elements.button import Button
from src.ui.page_elements.input import Input
from src.ui.page_elements.text import Text
from src.ui.pages.base_page import BasePage


class PaymentPage(BasePage):
    def __init__(self, page: Page, url=BASE_URL + PAYMENT_URL):
        super().__init__(page, url)
        self.field_first_name = Input(page, strategy="locator", selector="#input-payment-firstname",
                                      allure_name="First Name")
        self.field_last_name = Input(page, strategy="locator", selector="#input-payment-lastname",
                                     allure_name="Last Name")
        self.field_email = Input(page, strategy="locator", selector="#input-payment-email", allure_name="Email")
        self.field_telephone = Input(page, strategy="locator", selector="#input-payment-telephone",
                                     allure_name="Telephone")
        self.field_password = Input(page, strategy="locator", selector="#input-payment-password",
                                    allure_name="Password")
        self.field_password_confirm = Input(page, strategy="locator", selector="#input-payment-confirm",
                                            allure_name="Password")
        self.field_address_1 = Input(page, strategy="locator", selector="#input-payment-address-1",
                                     allure_name="Address 1")
        self.field_city = Input(page, strategy="locator", selector="#input-payment-city", allure_name="City")
        self.field_post_code = Input(page, strategy="locator", selector="#input-payment-postcode",
                                     allure_name="Post code")
        self.checkbox_privacy_policy = Text(page, strategy="locator",
                                            selector="(//*[text()='I have read and agree to the '])[1]",
                                            allure_name="Чекбокс 1")
        self.checkbox_terms_and_condition = Text(page, strategy="locator",
                                                 selector="(//*[text()='I have read and agree to the '])[2]",
                                                 allure_name="Чекбокс 2")
        self.button_continue = Button(page, strategy="by_role", role="button", value="Continue ",
                                      allure_name="Continue")
        self.button_confirm_order = Button(page, strategy="by_role", role="button", value="Confirm Order ",
                                           allure_name="Confirm Order")
        self.text_order_place = Text(page, strategy="by_text", value="Your order has been successfully processed!",
                                     allure_name="Your order has been successfully processed")
        self.button_continue_text = Button(page, strategy="locator", selector="//*[text()='Continue']",
                                           allure_name="Continue")


    def input_field_and_continue(self):
        """Заполняет формы и оплачивает товар"""
        with allure.step("Заполним формы"):
            self.field_first_name.fill(InputData.FIRST_NAME, delay=50)
            self.field_last_name.fill(InputData.LAST_NAME, delay=50)
            self.field_email.fill(InputData.EMAIL, delay=50)
            self.field_telephone.fill(InputData.TELEPHONE, delay=50)
            self.field_password.fill(InputData.PASSWORD, delay=50)
            self.field_password_confirm.fill(InputData.PASSWORD, delay=50)
            self.field_address_1.fill(InputData.ADDRESS_1, delay=50)
            self.field_city.fill(InputData.CITY, delay=50)
            self.field_post_code.fill(InputData.POST_CODE, delay=50)

        with allure.step("Проставим чек-боксы"):
            self.checkbox_privacy_policy.click()
            self.checkbox_terms_and_condition.click()
        self.button_continue.click()

        with allure.step("Проверим, что выполнен вход в информацию о платеже"):
            expect(self.page).to_have_url(BASE_URL + CONFIRM_ORDER_URL)
        self.button_confirm_order.click()

        with allure.step("Проверим, что выполнен вход в информацию о платеже"):
            expect(self.page).to_have_url(BASE_URL + ORDER_SUCCESS_URL)
        self.text_order_place.check_visible()
        self.button_continue_text.is_enebled()
