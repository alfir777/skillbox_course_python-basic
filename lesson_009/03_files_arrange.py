# -*- coding: utf-8 -*-

import os
import shutil
import time
import zipfile
from contextlib import closing
from tqdm import tqdm


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class FileManager:

    def __init__(self, path=None, target_path=None):
        if path:
            self.path = os.path.normpath(path)
        else:
            print('Не указана начальная папка')
        if target_path:
            self.target_path = os.path.normpath(target_path)
        else:
            print('Не указана папка назначения')
        self.count_file = self.count_files()

    def sorted(self):

        with closing(tqdm(total=self.count_file)) as p_bar:
            for dir_path, dir_names, filenames in os.walk(self.path):
                for file in filenames:
                    full_file_path = os.path.join(dir_path, file)
                    secs = os.path.getmtime(full_file_path)
                    file_time = time.gmtime(secs)
                    new_folder = self.target_path + '\\' + str(file_time.tm_year) + '\\' + str(file_time.tm_mon)
                    new_folder_normalized = os.path.normpath(new_folder)
                    if not os.path.isdir(new_folder_normalized):
                        os.makedirs(new_folder_normalized)
                    new_full_file_path = os.path.join(new_folder_normalized, file)
                    if not os.path.isfile(new_full_file_path):
                        shutil.copy2(full_file_path, new_full_file_path)
                    p_bar.update(1)
            print('Файлы успешно отсортированы')

    def count_files(self):
        count = 0
        for dir_path, dir_names, filenames in os.walk(self.path):
            for _ in filenames:
                count += 1
        return count


class FileManagerZip:

    def __init__(self, file=None, target_path=None):
        if os.path.isfile(file):
            self.file = os.path.normpath(file)
        else:
            print('Не указан файл')
        if os.path.exists(target_path):
            self.target_path = os.path.normpath(target_path)
        else:
            os.mkdir(target_path)
            self.target_path = os.path.normpath(target_path)

    def run(self):
        with zipfile.ZipFile(self.file) as zip_file:
            for zip_info in zip_file.infolist():
                if zip_info.filename[-1] == '/':
                    continue
                new_folder = self.target_path + '\\' + str(zip_info.date_time[0]) + '\\' + str(zip_info.date_time[1])
                new_folder_normalized = os.path.normpath(new_folder)
                if not os.path.isdir(new_folder_normalized):
                    os.makedirs(new_folder_normalized)
                new_full_file_path = new_folder_normalized
                zip_file.extract(zip_info, new_full_file_path)
        print('Файлы успешно отсортированы')


if __name__ == '__main__':
    file_or_path = 'icons.zip'
    target_folder = os.path.dirname(__file__) + '\\icons'
    if os.path.isfile(file_or_path):
        sorter = FileManagerZip(file=file_or_path, target_path=target_folder)
        sorter.run()
    else:
        sorter = FileManager(path=file_or_path, target_path=target_folder)
        sorter.sorted()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
