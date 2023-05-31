from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    URL = 'http://192.168.99.100:8081/'
    CHANGE_CURRENCY = (By.CSS_SELECTOR, "#form-currency > div > button")
    EURO = (By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(1) > button")
    SYMBOL = "€"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def click_currency(self):
        self.click(self.element(self.CHANGE_CURRENCY))

    def select_currency(self):
        self.click(self.element(self.EURO))

    def search_symbol_at_page(self):
        self.search_by_symbol(self.SYMBOL)
