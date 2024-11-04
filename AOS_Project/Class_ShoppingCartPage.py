from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


class ShoppingCartPage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def shopping_cart_page_screen(self):
        # shopping cart page has opened
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "nav>a[class= 'select  ng-binding']")))

    # sh = shopping cart
    def sh_page_bar(self):
        return self.driver.find_element(By.CSS_SELECTOR, "nav>a[class= 'select  ng-binding']")

    def get_sh_value(self):
        return self.sh_page_bar().text

    def get_edit_button(self, num: int):
        # get a line number from the and returns the edit button at the exact line
        cart_table = self.driver.find_element(By.CLASS_NAME, "fixedTableEdgeCompatibility")
        products_rows = cart_table.find_elements(By.TAG_NAME, "tr")
        line_details = products_rows[num].find_elements(By.TAG_NAME, "td")
        edit_button = line_details[5].find_element(By.CSS_SELECTOR, "[translate='EDIT']")
        return edit_button

    def get_prod_quan(self, num: int):
        # get a line number from the and returns the edit button at the exact line
        cart_table = self.driver.find_element(By.CLASS_NAME, "fixedTableEdgeCompatibility")
        products_rows = cart_table.find_elements(By.TAG_NAME, "tr")
        line_details = products_rows[num].find_elements(By.TAG_NAME, "td")
        prod_quan = line_details[4].find_element(By.CLASS_NAME, "ng-binding")
        return prod_quan

    def checkout_button(self):
        return self.driver.find_element(By.ID, "checkOutButton")

    def total_price(self):
        return self.driver.find_element(By.CSS_SELECTOR, "article>div>table>tfoot>tr>td[colspan='2']>span.roboto-medium")

    def continue_shopping(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class='a-button ng-scope']")