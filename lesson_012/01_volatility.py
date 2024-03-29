# -*- coding: utf-8 -*-

import os
import time


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result
    return surrogate


class SorterTrades:

    def __init__(self, file):
        self.file = os.path.normpath(file)
        self.trades = {}
        self.trades_list = []

    def run(self):
        with open(self.file, 'r', encoding='utf8') as file:
            previous_price = 0
            max_price = 0
            min_price = 0
            for line in file:
                sec_id, trade_time, price, quantity = line.split(',')
                if price.isalpha():
                    continue
                price = float(price)
                if previous_price <= price:
                    max_price = price
                else:
                    min_price = price
                previous_price = price
            average_price = round(((max_price + min_price) / 2), 2)
            volatility = round((((max_price - min_price) / average_price) * 100), 2)
            self.trades[sec_id] = volatility
        return self.trades


@time_track
def main():
    path = os.path.dirname(__file__) + '\\trades'
    trades_dict = {}
    for dir_path, dir_names, filenames in os.walk(path):
        for file in filenames:
            full_file_path = os.path.join(dir_path, file)
            sorter_trades = SorterTrades(file=full_file_path)
            sorter_trade = sorter_trades.run()
            for k, v in sorter_trade.items():
                trades_dict[k] = v
    sort_trades_dict = sorted(trades_dict.items(), key=lambda i: i[1])
    print(trades_dict)
    print(sort_trades_dict)

    print('Нулевая волатильность:')
    min_val = 0
    while min_val == 0:
        min_val = min(trades_dict.values())
        for key, value in trades_dict.items():
            if value == min_val:
                print(key, value)
                del_key = key
                break
        del trades_dict[del_key]
        min_val = min(trades_dict.values())

    print('Максимальная волатильность:')
    i = 0
    while i != 3:
        max_val = max(trades_dict.values())
        for key, value in trades_dict.items():
            if value == max_val:
                print(key, value)
                del_key = key
                i += 1
                break
        del trades_dict[del_key]

    print('Минимальная волатильность:')
    i = 0
    while i != 3:
        min_val = min(trades_dict.values())
        for key, value in trades_dict.items():
            if value == min_val:
                print(key, value)
                del_key = key
                i += 1
                break
        del trades_dict[del_key]


if __name__ == '__main__':
    main()
