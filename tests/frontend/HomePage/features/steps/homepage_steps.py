import time
from Common.CommonSteps import webstepscommon
from Common.CommonFuncs import webcommon
from behave import *
import config
import random


@step("I add {quantity} random item to the cart")
def i_add_random_item_to_the_cart(context, quantity):
    cart_btns_locator = config.HOMEPAGECONFIG["all_add_cart_btns"]
    cart_btns = webcommon.find_elements(context, cart_btns_locator)
    random_btns = random.sample(cart_btns, int(quantity))

    for i in random_btns:
        i.click()

    time.sleep(1)


@step("I verify cart page opens")
def i_verify_cart_page_opens(context):
    time.sleep(1)
    webcommon.assert_url_contains(context, "cart")