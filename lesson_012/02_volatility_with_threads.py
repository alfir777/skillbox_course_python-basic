# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
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
import os
import time
from threading import Thread


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result
    return surrogate


class SorterTrades(Thread):

    def __init__(self, file, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
    sorter_trades = []
    for dir_path, dir_names, filenames in os.walk(path):
        for file in filenames:
            full_file_path = os.path.join(dir_path, file)
            sorter_trades.append(SorterTrades(file=full_file_path))
    for sorter_trade in sorter_trades:
        sorter_trade.start()
    for sorter_trade in sorter_trades:
        sorter_trade.join()
    for sorter_trade in sorter_trades:
        for key, value in sorter_trade.trades.items():
            trades_dict[key] = value

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
