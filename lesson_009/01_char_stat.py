# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class StatisticsByLetter:
    count_letter = 0

    def __init__(self, file_name):
        self.file_name = file_name
        self.all_letters = set()
        self.all_letters_count = {}

    def collect(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for i in line:
                    if i.isalpha():
                        self.all_letters.add(i)
                        if i in self.all_letters_count:
                            self.all_letters_count[i] += 1
                            self.count_letter += 1
                        else:
                            self.all_letters_count[i] = 0
                            self.all_letters_count[i] += 1
                            self.count_letter += 1


statistics_letters = StatisticsByLetter(file_name='voyna-i-mir.txt')
statistics_letters.collect()
print('+---------+----------+')
print('|  буква  | частота  |')
print('+---------+----------+')
for key, value in statistics_letters.all_letters_count.items():
    print("|{key:^9}| {value:^9}|".format(key=key, value=value))
print('+---------+----------+')
print('|  итого  | {count:^9}|'.format(count=statistics_letters.count_letter))
print('+---------+----------+')

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
