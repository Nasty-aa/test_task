from selenium import webdriver
from pages.sbis.sbis import SbisRu
from pages.sbis.contacts import Contacts
import unittest


class TestChangeRegion(unittest.TestCase):

     def test_change_region_001(self):
          driver = webdriver.Chrome()
          driver.maximize_window()
          driver = webdriver.Chrome()
          driver.maximize_window()
          SbisRu.open_sbis(driver)
          SbisRu.open_contacts(driver)
          Contacts.check_region(driver, 'Ярославская обл.')
          Contacts.check_parners_block(driver, 'СБИС - Ярославль')
          Contacts.change_region(driver, 'Камчатский край')
          Contacts.check_region(driver, 'Камчатский край')
          Contacts.check_parners_block(driver, 'СБИС - Камчатка')
          driver.quit()