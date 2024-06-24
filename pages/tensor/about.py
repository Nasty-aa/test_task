from methods.page_methods import MethodsPage
from selenium.webdriver.common.by import By
import logging
from elements.base_page import BasePage


class About(BasePage):
    """Класс для работы с объектами страницы о компании"""

    def check_open(self):
        """Проверяем открытие страницы"""

        logging.info('Проверяем открытие страницы')
        about_url = 'https://tensor.ru/about'
        assert self.driver.current_url == about_url, 'Не верная ссылка'

    def check_width_and_height_from_blocks(self):
        """Проверяем ширину и высоту блоков"""

        logging.info('Проверяем ширину и высоту блоков')
        MethodsPage.search_block(self, self.driver, '.tensor_ru-text-main .tensor_ru-About__block3-subtitle',
                                 'Блок работаем')
        blocks_img = self.driver.find_elements(By.CSS_SELECTOR, '.tensor_ru-About__block3-image-wrapper')
        for i in range(len(blocks_img) - 1):
            assert blocks_img[i].size['height'] == blocks_img[i + 1].size['height'], 'Не равна высота'
            assert blocks_img[i].size['width'] == blocks_img[i + 1].size['width'], 'Не равна ширина'
