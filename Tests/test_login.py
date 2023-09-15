# tests/test_login.py
import time

import pytest
from selenium import webdriver

from Pages.loginPage import (
    perform_successful_login,
    perform_failed_login,
    is_error_message_displayed, is_product_label_displayed
)

# Define the URL of the Sauce Demo website
SAUCE_DEMO_URL = "https://www.saucedemo.com/"


@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Adjust the path to your chromedriver.exe
    yield driver
    driver.quit()


def test_successful_login_with_screenshot(browser):
    # Open the Sauce Demo website
    browser.get(SAUCE_DEMO_URL)

    # Perform successful login with a screenshot
    perform_successful_login(browser, "standard_user", "secret_sauce")
    browser.save_screenshot("screenshoots/successful_login.png")
    time.sleep(5)

    # Verify successful login by checking the presence of the product page element
    assert is_product_label_displayed(browser)


def test_failed_login_with_screenshot(browser):
    # Open the Sauce Demo website
    browser.get(SAUCE_DEMO_URL)

    # Perform failed login with a screenshot
    perform_failed_login(browser, "locked_out_user", "wrong_password")
    browser.save_screenshot("screenshoots/failed_login.png")
    time.sleep(5)
    # Verify failed login by checking the error message
    assert is_error_message_displayed(browser)


if __name__ == "__main__":
    pytest.main()
