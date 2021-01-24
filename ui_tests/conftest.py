""" The file contains all the fixtures used for flaconi test automation  """

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='module')
def logged_in_driver():
    """ This fixture is used to open and close the flaconi application.

    """

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.flaconi.de/")
    driver.maximize_window()

    # Wait until an cookies popup to be visible and close
    search_text = "//div//button[contains(@id,'uc-btn-accept-banner')]"
    wait = WebDriverWait(driver, 10)
    accept_cookies = wait.until(EC.visibility_of_element_located((By.XPATH, search_text)))
    accept_cookies.click()

    # Wait until an element is visible
    search_text = "//div[contains(@class,'logo')]//a[contains(@title,'flaconi')]"
    wait.until(EC.presence_of_element_located((By.XPATH, search_text)))

    assert driver.title is not None

    yield driver
    # close the browse once the execution is completed
    driver.close()
