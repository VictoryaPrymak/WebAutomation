from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


class MainPage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    # Choose random product category from main page
    def product_category(self):
        return self.driver.find_elements(By.CLASS_NAME, "shop_now_slider")[random.randint(0, 4)]

    # choose tablet category
    def product_category_tablet(self):
        return self.driver.find_elements(By.CLASS_NAME, "shop_now_slider")[1]

    # special offer title
    def main_screen(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[id='special_offer_items']>h3")

    # wait until the main screen is loading, special offer title is appearing
    def main_page_screen(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[id='special_offer_items']>h3")))

    def logo(self):
        return self.driver.find_element(By.CLASS_NAME, "logo")

    # wait until the shopping cart screen is loading, shopping cart title is appearing
    def shopping_cart(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "[class='roboto-regular screen768 ng-binding']")))

    # shopping cart button
    def get_shopping_cart(self):
        return self.driver.find_element(By.ID, "shoppingCartLink")

    def my_profile(self):
        return self.driver.find_element(By.ID, "menuUserLink")

    # username
    def this_user(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class ='hi-user containMiniTitle ng-binding']")

    def my_account(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "[class='option roboto-medium ng-scope']")

    # wait until my account window is loading, my account window is appearing
    def wait_my_account(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "[class='option roboto-medium ng-scope']")))

    def delete_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class='deleteBtnText']")

    # wait until my account screen is loading, delete button is appearing
    def wait_delete_button(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[class='deleteBtnText']")))

    def wait_delete_window(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[class ='deleteAccountPopupContent']")))

    def yes_button_delete_account(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class='deletePopupBtn deleteRed']")

    def log_out_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[translate = 'Sign_out']"
                                                         "[class ='option roboto-medium ng-scope']")
    def wait_logout_button(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[translate = 'Sign_out']"
                                                         "[class ='option roboto-medium ng-scope']")))
