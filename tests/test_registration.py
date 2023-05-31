
def test_registration(registration_page):
    registration_page.open()
    registration_page.click_myaccount()
    registration_page.select_reg_page()
    registration_page.fill_registration_form(email="mail_test19@mtt.ru", password="qwerty")

    '''
    Что бы заполнить какими то не рандомными данными, то можно передать значения для аргументов в функцию. Например,
    registration_page.fill_registration_form(firstname="Alexander", lastname="Zakhvatov", email="AZahvatov@mtt.ru", telephone="5555555", password="qwerty")
    
    Ранее использовал реализацию вида:
    def test_registration(registration_page):
    fake = faker.Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    telephone = fake.phone_number()
    password = fake.password()

    registration_page.click_myaccount()
    registration_page.select_reg_page()
    registration_page.set_random_first_name(first_name)
    registration_page.set_random_last_name(last_name)
    registration_page.set_random_email(email)
    registration_page.set_random_telephone(telephone)
    registration_page.set_random_password(password)
    registration_page.set_confirm_password(password)
    registration_page.select_checkbox()
    registration_page.click_submit()
    '''
