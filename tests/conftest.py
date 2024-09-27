from collections import namedtuple

import pytest
import allure
from selenium import webdriver
from testdata import ApplicationData
from pages.main_page import MainPageStellarBurgers as Main
from pages.login_page import LoginPageStellarBurgers as Login
from pages.password_forgot_page import PasswordForgotPageStellarBurgers as PasswordForgot
from pages.user_account_page import UserAccountPageStellarBurgers as UserAccount
from pages.list_order_page import ListOrderPageStellarBurgers as ListOrder
from utils import FakeData, Body, Request


@allure.step('Инициализируем драйвер')
@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    driver = None
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
    driver.get(ApplicationData.STELLAR_BURGERS_URL)
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    main_page = Main(driver)
    return main_page


@pytest.fixture
def login_page(driver):
    login_page = Login(driver)
    return login_page


@pytest.fixture
def password_forgot_page(driver):
    password_forgot_page = PasswordForgot(driver)
    return password_forgot_page


@pytest.fixture
def user_account_page(driver):
    user_account_page = UserAccount(driver)
    return user_account_page


@pytest.fixture
def list_order_page(driver):
    list_order_page = ListOrder(driver)
    return list_order_page


@allure.step('Создаем пользователя, получаем кортеж с токеном авторизации и данными пользователя')
@pytest.fixture
def authorized_user():
    email = FakeData.email()
    password = FakeData.password()
    name = FakeData.name()
    user_body = Body.build_user_body(email, password, name)
    Request.create_user(user_body)
    login_pass_body = Body.build_login_pass_body(email, password)
    response = Request.login_user(login_pass_body)
    token = response.json()['accessToken']
    UserData = namedtuple('UserData', ['email', 'password', 'name', 'token'])
    yield UserData(email, password, name, token)
    Request.delete_user(token)
