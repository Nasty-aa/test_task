from pages.sbis.sbis import SbisRu
from pages.sbis.contacts import Contacts
from selenium import webdriver
import unittest


class TestChangeRegion(unittest.TestCase):
     def setUp(self):
          self.driver = webdriver.Chrome()
          self.driver.maximize_window()
          self.driver.get('https://sbis.ru/')

     def test_change_region_001(self):
          self.sbis_ru = SbisRu(self.driver)
          self.contacts_page = Contacts(self.driver)
          self.sbis_ru.open_contacts()
          self.contacts_page.check_region(reg='Ярославская обл.')
          self.contacts_page.check_parners_block(text='СБИС - Ярославль')
          self.contacts_page.change_region(reg='Камчатский край')
          self.contacts_page.check_region(reg='Камчатский край')
          self.contacts_page.check_parners_block(text='СБИС - Камчатка')

     def tearDown(self):
          self.driver.quit()

if __name__ == "__main__":
    unittest.main()