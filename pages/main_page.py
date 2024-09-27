import allure
from locators.main_page_locators import MainPageLocators as MainLock
from pages.base_page import BasePage


class MainPageStellarBurgers(BasePage):
    @allure.step('Ожидаем загрузки страницы')
    def wait_main_page(self):
        self.find_and_wait_element_until_visible(MainLock.SIGN_IN_BUTTON)

    @allure.step('Кликаем по кнопке "Войти в аккаунт"')
    def click_sign_in_button(self):
        self.find_and_wait_element_until_clickable(MainLock.SIGN_IN_BUTTON)
        self.click_element(MainLock.SIGN_IN_BUTTON)

    @allure.step('Кликаем по кнопке "Личный кабинет"')
    def click_user_account_button(self):
        self.find_and_wait_element_until_visible(MainLock.USER_ACCOUNT_BUTTON)
        self.click_element(MainLock.USER_ACCOUNT_BUTTON)

    @allure.step('Ожидаем загрузки страницы после авторизации')
    def wait_make_order_page(self):
        self.find_and_wait_element_until_clickable(MainLock.MAKE_ORDER_BUTTON)

    @allure.step('Получаем текст заголовка "Соберите бургер"')
    def get_make_burger_text(self):
        self.wait_main_page()
        return self.get_element_text(MainLock.MAKE_BURGER)

    @allure.step('Кликаем по кнопке "Лента Заказов"')
    def click_list_order_button(self):
        self.find_and_wait_element_until_visible(MainLock.LIST_ORDER_BUTTON)
        self.click_element(MainLock.LIST_ORDER_BUTTON)

    @allure.step('Кликаем по ингредиенту булка')
    def click_ingredient_bun(self):
        self.find_and_wait_element_until_visible(MainLock.FLUORESCENT_BUN)
        self.click_element(MainLock.FLUORESCENT_BUN)

    @allure.step('Закрываем окно с деталями ингредиента булки')
    def close_popup_with_details_ingredient_bun(self):
        self.find_and_wait_element_until_visible(MainLock.CLOSE_BUTTON)
        self.click_element(MainLock.CLOSE_BUTTON)

    @allure.step('Получаем число со счетчика ингредиента булки')
    def get_count_ingredient_bun(self):
        count = int(self.get_element_text(MainLock.COUNTER_FLUORESCENT_BUN))
        return count

    @allure.step('Ожидаем, когда ингредиент булка появится в конструкторе бургера')
    def wait_ingredient_bun_to_constructor_burger(self):
        self.find_and_wait_element_until_visible(MainLock.FLUORESCENT_BUN_IN_BURGER)

    @allure.step('Перемещаем ингредиент булка в конструктор бургера')
    def move_ingredient_bun_to_constructor_burger(self):
        element = self.find_element(MainLock.FLUORESCENT_BUN)
        target = self.find_element(MainLock.CONSTRUCTOR_BURGER)
        self.move_element(element, target)
        self.wait_ingredient_bun_to_constructor_burger()

    @allure.step('Кликаем по кнопке "Заказать бургер"')
    def click_make_order_button(self):
        self.wait_make_order_page()
        self.click_element(MainLock.MAKE_ORDER_BUTTON)

    @allure.step('Проверяем, что появилось всплывающее окно с деталями игридиента')
    def check_open_popup_with_details_ingredient_bun(self):
        self.find_and_wait_element_until_visible(MainLock.INGREDIENT_POPUP_TITLE)
        return self.check_displaying_of_element(MainLock.INGREDIENT_POPUP_TITLE)

    @allure.step('Проверяем, что окно с деталями ингредиента закрылось')
    def check_not_displaying_of_popup_details(self):
        self.wait_close_element(MainLock.INGREDIENT_POPUP_TITLE)
        return self.check_invisibility(MainLock.INGREDIENT_POPUP_TITLE)

    @allure.step('Проверяем, что появилось всплывающее окно с оформленным заказом')
    def check_open_popup_with_details_order(self):
        self.find_and_wait_element_until_visible(MainLock.ORDER_IS_PREPARING)
        return self.check_displaying_of_element(MainLock.ORDER_IS_PREPARING)