"""
Description:
    The purpose of this test is to verify the functionality of flaconi procucts, cart and  main links.

Execution Frequency:
    Daily

Executioin in OS:
    Mac
    Linux
    windows

Owner(s):
    Natesh Chetty

Author:
    Natesh Chetty

"""

import random
import pytest
import requests
import logging

from ui_tests.page_objects.fl_page_objects import FlaconiPage


def pytest_namespace1():
    return {'product_name': None}


def pytest_namespace2():
    return {'price': None}


log = logging.getLogger()
log.setLevel(logging.INFO)


@pytest.mark.ui_test
def test_select_random_product(logged_in_driver):
    """This test will verify the random selected product from the flaconi application.

    Args:
        logged_in_driver (flaconi main page): Fixture that ensures the will navigates to the flaconi application

    Steps:
        1. Navigate to the flaconi page
        2. Randomly select the product and click on the product
        3. Select the quantity of the product
        4. click on the add to cart button

    """

    driver = logged_in_driver
    flaconi_page = FlaconiPage(driver=logged_in_driver)

    # Click on the parfum link
    flaconi_page.parfum_link.click()

    # Wait until an element to visible and click on the selection
    flaconi_page.herrendufte_button.click()

    # select  and get the product details to add it to the cart
    get_list_of_products = flaconi_page.list_of_products
    log.info("Number of products are:-" + str(len(get_list_of_products)))
    random_product = random.choice(get_list_of_products)
    index_num = get_list_of_products.index(random_product)
    log.info("the index number selected randomly is:-" + str(index_num))
    search_text = "//div[contains(@class,'category-products')]//ul[contains(@class,'medium-block-" \
                  "grid-3')]//li[contains(@data-impression-counter,'catalog')]" \
                  "[" + str(1 + int(index_num)) + "]//div[2]//strong"
    product_name = driver.find_element_by_xpath(search_text).text
    pytest.product_name = product_name
    log.info("The product name is:" + product_name)
    random_product.click()

    # select a quantity of the product to add it to the cart
    get_list_of_quantities = flaconi_page.list_of_quantities
    select_random_quantity = random.choice(get_list_of_quantities)
    index_num = get_list_of_quantities.index(select_random_quantity)
    log.info("The index number selected randomly is:-" + str(index_num))
    search_text = "//div[contains(@id,'purchasepanel')]" \
                  "//ul//li[" + str(1 + int(index_num)) + "]//div[contains(@class,'price-box')]//span" \
                                                          "[contains(@class,'price')][1]"
    selected_quantity_price = driver.find_element_by_xpath(search_text).text
    pytest.price = selected_quantity_price
    log.info("The price details is:" + selected_quantity_price)
    select_random_quantity.click()
    if index_num == 0:
        flaconi_page.in_den_warenkorb_button.click()
    else:
        driver.find_element_by_xpath(
            "//div[contains(@id,'purchasepanel')]//div[contains(@id,'addToCartContainer')][" + str(
                1 + int(index_num)) + "]//form//div//button").click()
    # click on add to cart
    flaconi_page.zum_warenkorb_button.click()

    # validate the quantity in the cart
    quanity_in_cart = flaconi_page.quantity_in_warenkorb_button.text
    log.info("The quantity in the cart is: " + quanity_in_cart)
    assert quanity_in_cart == "1", f"There are more items added then expected in the cart"


@pytest.mark.ui_test
def test_verify_price_of_the_product(logged_in_driver):
    """This test will verify the price on the cart

    Args:
        logged_in_driver (flaconi main page): Fixture that ensures driver is on flaconi application

    Steps:
        1. Navigate to the flaconi page
        2. Get the price of the selected item
        3. Compare the price and product name of the randomly selected item

    """

    driver = logged_in_driver
    flaconi_page = FlaconiPage(driver=logged_in_driver)
    flaconi_page.warenkorb_button.click()

    # validate the price in the cart
    price_in_cart = driver.find_element_by_xpath("//div[contains(@class,'price-box')]//span").text
    log.info("The price in the cart is:" + price_in_cart)
    returned_price_details = pytest.price
    price = returned_price_details.replace('*', '')
    assert price in price_in_cart, f"Price:{price} is not available in the cart"

    # Validate the product name in the cart
    product_name_in_cart = flaconi_page.product_name_in_cart_text.text
    pro_name_text_cart = "".join(c for c in product_name_in_cart if c.isalnum())
    log.info("The product name in the cart item is:" + pro_name_text_cart)
    product_details = pytest.product_name
    pro_name_text_item = "".join(c for c in product_details if c.isalnum())
    assert pro_name_text_item in pro_name_text_cart, f"Product name is not available in the cart"


@pytest.mark.ui_test
def test_verify_main_navigation_menu_links(logged_in_driver):
    """This test will verify the main navigation links.

    Args:
        logged_in_driver (flaconi main page): Fixture that ensures driver is on flaconi application

    Steps:
        1. Navigate to the flaconi page
        2. Get all the links of main navigation
        3. Verify each link is working and giving us the 200 response

    """

    flaconi_page = FlaconiPage(driver=logged_in_driver)

    # get all the links of the main navigation bar
    get_list_of_main_navigation_links = flaconi_page.list_of_main_navigation_links
    log.info("The number of main links are" + str(len(get_list_of_main_navigation_links)))

    # loop each link and verify the response
    for link in get_list_of_main_navigation_links:
        log.info("The main navigation link name is:" + link.get_attribute('title'))
        r = requests.head(link.get_attribute('href'))
        assert r.status_code == 200, f"The link:{link} is broken"
