import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from faker import Faker

from pages.base_page import BasePage


class BuyPage(BasePage):
    URL = 'http://192.168.99.100:8081/'
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#content > div.row > div:nth-child(2) > div > div.button-group > button:nth-child(1)")
    SHOPPING_CART = (By.XPATH, "//a[text()='shopping cart']")
    CHECKOUT = (By.CSS_SELECTOR, "#content > div.buttons.clearfix > div.pull-right > a")
    EMAIL_FORM = (By.NAME, "email")
    EMAIL_FORM_GUEST = (By.CSS_SELECTOR, "#input-payment-email")
    PASSWORD_FORM = (By.NAME, "password")
    FIRSTNAME_BILLING_FORM = (By.CSS_SELECTOR, "#input-payment-firstname")
    LASTNAME_BILLING_FORM = (By.CSS_SELECTOR, "#input-payment-lastname")
    ADDRESS_BILLING_FORM = (By.ID, "input-payment-address-1")
    CITY_BILLING_FORM = (By.ID, "input-payment-city")
    POSTCODE_BILLING_FORM = (By.ID, "input-payment-postcode")
    REGION_SELECT = (By.ID, "input-payment-zone")
    CONTINUE_BUTTON_PAYMENT_ADDRESS = (By.CSS_SELECTOR, 'input[value="Continue"]')
    CONTINUE_BUTTON_DELIVERY_DETAILS = (By.CSS_SELECTOR, "#button-shipping-address")
    CHECKBOX_PAYMENT = (By.CSS_SELECTOR, "input[name='agree']")
    CONTINUE_BUTTON_PAYMENT_METHOD = (By.CSS_SELECTOR, "#button-payment-method")
    CONTINUE_BUTTON_DELIVERY_METHOD = (By.CSS_SELECTOR, "#button-shipping-method")
    CONFIRM_ORDER_BUTTON = (By.ID, "button-confirm")
    LOGIN_BUTTON = (By.ID, "button-login")
    REGION = (By.CSS_SELECTOR, "[name='zone_id']")
    CONTINUECHECKOUTBTN = (By.CSS_SELECTOR, 'input[value="Continue"]')
    SELECT_GUEST_CHECKOUT = (By.CSS_SELECTOR, "#collapse-checkout-option > div > div > div:nth-child(1) > div:nth-child(4) > label > input[type=radio]")
    CONTINUE_GUEST_CUSTOMER = (By.CSS_SELECTOR, "#button-account")
    CONTINUE_BUTTON_PAYMENT_ADDRESS_GUEST = (By.CSS_SELECTOR, "#button-guest")
    TELEPHONE = (By.NAME, "telephone")

    def __init__(self, driver):
        super().__init__(driver)
        self.fake = Faker()
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

    def open(self):
        self.driver.get(self.URL)

    def add_to_cart(self):
        self.click(self.element(self.ADD_TO_CART_BUTTON))

    def go_to_shopping_cart(self):
        self.click(self.element(self.SHOPPING_CART))

    def click_checkout(self):
        self.click(self.element(self.CHECKOUT))

    def fill_login_form(self, email, password):
        self.set_field_value(self.EMAIL_FORM, email)
        self.set_field_value(self.PASSWORD_FORM, password)

    def click_login_button(self):
        self.click(self.element(self.LOGIN_BUTTON))

    def fill_billing_form(self, firstname=None, lastname=None, address=None, city=None, postcode=None):
        firstname = firstname or self.fake.first_name()
        lastname = lastname or self.fake.last_name()
        address = address or self.fake.email()
        city = city or self.fake.phone_number()
        postcode = postcode or self.fake.password()

        self.set_field_value(self.FIRSTNAME_BILLING_FORM, firstname)
        self.set_field_value(self.LASTNAME_BILLING_FORM, lastname)
        self.set_field_value(self.ADDRESS_BILLING_FORM, address)
        self.set_field_value(self.CITY_BILLING_FORM, city)
        self.set_field_value(self.POSTCODE_BILLING_FORM, postcode)

    def select_region_ddmenu(self):
        self.click(self.element(self.REGION))
        time.sleep(3)
        select = Select(self.element(self.REGION))
        select.select_by_visible_text("Aberdeen")

    def continue_checkout_click_button(self):
        self.click(self.element(self.CONTINUECHECKOUTBTN))

    def click_continue_billing_details(self):
        self.click(self.element(self.CONTINUE_BUTTON_PAYMENT_ADDRESS))

    def click_continue_delivery_details(self):
        self.click(self.element(self.CONTINUE_BUTTON_DELIVERY_DETAILS))

    def click_continue_delivery_method(self):
        self.click((self.element(self.CONTINUE_BUTTON_DELIVERY_METHOD)))

    def click_continue_payment_method(self):
        checkbox = self.driver.find_element(*self.CHECKBOX_PAYMENT)
        checkbox.click()
        self.click(self.element(self.CONTINUE_BUTTON_PAYMENT_METHOD))

    def check_success_buy_order(self):
        self.click(self.element(self.CONFIRM_ORDER_BUTTON))

    def select_guest_customer(self):
        self.click(self.element(self.SELECT_GUEST_CHECKOUT))
        self.click(self.element(self.CONTINUE_GUEST_CUSTOMER))

    def fill_billing_form_guest_customer(self, firstname=None, lastname=None, address=None, city=None, postcode=None, email=None, telephone=None):
        firstname = firstname or self.fake.first_name()
        lastname = lastname or self.fake.last_name()
        address = address or self.fake.email()
        city = city or self.fake.phone_number()
        postcode = postcode or self.fake.password()
        email = email or self.fake.email()
        telephone = telephone or self.fake.phone_number()

        self.set_field_value(self.FIRSTNAME_BILLING_FORM, firstname)
        self.set_field_value(self.LASTNAME_BILLING_FORM, lastname)
        self.set_field_value(self.ADDRESS_BILLING_FORM, address)
        self.set_field_value(self.CITY_BILLING_FORM, city)
        self.set_field_value(self.POSTCODE_BILLING_FORM, postcode)
        self.set_field_value(self.EMAIL_FORM_GUEST, email)
        self.set_field_value(self.TELEPHONE, telephone)

    def click_continue_billing_details_guest(self):
        self.click(self.element(self.CONTINUE_BUTTON_PAYMENT_ADDRESS_GUEST))