from selenium.webdriver.common.by import By
from methods.page_methods import MethodsPage
import logging
from elements.base_page import BasePage


class Tensor(BasePage):
    """Класс для работы с главной страницей тензор"""

    def check_open(self, driver):
        """Проверяем открытие сайта """

        tensor = 'https://tensor.ru/'
        logging.info(f'Проверяем открытие сайта {tensor}')
        handles = driver.window_handles
        driver.switch_to.window(handles[1])
        assert driver.current_url == tensor, 'Не верная ссылка'

    def check_block_strength_is_in_people(self, driver):
        """Проверяем блок сила в людях"""

        logging.info('Проверяем блок сила в людях')
        MethodsPage.search_block(self, driver, '.tensor_ru-Index__block4-content .tensor_ru-Index__card-title',
                                 'Сила в людях')

    def open_about_people(self):
        """Нажимаем на подробнее в блоке сила в людях"""

        about = self.driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__card-text> a[href="/about"]')
        assert about.is_displayed(), 'Кнопка подробнее не отображается'
        logging.info('Нажимаем на подбробнее в блоке сила в людях')
        about.click()
