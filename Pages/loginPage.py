# loginPage.py
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


# locators
class LoginPageLocators:
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    MENU_ICON = (By.ID, "react-burger-menu-btn")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-button")
    ITEM_BACKPACK = (By.ID, "item_4_title_link")


def capture_screenshot(browser, filename):
    try:
        browser.save_screenshot(filename)
        return True
    except Exception as e:
        print(f"Failed to capture screenshot: {str(e)}")
        return False


def login(browser, username, password):
    username_input = browser.find_element(*LoginPageLocators.USERNAME_INPUT)
    password_input = browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
    login_button = browser.find_element(*LoginPageLocators.LOGIN_BUTTON)

    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()


def is_error_message_displayed(browser):
    error_message = browser.find_element(*LoginPageLocators.ERROR_MESSAGE)
    return error_message.is_displayed()


def is_product_label_displayed(browser):
    product_label = browser.find_element(*LoginPageLocators.ITEM_BACKPACK)
    return product_label.is_displayed()


# error method
def perform_successful_login(browser, username, password, screenshot_filename=None):
    login(browser, username, password)
    if screenshot_filename:
        capture_screenshot(browser, screenshot_filename)


def perform_failed_login(browser, username, password, screenshot_filename=None):
    login(browser, username, password)
    if screenshot_filename:
        capture_screenshot(browser, screenshot_filename)
