from selenium.webdriver.common.by import By
from methods.page_methods import MethodsPage
import logging
from elements.base_page import BasePage


class SbisRu(BasePage):
    """Класс для работы с объектами страницы Сбис"""

    def __init__(self, driver):
        super().__init__(driver)
        self.contacts = self.driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item> a[href="/contacts"]')
        self.button_link = self.driver.find_element(By.CSS_SELECTOR, '.sbisru-Footer__list-item> a[href="/download"]')

    def open_contacts(self):
        """ Переходим на вкладку контакты """

        assert self.contacts.is_displayed(), 'Кнопка контакты не отображается'
        logging.info('Переходим на вкладку контакты')
        self.contacts.click()

    def save_local_version(self):
        """ Открыть страницу скачать локальные версии """

        MethodsPage.search_block(self, self.driver, '.sbisru-Footer__title', 'Footer сайта')
        assert self.button_link.is_displayed(), 'Ссылка на локальные версии не отображается'
        logging.info('Нажимаем ссылку скачать локальные версии')
        self.button_link.click()
