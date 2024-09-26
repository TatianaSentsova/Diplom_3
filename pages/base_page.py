import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    @allure.step('Подгружаем драйвер в конструктор')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Получаем элемент')
    def find_element(self, locator):
        element = self.driver.find_element(*locator)
        return element

    @allure.step('Ожидаем, что элемент появился на странице и его видно')
    def find_and_wait_element_until_visible(self, locator):
        WebDriverWait(self.driver, 12).until(EC.visibility_of_element_located(locator))
        return self.find_element(locator)

    @allure.step('Ожидаем, что элемент на странице кликабелен')
    def find_and_wait_element_until_clickable(self, locator):
        WebDriverWait(self.driver, 12).until(EC.element_to_be_clickable(locator))
        return self.find_element(locator)

    @allure.step('Кликаем по элементу')
    def click_element(self, locator):
        self.find_element(locator).click()

    @allure.step('Вводим текст в элемент')
    def set_text_to_element(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step("Проверка текущего url")
    def get_current_url(self):
        return self.driver.current_url
