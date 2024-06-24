import time
from selenium.webdriver.common.by import By


class SavePage:

    def save_veb_installer(self):
        """ Скачать веб установщик"""

        link = 'https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe'
        link_download = self.find_element(By.CSS_SELECTOR, f'.sbis_ru-DownloadNew-loadLink> a[href="{link}"]')
        assert link_download.is_displayed(), 'Кнопка скачать не отображается'
        print('Скачиваем файл')
        link_download.click()
        time.sleep(10)