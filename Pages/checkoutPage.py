import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Pages.loginPage import LoginPageLocators
from Pages.productPage import ProductPageLocators

from selenium.webdriver.common.by import By


class CheckoutPageLocators:
    CHECKOUT_PAGE_INFO = (By.ID, "checkout_info_container")
    NAME = (By.ID, "first-name")
    LASTNAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CANCEL_BUTTON = (By.ID, "cancel")
    CONTINUE_BUTTON = (By.ID, "continue")


def login(browser, username, password):
    username_input = browser.find_element(*LoginPageLocators.USERNAME_INPUT)
    password_input = browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
    login_button = browser.find_element(*LoginPageLocators.LOGIN_BUTTON)

    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()


# def products(browser, item_name):


def is_error_message_displayed(browser):
    error_message = browser.find_element(*LoginPageLocators.ERROR_MESSAGE)
    return error_message.is_displayed()


def is_product_label_displayed(browser):
    product_label = browser.find_element(*LoginPageLocators.MENU_ICON)
    return product_label.is_displayed()


def capture_screenshot(browser, filename):
    try:
        browser.save_screenshot(filename)
        return True
    except Exception as e:
        print(f"Failed to capture screenshot: {str(e)}")
        return False


def perform_successful_login(browser, username, password, screenshot_filename=None):
    login(browser, username, password)
    if screenshot_filename:
        capture_screenshot(browser, screenshot_filename)
