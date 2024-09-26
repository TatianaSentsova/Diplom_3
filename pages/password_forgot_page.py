import allure
from locators.password_forgot_page_locators import PasswordForgotPageLocators as PasswordLock
from pages.base_page import BasePage
from utils import FakeData


class PasswordForgotPageStellarBurgers(BasePage):
    @allure.step('Ожидаем, когда загрузится страница с формой восстановления пароля')
    def wait_password_forgot_page(self):
        self.find_and_wait_element_until_visible(PasswordLock.HEADER_PASSWORD_FORGOT_FORM)

    # @allure.step('Получаем текст заголовка формы восстановления пароля')
    # def get_header_password_forgot_form_text(self):
    #     self.wait_password_forgot_page()
    #     return self.get_element_text(PasswordLock.HEADER_PASSWORD_FORGOT_FORM)

    @allure.step('Вводим текст в поле email формы восстановления пароля')
    def set_email(self):
        self.find_and_wait_element_until_clickable(PasswordLock.USER_EMAIL_FIELD)
        self.set_text_to_element(PasswordLock.USER_EMAIL_FIELD, FakeData.email())

    @allure.step('Кликаем по кнопке "Восстановить"')
    def click_recovery_button(self):
        self.find_and_wait_element_until_clickable(PasswordLock.RECOVERY_BUTTON)
        self.click_element(PasswordLock.RECOVERY_BUTTON)

    # @allure.step('Получаем плейсхолдер поля с кодом с формы сброса пароля')
    # def get_code_field_text(self):
    #     self.find_and_wait_element_until_clickable(PasswordLock.CODE_FIELD)
    #     return self.get_element_text(PasswordLock.CODE_FIELD)

    @allure.step('Кликаем по кнопке "Показать/скрыть пароль"')
    def click_show_or_hide_password_button(self):
        self.find_and_wait_element_until_clickable(PasswordLock.SHOW_OR_HIDE_PASSWORD_BUTTON)
        self.click_element(PasswordLock.SHOW_OR_HIDE_PASSWORD_BUTTON)

    @allure.step('Ожидаем пока кнопка "Сохранить" в станет кликабельна в форме сброса пароля')
    def wait_save_button_clickable(self):
        self.find_and_wait_element_until_clickable(PasswordLock.SAVE_BUTTON)

    @allure.step('Проверяем, что поле "Пароль" активно')
    def check_password_field_active(self):
        return self.find_and_wait_element_until_visible(PasswordLock.PASSWORD_FIELD_ACTIVE)
