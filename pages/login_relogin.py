from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = 'http://192.168.99.100:8081/'
    MYACCOUNT = (By.CSS_SELECTOR, "#top a[title='My Account']")
    LOGIN = (By.XPATH, "//a[text()='Login']")
    EMAIL_FORM = (By.NAME, 'email')
    PASSWORD_FORM = (By.NAME, 'password')
    ACCESS_LOGIN_TITLE = "My Orders"
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#content > div > div:nth-child(2) > div > form > input")
    LOGOUT = (By.XPATH, "//a[text()='Logout']")
    ACCESS_LOGOUT_TITLE = "Account Logout"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def click_myaccount(self):
        self.click(self.element(self.MYACCOUNT))

    def select_login_page(self):
        self.click(self.element(self.LOGIN))

    def fill_login_form(self, email, password):
        self.set_field_value(self.EMAIL_FORM, email)
        self.set_field_value(self.PASSWORD_FORM, password)

    def click_login(self):
        self.click((self.element(self.LOGIN_BUTTON)))

    def select_logout(self):
        self.click(self.element(self.LOGOUT))


