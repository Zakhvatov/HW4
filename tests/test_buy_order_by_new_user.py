import time


def test_buy_order(buy_page):
    buy_page.open()
    time.sleep(1)
    buy_page.add_to_cart()
    time.sleep(1)
    buy_page.go_to_shopping_cart()
    buy_page.click_checkout()
    time.sleep(2)
    buy_page.select_guest_customer()
    buy_page.fill_billing_form_guest_customer(postcode=1235)
    buy_page.select_region_ddmenu()
    buy_page.click_continue_billing_details_guest()
    time.sleep(2)
    buy_page.click_continue_delivery_method()
    time.sleep(2)
    buy_page.click_continue_payment_method()
    time.sleep(2)
    buy_page.check_success_buy_order()