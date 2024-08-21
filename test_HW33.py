import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    #добавил данную строку т.к. сайт открывается не моментально
    driver.implicitly_wait(10)
    driver.get('https://b2c.passport.rt.ru/auth/')
    driver.maximize_window()
    yield driver

    driver.quit()


#1
def test_auth_with_valid_num(driver):
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    driver.find_element(By.ID, 'username').send_keys('9377724666')
    driver.find_element(By.ID, 'password').send_keys('434310_ASDFg')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    driver.implicitly_wait(3)
    assert driver.find_element(By.XPATH, "//h2[@title='Гайнутдинов Динар']").text == "Гайнутдинов Динар"


#2
def test_auth_with_valid_email(driver):
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    driver.find_element(By.ID, 'username').send_keys('dinar0002@mail.ru')
    driver.find_element(By.ID, 'password').send_keys('434310_ASDFg')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    driver.implicitly_wait(3)
    assert driver.find_element(By.XPATH, "//h2[@title='Гайнутдинов Динар']").text == "Гайнутдинов Динар"


#3
def test_auth_with_valid_login(driver):
    driver.find_element(By.ID, 't-btn-tab-login').click()
    driver.find_element(By.ID, 'username').send_keys('rtkid_1724146177260')
    driver.find_element(By.ID, 'password').send_keys('434310_ASDFg')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    driver.implicitly_wait(3)
    assert driver.find_element(By.XPATH, "//h2[@title='Гайнутдинов Динар']").text == "Гайнутдинов Динар"


#4. Тест будет падать в ошибку т.к. у меня не получилось получить номер лицевой счет, но тест рабочий :)
def test_auth_with_valid_ls(driver):
    driver.find_element(By.ID, 't-btn-tab-ls').click()
    driver.find_element(By.ID, 'username').send_keys('123456789010')
    driver.find_element(By.ID, 'password').send_keys('434310_ASDFg')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    driver.implicitly_wait(3)
    assert driver.find_element(By.XPATH, "//h2[@title='Гайнутдинов Динар']").text == "Гайнутдинов Динар"


#5
def test_auth_with_not_valid_num(driver):
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    driver.find_element(By.ID, 'username').send_keys('9377724333')
    driver.find_element(By.ID, 'password').send_keys('434310_ASDFg')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    driver.implicitly_wait(3)
    assert driver.find_element(By.ID, "form-error-message").text == "Неверный логин или пароль"


#6
def test_auth_with_not_valid_email(driver):
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    driver.find_element(By.ID, 'username').send_keys('example@mail.ru')
    driver.find_element(By.ID, 'password').send_keys('434310_ASDFg')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    driver.implicitly_wait(3)
    assert driver.find_element(By.ID, "form-error-message").text == "Неверный логин или пароль"


#7
def test_auth_with_not_valid_login(driver):
    driver.find_element(By.ID, 't-btn-tab-login').click()
    driver.find_element(By.ID, 'username').send_keys('rtkid_00000000000')
    driver.find_element(By.ID, 'password').send_keys('434310_ASDFg')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    driver.implicitly_wait(3)
    assert driver.find_element(By.ID, "form-error-message").text == "Неверный логин или пароль"


#8
def test_auth_with_not_valid_ls(driver):
    driver.find_element(By.ID, 't-btn-tab-ls').click()
    driver.find_element(By.ID, 'username').send_keys('100987654321')
    driver.find_element(By.ID, 'password').send_keys('434310_ASDFg')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    driver.implicitly_wait(3)
    assert driver.find_element(By.ID, "form-error-message").text == "Неверный логин или пароль"


#9
def test_forgot_pass_with_phone(driver):
    driver.find_element(By.ID, 'forgot_password').click()
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    driver.find_element(By.ID, 'username').send_keys('9377724666')
    #Тайм слип для ввода капчи
    time.sleep(20)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, '//*[@id="email-reset-type"]//span[1]').click()
    driver.find_element(By.XPATH, '//*[@id="reset-form-submit"]').click()
    # Тайм слип для ввода кода из смс
    time.sleep(20)
    driver.find_element(By.ID, 'password-new').send_keys('434310_ASd')
    driver.find_element(By.ID, 'password-confirm').send_keys('434310_ASd')
    driver.find_element(By.ID, 't-btn-reset-pass').click()
    assert driver.current_url.startswith("https://b2c.passport.rt.ru/auth/")


#10
def test_forgot_pass_with_email(driver):
    driver.find_element(By.ID, 'forgot_password').click()
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    driver.find_element(By.ID, 'username').send_keys('dinar0002@mail.ru')
    #Тайм слип для ввода капчи
    time.sleep(20)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, '//*[@id="email-reset-type"]//span[2]').click()
    driver.find_element(By.XPATH, '//*[@id="reset-form-submit"]').click()
    # Тайм слип для ввода кода из смс
    time.sleep(20)
    driver.find_element(By.ID, 'password-new').send_keys('434310_ASd')
    driver.find_element(By.ID, 'password-confirm').send_keys('434310_ASd')
    driver.find_element(By.ID, 't-btn-reset-pass').click()
    assert driver.current_url.startswith("https://b2c.passport.rt.ru/auth/")


