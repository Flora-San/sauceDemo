import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Pages.loginPage import LoginPageLocators
from Pages.productPage import ProductPageLocators
from Pages.cartPage import CartPageLocators

from selenium.webdriver.common.by import By


class CheckoutPageLocators:
    CHECKOUT_PAGE_INFO = (By.ID, "checkout_info_container")
    NAME = (By.ID, "first-name")
    LASTNAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CANCEL_BUTTON = (By.ID, "cancel")
    CONTINUE_BUTTON = (By.ID, "continue")
    ERROR_BUTTON = (By.CLASS_NAME, "error-button")

    CHECKOUT_SUMMARY = (By.ID, "checkout_summary_container")
    FINISH_BUTTON = (By.ID, "finish")
    CHECKOUT_COMPLETED = (By.ID, "checkout_complete_container")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")


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


def remove_item_cart(browser):
    remove_item = browser.find_element(*CartPageLocators.REMOVE_ITEM_BACKPACK)
    remove_item.click()
    # return remove_item.text


def checkout_click(browser):
    checkout_button_click = browser.find_element(*CartPageLocators.CHECKOUT_BUTTON)
    checkout_button_click.click()


def checkout_customer_ok(browser, name, lastname):
    zipcode = '1234'
    add_name = browser.find_element(*CheckoutPageLocators.NAME)
    add_lastname = browser.find_element(*CheckoutPageLocators.LASTNAME)
    add_zipcode = browser.find_element(*CheckoutPageLocators.ZIP_CODE)
    continue_button = browser.find_element(*CheckoutPageLocators.CONTINUE_BUTTON)

    add_name.send_keys(name)
    add_lastname.send_keys(lastname)
    add_zipcode.send_keys(zipcode)
    continue_button.click()


def is_error_message_displayed_checkout(browser):
    checkout_empty_fields = browser.find_element(*CheckoutPageLocators.CONTINUE_BUTTON)
    checkout_empty_fields.click()
    error_message = browser.find_element(*CheckoutPageLocators.ERROR_BUTTON)
    return error_message.is_displayed()


def cancel_action(browser):
    cancel_button_click = browser.find_element(*CheckoutPageLocators.CANCEL_BUTTON)
    cancel_button_click.click()


def checkout_completed_ok(browser):
    checkout_completed_title = browser.find_element(*CheckoutPageLocators.CHECKOUT_COMPLETED)
    checkout_completed_title.is_displayed()


def click_finish_button(browser):
    finish_button = browser.find_element(*CheckoutPageLocators.FINISH_BUTTON)
    finish_button.click()


def checkout_return_home(browser):
    checkout_return = browser.find_element(*CheckoutPageLocators.BACK_HOME_BUTTON)
    checkout_return.click()
