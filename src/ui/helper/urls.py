import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_URL")
APPLE_DEVICES_URL = "/index.php?route=product/manufacturer/info&manufacturer_id=8"
CART_URL = "/index.php?route=checkout/cart"
PAYMENT_URL = "/index.php?route=checkout/checkout"
CONFIRM_ORDER_URL = "index.php?route=extension/maza/checkout/confirm"
ORDER_SUCCESS_URL = "index.php?route=checkout/success"
COMPARISON_URL = "index.php?route=product/compare"