from methods.page_methods import MethodsPage
from selenium.webdriver.common.by import By


class About:

    def check_open(self):
        """Проверяем открытие страницы"""

        print('Проверяем открытие страницы')
        about_url = 'https://tensor.ru/about'
        assert self.current_url == about_url, 'Не верная ссылка'

    def check_width_and_height_from_blocks(self):
        """Проверяем ширину и высоту блоков"""

        print('Проверяем ширину и высоту блоков')
        MethodsPage.search_block(self, '.tensor_ru-text-main .tensor_ru-About__block3-subtitle', 'Блок работаем')
        blocks_img = self.find_elements(By.CSS_SELECTOR, '.tensor_ru-About__block3-image-wrapper')
        for i in range(len(blocks_img) - 1):
            assert blocks_img[i].size['height'] == blocks_img[i + 1].size['height'], 'Не равна высота'
            assert blocks_img[i].size['width'] == blocks_img[i + 1].size['width'], 'Не равна ширина'
