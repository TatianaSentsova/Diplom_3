from selenium.webdriver.common.by import By


class LandingPageLocators:
    # кнопка "Войти в аккаунт" на главной странице
    SIGN_IN_BUTTON = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")