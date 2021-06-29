# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234


def log_parser(file_name=None):
    event_count_nok = 0
    previous_line = ''
    with open(file_name, 'r', encoding='cp1251') as file:
        for line in file:
            line_left = line[1:17]
            line_right = line[-4:-1]
            if previous_line == '':
                previous_line = line_left
            if previous_line != line_left:
                group_time = previous_line
                event_count = event_count_nok
                event_count_nok = 0
                previous_line = line_left
                yield group_time, event_count
            if line_right == 'NOK':
                event_count_nok += 1


grouped_events = log_parser(file_name='events.txt')
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
