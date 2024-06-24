import os


class MethodsFile:

    def check_size_file(self, path, size):
        """
            Метод для получения размера загруженного файла
            path - Путь до файла
        """

        file_size = os.path.getsize(f"{os.getcwd()}\downloads\sbisplugin-setup-web.exe")
        file_size /= 1024
        file_size /= 1024
        assert round(file_size, 2) == size, 'Размер файла не совпадает'
