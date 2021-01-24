import random

import pytest
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def pytest_namespace1():
    return {'product_name': None}


def pytest_namespace2():
    return {'price': None}


@pytest.mark.ui_test
def test_select_random_product(logged_in_driver):
    """This test will verify automox supported checkbox is true if checked and false if unchecked.

    Args:
        logged_in_driver (SoftwarePage): Fixture that ensures the test is on the software page

    Steps:
        1. Navigate to the software page
        2. click on the automox supported checkbox
        3. Validate the URL has the automox supported true and false

    """

    driver = logged_in_driver
    wait = WebDriverWait(driver, 10)

    driver.find_element_by_xpath("//nav[contains(@id,'main-navigation')]//ul[contains(@class,"
                                 "'nav-main')]//li[2]//a[@title='Parfum']").click()

    # Wait until an element to visible and click on the selection
    search_text = "//div[contains(@class,'billboard')]//div//div[2]//figure//a//figcaption[text()='Herrendüfte']"
    element_1 = wait.until(EC.presence_of_element_located((By.XPATH, search_text)))
    element_1.click()

    # select a product to add it to the cart
    search_text = "//div[contains(@class,'category-products')]//ul[contains(@class,'medium-block" \
                  "-grid-3')]//li[contains(@data-impression-counter,'catalog')]"
    list_of_products = wait.until(EC.presence_of_all_elements_located((By.XPATH, search_text)))
    print(len(list_of_products))

    random_product = random.choice(list_of_products)
    index_num = list_of_products.index(random_product)
    print("index number" + str(index_num))
    search_text = "//div[contains(@class,'category-products')]//ul[contains(@class,'medium-block-" \
                  "grid-3')]//li[contains(@data-impression-counter,'catalog')]" \
                  "[" + str(1 + int(index_num)) + "]//div[2]//strong"
    product_name = driver.find_element_by_xpath(search_text).text
    pytest.product_name = product_name
    print("The product details is:" + product_name)
    random_product.click()

    # select a product to add it to the cart
    search_text = "//div[contains(@id,'purchasepanel')]//ul//li"
    list_of_quantities = wait.until(EC.presence_of_all_elements_located((By.XPATH, search_text)))
    select_random_quantity = random.choice(list_of_quantities)
    index_num = list_of_quantities.index(select_random_quantity)
    search_text = "//div[contains(@id,'purchasepanel')]" \
                  "//ul//li[" + str(1 + int(index_num)) + "]//div[contains(@class,'price-box')]//span" \
                                                          "[contains(@class,'price')][1]"
    selected_quantity_price = driver.find_element_by_xpath(search_text).text
    pytest.price = selected_quantity_price
    print("The price details is:" + selected_quantity_price)
    select_random_quantity.click()
    if index_num == 0:
        driver.find_element_by_xpath(
            "//div[contains(@id,'purchasepanel')]//div[contains(@id,'addToCartContainer')]"
            "[1]//div//button").click()
    else:
        driver.find_element_by_xpath(
            "//div[contains(@id,'purchasepanel')]//div[contains(@id,'addToCartContainer')][" + str(
                1 + int(index_num)) + "]//form//div//button").click()
    driver.find_element_by_xpath(
        "//div[contains(@class,'columns')]//a[contains(text(),'Zum Warenkorb')]").click()


@pytest.mark.ui_test
def test_verify_price_of_the_product(logged_in_driver):
    """This test will verify automox supported checkbox is true if checked and false if unchecked.

    Args:
        logged_in_driver (SoftwarePage): Fixture that ensures the test is on the software page

    Steps:
        1. Navigate to the software page
        2. click on the automox supported checkbox
        3. Validate the URL has the automox supported true and false

    """
    driver = logged_in_driver
    driver.find_element_by_xpath("//div[contains(@class,'main-header')]//ul[contains(@class,'right')]"
                                 "//li[contains(@id,'mini-basket')]").click()

    price_in_cart = driver.find_element_by_xpath("//div[contains(@class,'price-box')]//span").text
    print(price_in_cart)
    returned_price_details = pytest.price
    price = returned_price_details.replace('*', '')
    assert price in price_in_cart, f"Price is not available in the cart"

    product_name_in_cart = driver.find_element_by_xpath(
        "//div[contains(@class,'gap-margin')]//div//strong//a").text
    print(product_name_in_cart)
    product_details = pytest.product_name
    assert product_details in product_name_in_cart, f"Product name is not available in the cart"


@pytest.mark.ui_test
def test_verify_main_navigation_menu_links(logged_in_driver):
    """This test will verify automox supported checkbox is true if checked and false if unchecked.

    Args:
        logged_in_driver (SoftwarePage): Fixture that ensures the test is on the software page

    Steps:
        1. Navigate to the software page
        2. click on the automox supported checkbox
        3. Validate the URL has the automox supported true and false

    """

    driver = logged_in_driver
    wait = WebDriverWait(driver, 10)

    # select a product to add it to the cart
    search_text = "//nav[contains(@id,'main-navigation')]//ul[contains(@class,'nav-main')]//li//a" \
                  "[contains(@data-webtrekk-link-id,'header.nav')]"
    list_of_main_navigation_links = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, search_text)))
    print(len(list_of_main_navigation_links))

    for link in list_of_main_navigation_links:
        print(link.get_attribute('title'))
        r = requests.head(link.get_attribute('href'))
        assert r.status_code == 200, f"The link:{link} is broken"
