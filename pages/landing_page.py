import allure
from locators.landing_page_locators import LandingPageLocators as LandLock
from pages.base_page import BasePage


class LandingPageStellarBurgers(BasePage):
    @allure.step('Кликаем по кнопке "Войти в аккаунт"')
    def click_sign_in_button(self):
        self.find_and_wait_element_until_clickable(LandLock.SIGN_IN_BUTTON)
        self.click_element(LandLock.SIGN_IN_BUTTON)

    @allure.step('Кликаем по кнопке "Личный кабинет"')
    def click_user_account_button(self):
        self.find_and_wait_element_until_visible(LandLock.USER_ACCOUNT_BUTTON)
        self.click_element(LandLock.USER_ACCOUNT_BUTTON)

    @allure.step('Ожидаем загрузки страницы после авторизации')
    def wait_make_order_page(self):
        self.find_and_wait_element_until_clickable(LandLock.ORDER_BUTTON)
