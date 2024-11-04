import random
from unittest import TestCase
from selenium import webdriver
from time import sleep
from re import sub
from decimal import Decimal
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

from Class_MainPage import MainPage
from Class_CategoryPage import CategoryPage
from Class_ProductPage import ProductPage
from Class_ShoppingCartPage import ShoppingCartPage
from Class_OrderPage import OrderPage
from Class_RegistrationPage import RegistrationPage
from Class_LoginPage import LoginPage


class TestCalcPage(TestCase):
    def setUp(self):
        service_chrome = Service(r"C:\Users\User\OneDrive\chromedriver.exe")

        # Open browser (create a driver object)
        self.driver = webdriver.Chrome(service=service_chrome)

        # Go to the required URL
        self.driver.get("http://www.advantageonlineshopping.com/#/")

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        # Create an object for the Calc page

        self.Main_page = MainPage(self.driver)
        self.Category_page = CategoryPage(self.driver)
        self.Product_page = ProductPage(self.driver)
        self.sh_page = ShoppingCartPage(self.driver)
        self.order_page = OrderPage(self.driver)
        self.registration_page = RegistrationPage(self.driver)
        self.login_page = LoginPage(self.driver)

    def test_targil1(self):
        self.Main_page.main_page_screen()
        self.sum_total = 0
        # add 2 products
        for i in range(2):
            count = 0
            self.Main_page.main_page_screen()
            self.Main_page.product_category().click()
            self.Category_page.choose_product().click()
            # sold out item
            if self.Product_page.product_name().text == "BOSE SOUNDLINK AROUND-EAR WIRELESS HEADPHONES II":
                self.driver.back()
                self.Category_page.choose_product().click()
                self.Product_page.quantity(random.randint(1, 9))
                self.Product_page.add_to_cart().click()
            else:
                self.Product_page.quantity(random.randint(1, 9))
                self.Product_page.add_to_cart().click()

            # shopping cart window quantity
            self.total_1 = self.Product_page.sh_cart_window_quantity()[count].text
            self.product_quan = float(sub(r'[^\d.]', '', self.total_1))
            print(f" Product Quantity : {self.product_quan}")

            self.num = print(int(self.product_quan))
            self.sum_total = self.sum_total + int(self.product_quan)

            self.Main_page.logo().click()

        self.total = self.Product_page.sh_cart_window_total().text
        self.total_items = float(sub(r'[^\d.]', '', self.total))
        print(f" Product total Quantity  : {self.total_items}")
        # check if product quantity in shopping cart window same as total shopping cart window
        self.assertEqual(self.sum_total, self.total_items)
        print(self.sum_total)
        print(self.total_items)

    def test_targil_2(self):
        self.Main_page.main_page_screen()
        self.sum_total = 0
        # add 3 products
        for i in range(3):
            count = 0
            self.sum_list = []
            self.Main_page.main_page_screen()
            self.Main_page.product_category().click()
            self.Category_page.choose_product().click()
            if self.Product_page.product_name().text == "BOSE SOUNDLINK AROUND-EAR WIRELESS HEADPHONES II":
                self.driver.back()
                self.Category_page.choose_product().click()
                self.Product_page.quantity(random.randint(1, 9))
                self.Product_page.add_to_cart().click()
            else:
                self.Product_page.quantity(random.randint(1, 9))
                self.Product_page.add_to_cart().click()
            sleep(1)

            # text test
            self.product_name = self.Product_page.product_name().text
            self.len_name = len(self.product_name)
            if self.len_name > 27:
                self.len_name = 27

            # name test
            self.sh_product_name = self.Product_page.sh_cart_window_name()[count].text
            print(f"Product name from product page : {self.product_name}")
            print(f"Product name from shopping cart : {self.sh_product_name}")

            self.assertEqual(self.product_name[0:self.len_name], self.sh_product_name[0:self.len_name])

            # quantity test
            self.product_quantity = self.Product_page.product_quantity_value()
            self.product_quantity = int(self.product_quantity)
            print(f"Product Quantity from product page : {self.product_quantity}")

            self.sh_product_quantity = self.Product_page.sh_cart_window_quantity()[count].text
            self.sh_product_quantity = int(self.sh_product_quantity[5:])
            print(f"Product Quantity from shopping cart : {self.sh_product_quantity}")

            self.assertEqual(self.sh_product_quantity, self.product_quantity)

            # price test
            self.product_price = self.Product_page.product_price().text
            self.value = float(sub(r'[^\d.]', '', self.product_price))
            self.value = round(self.value)
            self.sum_list.append(self.value * self.product_quantity)
            print(self.sum_list)
            print(f"Product Price from product page : {round(self.value)}")

            self.sh_product_price = self.Product_page.sh_cart_window_price().text
            self.value_1 = float(sub(r'[^\d.]', '', self.sh_product_price))
            self.value_1 = round(self.value_1)
            print(f"Product Price from shopping cart : {round(self.value_1)}")

            self.assertEqual(self.value_1, self.sum_list[count])

            # color test
            self.product_color = self.Product_page.product_color()[0].get_attribute("title")
            print(f"Product color from product page : {self.product_color}")

            self.sh_product_color = self.Product_page.sh_cart_window_color()[count].text
            self.sh_product = self.sh_product_color.split(" ")
            print(f"Product color from shopping cart : {self.sh_product[1]}")

            self.assertEqual(self.sh_product[1], self.product_color)

            self.Main_page.logo().click()

    def test_targil_3(self):
        self.Main_page.main_page_screen()
        self.list_sh_products = []
        # add 2 products
        for i in range(2):
            count = 0
            self.Main_page.main_page_screen()
            self.Main_page.product_category().click()
            self.Category_page.choose_product().click()
            if self.Product_page.product_name().text == "BOSE SOUNDLINK AROUND-EAR WIRELESS HEADPHONES II":
                self.driver.back()
                self.Category_page.choose_product().click()
                self.Product_page.quantity(random.randint(1, 9))
                self.Product_page.add_to_cart().click()
            else:
                self.Product_page.quantity(random.randint(1, 9))
                self.Product_page.add_to_cart().click()


            # if product name length more than 27 check first 27 chars

            self.product_name = self.Product_page.product_name().text
            self.len_name = len(self.product_name)
            if self.len_name > 27:
                self.len_name = 27

            print(self.product_name)
            self.list_sh_products.append(self.product_name)

            self.sh_product_name = self.Product_page.sh_cart_window_name()[count].text
            # check if product name same as product name in the shopping cart
            self.assertEqual(self.product_name[0:self.len_name], self.sh_product_name[0:self.len_name])

            self.Main_page.logo().click()

        self.deleted_product = self.Product_page.delete_product()[1].click()
        # delete first chosen product
        self.list_sh_products.pop(1)
        # check if deleted product not in the product list
        self.assertNotIn(self.product_name, self.list_sh_products)

        self.Main_page.shopping_cart()

    def test_targil_4(self):

        self.Main_page.main_page_screen()
        # adding one product to the cart
        self.Main_page.main_page_screen()
        self.Main_page.product_category().click()
        self.Category_page.choose_product().click()
        if self.Product_page.product_name().text == "BOSE SOUNDLINK AROUND-EAR WIRELESS HEADPHONES II":
            self.driver.back()
            self.Category_page.choose_product().click()
            self.Product_page.quantity(random.randint(1, 9))
            self.Product_page.add_to_cart().click()
        else:
            self.Product_page.quantity(random.randint(1, 9))
            self.Product_page.add_to_cart().click()
        # shopping cart page
        self.Main_page.get_shopping_cart().click()
        self.sh_page.shopping_cart_page_screen()
        self.sh_page.get_sh_value()
        print(self.sh_page.get_sh_value())
        # check if shopping cars page is opening
        self.assertEqual("SHOPPING CART", self.sh_page.get_sh_value())

    def test_targil5(self):
        self.sum_list = []
        for i in range(3):
            count = 0
            self.Main_page.main_page_screen()
            self.Main_page.product_category().click()
            self.Category_page.choose_product().click()
            if self.Product_page.product_name().text == "BOSE SOUNDLINK AROUND-EAR WIRELESS HEADPHONES II":
                self.driver.back()
                self.Category_page.choose_product().click()
                self.Product_page.quantity(random.randint(1, 9))
                self.Product_page.add_to_cart().click()
            else:
                self.Product_page.quantity(random.randint(1, 9))
                self.Product_page.add_to_cart().click()

            # products details
            self.product_name = self.Product_page.product_name().text
            print(f" Product Name : {self.product_name}")

            self.product_quantity = self.Product_page.product_quantity_value()
            self.product_quantity = int(self.product_quantity)
            print(f" Product Quantity : {self.product_quantity}")

            self.product_price = self.Product_page.product_price().text
            self.value = float(sub(r'[^\d.]', '', self.product_price))
            print(f" Product Price : {self.value}")

            # list of sum product price
            self.sum_list.append(self.value * self.product_quantity)
            print(self.sum_list)
            self.Main_page.logo().click()

        # got a total price from the product price list
        self.sum = sum(self.sum_list, 0)
        self.Main_page.get_shopping_cart().click()
        self.sh_page.shopping_cart_page_screen()
        print(f"Sum price Product page : {self.sum}")

        # total price from shopping cart page
        self.total_sh = self.sh_page.total_price().text
        self.value_sh = float(sub(r'[^\d.]', '', self.total_sh))
        print(f"Sum price Shopping cart page : {self.value_sh}")
        # check if products total price is the same as the total products price in the shopping cart
        self.assertEqual(round(self.sum), round(self.value_sh))

    def test_targil6(self):
        #                                      !!!!!!!!BUG!!!!!!!!
        self.Main_page.main_page_screen()
        for i in range(2):
            self.Main_page.main_page_screen()
            self.Main_page.product_category().click()
            self.Category_page.choose_product().click()
            if self.Product_page.product_name().text == "BOSE SOUNDLINK AROUND-EAR WIRELESS HEADPHONES II":
                self.driver.back()
                self.Category_page.choose_product().click()
                self.Product_page.quantity(random.randint(1, 9))
                self.Product_page.add_to_cart().click()
            else:
                self.Product_page.quantity(random.randint(1, 9))
                self.Product_page.add_to_cart().click()
            self.Main_page.logo().click()

        # open shopping cart screen
        self.Main_page.get_shopping_cart().click()
        self.sh_page.shopping_cart_page_screen()
        quant_add = 3 # add 3 units to the product
        for i in range(2):
            i += 1
            # before changes product quantity
            start_quan = int(self.sh_page.get_prod_quan(i).text)
            self.sh_page.get_edit_button(i).click()
            # add 3 units
            self.Product_page.quantity(quant_add)
            self.Product_page.add_to_cart().click()
            end_quan = int(self.sh_page.get_prod_quan(i).text)
            # check if the quantity before adding and after is the same
            self.assertEqual(start_quan + quant_add, end_quan)

    def test_targil7(self):
        self.Main_page.main_page_screen()
        self.Main_page.product_category_tablet().click()
        self.Category_page.choose_product().click()
        # returns to category page
        self.Product_page.category_at_bar().click()
        self.Category_page.category_page_screen()
        # check if it is the tablets category screen
        self.assertEqual(self.Category_page.category_page_tablets().text, "TABLETS")
        # returns to main page
        self.Category_page.main_at_bar().click()
        self.Main_page.main_page_screen()
        # check if it is the main screen page
        self.assertEqual(self.Main_page.main_screen().text, "SPECIAL OFFER")

    def test_targil8(self):
        self.Main_page.main_page_screen()
        # add 2 products
        for i in range(2):
            count = 0
            self.Main_page.main_page_screen()
            self.Main_page.product_category().click()
            self.Category_page.choose_product().click()
            if self.Product_page.product_name().text == "BOSE SOUNDLINK AROUND-EAR WIRELESS HEADPHONES II":
                self.driver.back()
                self.Category_page.choose_product().click()
                self.Product_page.quantity(random.randint(1, 9))
                self.Product_page.add_to_cart().click()
                self.Main_page.logo().click()
            else:
                self.Product_page.quantity(random.randint(1, 9))
                self.Product_page.add_to_cart().click()
                self.Main_page.logo().click()

        self.Main_page.get_shopping_cart().click()

        self.sh_page.checkout_button().click()

        self.order_page.register_button().click()

        # registration of new user at the registration page
        username = "Targil11"
        password = "Targil11"
        postalcode = 123456789
        self.registration_page.type_username(username)
        self.registration_page.type_password(password)
        self.registration_page.type_con_password(password)
        self.registration_page.type_postal_code(postalcode)
        self.registration_page.type_email("Targil10@mail.com")

        # scrolling down
        self.registration_page.registration_page().send_keys(Keys.PAGE_DOWN)

        self.registration_page.agreement_button().click()

        self.registration_page.registration_button().click()

        # shipping details in the order payment page safe pay
        self.order_page.wait_next_button()
        self.order_page.next_button().click()

        if not self.order_page.radio_button_safepay().is_selected():
            self.order_page.radio_button_safepay().click()

        self.order_page.type_sp_username("Targil8")
        self.order_page.type_sp_password("Targil8A")

        self.order_page.paynow_button_sp().click()

        self.order_page.wait_order_page_summary()
        # check if the order is appeared to the order page
        self.assertEqual(self.order_page.order_page_summary().text, "Order Summary")

        self.Main_page.get_shopping_cart().click()
        self.sh_page.shopping_cart_page_screen()
        # check if the shopping cart page is empty
        self.assertEqual(self.sh_page.continue_shopping().text, "CONTINUE SHOPPING")

        # DELETE ACCOUNT
        self.sh_page.continue_shopping().click()
        self.Main_page.my_profile().click()
        self.Main_page.my_account()[1].click()

        self.Main_page.wait_delete_button()
        self.Main_page.delete_button().click()

        self.Main_page.wait_delete_window()
        self.Main_page.yes_button_delete_account().click()

        self.Main_page.main_page_screen()

    def test_targil9(self):
        self.Main_page.main_page_screen()
        # add 2 products
        for i in range(2):
            count = 0
            self.Main_page.main_page_screen()
            self.Main_page.product_category().click()
            self.Category_page.choose_product().click()
            if self.Product_page.product_name().text == "BOSE SOUNDLINK AROUND-EAR WIRELESS HEADPHONES II":
                self.driver.back()
                self.Category_page.choose_product().click()
                self.Product_page.quantity(random.randint(1, 9))
                self.Product_page.add_to_cart().click()
                self.Main_page.logo().click()
            else:
                self.Product_page.quantity(random.randint(1, 9))
                self.Product_page.add_to_cart().click()
                self.Main_page.logo().click()

        self.Main_page.get_shopping_cart().click()

        self.sh_page.checkout_button().click()

        self.order_page.register_button().click()

        # registration of new user at the registration page
        username = "Targil9"
        password = "Targil9"
        postalcode = 123456789
        self.registration_page.type_username(username)
        self.registration_page.type_password(password)
        self.registration_page.type_con_password(password)
        self.registration_page.type_postal_code(postalcode)
        self.registration_page.type_email("Targil9@mail.com")

        # scrolling down
        self.registration_page.registration_page().send_keys(Keys.PAGE_DOWN)

        self.registration_page.agreement_button().click()

        self.registration_page.registration_button().click()

        # shipping details in the order payment page master credit
        self.order_page.wait_next_button()
        self.order_page.next_button().click()

        self.order_page.radio_button_masterCredit().click()
        self.order_page.cardnumber().send_keys("6464 5656 5657")
        self.order_page.cvv_number().send_keys("883")
        self.order_page.card_holder().send_keys("Targil Nine")
        self.order_page.paynow_button_mc().is_displayed()
        self.order_page.paynow_button_mc().click()

        self.order_page.wait_order_page_summary()
        # check if the order is appeared to the order page
        self.assertEqual(self.order_page.order_page_summary().text, "Order Summary")

        self.Main_page.get_shopping_cart().click()
        self.sh_page.shopping_cart_page_screen()
        # check if the shopping cart page is empty
        self.assertEqual(self.sh_page.continue_shopping().text, "CONTINUE SHOPPING")

        # DELETE ACCOUNT
        self.sh_page.continue_shopping().click()
        self.Main_page.my_profile().click()
        self.Main_page.wait_my_account()
        self.Main_page.my_account()[1].click()

        self.Main_page.wait_delete_button()
        self.Main_page.delete_button().click()

        self.Main_page.wait_delete_window()
        self.Main_page.yes_button_delete_account().click()

        self.Main_page.main_page_screen()

    def test_targil10(self):
        self.Main_page.main_page_screen()
        # opening the login window and enter the user details

        self.Main_page.my_profile().click()
        self.login_page.type_username("unemi")
        self.login_page.type_password("vkp1609A")
        self.login_page.sign_in_button().click()
        # open the connected user homepage
        self.Main_page.main_page_screen()
        # check user's homepage is connected
        self.assertEqual("unemi", self.Main_page.this_user().text)
        # disconnecting from the user's account
        self.Main_page.my_profile().click()
        self.Main_page.wait_logout_button()
        self.Main_page.log_out_button().click()
        self.Main_page.main_page_screen()
        # open my profile login window
        self.Main_page.my_profile().click()
        self.assertEqual(self.login_page.create_new_account().text, "CREATE NEW ACCOUNT")



























