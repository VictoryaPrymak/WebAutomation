from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


class CategoryPage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def existing_products(self):
        return self.driver.find_elements(By.CLASS_NAME, "imgProduct")

    def choose_product(self):
        last_product = len(self.existing_products())-1
        return self.existing_products()[random.randint(0, last_product)]

    def category_page_tablets(self):
        return self.driver.find_element(By.CLASS_NAME, "categoryTitle")

    def category_page_screen(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "categoryTitle")))

    def main_at_bar(self):
        return self.driver.find_element(By.CSS_SELECTOR, "nav > a[class ='ng-scope']")

