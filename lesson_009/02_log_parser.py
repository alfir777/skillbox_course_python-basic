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


class LogParser:

    def __init__(self, file_name, out_file_name):
        self.count_letter = 0
        self.file_name = file_name
        self.out_file_name = out_file_name
        self.all_timers_count = {}

    def collect(self):
        pass

    def writing_to_file(self):
        pass


class ByHour(LogParser):

    def __init__(self, file_name, out_file_name):
        super().__init__(file_name, out_file_name)

    def collect(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                if line[1:14] in self.all_timers_count:
                    if line[-4:-1] == 'NOK':
                        self.all_timers_count[line[1:14]] += 1
                        self.count_letter += 1
                else:
                    self.all_timers_count[line[1:14]] = 0
                    self.all_timers_count[line[1:14]] += 1
                    self.count_letter += 1

    def writing_to_file(self):
        with open(self.out_file_name, 'w+') as f:
            for key, value in parser.all_timers_count.items():
                f.write("[{key:^9}] : {value:^3}| \n".format(key=key, value=value))


class ByMonth(LogParser):

    def __init__(self, file_name, out_file_name):
        super().__init__(file_name, out_file_name)

    def collect(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                if line[1:11] in self.all_timers_count:
                    if line[-4:-1] == 'NOK':
                        self.all_timers_count[line[1:11]] += 1
                        self.count_letter += 1
                else:
                    self.all_timers_count[line[1:11]] = 0
                    self.all_timers_count[line[1:11]] += 1
                    self.count_letter += 1

    def writing_to_file(self):
        with open(self.out_file_name, 'w+') as f:
            for key, value in parser.all_timers_count.items():
                f.write("[{key:^9}] : {value:^3}| \n".format(key=key, value=value))


class ByYear(LogParser):

    def __init__(self, file_name, out_file_name):
        super().__init__(file_name, out_file_name)

    def collect(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                if line[1:5] in self.all_timers_count:
                    if line[-4:-1] == 'NOK':
                        self.all_timers_count[line[1:5]] += 1
                        self.count_letter += 1
                else:
                    self.all_timers_count[line[1:5]] = 0
                    self.all_timers_count[line[1:5]] += 1
                    self.count_letter += 1

    def writing_to_file(self):
        with open(self.out_file_name, 'w+') as f:
            for key, value in parser.all_timers_count.items():
                f.write("[{key:^4}]:{value:^4}| \n".format(key=key, value=value))


parser = ByYear(file_name='events.txt', out_file_name='out.txt')
parser.collect()
parser.writing_to_file()


# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
