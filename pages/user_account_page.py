import allure
from pages.base_page import BasePage
from locators.user_account_locators import UserAccountPageLocators as UserLock


class UserAccountPageStellarBurgers(BasePage):
    @allure.step('Ожидаем, пока загрузится личный кабинет пользователя')
    def wait_user_account_page(self):
        self.find_and_wait_element_until_visible(UserLock.SAVE_BUTTON)

    @allure.step('Кликаем по кнопке "История заказов" в личном кабинете пользователя')
    def click_order_history_button(self):
        self.find_and_wait_element_until_visible(UserLock.ORDER_HISTORY_BUTTON)
        self.click_element(UserLock.ORDER_HISTORY_BUTTON)

    @allure.step('Кликаем по кнопке "Выход" в личном кабинете пользователя')
    def click_logout_button(self):
        self.find_and_wait_element_until_visible(UserLock.LOGOUT_BUTTON)
        self.click_element(UserLock.LOGOUT_BUTTON)

    @allure.step('Получаем id последнего заказа пользователя')
    def get_id_last_order(self):
        self.find_and_wait_element_until_visible(UserLock.ID_LAST_ORDER_IN_HISTORY)
        return self.get_element_text(UserLock.ID_LAST_ORDER_IN_HISTORY)

    @allure.step('Кликаем по кнопке "Лента заказов" в личном кабинете пользователя')
    def click_list_order_button(self):
        self.find_and_wait_element_until_visible(UserLock.LIST_ORDER_BUTTON)
        self.click_element(UserLock.LIST_ORDER_BUTTON)
