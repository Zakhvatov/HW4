from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class RegistrationPage(BasePage):
    URL = 'http://192.168.99.100:8081/'
    MYACCOUNT = (By.CSS_SELECTOR, "#top a[title='My Account']")
    REGISTER = (By.XPATH, "//a[text()='Register']")
    FIRSTNAME = (By.NAME, 'firstname')
    LASTNAME = (By.NAME, 'lastname')
    EMAIL = (By.NAME, 'email')
    TELEPHONE = (By.NAME, 'telephone')
    PASSWORD = (By.NAME, 'password')
    CONFIRMPASSWORD = (By.NAME, 'confirm')
    CHECKBOX = (By.NAME, 'agree')
    SUBMIT = (By.CSS_SELECTOR, "#content input.btn.btn-primary")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.fake = Faker()
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def click_myaccount(self):
        self.click(self.element(self.MYACCOUNT))

    def select_reg_page(self):
        self.click(self.element(self.REGISTER))

    def fill_registration_form(self, firstname=None, lastname=None, email=None, telephone=None, password=None):
        firstname = firstname or self.fake.first_name()
        lastname = lastname or self.fake.last_name()
        email = email or self.fake.email()
        telephone = telephone or self.fake.phone_number()
        password = password or self.fake.password()

        self.set_field_value(self.FIRSTNAME, firstname)
        self.set_field_value(self.LASTNAME, lastname)
        self.set_field_value(self.EMAIL, email)
        self.set_field_value(self.TELEPHONE, telephone)
        self.set_field_value(self.PASSWORD, password)
        self.set_field_value(self.CONFIRMPASSWORD, password)

        '''
        Ранее использовал реализацию:
        def set_random_first_name(self, first_name):
        first_name_input = self.wait.until(EC.presence_of_element_located(self.FIRSTNAME)) 
        first_name_input.send_keys(first_name)

        def set_random_last_name(self, last_name):
        last_name_input = self.wait.until(EC.presence_of_element_located(self.LASTNAME))
        last_name_input.send_keys(last_name)
        
        Но решил вынести в родительский класс метод по заполнению, а здесь просто аргументы со значениями передать разные. Вроде так лаконичнее выглядит
        '''
    def select_checkbox(self):
        checkbox = self.driver.find_element(*self.CHECKBOX)
        checkbox.click()

    def click_submit(self):
        self.click(self.element(self.SUBMIT))
