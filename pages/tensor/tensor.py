from selenium.webdriver.common.by import By
from methods.page_methods import MethodsPage


class Tensor:

    def check_open(self):
        """Проверяем открытие сайта """

        tensor = 'https://tensor.ru/'
        print(f'Проверяем открытие сайта {tensor}')
        handles = self.window_handles
        self.switch_to.window(handles[1])
        assert self.current_url == tensor, 'Не верная ссылка'

    def check_block_strength_is_in_people(self):
        """Проверяем блок сила в людях"""

        print('Проверяем блок сила в людях')
        MethodsPage.search_block(self, '.tensor_ru-Index__block4-content .tensor_ru-Index__card-title', 'Сила в людях')

    def open_about_people(self):
        """Нажимаем на подробнее в блоке сила в людях"""

        about = self.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__card-text> a[href="/about"]')
        assert about.is_displayed(), 'Кнопка подробнее не отображается'
        print('Нажимаем на подбробнее в блоке сила в людях')
        about.click()
