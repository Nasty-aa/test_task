from selenium.webdriver.common.by import By
from methods.page_methods import MethodsPage

class SbisRu:

    def open_sbis(self):
        """ Открываем страницу https://sbis.ru/"""

        site = 'https://sbis.ru/'
        print(f'Открываем сайт {site}')
        self.get(site)
        assert self.current_url == site, 'Не верная ссылка'

    def open_contacts(self):
        """ Переходим на вкладку контакты """

        contacts = self.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item> a[href="/contacts"]')
        assert contacts.is_displayed(), 'Кнопка контакты не отображается'
        print('Переходим на вкладку контакты')
        contacts.click()

    def save_local_version(self):
        """ Открыть страницу скачать локальные версии """

        MethodsPage.search_block(self, '.sbisru-Footer__title', 'Footer сайта')
        button_link = self.find_element(By.CSS_SELECTOR, '.sbisru-Footer__list-item> a[href="/download"]')
        assert button_link.is_displayed(), 'Ссылка на локальные версии не отображается'
        print('Нажимаем ссылку скачать локальные версии')
        button_link.click()
