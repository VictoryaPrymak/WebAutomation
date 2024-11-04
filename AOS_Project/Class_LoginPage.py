from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


class LoginPage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def login_page_screen(self):
        # login page has opened
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "facebook ng-scope")))

    def username(self):
        return self.driver.find_element(By.NAME, "username")

    def password(self):
        return self.driver.find_element(By.NAME, "password")

    def username_value(self):
        # למקרה שנצטרך
        return self.username().get_attribute("value")

    def password_value(self):
        # למקרה שנצטרך
        return self.password().get_attribute("value")

    def type_username(self,str1: str):
        self.username().send_keys(str1)

    def type_password(self,str2: str):
        self.password().send_keys(str2)

    def sign_in_button(self):
        return self.driver.find_element(By.ID, "sign_in_btnundefined")

    def create_new_account(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class='create-new-account ng-scope']")