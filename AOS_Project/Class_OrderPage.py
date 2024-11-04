from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


class OrderPage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def register_button(self):
        return self.driver.find_element(By.ID, "registration_btnundefined")

    def login_button(self):
        return self.driver.find_element(By.ID, "login_btnundefined")

    # wait until "login" button will be clickable
    def wait_login_able(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.ID, "login_btnundefined")))

    def next_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[id='next_btn']")

    # wait until "next" button will be clickable
    def wait_next_button(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[class='a-button nextBtn marginTop75 ng-scope']")))

    # sp = safe pay

    def radio_button_safepay(self):
        return self.driver.find_element(By.NAME, "safepay")

    def sp_username(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[name='safepay_username']")

    def type_sp_username(self, username: str):
        return self.sp_username().send_keys(username)

    def sp_password(self):
        return self.driver.find_element(By.NAME, "safepay_password")

    def type_sp_password(self, password: str):
        return self.sp_password().send_keys(password)

    def paynow_button_sp(self):
        return self.driver.find_element(By.ID, "pay_now_btn_SAFEPAY")

    # mastercredit details

    def radio_button_masterCredit(self):
        return self.driver.find_element(By.NAME, "masterCredit")

    def cardnumber(self):
        return self.driver.find_element(By.ID, "creditCard")

    def cvv_number(self):
        return self.driver.find_element(By.NAME, "cvv_number")

    def card_holder(self):
        return self.driver.find_element(By.NAME, "cardholder_name")

    def card_year(self):
        return self.driver.find_elements(By.NAME, "yyyyListbox")

    def card_month(self):
        return self.driver.find_elements(By.NAME, "mmListbox")

    def paynow_button_mc(self):
        return self.driver.find_element(By.ID, "pay_now_btn_ManualPayment")

    def order_page_summary(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class='seccion']>span")

    def wait_order_page_summary(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[class='seccion']>span")))


