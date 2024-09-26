import pytest
import allure
from selenium import webdriver
from testdata import ApplicationData
from pages.landing_page import LandingPageStellarBurgers as Landing
from pages.login_page import LoginPageStellarBurgers as Login
from pages.password_forgot_page import PasswordForgotPageStellarBurgers as PasswordForgot


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
def landing_page(driver):
    landing_page = Landing(driver)
    return landing_page


@pytest.fixture
def login_page(driver):
    login_page = Login(driver)
    return login_page


@pytest.fixture
def password_forgot_page(driver):
    password_forgot_page = PasswordForgot(driver)
    return password_forgot_page
