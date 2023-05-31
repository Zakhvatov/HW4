from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    URL = None
    EMAIL_FORM = None
    PASSWORD_FORM = None

    def __init__(self, driver):
        self.driver = driver

    def element(self, locator):
        return self.driver.find_element(*locator)

    @staticmethod
    def click(element):
        element.click()

    def search_by_symbol(self, symbol):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, f"//*[normalize-space()='{symbol}']")))

    def set_field_value(self, locator, value):
        field_input = self.wait.until(EC.presence_of_element_located(locator))
        field_input.send_keys(value)

