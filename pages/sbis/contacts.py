from selenium.webdriver.common.by import By
from methods.page_methods import MethodsPage
import time
import logging
from elements.base_page import BasePage


class Contacts(BasePage):
    """Класс для работы с объектами страницы контакты"""

    def __init__(self, driver):
        super().__init__(driver)
        self.tensor_href = self.driver.find_elements(By.CLASS_NAME,
                                            'sbisru-Contacts__border-left> a[href="https://tensor.ru/"]')

    def click_banner_tensor(self):
        """Находим и нажимаем на баннер тензора"""

        assert self.tensor_href[0].is_displayed(), 'Баннер не отображается'
        logging.info('Нажимаем на баннер тензор')
        self.tensor_href[0].click()

    def check_region(self, reg: str):
        """  Проверяем отображаение региона """

        logging.info('Проверяем отображение элемента')
        reg_html = self.driver.find_element(By.CLASS_NAME, 'sbis_ru-Region-Chooser__text')
        assert reg_html.is_displayed(), 'Регион не отображается'
        assert reg_html.get_attribute("textContent") == reg, f'Регион не {reg}'

    def check_parners_block(self, text: str):
        """ Проверяем отображение блока с партнерами """

        blocks = self.driver.find_elements(By.CSS_SELECTOR, '.sbisru-Contacts-List__name')
        MethodsPage.search_block(self, self.driver, '.controls-Tree__item', 'Таблица с партнерами', False)
        logging.info('Проверяем отображение блока с партнерами')
        assert blocks[0].text == text, 'Не верный список партнеров'

    def change_region(self, reg: str):
        """Изменяем регион"""

        reg_html = self.driver.find_element(By.CLASS_NAME, 'sbis_ru-Region-Chooser__text')
        assert reg_html .is_displayed(), 'Регион не отображается'
        logging.info('Открываем окно выбора региона')
        reg_html .click()

        #Нужно для ожидания выбора региона
        time.sleep(3)

        reg_button = self.driver.find_element(By.XPATH, f'//*[@title="{reg}"]')
        assert reg_button.is_displayed(), f'Регион - {reg} не отображется'
        logging.info(f'Выбираем регион {reg}')
        reg_button.click()
        time.sleep(3)
