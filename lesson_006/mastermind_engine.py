# -*- coding: utf-8 -*-

# Игра «Быки и коровы»
# https://goo.gl/Go2mb9
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».
#
# Формат ответа компьютера
# > быки - 1, коровы - 1


# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
import random


def guess_number():
    global secret_number
    set_numbers = set(range(10))
    first_number = random.randint(1, 9)
    last_3 = random.sample(set_numbers - {first_number}, 3)
    secret_number = int(str(first_number) + ''.join(map(str, last_3)))
    print(secret_number)      # off debug


def check_number(user_number):
    dict_bulls_cows = {'bulls': 0, 'cows': 0}
    for i, number in enumerate(str(user_number)):
        if number == str(secret_number)[i]:
            dict_bulls_cows['bulls'] += 1
        if number in str(secret_number):
            dict_bulls_cows['cows'] += 1

    return print('> быки -', dict_bulls_cows['bulls'], ', коровы -', dict_bulls_cows['cows'])


guess_number()
