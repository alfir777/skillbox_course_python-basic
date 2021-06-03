# -*- coding: utf-8 -*-

import os, time, shutil

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

    def __init__(self, path=None, file=None, target_path=None):
        self.path = path
        self.file = file
        self.target_path = target_path

    def sorted_folder_to_date(self):
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
                else:
                    print('Такой файл существует: ', new_full_file_path)


paths = os.path.dirname(__file__) + '\\icons'
path_normalized = os.path.normpath(paths)
target_folder = os.path.dirname(__file__) + '\\icons_by_year'
target_folder_normalized = os.path.normpath(target_folder)

sorter = FileManager(path=path_normalized, target_path=target_folder_normalized)
sorter.sorted_folder_to_date()

print('Файлы успешно отсортированы')

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
