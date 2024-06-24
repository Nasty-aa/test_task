import os
from selenium import webdriver
from pages.sbis.sbis import SbisRu
from pages.sbis.save import SavePage
from webdrivermanager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from methods.file_methods import MethodsFile
import unittest


class TestCheckSizeUpload(unittest.TestCase):

     def test_check_size_upload_001(self):

          #Настройки загрузки файла
          chrome_options = webdriver.ChromeOptions()
          prefs = {
               "download.default_directory": f"{os.getcwd()}\downloads",
               "download_restrictions": False
          }
          chrome_options.add_experimental_option("prefs", prefs)
          service = Service(executable_path=ChromeDriverManager().download_and_install())

          #Открытие браузера
          driver = webdriver.Chrome(options=chrome_options)
          driver.maximize_window()

          SbisRu.open_sbis(driver)
          SbisRu.save_local_version(driver)
          SavePage.save_veb_installer(driver)
          MethodsFile.check_size_file(driver,path=f"{os.getcwd()}\downloads\sbisplugin-setup-web.exe", size=7.22)

          driver.quit()
          os.remove(f"{os.getcwd()}\downloads\sbisplugin-setup-web.exe")