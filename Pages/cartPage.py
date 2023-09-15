# loginPage.py
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Pages.loginPage import LoginPageLocators
from Pages.productPage import ProductPageLocators


class CartPageLocators:
    ITEM_BACKPACK = (By.ID, "item_4_title_link")
    ITEM_LIGHT = (By.ID, "item_0_title_link")
    ADD_TO_CART_BUTTON_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.ID, "shopping_cart_container")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    REMOVE_ITEM_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")


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


def perform_failed_login(browser, username, password, screenshot_filename=None):
    login(browser, username, password)
    if screenshot_filename:
        capture_screenshot(browser, screenshot_filename)


def add_item_to_cart(browser, screenshot_filename=None):
    item_name = browser.find_element(*LoginPageLocators.ITEM_BACKPACK)
    item_name.click()
    time.sleep(3)
    add_to_cart_button = browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON_BACKPACK)
    add_to_cart_button.click()

    if screenshot_filename:
        capture_screenshot(browser, screenshot_filename)

    # return get_cart_item_count(browser)


def get_cart_item_count(browser):
    cart_icon = browser.find_element(*ProductPageLocators.CART_ICON)
    return cart_icon.text


def check_item_cart(browser, screenshot_filename=None):
    item_cart = browser.find_element(*ProductPageLocators.ITEM_BACKPACK)
    time.sleep(3)
