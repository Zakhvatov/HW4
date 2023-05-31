from selenium import webdriver
import pytest

from pages.buy_page import BuyPage
from pages.login_relogin import LoginPage
from pages.registration_page import RegistrationPage
from pages.main_page import MainPage


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


'''
ЗАМЕТКА НЕ ЗАБЫТЬ ПОДУМАТЬ
Фикстуры под каждую страницу выглядят избыточно. Наверное, можно переписать под одну, например, def browser(request)
Тогда передавать в тестах {page}(browser).function 
'''


@pytest.fixture(scope='module')
def registration_page(driver):
    page = RegistrationPage(driver)
    page.open()
    return page


@pytest.fixture(scope='module')
def main_page(driver):
    page = MainPage(driver)
    page.open()
    return page


@pytest.fixture(scope='module')
def login_page(driver):
    page = LoginPage(driver)
    page.open()
    return page


@pytest.fixture(scope='module')
def buy_page(driver):
    page = BuyPage(driver)
    page.open()
    return page
