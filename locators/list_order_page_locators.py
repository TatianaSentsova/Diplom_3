from selenium.webdriver.common.by import By


class ListOrderPageLocators:
    # заголовок "Выполнено за все время" на странице "Лента заказов"
    ORDERS_FOR_ALL_TIME = (By.XPATH, ".//p[contains(text(), 'Выполнено за все время')]")
    # заголовок "Лента заказов" на странице "Лента заказов"
    LIST_ORDER_HEADER = (By.XPATH, ".//div[contains(@class, 'OrderFeed')]/h1[contains(@class, 'mt-10 mb-5')]")
