from selenium import webdriver
from pages.sbis.sbis import SbisRu
from pages.sbis.contacts import Contacts

#Открытие браузера
driver = webdriver.Chrome()
driver.maximize_window()

try:

     SbisRu.open_sbis(driver)
     SbisRu.open_contacts(driver)
     Contacts.check_region(driver, 'Ярославская обл.')
     Contacts.check_parners_block(driver, 'СБИС - Ярославль')
     Contacts.change_region(driver, 'Камчатский край')
     Contacts.check_region(driver, 'Камчатский край')
     Contacts.check_parners_block(driver, 'СБИС - Камчатка')

finally:
     driver.quit()