from selenium.webdriver.common.by import By
import logging
from elements.base_page import BasePage


class MethodsPage(BasePage):
    """Класс для работы с блоками"""

    def search_block(self, driver, css: str, name_block: str, scroll=True):
        """
            Метод для поиска элемента на странице
            css - Класс по которому нужно искать
            name_block - название искомого блока
            scroll - Нужно ли скроллить до элемента (по умолчанию True)
        """

        block = driver.find_element(By.CSS_SELECTOR, css)
        logging.info('Проверяем отображение элемента')
        assert block.is_displayed(), f'{name_block}Не отображается'
        if scroll:
            logging.info('Скроллим страницу до элемента')
            driver.execute_script("return arguments[0].scrollIntoView(true);", block)
