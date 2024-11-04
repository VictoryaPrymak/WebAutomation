from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


class RegistrationPage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def registration_page(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[lang='en']")

    # wait until registration page has opened
    def wait_registration_page(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "roboto-regular sticky fixedImportant ng-scope")))

    def username(self):
        return self.driver.find_element(By.NAME, "usernameRegisterPage")

    def password(self):
        return self.driver.find_element(By.NAME, "passwordRegisterPage")

    def confirm_password(self):
        return self.driver.find_element(By.NAME, "confirm_passwordRegisterPage")

    def email(self):
        return self.driver.find_element(By.NAME, "emailRegisterPage")

    def agreement_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='i_agree']")

    def type_username(self, username: str):
        self.username().send_keys(username)

    def type_password(self, password: str):
        self.password().send_keys(password)

    def type_con_password(self, password: str):
        self.confirm_password().send_keys(password)

    def type_email(self, email: str):
        self.email().send_keys(email)

    def postal_code(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[name='postal_codeRegisterPage']")

    def type_postal_code(self, postal_code: int):
        self.postal_code().send_keys(postal_code)

    def registration_button(self):
        return self.driver.find_element(By.ID, "register_btnundefined")