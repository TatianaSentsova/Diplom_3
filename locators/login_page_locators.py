from selenium.webdriver.common.by import By


class LoginPageLocators:
    # кнопка "Восстановить пароль" на странице авторизации
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, ".//a[text() = 'Восстановить пароль']")

