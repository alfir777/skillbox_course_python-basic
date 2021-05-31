# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class Log_parser:
    count_letter = 0

    def __init__(self, file_name):
        self.file_name = file_name
        self.all_letters = set()
        self.all_timers_count = {}

    def collect(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self.all_letters.add(line)
                if line[1:17] in self.all_timers_count and line[-4:-1] == 'NOK':
                    self.all_timers_count[line[1:17]] += 1
                    self.count_letter += 1
                else:
                    self.all_timers_count[line[1:17]] = 0
                    self.all_timers_count[line[1:17]] += 1
                    self.count_letter += 1

    def writing_to_file(self, out_file_name):
        with open(out_file_name, 'w+') as f:
            for key, value in parser.all_timers_count.items():
                f.write("[{key:^9}]:{value:^3}| \n".format(key=key, value=value))


parser = Log_parser(file_name='events.txt')
parser.collect()
parser.writing_to_file('out.txt')


# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
