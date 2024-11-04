from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


class ProductPage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def add_quantity(self):
        return self.driver.find_element(By.CLASS_NAME, "plus")

    def quantity(self, count: int):
        for i in range(count):
            self.add_quantity().click()

    def product_quantity(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='quantity']")

    def product_quantity_value(self):
        return self.product_quantity().get_attribute("value")

    def add_to_cart(self):
        return self.driver.find_element(By.NAME, "save_to_cart")

    def product_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class='roboto-regular screen768 ng-binding']")

    def product_color(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "[id='Description']>div>div>div>span")

    def choose_color(self):
        self.colors = len(self.product_color()) - 1
        return self.product_color()[random.randint(1, self.colors)]

    def product_price(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class='roboto-thin screen768 ng-binding']")

    # sh = shopping cart

    # delete from shopping cart window
    def delete_product(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "[class='removeProduct iconCss iconX']")

    def sh_cart_window_name(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "h3[class='ng-binding']")

    def sh_cart_window_price(self):
        return self.driver.find_element(By.CSS_SELECTOR, "p[class='price roboto-regular ng-binding']")

    def sh_cart_window_quantity(self):
        return self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[2]/a/label[1]")

    def sh_cart_window_color(self):
        return self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[2]/a/label[2]")

    def sh_cart_window_total(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class='roboto-regular ng-binding']")

    def category_at_bar(self):
        return self.driver.find_element(By.CSS_SELECTOR, "nav>a[class='ng-binding']")











