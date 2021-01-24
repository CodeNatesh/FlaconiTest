""" The file contains all the page objects for the flaconi page """

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By


class FlaconiPage:
    """ The flaconi page that   . """

    def __init__(self, *args, driver=None, **kwargs):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @property
    def parfum_link(self):
        """ The parfum link on the flaconi main navigation bar"""
        search_text = "//nav[contains(@id,'main-navigation')]//ul[contains(@class,'nav-main')]" \
                      "//li[2]//a[@title='Parfum']"
        return self.wait.until(EC.presence_of_element_located((By.XPATH, search_text)))

    @property
    def herrendufte_button(self):
        """ The herrendufte button on the parfum page"""
        search_text = "//div[contains(@class,'billboard')]//div//div[2]//figure//a" \
                      "//figcaption[text()='Herrendüfte']"
        return self.wait.until(EC.presence_of_element_located((By.XPATH, search_text)))

    @property
    def list_of_products(self):
        """ The list of products in the parfum page"""
        search_text = "//div[contains(@class,'category-products')]//ul[contains(@class,'medium-block" \
                      "-grid-3')]//li[contains(@data-impression-counter,'catalog')]"
        return self.wait.until(EC.presence_of_all_elements_located((By.XPATH, search_text)))

    @property
    def list_of_quantities(self):
        """ The list of quantities in the parfum page"""
        search_text = "//div[contains(@id,'purchasepanel')]//ul//li"
        return self.wait.until(EC.presence_of_all_elements_located((By.XPATH, search_text)))

    @property
    def in_den_warenkorb_button(self):
        """ The In den Warenkorb button on cart selection page"""
        search_text = "//div[contains(@id,'purchasepanel')]//div[contains(@id,'addToCartContainer')]" \
                      "[1]//div//button"
        return self.wait.until(EC.presence_of_element_located((By.XPATH, search_text)))

    @property
    def zum_warenkorb_button(self):
        """ The Zum Warenkorb button on cart selection page"""
        search_text = "//div[contains(@class,'columns')]//a[contains(text(),'Zum Warenkorb')]"
        return self.wait.until(EC.presence_of_element_located((By.XPATH, search_text)))

    @property
    def quantity_in_warenkorb_button(self):
        """ The quantity in warenkorb"""
        search_text = "//div[contains(@class,'main-header')]//ul[contains(@class,'right')]//li" \
                      "[contains(@id,'mini-basket')]//a//span//span"
        return self.wait.until(EC.presence_of_element_located((By.XPATH, search_text)))

    @property
    def warenkorb_button(self):
        """ The warenkorb in the flaconi page"""
        search_text = "//div[contains(@class,'main-header')]//ul[contains(@class,'right')]" \
                      "//li[contains(@id,'mini-basket')]"
        return self.wait.until(EC.presence_of_element_located((By.XPATH, search_text)))

    @property
    def product_name_in_cart_text(self):
        """ The product name on the cart item"""
        search_text = "//div[contains(@class,'gap-margin')]//div//strong//a"
        return self.wait.until(EC.presence_of_element_located((By.XPATH, search_text)))

    @property
    def list_of_main_navigation_links(self):
        """ The list of main navigation links in the flaconi page"""
        search_text = "//nav[contains(@id,'main-navigation')]//ul[contains(@class,'nav-main')]//li//a" \
                      "[contains(@data-webtrekk-link-id,'header.nav')]"
        return self.wait.until(EC.presence_of_all_elements_located((By.XPATH, search_text)))
