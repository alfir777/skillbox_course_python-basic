# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
import random
from termcolor import cprint

ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


def one_day():
    exceptions = (IamGodError('IamGodError - карма не растет'),
                  DrunkError('DrunkError - карма не растет'),
                  CarCrashError('CarCrashError - карма не растет'),
                  GluttonyError('GluttonyError - карма не растет'),
                  DepressionError('DepressionError - карма не растет'),
                  SuicideError('SuicideError - карма не растет'))
    if random.randint(1, 13) == 13:
        raise random.choice(exceptions)
    return random.randint(1, 7)


if __name__ == "__main__":
    count_day = 0
    count_error = 0
    carma = 0
    with open('02_error.txt', 'w+', encoding='utf8') as f:
        while True:
            if carma >= ENLIGHTENMENT_CARMA_LEVEL:
                break
            count_day += 1
            try:
                carma += one_day()
            except (IamGodError, DrunkError, CarCrashError, GluttonyError,
                    DepressionError, SuicideError) as exc:
                count_error += 1
                f.write(f'День {count_day} - выдало ошибку: {exc} \n')
                print(f'День {count_day} - выдало ошибку: {exc}')
        f.write(f'Потребовалось прожить {count_day} дней. Выдало {count_error} ошибок')
    cprint(f'Потребовалось прожить {count_day} дней. Выдало {count_error} ошибок', color='red')

# https://goo.gl/JnsDqu
