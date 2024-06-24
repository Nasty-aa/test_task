from selenium import webdriver
from selenium.webdriver.common.by import By
from methods.page_methods import MethodsPage
import time


class Contacts:

    def click_banner_tensor(self):
        """Находим и нажимаем на баннер тензора"""

        tensor_href = self.find_elements(By.CLASS_NAME, 'sbisru-Contacts__border-left> a[href="https://tensor.ru/"]')
        assert tensor_href[0].is_displayed(), 'Баннер не отображается'
        print('Нажимаем на баннер тензор')
        tensor_href[0].click()

    def check_region(self, reg):
        """  Проверяем отображаение региона """

        reg_html = self.find_element(By.CLASS_NAME, 'sbis_ru-Region-Chooser__text')
        print('Проверяем отображение элемента')
        assert reg_html.is_displayed(), 'Регион не отображается'
        assert reg_html.get_attribute("textContent") == reg, f'Регион не {reg}'

    def check_parners_block(self, text):
        """ Проверяем отображение блока с партнерами """

        MethodsPage.search_block(self, '.controls-Tree__item', 'Таблица с партнерами', False)
        print('Проверяем отображение блока с партнерами')
        blocks = self.find_elements(By.CSS_SELECTOR, '.sbisru-Contacts-List__name')
        assert blocks[0].text == text, 'Не верный список партнеров'

    def change_region(self, reg):
        """Изменяем регион"""

        reg_html = self.find_element(By.CLASS_NAME, 'sbis_ru-Region-Chooser__text')
        assert reg_html.is_displayed(), 'Регион не отображается'
        print('Открываем окно выбора региона')
        reg_html.click()

        #Нужно для ожидания выбора региона
        time.sleep(3)

        comchatca_button = self.find_element(By.XPATH, f'//*[@title="{reg}"]')
        assert comchatca_button.is_displayed(), f'Регион - {reg} не отображется'
        print(f'Выбираем регион {reg}')
        comchatca_button.click()
        time.sleep(3)
