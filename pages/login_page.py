import allure
from locators.login_page_locators import LoginPageLocators as LoginLock
from pages.base_page import BasePage


class LoginPageStellarBurgers(BasePage):
    # @allure.step('Ожидаем когда загрузится страница с формой авторизации')
    # def wait_login_page(self):
    #     self.find_and_wait_element_until_visible(LoginLock.PASSWORD_RECOVERY_BUTTON)

    @allure.step('Ожидаем, когда кнопка "Восстановить пароль" станет кликабельной и кликаем по ней')
    def click_password_recovery_button(self):
        self.find_and_wait_element_until_clickable(LoginLock.PASSWORD_RECOVERY_BUTTON)
        self.click_element(LoginLock.PASSWORD_RECOVERY_BUTTON)
