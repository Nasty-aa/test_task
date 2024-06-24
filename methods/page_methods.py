from selenium.webdriver.common.by import By


class MethodsPage:

    def search_block(self, css, name_block, scroll=True):
        """
            Метод для поиска элемента на странице
            css - Класс по которому нужно искать
            name_block - название искомого блока
            scroll - Нужно ли скроллить до элемента (по умолчанию True)
        """

        block = self.find_element(By.CSS_SELECTOR, css)
        print('Проверяем отображение элемента')
        assert block.is_displayed(), name_block + 'Не отображается'
        if scroll:
            print('Скроллим страницу до элемента')
            self.execute_script("return arguments[0].scrollIntoView(true);", block)
