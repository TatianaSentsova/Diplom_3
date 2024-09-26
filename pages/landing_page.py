import allure
from locators.landing_page_locators import LandingPageLocators as LandLock
from pages.base_page import BasePage


class LandingPageStellarBurgers(BasePage):
    @allure.step('Кликаем по кнопке "Войти в аккаунт"')
    def click_sign_in_button(self):
        self.find_and_wait_element_until_clickable(LandLock.SIGN_IN_BUTTON)
        self.click_element(LandLock.SIGN_IN_BUTTON)
