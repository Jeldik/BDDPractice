from Common.CommonSteps import webstepscommon
from Common.CommonFuncs import webcommon
from behave import *
import config
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@step("User should be logged in")
def user_should_be_logged_in(context):
    left_nav_present = WebDriverWait(context.driver, 5).until(expected_conditions.presence_of_element_located(config.ELEMENTCONFIG['left_nav']))
    log_out_btn_present = WebDriverWait(context.driver, 5).until(expected_conditions.presence_of_element_located(config.ELEMENTCONFIG['log_out_btn']))

    assert (left_nav_present and log_out_btn_present) is not None


@then("User should get {message}")
def user_should_get_error_message(context, message):
    expected_message = config.DATACONFIG[message]
    element = config.ELEMENTCONFIG['error message']
    assert webcommon.assert_text_visible(context, expected_message, element)
