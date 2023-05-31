
def test_search_currency(main_page):
    main_page.open()
    main_page.click_currency()
    main_page.select_currency()
    main_page.search_symbol_at_page()
