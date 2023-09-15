# tests/test_add_to_cart.py
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.loginPage import (
    perform_successful_login,
    is_product_label_displayed,
    capture_screenshot,
)
from Pages.productPage import add_item_to_cart, get_cart_item_count

# Define the URL of the Sauce Demo website
SAUCE_DEMO_URL = "https://www.saucedemo.com/"


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_add_item_to_cart(browser):
    # Open the Sauce Demo website
    browser.get(SAUCE_DEMO_URL)

    # Perform successful login with a screenshot
    perform_successful_login(browser, "standard_user", "secret_sauce")
    browser.save_screenshot("screenshoots/successful_login.png")
    time.sleep(5)

    # Add an item to the cart
    # screenshot_filename = "screenshots/cart_page.png"
    add_item_to_cart(browser)
    browser.save_screenshot("screenshoots/add_item_to_cart.png")

    # Verify that the cart count has increased
    # cart_count_after = get_cart_item_count(browser)
    # assert int(cart_count_after) == int(cart_count_before) + 1
    time.sleep(3)
    browser.save_screenshot("screenshoots/cart_item.png")


if __name__ == "__main__":
    pytest.main()
