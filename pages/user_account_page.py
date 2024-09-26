import allure
from pages.base_page import BasePage
from locators.user_account_locators import UserAccountPageLocators as UserLock


class UserAccountPageStellarBurgers(BasePage):
    @allure.step('Ожидаем, пока загрузится личный кабинет пользователя')
    def wait_user_account_page(self):
        self.find_and_wait_element_until_clickable(UserLock.SAVE_BUTTON)

    @allure.step('Кликаем по кнопке "История заказов" в личном кабинете пользователя')
    def click_order_history_button(self):
        self.find_and_wait_element_until_visible(UserLock.ORDER_HISTORY_BUTTON)
        self.click_element(UserLock.ORDER_HISTORY_BUTTON)

    @allure.step('Кликаем по кнопке "Выход" в личном кабинете пользователя')
    def click_logout_button(self):
        self.find_and_wait_element_until_visible(UserLock.LOGOUT_BUTTON)
        self.click_element(UserLock.LOGOUT_BUTTON)
