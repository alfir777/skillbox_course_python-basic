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
from collections import OrderedDict


class StatisticsByLetter:

    def __init__(self, file_name):
        self.file_name = file_name
        self.count_letter = 0
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
        self.sort()

    def sort(self):
        pass


class ByFrequency(StatisticsByLetter):

    def __init__(self, file_name):
        super().__init__(file_name)
        self.all_letters_count_list = []

    def sort(self):
        """по частоте по возрастанию"""
        self.all_letters_count_list = list(self.all_letters_count.items())
        self.all_letters_count_list.sort(key=lambda i: i[1])
        self.all_letters_count = dict(self.all_letters_count_list)


class Alphabet(StatisticsByLetter):

    def __init__(self, file_name):
        super().__init__(file_name)

    def sort(self):
        """по алфавиту"""
        self.all_letters_count = OrderedDict(sorted(self.all_letters_count.items(), key=lambda t: t[0]))


def main():
    statistics_letters = Alphabet(file_name='voyna-i-mir.txt')
    statistics_letters.collect()
    print('+---------+----------+')
    print('|  буква  | частота  |')
    print('+---------+----------+')
    for key, value in statistics_letters.all_letters_count.items():
        print("|{key:^9}| {value:^9}|".format(key=key, value=value))
    print('+---------+----------+')
    print('|  итого  | {count:^9}|'.format(count=statistics_letters.count_letter))
    print('+---------+----------+')


if __name__ == '__main__':
    main()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
