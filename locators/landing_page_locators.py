from selenium.webdriver.common.by import By


class LandingPageLocators:
    # кнопка "Войти в аккаунт" на главной странице
    SIGN_IN_BUTTON = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")
    # кнопка "Личный кабинет" на главной странице
    USER_ACCOUNT_BUTTON = (By.XPATH, ".//a[@href = '/account']")
    # кнопка "Оформить заказ" на главной странице
    ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']")
