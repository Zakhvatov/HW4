import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_login(login_page):
    login_page.open()
    login_page.click_myaccount()
    login_page.select_login_page()
    login_page.fill_login_form(email="mail_test@mail.ru", password="testmtt")
    login_page.click_login()
    WebDriverWait(login_page.driver, 2).until(EC.presence_of_element_located((By.XPATH, "//h2[text()='My Orders']")))
    login_page.click_myaccount()
    login_page.select_logout()
    WebDriverWait(login_page.driver, 2).until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Account Logout']")))
