from faker import Faker


class Data:
    APPLE = "apple"
    BREADCRUMB = ["Главная страница", "Software", "Brand", "Apple", "iPod Shuffle"]
    HTC = "HTC"
    BORN_TO = "Born to be worn."
    INTEL_CORE = "Intel Core 2 Duo processor"


class InputData:

    @staticmethod
    def generator_email():
        fake = Faker()
        username = fake.user_name()
        return f"{username}@mail.com"

    EMAIL = generator_email()
    FIRST_NAME = "Agent"
    LAST_NAME = "Smith"
    TELEPHONE = "89001234567"
    PASSWORD = "12345678"
    ADDRESS_1 = "Vice"
    CITY = "London"
    POST_CODE = "123456"