#11
def test_forgot_pass_with_not_valid_pass(driver):
    driver.find_element(By.ID, 'forgot_password').click()
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    driver.find_element(By.ID, 'username').send_keys('9377724666')
    #Тайм слип для ввода капчи
    time.sleep(20)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, '//*[@id="email-reset-type"]//span[1]').click()
    driver.find_element(By.XPATH, '//*[@id="reset-form-submit"]').click()
    # Тайм слип для ввода кода из смс
    time.sleep(20)
    driver.find_element(By.ID, 'password-new').send_keys('434310')
    driver.find_element(By.ID, 'password-confirm').send_keys('434310')
    assert driver.find_element(By.ID, "password-new-meta").text == "Длина пароля должна быть не менее 8 символов"


#12
def test_register_with_valid_value(driver):
    driver.find_element(By.ID, 'kc-register').click()
    driver.find_element(By.NAME, "firstName").send_keys('Динар')
    driver.find_element(By.NAME, "lastName").send_keys('Гайнутдинов')
    driver.find_element(By.ID, 'address').send_keys('dinar0002@bk.ru')
    driver.find_element(By.ID, 'password').send_keys('434310_ASDf')
    driver.find_element(By.ID, 'password-confirm').send_keys('434310_ASDf')
    driver.find_element(By.NAME, "register").click()
    #Тайм слип для ввода кода с почты
    time.sleep(20)
    assert driver.find_element(By.XPATH, "//h2[@title='Гайнутдинов Динар']").text == "Гайнутдинов Динар"


#13
def test_register_with_not_valid_email(driver):
    driver.find_element(By.ID, 'kc-register').click()
    driver.find_element(By.NAME, "firstName").send_keys('Динар')
    driver.find_element(By.NAME, "lastName").send_keys('Гайнутдинов')
    driver.find_element(By.ID, 'address').send_keys('dinar0002@mail.ru')
    driver.find_element(By.ID, 'password').send_keys('434310_ASDf')
    driver.find_element(By.ID, 'password-confirm').send_keys('434310_ASDf')
    driver.find_element(By.NAME, "register").click()
    assert driver.find_element(By.XPATH, "//h2[contains(@class, 'card-modal__title')]").text == "Учётная запись уже существует"


#14
def test_register_with_not_valid_data(driver):
    driver.find_element(By.ID, 'kc-register').click()
    driver.find_element(By.ID, 'address').send_keys('dinar0002@mail.ru')
    driver.find_element(By.ID, 'password').send_keys('434310_ASDf')
    driver.find_element(By.ID, 'password-confirm').send_keys('434310_ASDf')
    driver.find_element(By.NAME, "register").click()
    assert driver.find_element(By.XPATH, "//span[contains(@class, 'rt-input-container__meta--error')]").text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


#15
def test_register_with_not_valid_leng(driver):
    driver.find_element(By.ID, 'kc-register').click()
    driver.find_element(By.NAME, "firstName").send_keys('Dinar')
    driver.find_element(By.NAME, "lastName").send_keys('Gaynutdinov')
    driver.find_element(By.ID, 'address').send_keys('dinar0002@mail.ru')
    driver.find_element(By.ID, 'password').send_keys('434310_ASDf')
    driver.find_element(By.ID, 'password-confirm').send_keys('434310_ASDf')
    driver.find_element(By.NAME, "register").click()
    assert driver.find_element(By.XPATH, "//span[contains(@class, 'rt-input-container__meta--error')]").text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


#16
def test_auth_with_code_and_valid_phone(driver):
    driver.implicitly_wait(10)
    driver.get('https://lk.rt.ru/')
    driver.find_element(By.ID, "address").send_keys('9377724666')
    driver.find_element(By.ID, "otp_get_code").click()
    # Тайм слип для ввода кода из смс
    time.sleep(20)
    driver.implicitly_wait(5)
    assert driver.find_element(By.XPATH, '//h2[@class="sc-fvxzrP gijTgo"]').text == "Динар"


#17
def test_auth_with_code_and_valid_email(driver):
    driver.implicitly_wait(10)
    driver.get('https://lk.rt.ru/')
    driver.find_element(By.ID, "address").send_keys('dinar0002@mail.ru')
    driver.find_element(By.ID, "otp_get_code").click()
    # Тайм слип для ввода кода с почты
    time.sleep(20)
    driver.implicitly_wait(5)
    assert driver.find_element(By.XPATH, '//h2[@class="sc-fvxzrP gijTgo"]').text == "Динар"


#18
def test_auth_with_code_and_not_valid_phone(driver):
    driver.implicitly_wait(10)
    driver.get('https://lk.rt.ru/')
    driver.find_element(By.ID, "address").send_keys('9377724333')
    driver.find_element(By.ID, "otp_get_code").click()
    assert driver.find_element(By.XPATH, '//h1[@id="card-title" and @class="card-container__title"]').text == "Код подтверждения отправлен"


#19
def test_auth_with_code_and_not_valid_email(driver):
    driver.implicitly_wait(10)
    driver.get('https://lk.rt.ru/')
    driver.find_element(By.ID, "address").send_keys('dinar@net_takogo_email.ru')
    driver.find_element(By.ID, "otp_get_code").click()
    assert driver.find_element(By.XPATH, '//h1[@id="card-title" and @class="card-container__title"]').text == "Код подтверждения отправлен"


#20
def test_auth_with_not_valid_code(driver):
    driver.implicitly_wait(10)
    driver.get('https://lk.rt.ru/')
    time.sleep(20)
    driver.find_element(By.ID, "address").send_keys('dinar0002@mail.ru')
    driver.find_element(By.ID, "otp_get_code").click()
    # Тайм слип для ввода не правильного кода (например 123456)
    time.sleep(20)
    assert driver.find_element(By.XPATH, '//span[@id="form-error-message"]').text == "Неверный код. Повторите попытку"
