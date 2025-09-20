from pages.swag_labs import SwagLabs
from selenium.webdriver.common.by import By


# Переход на страницу, проверка наличия иконки.
def test_check_icon(browser):
    sauce_demo_page = SwagLabs(browser)
    sauce_demo_page.visit()
    assert  sauce_demo_page.exist_icon()


# Переход на страницу, проверка наличия поля имени
def test_check_name_field(browser):
    sauce_demo_page = SwagLabs(browser)
    sauce_demo_page.visit()
    assert sauce_demo_page.exist_username_field()


# Переход на страницу, проверка наличия поля пароля
def test_check_password_field(browser):
    sauce_demo_page = SwagLabs(browser)
    sauce_demo_page.visit()
    assert sauce_demo_page.exist_password_field()