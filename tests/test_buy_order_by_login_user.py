import time
"""
Слипы для отладки теста использовал. Можно убрать большинство
"""


def test_buy_order(buy_page):
    buy_page.open()
    time.sleep(1)
    buy_page.add_to_cart()
    time.sleep(1)
    buy_page.go_to_shopping_cart()
    buy_page.click_checkout()
    buy_page.fill_login_form(email="mail_test26@mail.ru", password="test")
    buy_page.click_login_button()
    time.sleep(2)
    buy_page.fill_billing_form(postcode=123456)
    buy_page.select_region_ddmenu()
    buy_page.continue_checkout_click_button()
    time.sleep(2)
    buy_page.click_continue_delivery_details()
    time.sleep(2)
    buy_page.click_continue_delivery_method()
    time.sleep(2)
    buy_page.click_continue_payment_method()
    time.sleep(2)
    buy_page.check_success_buy_order()

