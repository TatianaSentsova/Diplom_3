class ApplicationData:
    STELLAR_BURGERS_URL = 'https://stellarburgers.nomoreparties.site'
    LOGIN = f'{STELLAR_BURGERS_URL}/login'
    FORGOT_PASSWORD = f'{STELLAR_BURGERS_URL}/forgot-password'
    RESET_PASSWORD = f'{STELLAR_BURGERS_URL}/reset-password'
    ACCOUNT_PROFILE = f'{STELLAR_BURGERS_URL}/account/profile'
    ORDER_HISTORY = f'{STELLAR_BURGERS_URL}/account/order-history'
    ENDPOINT_CREATING_USER = '/api/auth/register'
    ENDPOINT_LOGIN = '/api/auth/login'
    ENDPOINT_USER = '/api/auth/user'


class MessageSuccess:
    MAKE_BURGER = "Соберите бургер"
    LIST_ORDER = "Лента заказов"
