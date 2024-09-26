from selenium.webdriver.common.by import By


class UserAccountPageLocators:
    # Кнопка "Сохранить" в личном кабинете пользователя
    SAVE_BUTTON = (By.XPATH, ".//button[text() = 'Сохранить']")
    # Кнопка "История заказов" в личном кабинете пользователя
    ORDER_HISTORY_BUTTON = (By.XPATH, ".//a[@href = '/account/order-history']")
    # Кнопка "Выход" в личном кабинете пользователя
    LOGOUT_BUTTON = (By.XPATH, ".//button[text() = 'Выход']")

