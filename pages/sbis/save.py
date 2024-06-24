from selenium.webdriver.common.by import By
import logging
from elements.base_page import BasePage


class SavePage(BasePage):
    """Класс для работы с объектами страницы скачать"""

    def save_veb_installer(self):
        """ Скачать веб установщик"""

        link = 'https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe'
        link_download = self.driver.find_element(By.CSS_SELECTOR,
                                                      f'.sbis_ru-DownloadNew-loadLink> a[href="{link}"]')
        assert link_download.is_displayed(), 'Кнопка скачать не отображается'
        logging.info('Скачиваем файл')
        link_download.click()