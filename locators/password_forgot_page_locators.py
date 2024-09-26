from selenium.webdriver.common.by import By


class PasswordForgotPageLocators:
    # Заголовок в форме восстановления пароля
    HEADER_PASSWORD_FORGOT_FORM = (By.XPATH, ".//div[@class = 'Auth_login__3hAey']/h2")
    # Поле email в форме восстановления пароля
    USER_EMAIL_FIELD = (By.XPATH, ".//label[text() = 'Email']/following-sibling::input")
    # Кнопка "Восстановить" на странице восстановления пароля
    RECOVERY_BUTTON = (By.XPATH, ".//button[text() = 'Восстановить']")
    # # Поле с кодом в форме восстановления пароля
    # CODE_FIELD = (By.XPATH, ".//div[contains(@class, 'input_type_text')]/label")
    # Кнопка "Показать/скрыть" пароль
    SHOW_OR_HIDE_PASSWORD_BUTTON = (By.XPATH, ".//div[contains(@class, 'input__icon-action')]")
    # Поле "Пароль" в активном состоянии
    PASSWORD_FIELD_ACTIVE = (By.CSS_SELECTOR, '.input.input_status_active')
    # Кнопка "Сохранить" в форме сброса пароля
    SAVE_BUTTON = (By.XPATH, ".//button[text() = 'Сохранить']")
