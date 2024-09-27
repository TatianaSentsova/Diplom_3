import allure
from pages.base_page import BasePage
from locators.list_order_page_locators import ListOrderPageLocators as ListOrderLock


class ListOrderPageStellarBurgers(BasePage):
    @allure.step('Ожидаем загрузки страницы')
    def wait_list_order_page(self):
        self.find_and_wait_element_until_visible(ListOrderLock.ORDERS_FOR_ALL_TIME)

    @allure.step('Получаем текст заголовка "Лента заказов"')
    def get_list_order_header_text(self):
        self.wait_list_order_page()
        return self.get_element_text(ListOrderLock.LIST_ORDER_HEADER)
