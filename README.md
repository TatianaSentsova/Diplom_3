# Дипломный проект. Задание 3: тестирование UI
## Автотесты для проверки UI Stellar Burgers

### Реализованные сценарии

    Восстановление пароля
        переход на страницу восстановления пароля по кнопке «Восстановить пароль»,
        ввод почты и клик по кнопке «Восстановить»,
        клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.
    Личный кабинет пользователя
        переход по клику на «Личный кабинет»,
        переход в раздел «История заказов»,
        выход из аккаунта.
    Проверка основного функционала
        переход по клику на «Конструктор»,
        переход по клику на «Лента заказов»,
        если кликнуть на ингредиент, появится всплывающее окно с деталями,
        всплывающее окно закрывается кликом по крестику,
        при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается,
        залогиненный пользователь может оформить заказ.
    Раздел «Лента заказов»
        если кликнуть на заказ, откроется всплывающее окно с деталями,
        заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»,
        при создании нового заказа счётчик Выполнено за всё время увеличивается,
        при создании нового заказа счётчик Выполнено за сегодня увеличивается,
        после оформления заказа его номер появляется в разделе В работе.

### Структура проекта

    tests — пакет, содержащий тесты, разделенные по тестируемым страницам
    pages — пакет, содержащий файлы с кодом, описывающий методы длы тестов
    locators — пакте, содержащий файлы с локаторами для страниц 
    testdata — файл, содержащий данные с эндпоинтами и адресом сервиса и др. тестовые данные
    utils — файл, содержащий методы, генерирующие наборы данных для тестов
    conftest — файл, содержащий фикстуры, используемые в тестах
    requirements — файл, с перечислением внешних зависимостей исполняемых тестов
    README — файл, содержащий описание проекта

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск всех тестов одной командой**

>  `pytest -v tests`

**Allure-отчет о тестировании в формате веб-страницы**

>  `allure serve allure_results`
