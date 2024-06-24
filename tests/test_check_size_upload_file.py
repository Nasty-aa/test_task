import os
from selenium import webdriver
from pages.sbis.sbis import SbisRu
from pages.sbis.save import SavePage
from methods.file_methods import MethodsFile
import unittest


class TestCheckSizeUpload(unittest.TestCase):

     def setUp(self):
          # Настройки загрузки файла
          chrome_options = webdriver.ChromeOptions()
          prefs = {
               "download.default_directory": f"{os.getcwd()}\downloads",
               "download_restrictions": False
          }
          chrome_options.add_experimental_option("prefs", prefs)

          # Открытие браузера
          self.driver = webdriver.Chrome(options=chrome_options)
          self.driver.maximize_window()
          self.driver.get('https://sbis.ru/')

     def test_check_size_upload_001(self):
          self.sbis_ru = SbisRu(self.driver)
          self.sbis_ru.save_local_version()
          self.save_page = SavePage(self.driver)
          self.save_page.save_veb_installer()
          MethodsFile.check_size_file(self, path=f"{os.getcwd()}\downloads\sbisplugin-setup-web.exe", size=7.22)

     def tearDown(self):
          self.driver.quit()
          os.remove(f"{os.getcwd()}\downloads\sbisplugin-setup-web.exe")

if __name__ == "__main__":
    unittest.main()