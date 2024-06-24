from selenium import webdriver
from pages.sbis.sbis import SbisRu
from pages.sbis.contacts import Contacts
from pages.tensor.tensor import Tensor
from pages.tensor.about import About
import unittest


class TestCheckSizeImage(unittest.TestCase):

     def test_check_size_image_001(self):
          driver = webdriver.Chrome()
          driver.maximize_window()
          SbisRu.open_sbis(driver)
          SbisRu.open_contacts(driver)
          Contacts.click_banner_tensor(driver)
          Tensor.check_open(driver)
          Tensor.check_block_strength_is_in_people(driver)
          Tensor.open_about_people(driver)
          About.check_open(driver)
          About.check_width_and_height_from_blocks(driver)
          driver.quit()
