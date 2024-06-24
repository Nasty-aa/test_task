from selenium import webdriver
from pages.sbis.sbis import SbisRu
from pages.sbis.contacts import Contacts
from pages.tensor.tensor import Tensor
from pages.tensor.about import About
import unittest


class TestCheckSizeImage(unittest.TestCase):

     def setUp(self):
          self.driver = webdriver.Chrome()
          self.driver.maximize_window()
          self.driver.get('https://sbis.ru/')

     def test_check_size_image_001(self):
          self.sbis_ru = SbisRu(self.driver)
          self.sbis_ru.open_contacts()
          self.contacts = Contacts(self.driver)
          self.contacts.click_banner_tensor()
          self.tensor = Tensor(self.driver)
          self.tensor.check_open(self.driver)
          self.tensor.check_block_strength_is_in_people(self.driver)
          self.tensor.open_about_people()
          self.about = About(self.driver)
          self.about.check_open()
          self.about.check_width_and_height_from_blocks()

     def tearDown(self):
               self.driver.quit()


if __name__ == "__main__":
     unittest.main()
