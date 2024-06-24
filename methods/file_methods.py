import os


class MethodsFile:
    """Класс для работы с файлами"""

    def check_size_file(self, path: str, size: int):
        """
            Метод для получения размера загруженного файла
            path - Путь до файла
        """

        file_size = os.path.getsize(path)
        file_size /= 1024
        file_size /= 1024
        assert round(file_size, 2) == size, 'Размер файла не совпадает'
